import json
import logging
import datetime
import falcon

from pydash import get
from operator import itemgetter
from ice_commons.store.base import VerbisStore
from ice_commons.utils import MODEL_TYPE_NER
from ice_rest.decorators import route
from ice_commons.core.model_utils import get_default_models, get_entities_for_default_model, get_engine
from ice_commons.core.project_utils import get_ner_status
from ice_commons.data.dl.manager import DatasourceManager, ProjectManager, IceEntitiesModelManager
from ice_rest.rest.services.parse.impl.common.store_utils import get_model_store
from ice_commons.config_settings import app_config
from dateutil.relativedelta import relativedelta
import uuid
from ice_rest.manager.analytics.botanalyticsapi import BotAnalyticsAPI

logger = logging.getLogger(__name__)
ds_manager = DatasourceManager()
project_manager = ProjectManager()
ice_entities_manager = IceEntitiesModelManager()

def remove_overlapping(def_tags, cust_tags):
    final_tags = cust_tags
    cust_tag_index_list = []
    for cust_tag_each in cust_tags:
        for i in range(cust_tag_each["start"], cust_tag_each["end"]):
            cust_tag_index_list.append(i)
    for def_tag_each in def_tags:
        def_tag_index_list = []
        for i in range(def_tag_each["start"], def_tag_each["end"]):
            def_tag_index_list.append(i)
        common_tags = list(set(def_tag_index_list).intersection(cust_tag_index_list))
        if len(common_tags) == 0:
            final_tags.append(def_tag_each)
    final_tags = sorted(final_tags, key=itemgetter('start'))
    return final_tags


def retag(serviceid, utterances, new_default_model_class, predefined_entities, project_config):
    store = get_model_store()

    for utterances_each in utterances:
        utterance = get(utterances_each, "utterance")
        case_converted_utterance = get(utterances_each, "case_converted_utterance")
        mapping = get(utterances_each, "mapping")
        mapping = json.loads(mapping)
        doc = {
            "serviceid": serviceid,
            "text": utterance
        }
        default_engine = get_engine(new_default_model_class)
        def_tags = store.tag_predefined(MODEL_TYPE_NER, default_engine, case_converted_utterance, utterance)
        def_tags = [tag for tag in def_tags if str(tag['tag']) in predefined_entities]
        final_tags = []
        cust_tags = get(mapping, "tags", [])
        final_tags = remove_overlapping(def_tags, cust_tags)
        mapping["tags"] = final_tags
        mapping = json.dumps(mapping)
        utterances_each["mapping"] = mapping
        utterances_each["ir_trained"] = False
        utterances_each["ner_trained"] = False
    return utterances


def untag_predefined(utterances, custom_entities):
    for utterances_each in utterances:
        mapping = get(utterances_each, "mapping")
        mapping = json.loads(mapping)
        tags = get(mapping, "tags")
        final_tags = []
        custom_entities= [x.lower() for x in custom_entities]
        for tags_each in tags:
            tag = tags_each['tag']
            tag=tag.lower()
            if tag in custom_entities:
                final_tags.append(tags_each)
        mapping["tags"] = final_tags
        mapping = json.dumps(mapping)
        utterances_each["mapping"] = mapping
    return utterances


def replace_predefined_entities(new_predefined_model):
    predefined_models = get_default_models()
    predefined_models = [each_model.lower() for each_model in predefined_models]
    new_predefined_entities = []
    if new_predefined_model.lower() in predefined_models:
        new_predefined_entities = get_entities_for_default_model(new_predefined_model)
    else:
        logger.error("Invalid model name specified!!!")
    return new_predefined_entities


def update_projects_collection(serviceid, predefined_model, custom_model):
    query = {
        "serviceid": serviceid
    }
    document = {
        "$set": {
            'predefined_entity_model': predefined_model,
            'custom_entity_model': custom_model
        }
    }
    project_manager.update_config(query, document)


