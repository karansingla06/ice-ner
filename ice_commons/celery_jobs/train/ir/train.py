# coding=utf-8
import datetime
import logging
import traceback
from json import loads

import numpy as np
import pandas as pd
from ice_commons.utility.custom_tokenizer import tokenize_utterance
from pydash import get

from ice_commons.core.interfaces import IntentRecognizer
from ice_commons.data.dl.manager import ProjectManager, DatasourceManager
from ice_commons.stopword import get_stopwords
from ice_commons.store.base import VerbisStore
from ice_commons.utility.logger import get_redis_handler, LogArrayHandler

logger = logging.getLogger(__name__)

stopwords_language = {"EN": "english", "ES": "spanish"}


class StreamingMixin(object):
    domain = 'verbis.streaming.notifications.model'

    @staticmethod
    def get_topic(serviceid, model_type):
        if serviceid is not None and model_type is not None:
            return StreamingMixin.domain + '.' + serviceid + '.' + model_type
        return StreamingMixin.domain


def stopword_remover(text, language):
    # stop_words = set(stopwords.words(language))
    stop_words = get_stopwords(language)
    # if language == "english":
    #     stop_words = ["it", "it’s", "its", "this", "that", "that’ll", "these", "those", "am", "is", "are", "was",
    #                   "were", "be", "been", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
    #                   "the", "and", "but", "if", "or", "as", "of", "at", "by", "for", "to", "so", "than", "too",
    #                   "should", "should’ve", "ain", "aren", "aren’t", "couldn", "couldn’t", "didn", "didn’t", "doesn",
    #                   "doesn’t", "hadn", "hadn’t", "hasn", "hasn’t", "haven", "haven’t", "isn", "isn’t", "mightn",
    #                   "mightn’t", "mustn", "mustn’t", "needn", "needn’t", "shall", "shouldn", "shouldn’t", "wasn",
    #                   "wasn’t", "weren", "weren’t", "won’t", "wouldn", "wouldn’t"]
    # else:
    #     stop_words = []

    word_tokens = tokenize_utterance(text)
    filtered_sentence = []
    for w in word_tokens:
        if w.lower() not in stop_words:
            filtered_sentence.append(w)

    return filtered_sentence


def remove_single_character_tokens(tokens):
    for token in tokens:
        if len(token) == 1:
            tokens.remove(token)
    return tokens


def db_add_dict(serviceid, text):
    manager = DatasourceManager()
    manager2 = ProjectManager()
    project_config = manager2.find_config_by_id(serviceid)
    language_code = get(project_config, "language", "EN")
    corpus = manager.find_datasource_by_service_id(serviceid)
    distinct_token_list = get(corpus, "distinct_token_list")
    if distinct_token_list is None:
        distinct_token_list = []
    stopword_removed_text = stopword_remover(text, language_code)
    distinct_token_list.extend(list(set(remove_single_character_tokens(stopword_removed_text))))
    distinct_token_list = list(set(distinct_token_list))
    document = {
        "$set": {
            "distinct_token_list": distinct_token_list,
        }
    }
    manager.update_datasource_by_service_id(serviceid, document)


DEFAULT_CONFIG = {
    "preprocessors": [
        {
            "columns": [
                "text"
            ],
            "transformations": [
                {
                    "class": "ice_commons.core.text.UnicodeDecoder"
                },
                {
                    "class": "ice_commons.core.text.Concatenate"
                },
                {
                    "class": "ice_commons.core.text.HTMLTagRemover"
                },
                {
                    "class": "ice_commons.core.text.Lemma"
                },
                {
                    "class": "sklearn.feature_extraction.text.TfidfVectorizer",
                    "params": {
                        "ngram_range": [
                            1,
                            5
                        ],
                        "sublinear_tf": True,
                        "use_idf": True,
                        "max_features": 15000
                    }
                }
            ]
        }
    ],
    "selector": {
        "class": "ice_commons.core.features.OneVsOne"
    },
    "target_label": "intent"
}


