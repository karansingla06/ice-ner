import logging

from pydash import get
from ice_commons.store.models import ModelStore
from ice_commons.utils import get_model_name, MODEL_TYPE_IR, MODEL_TYPE_NER

logger = logging.getLogger(__name__)

model_store = ModelStore()

##The order of adding services in this list is inportant.
# NER should be added first.
##
def get_requested_services(doc):
    serviceid = get(doc,'serviceid')
    intent = get(doc, 'intent', default=True)
    ner = get(doc, 'entity', default=True)
    pos = get (doc, 'pos', default='yes')
    requested_services = []
    if ner is True:
        requested_services.append((serviceid, MODEL_TYPE_NER,pos))
    if intent is True:
        requested_services.append((serviceid, MODEL_TYPE_IR, None))
    return requested_services


def get_requested_service_names(doc):
    def _get_model_name(dct):
        return get_model_name(*dct)
    return list(map(_get_model_name, get_requested_services(doc)))

def get_model_store():
    return  model_store
