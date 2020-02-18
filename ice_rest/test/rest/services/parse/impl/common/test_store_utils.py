from ice_rest.rest.services.parse.impl.common.store_utils import get_requested_services


def test_get_requested_services_data():
    doc = dict(text="I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza",
               serviceid="MedicalAssistant-test", pos=True, intent=True, entity=True)
    resp = [('MedicalAssistant-test', 'ner', True), ('MedicalAssistant-test', 'ir', None)]
    requested_services = get_requested_services(doc)
    assert resp == requested_services


def test_get_requested_services_null():
    doc = {}
    resp = [(None, 'ner', 'yes'), (None, 'ir', None)]
    requested_services = get_requested_services(doc)
    assert resp == requested_services