def get_ir_dataset(serviceid, logger):
    logger = logger or logging.getLogger(__name__)
    data_manager = DatasourceManager()
    logger.info("Starting evaluation of service %s" % serviceid)

    def get_training_data(row):
        mapping = loads(get(row, "mapping"))
        intent = None
        if mapping is not None:
            intent = get(mapping, "intent")
        if intent is None:
            intent = "No intent"
        row["ir_trained"] = True
        text = get(row, "case_converted_utterance")
        l = []
        if get(row, "ner_trained") == True:
            tokens = text.split()
            tags = get(mapping, 'tags')
            prev_end = 0
            for tag_num, tag in enumerate(tags):
                start = get(tag, 'start')
                end = get(tag, 'end')
                label = get(tag, 'tag')
                for index, token_each in enumerate(tokens):
                    if ((index < start) and index >= prev_end):
                        l.append(token_each)
                    elif (index == start):
                        l.append(label.upper())
                prev_end = end
            if (prev_end < len(tokens)):
                l.extend(tokens[prev_end:len(tokens)])
            text = ' '.join(l)
        db_add_dict(serviceid, text)
        return row, text, intent

    query = {
        "serviceid": serviceid
    }
    corpus = data_manager.find_model(query)
    utterances = get(corpus, "utterances")
    results = list(map(get_training_data, utterances))
    trained_utterances = [items[0] for items in results]
    training_data = [(items[1], items[2]) for items in results]
    return trained_utterances, pd.DataFrame(training_data, columns=["text", "intent"])


class DeployIRHelper(StreamingMixin):
    """

    """

    def __init__(self, serviceid):
        assert serviceid is not None, \
            "Invalid serviceid specified -> %s" % serviceid

        self.serviceid = serviceid
        self.logger = logging.getLogger(__name__)
        real_time_handler = get_redis_handler(self.get_topic(self.serviceid, 'ner'))
        self.logger.addHandler(real_time_handler)
        self.logger.addHandler(LogArrayHandler())

    def deploy(self):
        """
        :param doc:
        :param n_test_percent:
        :return:
        """
        manager = ProjectManager()
        query = {
            "serviceid": self.serviceid
        }
        config = manager.find_model(query)
        if config is not None:
            try:
                trained_data, df = get_ir_dataset(self.serviceid, self.logger)
                self.logger.info("Unique labels %s" % np.unique(df.intent.tolist()))

                group = df.groupby(['intent']).agg('count')
                stats = group.reset_index().to_json(orient="records")
                useSelector = False
                if (len(group) > 1):
                    useSelector = True
                self.logger.info(stats)

                document = {
                    "$set": {
                        "ir.status": ProjectManager.STATUS_TRAINING,
                        "ir.status_message": "Intent training is in progress.",
                        "ir.dataset.stats": stats,
                        "ir.last_trained": datetime.datetime.utcnow()
                    }
                }
                manager.update_config(query, document)

                ir = IntentRecognizer(DEFAULT_CONFIG, serviceid=self.serviceid, useSelector=useSelector)
                self.logger.info("Starting fitting for deployment")
                ir.fit(df, df.intent)
                self.logger.info("Fitting for deployment completed")

                VerbisStore().save_ir(ir)
                ###############MINIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO##################
                # send file to minio server
                # no engine. .dat - extension
                VerbisStore().save_ir_minio(ir)
                document = {
                    "$set": {
                        "utterances": trained_data,
                    }
                }
                data_manager = DatasourceManager()
                data_manager.update_datasource(query, document)

                document = {
                    "$set": {
                        "ir.status": ProjectManager.STATUS_TRAINED,
                        "ir.status_message": "The Intent model has been successfully trained",
                        "ir.logs.deploy": ""
                    }
                }
                manager.update_config(query, document)
            except (RuntimeError, ValueError, Exception) as e:
                self.logger.error(e)
                message = e
                if (e == "After pruning, no terms remain. Try a lower min_df or a higher max_df."
                        or e == "max_df corresponds to < documents than min_df"):
                    message = "Sufficient vocabulary to build the model is not available. Please add more utterances."
                elif e == "Invalid type float for labels":
                    message = "Add more intents for intent training"
                document = {
                    "$set": {
                        "ir.status": ProjectManager.STATUS_TRAINING_FAILED,
                        "ir.status_message": message,
                        "ir.logs.deploy": self.logger.handlers[-1].logs
                    }
                }
                manager.update_config(query, document)
                traceback.print_exc()
        else:
            description = 'Unable to find project_config with given id.' \
                          'Please check your request params and retry'
            self.logger.error(description)
