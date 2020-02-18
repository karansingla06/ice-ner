# encoding: utf-8

#from __future__ import unicode_literals
import sys
from importlib import reload
reload(sys)
# sys.setdefaultencoding('utf8')
from ice_commons.er.engines.base_ner import BaseCustomEntityRecognizer, BaseDefaultEntityRecognizer, AbstractIceEngine
from mitie import ner_trainer, ner_training_instance, named_entity_extractor
from pydash import get, compact
import os
from ice_commons.core.project_utils import get_phrase_entities, get_pattern_entities, get_predefined_entities
from ice_commons.utility.custom_tokenizer import tokenize_utterance

# from ice_commons.data.dl.manager import ProjectManager
from ice_commons.config_settings import app_config
import logging
import json

logger = logging.getLogger(__name__)


class MitieNER(AbstractIceEngine):

    def get_engine(self):
        return "ICE"

    def get_extension(self):
        return "dat"


class MitieDefaultNER(BaseDefaultEntityRecognizer, MitieNER):

    def __init__(self, serviceid="DEFAULT"):
        super(MitieDefaultNER, self).__init__(serviceid)

    def load(self):
        user_dir = os.path.expanduser('~')
        mitieModelFilePath = os.path.join(user_dir, '.verbis/models/mitie', 'english', 'ner_model.dat')
        mitie_model = named_entity_extractor(mitieModelFilePath)

        return mitie_model

    def predict(self, text, original_text, pos):
        tokens = tokenize_utterance(text)
        entities = self.model.extract_entities(tokens)

        def default_entity_mapping(entity):
            range = entity[0]
            ind = []
            for i in range:
                ind.append(i)

            return {
                "tag": entity[1],
                "entity": " ".join(original_text.split()[range[0]:range[-1] + 1]),
                "start": ind[0],
                "end": ind[-1] + 1,
                "resolvedTo": {'baseEntity': " ".join(original_text.split()[range[0]:range[-1] + 1]) }
            }

        default_entities = compact(list(map(default_entity_mapping, entities)))

        return default_entities, None


class MitieCustomNER(BaseCustomEntityRecognizer, MitieNER):

    def __init__(self, serviceid=None):
        super(MitieCustomNER, self).__init__(serviceid)

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
            try:
                utterance = get(data, "case_converted_utterance")
                logger.debug("Preparing utterance: %s" % utterance)
                mapping = json.loads(get(data, "mapping"))
                assert "tags" in mapping, "Tags missing from training data"
                tags = get(mapping, 'tags')
                tokens = utterance.split()
                sample = ner_training_instance(tokens)
                for tag in tags:
                    start = get(tag, 'start')
                    end = get(tag, 'end')
                    label = get(tag, 'tag')
                    label=label.encode('utf-8')
                    # ignoreTag = (label.upper() in predefined_tags)
                    ignoreTag = (label.upper() in predefined_tags) \
                                or (label in patterns) or (label in phrases)
                    if not ignoreTag:
                        assert all(v is not None for v in [start, end, label]), \
                            "Missing information for adding entities to training"
                        logger.info("Adding entity: %s" % label)
                        logger.info("Start range: %s" % start)
                        logger.info("End range: %s" % end)
                        sample.add_entity(range(start, end), label.upper())
                        if not label.upper() in label_list:
                            label_list.append(label.upper())
                        logger.info("label_list %s" % (label_list))
                data['ner_trained'] = True
                return sample, data
            except (TypeError, Exception) as e:
                data['ner_trained'] = False
                return None, data

        assert len(utterances) > 0, "Not enough utterances for training"
        results = list(map(get_sample, utterances))
        assert len(
            label_list) > 0, "Unable to do entity training as no custom entities are mapped. Please map atleast 2 custom entities to proceed."
        assert len(
            label_list) > 1, "Atleast 2 custom entities are mandatory to perform entity training. Please add one more custom entity to proceed."
        samples = compact([items[0] for items in results])
        trained_utterances = [items[1] for items in results]
        return samples, trained_utterances

    @staticmethod
    def __get_models_root_dir():
        user_dir = os.path.expanduser('~')
        default_root = os.path.join(user_dir, '.verbis', 'models')
        return default_root

    def __get_model_path(self):
        root_dir = self.__get_models_root_dir()
        mitieModelFilePath = os.path.join(root_dir, 'mitie', 'english', 'total_word_feature_extractor.dat')

        logger.info("---------------filepath custom mitie_ner************----------   %s" % mitieModelFilePath)
        return mitieModelFilePath

    def train(self, corpus):
        utterances = get(corpus, "utterances")
        assert utterances is not None, "No training data available"
        samples, trained_utterances = self.prepare(utterances)
        trainer = ner_trainer(self.__get_model_path())
        trainer.num_threads = 4
        trainer.num_c = int(app_config['C'])
        for sample in samples:
            trainer.add(sample)
        self.model = trainer.train()
        return trained_utterances

    def predict(self, text, original_text, pos):
        assert self.model is not None, "Please build the NER before using it for prediction"
        #text = text.decode('utf-8')
        results = self.model.extract_entities(text.split())

        def entity_mapping(e):
            score = e[2]
            if score > 0:
                entity_range = e[0]
                return {
                    "entity": " ".join(original_text.split()[entity_range[0]:entity_range[-1] + 1]),
                    "tag": e[1],
                    "score": e[2],
                    "start": entity_range[0],
                    "end": entity_range[-1] + 1
                }

        entities = compact(list(map(entity_mapping, results)))
        return entities, None

    def save(self, file_name):
        self.model.save_to_disk(file_name)

    def load(self, file_name):
        self.model = named_entity_extractor(file_name)
