import logging

from pydash import get

from ice_rest.rest.services.parse.impl.common.store_utils import get_model_store
from ice_commons.data.dl.manager import ProjectManager, DatasourceManager

from ice_commons.core.model_utils import get_engine, get_all_corenlp_engines
from ice_commons.store.util import get_model_name

logger = logging.getLogger(__name__)
#store = get_model_store()
project_manager = ProjectManager()
datasource_manager = DatasourceManager()


def remove_resolved_to(response):
    default = response['default_tags'] if 'default_tags' in response else []
    custom = response['custom_tags'] if 'custom_tags' in response else []
    for map in default:
        if 'resolvedTo' in map:
            del map['resolvedTo']
    for map in custom:
        if 'resolvedTo' in map:
            del map['resolvedTo']
    response['default_tags'] = default
    response['custom_tags'] = custom
    return response


def tag(doc):
    store = get_model_store()
    text = get(doc, "text",default='')
    text= text.replace('\xa0', ' ')
    service_id = get(doc, "serviceid", default=None)
    text, original_text = store.change_case(text)
    query = {
        "serviceid": service_id
    }

    corpus = datasource_manager.find_datasource_by_service_id(doc["serviceid"])
    config = project_manager.find_model(query)
    datasources_map = {"predefined_entities": get(corpus, "predefined_entities", default=[]),
                       "entities": get(corpus, "entities", default=[]),
                       "patterns": get(corpus, "patterns", default=[]), "phrases": get(corpus, "phrases", default=[]),
                       "distinct_token_list": get(corpus, "distinct_token_list", default=[]),
                       "intents": get(corpus, "intents", default=[])}
    projects_map = {"custom_entity_model": get(config, "custom_entity_model", default=None),
                    "ner_status": get(config, "ner.status", default=[]),
                    "language" : get(config, 'language', 'EN')}

    default_class_name = get(config,'predefined_entity_model', None)
    custom_class_name = get(config, 'custom_entity_model', None)
    engine = get_engine(custom_class_name)
    last_trained = get(config, "ner.last_trained", default=None)
    default_engine = get_engine(default_class_name)
    model_name = get_model_name(service_id, "ner", engine)

    if get_engine(custom_class_name) not in get_all_corenlp_engines():
        if get(config, "ner.status", default=None) in ['trained', 'validated']:
           get_model_store().store.check_trained_time_and_reload(model_name, last_trained, service_id, "ner", engine, custom_class_name)

    response = store.tag(service_id, text, original_text, engine, default_engine, default_class_name, datasources_map,
                         projects_map)

    response = remove_resolved_to(response)

    return response
