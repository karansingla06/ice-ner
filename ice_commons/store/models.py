# -*- coding: utf-8 -*-
import logging
import traceback
import pandas as pd
from ice_commons.utility.custom_tokenizer import tokenize_utterance

from ice_commons.store.base import VerbisStore
from ice_commons.er.utils.corenlp_utils import get_corenlp_instance
from ice_commons.utils import MODEL_TYPE_NER, MODEL_TYPE_IR
from ice_commons.store.util import regex_checker, phrase_checker
from pydash import concat, get
from ice_commons.store.case_converter import convert_case
from ice_commons.data.dl.manager import IceEntitiesModelManager
from ice_commons.core.model_utils import get_default_models, get_entities_for_default_model, get_default_models_celery, \
    get_all_corenlp_engines
from ice_commons.core.class_utils import create_instance
from ice_commons.patterns.singleton import Borg

logger = logging.getLogger(__name__)


default_pos_tagging_engine_dic = {"EN": "SPACY", "ES": "SPACY-es"}


class ModelStore(Borg):
    def __init__(self):
        self.store = VerbisStore()

    def init(self, keys):
        for serviceid, model_type, engine in keys:
            if MODEL_TYPE_IR == model_type:
                self.publish(serviceid, model_type, None)
            elif MODEL_TYPE_NER == model_type:
                if (engine == None):
                    engine = "ICE"
                self.publish(serviceid, model_type, engine)
        # self.store.load_ngrams()

    def get_model(self, serviceid, model_type, engine):
        if engine in get_all_corenlp_engines():
            return get_corenlp_instance(serviceid, engine)
        else:
            return self.store.get(serviceid, model_type, engine)

    def load_default_models(self):
        for model_each in get_default_models():
            default_er = create_instance(model_each, serviceid="DEFAULT")
            if default_er.model is None:
                logger.warn("Could not load model %s" % model_each)
            else:
                self.store.put(default_er, serviceid="DEFAULT", model_type=MODEL_TYPE_NER,
                               engine=default_er.get_engine())

    def filter_prediction_results(self, default, predefined_tags):
        def is_selected(predicted_tag):
            if predicted_tag["tag"] in predefined_tags:
                return True
            else:
                return False

        default = list(filter(is_selected, default))
        return default

    def remove_overlaps_and_duplicates(self, entity_list, tagged_indexes):
        predictions = []
        for entity_each in entity_list:
            start = entity_each["start"]
            end = entity_each["end"]
            skip = False
            for tagged_index_each in tagged_indexes:
                if tagged_index_each in range(start, end):
                    skip = True
                    break
            if skip:
                continue
            predictions.append(entity_each)
            tagged_indexes.extend(list(range(start, end)))
        return predictions, tagged_indexes

    def filter_model_tags(self, custom, default):
        # if indexes of predefined tag fall in range of any of custom and score of custom is grater than .1, remove predefined.
        def is_unique(tag):
            for custom_each in custom:
                start_cust = custom_each["start"]
                end_cust = custom_each["end"]
                for tagged_index_each in range(tag["start"], tag["end"]):
                    if tagged_index_each in range(start_cust, end_cust) and custom_each["score"] > .2:
                        return False
            return True

        # Remove from custom when prediction indexes overlaps with predefined indexes and custom score is less than .1
        def is_unique_custom(tag):
            for default_each in default:
                start_def = default_each["start"]
                end_def = default_each["end"]
                for tagged_index_each in range(tag["start"], tag["end"]):
                    if tagged_index_each in range(start_def, end_def) and tag["score"] < .2:
                        return False
            return True

        def score_ok(tag):
            if (tag["score"] > .1):
                return True
            else:
                return False

        custom = list(filter(score_ok, custom))
        default = list(filter(is_unique, default))
        custom = list(filter(is_unique_custom, custom))
        return default, custom

    def filter_tag_results(self, default, custom, phrase, pattern, predefined_tags, custom_tags, resolved_mappings):
        selectedTagList = predefined_tags

        def to_upper(custom_tag_each):
            return custom_tag_each.upper()

        def is_selected(predicted_tag):
            if predicted_tag["tag"] in selectedTagList:
                return True
            else:
                return False

        default = list(filter(is_selected, default))
        selectedTagList = list(map(to_upper, custom_tags))
        custom = list(filter(is_selected, custom))
        tagged_indexes = []
        predictions_ice_entities, tagged_indexes = self.remove_overlaps_and_duplicates(resolved_mappings,
                                                                                       tagged_indexes)
        predictions_phrase, tagged_indexes = self.remove_overlaps_and_duplicates(phrase, tagged_indexes)
        predictions_pattern, tagged_indexes = self.remove_overlaps_and_duplicates(pattern, tagged_indexes)
        default, custom = self.filter_model_tags(custom, default)
        predictions_default, tagged_indexes = self.remove_overlaps_and_duplicates(default, tagged_indexes)
        predictions_custom, tagged_indexes = self.remove_overlaps_and_duplicates(custom, tagged_indexes)

        return concat(predictions_default, predictions_ice_entities), concat(predictions_custom, predictions_pattern,
                                                                             predictions_phrase)

    def get_entities(self, serviceid, model_type, custom_engine, text, original_text, pos, default_engine,
                     datasources_map, projects_map):
        logger.info("in get_entities")
        try:
            pos_tags, prediction_results, predictions_custom = [], [], []
            default_model = self.get_model("DEFAULT", MODEL_TYPE_NER, default_engine)
            datasources_predefined_entities = get(datasources_map, "predefined_entities", default=[])
            logger.info("Starting entity predictions")
            if default_model is not None and default_engine:
                prediction_results, pos_tags = default_model.predict(text, original_text, pos)
                logger.info("Done  default prediction ")
                prediction_results = self.filter_prediction_results(prediction_results, datasources_predefined_entities)

            ice_entities_config = IceEntitiesModelManager().get_ice_entities(
                get(projects_map, "language", default="EN"))
            ice_entities = []
            for item in ice_entities_config:
                if item['name'] in datasources_predefined_entities:
                    ice_entities.append(item)
            resolved_mappings = self.get_resolved_mappings(ice_entities, original_text)

            if serviceid is not None and serviceid != "DEFAULT":
                model = self.get_model(serviceid, model_type, custom_engine)
                if model is None:
                    predictions_custom = []
                else:
                    predictions_custom, _ = model.predict(text, original_text, None)
                    logger.info("Done custom prediction ")

            pattern_response, phrase_response, predefined_tags = self.get_entities_for_ds(serviceid, original_text,datasources_map)

            # prediction_results = self.filter_prediction_results(prediction_results, predefined_tags)

            prediction_results = concat(phrase_response, pattern_response, predictions_custom,
                                        prediction_results, resolved_mappings)
            if pos:
                return prediction_results, pos_tags
            else:
                return prediction_results, None
        except:
            logger.info(traceback.print_exc())

    def tag_predefined(self, MODEL_TYPE_NER, default_engine, text, original_text):
        default_model = self.get_model("DEFAULT", MODEL_TYPE_NER, default_engine)
        logger.info("Starting default entity prediction")
        if default_model is not None:
            default, _ = default_model.predict(text, original_text, None)
        return default

    def get_entities_for_ds(self, serviceid, text, datasources_map):
        predefined_tags = datasources_map["predefined_entities"] if 'predefined_entities' in datasources_map else []
        pattern_response = []
        phrase_response = []
        pattern_entities = datasources_map["patterns"] if 'patterns' in datasources_map else []
        phrase_entities = datasources_map["phrases"] if 'phrases' in datasources_map else []
        if len(pattern_entities) != 0:
            pattern_response = regex_checker(text, pattern_entities)
        if len(phrase_entities) != 0:
            phrase_response = phrase_checker(text, phrase_entities)
        return pattern_response, phrase_response, predefined_tags

    def get_resolved_mappings(self, ice_entities, text):
        resolved_mappings = []
        for entity in ice_entities:
            obj = create_instance(entity['resolutionClass'])
            mapping = obj.resolve(text)
            if len(mapping) != 0:
                for map in mapping:
                    if entity['name'].upper() == map['tag'].upper():
                        resolved_mappings.append(map)
            del obj
        return resolved_mappings

    def handle_resolution_overlap(self, resolved_mappings):
        if len(resolved_mappings) <= 1:
            return resolved_mappings
        else:
            try:
                i, j = 0, 1
                updated = []
                resolved_mappings.sort(key=lambda k: k['start'])
                while True:
                    if i == len(resolved_mappings) or j == len(resolved_mappings):
                        if resolved_mappings[j - 1] not in updated:
                            updated.append(resolved_mappings[j - 1])
                        break

                    if resolved_mappings[i]['start'] == resolved_mappings[j]['start'] or resolved_mappings[i]['end'] > \
                            resolved_mappings[j]['start']:
                        len1 = len(str(resolved_mappings[i]['entity']))
                        len2 = len(str(resolved_mappings[j]['entity']))
                        if len1 >= len2:
                            if resolved_mappings[i] not in updated:
                                updated.append(resolved_mappings[i])
                            j += 1
                        else:
                            if resolved_mappings[i] in updated:
                                updated.remove(resolved_mappings[i])
                            updated.append(resolved_mappings[j])
                            i = j
                            j += 1
                    else:
                        if resolved_mappings[i] not in updated:
                            updated.append(resolved_mappings[i])
                        i = j
                        j += 1
                return updated
            except Exception as ex:
                logger.exception(ex, exc_info=True)
                logger.error(traceback.format_exc())
                return []

    def tag(self, service_id, text, original_text, engine, default_engine, default_model_class, datasources_map,
            projects_map):
        try:
            default = []
            custom = []
            default_model = self.get_model("DEFAULT", MODEL_TYPE_NER, default_engine)
            datasources_predefined_entities = datasources_map['predefined_entities'] if 'predefined_entities' in datasources_map else []
            if default_model is not None:
                default, _ = default_model.predict(text, original_text, None)
                logger.info("default tags before filtering ---- %s " % default)
                default = self.filter_prediction_results(default, datasources_predefined_entities)
                logger.info("default tags after filtering ---- %s " % default)

            ice_entities_config = IceEntitiesModelManager().get_ice_entities(
                projects_map['language'] if 'language' in projects_map else 'EN')
            ice_entities = []
            if ice_entities_config is not None:
                for item in ice_entities_config:
                    if item['name'] in datasources_predefined_entities:
                        ice_entities.append(item)

            resolved_mappings = self.get_resolved_mappings(ice_entities, original_text)
            logger.info('resolved mapppings are-----------------   %s' % resolved_mappings)
            resolved_mappings = self.handle_resolution_overlap(resolved_mappings)
            logger.info("resolved mappings list after handling overlap----- %s " % resolved_mappings)

            custom_tags = []
            pattern_response = []
            phrase_response = []
            if service_id is not None and service_id != 'DEFAULT':
                pattern_response, phrase_response, predefined_tags = self.get_entities_for_ds(service_id, original_text,
                                                                                              datasources_map)
                if projects_map["ner_status"] in ["trained", "validated", "validating"]:
                    custom_model = self.get_model(service_id, MODEL_TYPE_NER, engine)
                    if custom_model is not None:
                        custom_tags = datasources_map["entities"]
                        custom, _ = custom_model.predict(text, original_text, None)

            tokens = text.split()
            logger.info("----Default predictions----- %s" % default)
            logger.info("----Resolution class predictions----- %s" % resolved_mappings)
            logger.info("----custom predictions---- %s" % custom)
            logger.info("----phrase predictions---- %s" % phrase_response)
            logger.info("----pattern predictions---- %s" % pattern_response)
            default, custom = self.filter_tag_results(default, custom, phrase_response, pattern_response,
                                                      datasources_predefined_entities, custom_tags, resolved_mappings)

            return {
                "utterance": original_text,
                "case_converted_utterance": text,
                "tokens": tokens,
                "custom_tags": custom,
                "default_tags": default
            }
        except:
            logger.info(traceback.print_exc())
            return {
                "utterance": original_text,
                "case_converted_utterance": text,
                "tokens": text.split(),
                "custom_tags": [],
                "default_tags": []
            }

    def tag_for_intent(self, service_id, text, original_text, engine, default_engine, default_model_class,
                       datasources_map, projects_map):
        try:
            predictions = self.tag(service_id, text, original_text, engine, default_engine, default_model_class,
                                   datasources_map, projects_map)
            result = concat(predictions["custom_tags"], predictions["default_tags"])
            result.sort(key=lambda tag: tag["start"], reverse=False)
            return result
        except:
            logger.info(traceback.print_exc())

    def get_intent(self, serviceid, model_type, engine, text):
        try:
            logger.info((serviceid, model_type, engine))
            model = self.get_model(serviceid, model_type, None)
            logger.info(model)
            if model is not None:
                logger.info("Starting intent predictions")
                data = pd.DataFrame([text], columns=["text"])
                predictions = model.predict(data)
                logger.info(predictions)
                logger.info("Done intent prediction ")
                logger.info("Starting probability prediction ")
                predict_proba = model.predict_proba(data)
                logger.info(predict_proba)
                logger.info("Done probability prediction ")
                probabilities = []
                if predict_proba is not None:
                    def get_predict_probabilities(x):
                        x = [i * 100 for i in x]  # Converting to percentage
                        x = ['{}%'.format(i) for i in x]  # formatting with %
                        return dict(list(zip(model.labels, x)))

                    probabilities = list(map(get_predict_probabilities, predict_proba.tolist()))
                logger.info("Done prediction ")
                return predictions.tolist()[0], probabilities
            return [], []
        except:
            logger.info(traceback.print_exc())

    def get_pos_tags(self, text, original_text, language="EN", pos="yes"):
        logger.info("in get_pos_tags")
        try:
            pos_tags = []

            default_model = self.get_model("DEFAULT", MODEL_TYPE_NER, default_pos_tagging_engine_dic[language])
            if default_model is not None:
                logger.info("get_pos_tags before invoking predict of spacy %s" % text)
                logger.info("get_pos_tags before invoking predict of spacy %s" % original_text)
                prediction_results, pos_tags = default_model.predict(text, original_text, pos)
                logger.info("Done  spacy pos tags prediction ")

            return pos_tags
        except:
            logger.info(traceback.print_exc())

    def get_active_models(self):
        return self.store.get_registered_ids()

    def change_case(self, utterance):
        try:
            tokensCorrect = tokenize_utterance(utterance)
            tokens = [token.lower() for token in tokensCorrect]
            wordCasingLookup = self.get_model("wordCasingLookup", "NGRAM", None)
            uniDist = self.get_model("uniDist", "NGRAM", None)
            backwardBiDist = self.get_model("backwardBiDist", "NGRAM", None)
            forwardBiDist = self.get_model("forwardBiDist", "NGRAM", None)
            trigramDist = self.get_model("trigramDist", "NGRAM", None)
            tokensTrueCase = convert_case(tokens, 'title', wordCasingLookup, uniDist, backwardBiDist, forwardBiDist,
                                          trigramDist)
            return " ".join(tokensTrueCase), " ".join(tokensCorrect)
        except:
            logger.info(traceback.print_exc())

    def save(self, model):
        """

        :param model:
        :return:
        """
        self.store.save(model)

    def publish(self, serviceid, model_type, engine=None, class_name=None):
        """

        :param serviceid:
        :param model_type:
        :param engine:
        :return:
        """
        self.store.publish(serviceid, model_type, engine, class_name)

    def unpublish(self, serviceid, model_type, engine=None):
        """

        :param serviceid:
        :param model_type:
        :param engine:
        :return:
        """
        self.store.unpublish(serviceid, model_type, engine)

    def load_default_models_celery(self):
        for model_each in get_default_models_celery():
            default_er = create_instance(model_each, serviceid="DEFAULT")
            if default_er.model is None:
                logger.warn("Could not load model %s" % model_each)
            else:
                self.store.put(default_er, serviceid="DEFAULT", model_type=MODEL_TYPE_NER,
                               engine=default_er.get_engine())
