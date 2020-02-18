from pydash import get
from ice_commons.data.dl.manager import ProjectManager, DatasourceManager


def get_predefined_entities(serviceid):
    manager = DatasourceManager()
    query = {"serviceid": serviceid}
    ds = manager.find_model(query)
    return get(ds, "predefined_entities", default=[])


def get_custom_entities(serviceid):
    manager = DatasourceManager()
    query = {"serviceid": serviceid}
    ds = manager.find_model(query)
    return get(ds, "entities", default=[])


def get_pattern_entities(serviceid):
    manager = DatasourceManager()
    query = {"serviceid": serviceid}
    ds = manager.find_model(query)
    return get(ds, "patterns", default=[])


def get_phrase_entities(serviceid):
    manager = DatasourceManager()
    query = {"serviceid": serviceid}
    ds = manager.find_model(query)
    return get(ds, "phrases", default=[])


def get_custom_class_name(serviceid):
    manager = ProjectManager()
    query = {"serviceid": serviceid}
    ds = manager.find_model(query)
    return get(ds, "custom_entity_model", default=[])


def get_ner_status(serviceid):
    manager = ProjectManager()
    query = {"serviceid": serviceid}
    ds = manager.find_model(query)
    return get(ds, "ner.status", default=[])


def get_corenlp_modelname(serviceid):
    manager = ProjectManager()
    query = {"serviceid": serviceid}
    ds = manager.find_model(query)
    return get(ds, "corenlp_model_name", default=None)


def put_corenlp_modelname(serviceid, model_name):
    manager = ProjectManager()
    query = {
        "serviceid": serviceid
    }
    document = {
        "$set": {
            "corenlp_model_name": model_name.split("/")[-1]
        }
    }
    manager.update_config(query, document)
