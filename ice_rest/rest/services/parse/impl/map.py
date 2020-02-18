import logging
import json
import falcon

from operator import itemgetter
from ice_commons.store.util import regex_checker, phrase_checker
from pydash import get
from ice_rest.decorators import route
from ice_commons.data.dl.manager import DatasourceManager, ProjectManager, IceEntitiesModelManager
from ice_commons.config_settings import app_config
import datetime
from dateutil.relativedelta import relativedelta
import uuid
from ice_rest.manager.analytics.botanalyticsapi import BotAnalyticsAPI
from ice_rest.rest.services.parse.impl.common.store_utils import get_model_store, MODEL_TYPE_NER
from ice_rest.rest.services.parse.retag_predefinedtags import untag_predefined
from ice_commons.core.model_utils import get_engine

logger = logging.getLogger(__name__)
manager = DatasourceManager()
project_manager = ProjectManager()
ice_entities_manager = IceEntitiesModelManager()

def remove_duplicates(tag_list):
    b = []
    for i in range(0, len(tag_list)):
        if tag_list[i] not in tag_list[i + 1:]:
            b.append(tag_list[i])
    return b


def check(existing_tgs, current_tg):  # current_tg['start']>=tag['start'] and current_tg['end']<=tag['end']
    current_tg_list = []
    common_tags = []
    # for i in range(current_tg['start'], current_tg['end']):
    for i in range(get(current_tg, 'start', default=0), get(current_tg, 'end', default=0)):
        current_tg_list.append(i)
    for tag in existing_tgs:
        existing_tgs_list = []
        for i in range(tag['start'], tag['end']):
            existing_tgs_list.append(i)
        common_tags = list(set(current_tg_list).intersection(existing_tgs_list))
        if len(common_tags) > 0:
            return tag
    return current_tg


def tag_pattern(patterns, utterances):
    final_utterances = []
    for iter in utterances:
        utterance = get(iter, "utterance")
        case_converted_utterance = get(iter, "case_converted_utterance")
        mapping = get(iter, "mapping")
        mapping = json.loads(mapping)
        tokens = get(mapping, "tokens")
        text = get(mapping, "text")
        tags = get(mapping, "tags")
        intent = get(mapping, "intent")
        pattern = regex_checker(utterance, patterns)
        final_tags = tags
        for pat in pattern:
            final_tags.append(check(tags, pat))
        final_tags = remove_duplicates(final_tags)
        final_tags = sorted(final_tags, key=itemgetter('start'))
        mappings = {
            "tokens": tokens,
            "text": text,
            "tags": final_tags,
            "intent": intent
        }
        data = {
            "utterance": utterance,
            "case_converted_utterance": case_converted_utterance,
            "mapping": json.dumps(mappings)
        }
        final_utterances.append(data)
    return final_utterances


def tag_phrase(phrases, utterances):
    final_utterances = []
    for iter in utterances:
        utterance = get(iter, "utterance")
        case_converted_utterance = get(iter, "case_converted_utterance")
        mapping = get(iter, "mapping")
        mapping = json.loads(mapping)
        tokens = get(mapping, "tokens")
        text = get(mapping, "text")
        tags = get(mapping, "tags")
        intent = get(mapping, "intent")
        phrase = phrase_checker(utterance, phrases)
        final_tags = tags
        for phr in phrase:
            final_tags.append(check(tags, phr))
        final_tags = remove_duplicates(final_tags)
        final_tags.sort(key=lambda k:len(k['entity']), reverse = True) 
        mappings = {
            "tokens": tokens,
            "text": text,
            "tags": final_tags,
            "intent": intent
        }
        data = {
            "utterance": utterance,
            "case_converted_utterance": case_converted_utterance,
            "mapping": json.dumps(mappings)
        }
        final_utterances.append(data)
    return final_utterances



def remove_resolved(mappings):
    for iter in mappings:
        if 'resolvedTo' in iter:
            del iter['resolvedTo']
    return mappings


def filter_predefined(default, predefined_entities):
    res = []
    try:
        for iter in default:
            if str(iter['tag']) in predefined_entities:
                res.append(iter)
    except:
        return default

    return res