def remove_from_minio(serviceid):
    if get_ner_status(serviceid) == 'trained' or get_ner_status(serviceid) == 'validated' or get_ner_status(serviceid) == 'training_failed':
        query = {
            "serviceid": serviceid
        }
        document = {
            "$set": {
                "ner.status": project_manager.STATUS_NEW,
                "ner.status_message": "Some checks haven't completed yet",
                "ir.status": project_manager.STATUS_NEW,
                "ir.status_message": "Some checks haven't completed yet"
            }
        }
        project_manager.update_config(query, document)
        VerbisStore().remove_models_from_remote(serviceid)


@route('/api/parse/retag')
class RetagWithPredefinedModel:
    def on_post(self, req, resp):
        log_flag = False
        if app_config['BOTANALYTICS_LOG_FLAG'].upper() == "ON":
            log_flag, req_id, botanalytics , start_time = True, str(uuid.uuid4()), BotAnalyticsAPI(), datetime.datetime.now()
        doc = req.context['doc'] or {}
        try:
            serviceid = doc["serviceid"]
            new_predefined_model = doc["predefined_model"]
            new_custom_model = doc["custom_model"]
            project_config = project_manager.find_config_by_id(serviceid)
            old_predefined_model = project_config["predefined_entity_model"]
            datasource = ds_manager.find_datasource_by_service_id(serviceid)
            if datasource is not None:
                utterances = get(datasource, "utterances", [])
                entities = get(datasource, "entities", [])
                patterns = get(datasource, "patterns", [])
                phrases = get(datasource, "phrases", [])
                for pattern_each in patterns:
                    entities.append(pattern_each["entity"])
                for phrase_each in phrases:
                    entities.append(phrase_each["entity"])
                    
                predefined_entities = get(datasource, "predefined_entities", [])

                if old_predefined_model != new_predefined_model:
                    predefined_entities = []
                    document = {
                        "$set": {
                            "model_updated_at": datetime.datetime.utcnow(),
                            "predefined_entities": predefined_entities
                        }
                    }
                    ds_manager.update_datasource_by_service_id(serviceid, document)
                else:
                    ice_entities_config = ice_entities_manager.get_ice_entities(project_config['language'])
                    if ice_entities_config is not None:
                        for item in ice_entities_config:
                            if item['name'] in predefined_entities:
                                entities.append(item['name'])
                                
                entities += predefined_entities
                updated_utterances = untag_predefined(utterances, entities)
                update_projects_collection(serviceid, new_predefined_model, new_custom_model)
                retagged_utterances = retag(serviceid, updated_utterances, new_predefined_model, predefined_entities, project_config)
                document = {
                    "$set": {
                        "model_updated_at": datetime.datetime.utcnow(),
                        "utterances": retagged_utterances
                    }
                }
                ds_manager.update_datasource_by_service_id(serviceid, document)

                remove_from_minio(serviceid)
                resp.data = {
                    "status": "Utterances retagged successfully"
                }
                resp.status = falcon.HTTP_200
            else:
                description = 'Unable to find datasource with given serviceid.'
                logger.error(description)

        except Exception as ex:
            logger.exception(ex)
            resp.data = {"msg": ex}
            resp.set_header('X-Powered-By', 'USTGlobal ICE')
            resp.status = falcon.HTTP_500

        finally:
            if log_flag:
                end_time = datetime.datetime.now()
                total_action_time = relativedelta(end_time, start_time)
                botanalytics.log(requesttype="nerrequests", serviceid=doc['serviceid'], req_id=req_id, action="RETAG", ner_req_timestamp=start_time.replace(microsecond=0).isoformat(), ner_req_end_timestamp=end_time.replace(microsecond=0).isoformat(), total_action_time=(total_action_time.hours*60*60*1000 + total_action_time.minutes*60*1000 + total_action_time.seconds*1000) + (total_action_time.microseconds / 1000))
