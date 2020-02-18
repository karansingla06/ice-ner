import json
import logging

from ice_commons.er.utils.corenlp_utils import create_model_file, write_to_tsv, stanfordcorenlp_defaultner, \
    stanfordcorenlp_customner, write_property_file

from pydash import get
from ice_commons.er.engines.base_ner import BaseCustomEntityRecognizer, BaseDefaultEntityRecognizer, AbstractIceEngine
from ice_commons.core.project_utils import get_predefined_entities, get_pattern_entities, get_phrase_entities


logger = logging.getLogger(__name__)


class CorenlpNER(AbstractIceEngine):
    def get_engine(self):
        return "CoreNLP"

    def get_extension(self):
        return "ser.gz"


class CorenlpDefaultNER(BaseDefaultEntityRecognizer, CorenlpNER):

    def __init__(self, serviceid="DEFAULT"):
        super(CorenlpDefaultNER, self).__init__(serviceid)

    def load(self):
        pass

    def predict(self, text, original_text, pos):
        return stanfordcorenlp_defaultner(text, original_text, language="en")


class CorenlpCustomNER(BaseCustomEntityRecognizer, CorenlpNER):

    def __init__(self, serviceid=None):
        super(CorenlpCustomNER, self).__init__(serviceid)

    def prepare(self, utterances):
        predefined_tags = get_predefined_entities(self.serviceid)

        def extract_entity_names(entry_each):
            return get(entry_each, "entity")

        patterns = list(map(extract_entity_names, get_pattern_entities(self.serviceid)))
        phrases = list(map(extract_entity_names, get_phrase_entities(self.serviceid)))

        def get_sample(data):
            assert 'mapping' in data, "Token mapping missing from training data"
            assert "utterance" in data, "Utterance text missing from training data"
            assert "case_converted_utterance" in data, "case_converted_utterance text missing from training data"

            label_list = []
            try:
                utterance = get(data, "case_converted_utterance")
                logger.debug("Preparing utterance: %s" % utterance)
                mapping = json.loads(get(data, "mapping"))
                assert "tags" in mapping, "Tags missing from training data"
                tags = get(mapping, 'tags')
                tokens = utterance.split()

                logger.info("utterance is: %s " % utterance)
                logger.info("tokens is : %s" % str(tokens))
                if len(tokens) != 0 or len(tags) != 0:
                    tag_list = ["O" for token_each in tokens]
                    tags_identified = []
                    for entity_each in tags:
                        tag_index = []
                        start = entity_each["start"]
                        end = entity_each["end"]
                        label = entity_each["tag"]
                        tag_index.append(start)
                        while end - start > 1:
                            start = start + 1
                            tag_index.append(start)

                        ignore_tag = (label.upper() in predefined_tags) \
                                     or (label in patterns) or (label in phrases)

                        if not ignore_tag:
                            assert all(v is not None for v in [start, end, label]), \
                                "Missing information for adding entities to training"
                            logger.info("Adding entity: %s" % label)
                            logger.info("Start range: %s" % start)
                            logger.info("End range: %s" % end)
                            [tags_identified.append((val, label)) for val in tag_index]
                            if not label.upper() in label_list:
                                label_list.append(label.upper())
                            logger.info("label_list %s" % (label_list))

                    for i in tags_identified:
                        tag_list[i[0]] = i[1]
                data['ner_trained'] = True
                return tokens, tag_list, data
            except (TypeError, Exception) as e:
                print(e)
                data['ner_trained'] = False
                return None, None, data

        assert len(utterances) > 0, "Not enough utterances for training"
        results = list(map(get_sample, utterances))
        tokens = [items[0] for items in results]
        tags = [items[1] for items in results]
        trained_utterances = [items[2] for items in results]
        assert len(tokens) > 0, "Not enough utterances for training"
        write_to_tsv(self.serviceid,tokens, tags)
        return trained_utterances

    def train(self, corpus):
        """
        :type corpus: object
        """
        assert corpus is not None, "No training data file given"
        assert 'utterances' in corpus, "Token mapping missing from training data"

        trained_utterances = self.prepare(corpus["utterances"])
        write_property_file(self.serviceid, self.get_engine())
        create_model_file(self.serviceid)
        return trained_utterances

    def predict(self, text, original_text, pos):
        return stanfordcorenlp_customner(self.serviceid, text, original_text, language="en")

    def save(self, filename):
        pass

    def load(self, filename):
        pass
