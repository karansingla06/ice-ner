import os
import json
import operator
import pickle
import dill
from itertools import chain
from pydash import get, compact
import scipy.stats
from sklearn.metrics import make_scorer
from sklearn.model_selection import RandomizedSearchCV
import sklearn_crfsuite
from sklearn_crfsuite import metrics, CRF
import logging

from ice_commons.er.engines.base_ner import BaseCustomEntityRecognizer, AbstractIceEngine, BaseDefaultEntityRecognizer
from ice_commons.core.project_utils import get_phrase_entities, get_pattern_entities, get_predefined_entities
from ice_commons.er.utils.crf_utils import sent2features, sent2labels, pos_tags_predict, pos_tags_train

language = "EN"


class CrfNER(AbstractIceEngine):
    def get_engine(self):
        return "CRF"

    def get_extension(self):
        return "pickle"


def format_response(entities):
    """

    :type entities: object
    """

    if len(entities) <= 1:
        return entities
    else:
        new_entities_list, same_tag_entities = [], []
        i = 0
        j = 1
        while (True):
            if i == len(entities) - 1:
                if len(same_tag_entities) != 0:
                    new_entities_list.append(same_tag_entities)
                else:
                    new_entities_list.append([entities[i]])
                break
            else:
                if entities[i]['tag'] == entities[j]['tag'] and entities[i]['end'] == entities[j]['start']:
                    same_tag_entities.append(entities[i])
                    same_tag_entities.append(entities[j])
                    i += 1
                    j += 1
                else:
                    if len(same_tag_entities) != 0:
                        new_entities_list.append(same_tag_entities)
                        same_tag_entities = []
                        i += 1
                        j += 1
                    else:
                        same_tag_entities.append(entities[i])

        final_result = []
        for list_of_entities in new_entities_list:
            combined_entity = {'entity': '', 'tag': list_of_entities[0]['tag'], 'start': list_of_entities[0]['start'],
                               'score': list_of_entities[0]['score']}
            res_list = [i for n, i in enumerate(list_of_entities) if i not in list_of_entities[n + 1:]]
            for entity in res_list:
                combined_entity['entity'] += entity['entity'] + ' '
                combined_entity['end'] = entity['end']
                if combined_entity['score'] < entity['score']:
                    combined_entity['score'] = entity['score']
            combined_entity['entity'] = combined_entity['entity'].strip()
            final_result.append(combined_entity)
        return final_result


