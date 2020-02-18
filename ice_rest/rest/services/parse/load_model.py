import logging

from ice_rest.rest.services.parse.impl.common.store_utils import get_model_store
from ice_commons.core.model_utils import get_engine
logger = logging.getLogger(__name__)

def cache_model(config,requested_services):
     for service_each in requested_services:
        serviceid = service_each[0]
        model_type = service_each[1]
        engine=""
        model_class = None
        if config[model_type]["status"] == 'trained' or config[model_type]["status"] == 'validated' or config[model_type]["status"] == 'validating':
            if model_type=="ner":
                model_class = config['custom_entity_model']
                engine = get_engine(model_class)
                model_name = serviceid + "-" + engine+ "-" +model_type
                last_trained = config["ner"]["last_trained"]
            else:
                model_name = serviceid + "-" +model_type
                last_trained = config["ir"]["last_trained"]
            get_model_store().store.check_trained_time_and_reload(model_name, last_trained, serviceid, model_type, engine, model_class)