def tag_all_predefined(store, patterns, phrases, entities, utterances, default_engine, predefined_entities, project_config):
    for pattern_each in patterns:
        entities.append(pattern_each["entity"])
    for phrase_each in phrases:
        entities.append(phrase_each["entity"])

    updated_utterances = untag_predefined(utterances, entities)

    ice_entities_config = ice_entities_manager.get_ice_entities(project_config['language'])
    ice_entities = []
    if ice_entities_config is not None:
        for item in ice_entities_config:
            if item['name'] in predefined_entities:
                ice_entities.append(item)

    final_utterances = []
    for iter in updated_utterances:
        utterance = get(iter, "utterance")
        case_converted_utterance = get(iter, "case_converted_utterance")
        mapping = get(iter, "mapping")
        mapping = json.loads(mapping)
        tokens = get(mapping, "tokens")
        text = get(mapping, "text")
        tags = get(mapping, "tags")
        intent = get(mapping, "intent")
        resolved_mappings = store.get_resolved_mappings(ice_entities, utterance)
        resolved_mappings = store.handle_resolution_overlap(resolved_mappings)
        resolved_mappings = remove_resolved(resolved_mappings)

        default = store.tag_predefined(MODEL_TYPE_NER, default_engine, case_converted_utterance, utterance)
        default = filter_predefined(default, predefined_entities)
        final_tags = tags
        for res_tag in resolved_mappings:
            final_tags.append(check(tags, res_tag))
        for def_tag in default:
            final_tags.append(check(tags, def_tag))

        final_tags = remove_duplicates(final_tags)

        final_tags.sort(key=lambda k: len(k['entity']), reverse=True)

        mappings = {
            "tokens": tokens,
            "text": text,
            "tags": final_tags,
            "intent": intent
        }
        data = {
            "utterance": utterance,
            "case_converted_utterance": case_converted_utterance,
            "mapping": json.dumps(mappings)
        }

        final_utterances.append(data)

    return final_utterances





@route('/api/parse/bulktag')
class MapUtterances(object):
    def on_post(self, req, resp):
        log_flag = False
        if app_config['BOTANALYTICS_LOG_FLAG'].upper() == "ON":
            log_flag, req_id, botanalytics, start_time = True, str(uuid.uuid4()), BotAnalyticsAPI(), datetime.datetime.now()
        doc = req.context['doc'] or {}
        try:
            store= get_model_store()
            serviceid = doc["serviceid"]
            datasource = manager.find_datasource_by_service_id(serviceid)
            phrases = get(datasource, "phrases")
            patterns = get(datasource, "patterns")
            entities = get(datasource, "entities", [])
            predefined_entities = get(datasource, "predefined_entities", [])
            utterances = get(datasource, "utterances")
            project_config = project_manager.find_config_by_id(serviceid)
            default_engine = get_engine(project_config['predefined_entity_model'])
            type = doc["type"]
            if type == "phrases":
                utterances = tag_phrase(phrases, utterances)
            if type == "patterns":
                utterances = tag_pattern(patterns, utterances)
            if type == "predefined":
                utterances= tag_all_predefined(store, patterns, phrases, entities, utterances, default_engine, predefined_entities, project_config)

            document = {
                "$set": {
                    "utterances": utterances
                }
            }
            manager.update_datasource_by_service_id(serviceid, document)
            resp.data = json.dumps({"msg": "Successfully Updated"})
            resp.set_header('X-Powered-By', 'USTGlobal ICE')
            resp.status = falcon.HTTP_200
        except Exception as ex:
            logger.exception(ex)
            resp.data = {"msg": ex}
            resp.set_header('X-Powered-By', 'USTGlobal ICE')
            resp.status = falcon.HTTP_500
        finally:
            if log_flag:
                end_time = datetime.datetime.now()
                total_action_time = relativedelta(end_time, start_time)
                botanalytics.log(requesttype="nerrequests", serviceid=doc['serviceid'], req_id=req_id, action="BULK TAG", ner_req_timestamp=start_time.replace(microsecond=0).isoformat(), ner_req_end_timestamp=end_time.replace(microsecond=0).isoformat(), total_action_time=(total_action_time.hours*60*60*1000+total_action_time.minutes*60*1000+ total_action_time.seconds*1000)+(total_action_time.microseconds/1000))