class CRFCustomNER(BaseCustomEntityRecognizer, CrfNER):

    def __init__(self, serviceid=None):
        super(CRFCustomNER, self).__init__(serviceid)

    def prepare(self, utterances):
        logger = logging.getLogger(__name__)
        predefined_tags = get_predefined_entities(self.serviceid)

        def extract_entity_names(entry_each):
            return get(entry_each, "entity")

        patterns = list(map(extract_entity_names, get_pattern_entities(self.serviceid)))
        phrases = list(map(extract_entity_names, get_phrase_entities(self.serviceid)))
        label_list = []

        def get_sample(data):
            assert 'mapping' in data, "Token mapping missing from training data"
            assert "utterance" in data, "Utterance text missing from training data"
            assert "case_converted_utterance" in data, "case_converted_utterance text missing from training data"

            try:
                feature_x = None
                feature_y = None
                utterance = get(data, "case_converted_utterance")
                original_text = get(data, "utterance")
                logger.info("Preparing utterance: %s" % utterance)
                mapping = json.loads(get(data, "mapping"))
                assert "tags" in mapping, "Tags missing from training data"
                tags = get(mapping, 'tags')
                tokens = utterance.split()

                if len(tokens) != 0:
                    each_sent_tuple = ["O" for val in tokens]
                    tmp_dict_final = []

                    for entity_each in tags:
                        tmp_dict_ind = []
                        start = entity_each["start"]
                        end = entity_each["end"]
                        label = entity_each["tag"]
                        label = label.encode('utf-8')
                        tmp_dict_ind.append(start)

                        while end - start > 1:
                            start = start + 1
                            tmp_dict_ind.append(start)

                        ignore_tag = (label.upper() in predefined_tags) \
                                     or (label in patterns) or (label in phrases)
                        if not ignore_tag:
                            assert all(v is not None for v in [start, end, label]), \
                                "Missing information for adding entities to training"
                            logger.info("Adding entity: %s" % label)
                            logger.info("Start range: %s" % start)
                            logger.info("End range: %s" % end)
                            [tmp_dict_final.append((val, label.upper())) for val in tmp_dict_ind]
                            if not label.upper() in label_list:
                                label_list.append(label.upper())
                            logger.info("label_list %s" % (label_list))

                    for ind_val in tmp_dict_final:
                        each_sent_tuple[ind_val[0]] = ind_val[1]

                    each_sent_pos_tag_lemma = pos_tags_train(utterance, original_text, language)
                    each_sent_pos_tag = [val[1] for val in each_sent_pos_tag_lemma]
                    each_sent_word_lemma = [val[2] for val in each_sent_pos_tag_lemma]
                    feature_x = list(zip(tokens, each_sent_pos_tag, each_sent_word_lemma))
                    feature_y = each_sent_tuple

                data['ner_trained'] = True
                return feature_x, feature_y, data
            except (TypeError, Exception) as e:
                print(e)
                data['ner_trained'] = False
                return None, None, data

        assert len(utterances) > 0, "Not enough utterances for training"

        results = list(map(get_sample, utterances))
        return_val_x = compact([items[0] for items in results])
        return_val_y = compact([items[1] for items in results])
        trained_utterances = compact([items[2] for items in results])

        assert len(return_val_x) > 0, "Not enough utterances for training"

        train_sents = []

        for i in list(zip(return_val_x, return_val_y)):
            train_sents.append([(i[0][ind][0], i[0][ind][1], i[0][ind][2], i[1][ind]) for ind in range(0, len(i[0]))])

        x_train = [sent2features(s) for s in train_sents]
        y_train = [sent2labels(s) for s in train_sents]

        return x_train, y_train, trained_utterances

    @staticmethod
    def __get_models_root_dir():
        user_dir = os.path.expanduser('~')
        default_root = os.path.join(user_dir, '.verbis', 'models')
        return default_root

    def train(self, corpus):
        """

        :param corpus:
        :return:
        """
        assert corpus is not None, "No training data file given"
        assert 'utterances' in corpus, "Token mapping missing from training data"

        x_train, y_train, trained_utterances = self.prepare(corpus["utterances"])

        unq_labels = list(set(list(chain(*y_train))))

        # assert len(unq_labels) > 1, "Not enough unique labels for training"

        # best parameter selection for model-lbfgs
        def get_best_model(X_train, y_train):
            crf = sklearn_crfsuite.CRF(
                algorithm='lbfgs',
                max_iterations=100,
                all_possible_transitions=True
            )
            params_space = {
                'c1': scipy.stats.expon(scale=0.5),
                'c2': scipy.stats.expon(scale=0.05),
            }

            # use the same metric for evaluation
            f1_scorer = make_scorer(metrics.flat_f1_score, average='weighted', labels=unq_labels)

            # search
            rs = RandomizedSearchCV(crf, params_space,
                                    cv=3,
                                    verbose=1,
                                    n_jobs=3,
                                    n_iter=10,
                                    scoring=f1_scorer)
            rs.fit(X_train, y_train)

            return rs

        rs = get_best_model(x_train, y_train)


        self.model = sklearn_crfsuite.CRF(
            algorithm='lbfgs',
            c1=rs.best_params_.get('c1'),  # 0.1,
            c2=rs.best_params_.get('c2'),
            max_iterations=100,
            all_possible_transitions=True
        )
        self.model.fit(x_train, y_train)


        return trained_utterances

    def predict(self, text, original_text, pos):
        assert self.model is not None, "Please build the NER before using it for prediction"
        input_text_pos_tag = pos_tags_predict(text, original_text, language)
        original_text_list = original_text.split()
        input_text_test = sent2features(input_text_pos_tag)
        entities_list = self.model.predict_marginals_single(input_text_test)

        def entity_mapping(indx):
            tag = max(iter(entities_list[indx].items()), key=operator.itemgetter(1))[0]

            if tag != "O":
                return {
                    "entity": original_text_list[indx],  # input_text_pos_tag[indx][0],
                    "tag": tag,
                    "score": entities_list[indx][tag],
                    "start": indx,
                    "end": indx + 1
                }

        entities = compact(list(map(entity_mapping, list(range(0, len(input_text_pos_tag))))))
        entities = format_response(entities)

        return entities, None

    def save(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.model, f)

    def load(self, filename):
        with open(filename, "rb") as f:
            self.model = dill.load(f)
