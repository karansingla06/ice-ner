from falcon import testing
import pytest, falcon
from ice_rest.rest.services.parse.predict import validate_prediction_request, validate_service_id_and_cache, \
    update_last_access_to_predict_api, PredictionResource, PredictionResource_V1
from ice_commons.data.dl.manager import ProjectManager


class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client_predict():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/predict', PredictionResource())
    client = falcon.testing.TestClient(api)
    return client


@pytest.fixture()
def client_predictv1():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/v1/predict', PredictionResource_V1())
    client = falcon.testing.TestClient(api)
    return client


req_init = falcon.request.Request.__init__


def mock_init_predict(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "text": "hello",
        "serviceid": "abc"
    }}


def test_validate_service_id_and_cache_null(mocker):
    manager = mocker.patch('ice_rest.rest.services.parse.predict.ProjectManager', return_value=ProjectManager())
    mocker.patch.object(manager.return_value, 'find_model', return_value=None)
    with pytest.raises(Exception) as exception:
        assert validate_service_id_and_cache({})
    assert str(exception.value) == "Invalid Service ID."


def test_validate_service_id_and_cache_data(mocker):
    doc = dict(text="I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza",
               serviceid="MedicalAssistant-test", pos=True, intent=True, entity=True)
    conf = dict(predefined_entity_model="ice_commons.er.engines.spacy_ner.SpacyDefaultNER",
                custom_entity_model="ice_commons.er.engines.mitie_ner.MitieCustomNER",
                serviceid="MedicalAssistant-test", language="EN", ner=dict(status="new"), ir=dict(status="new"))
    manager = mocker.patch('ice_rest.rest.services.parse.predict.ProjectManager', return_value=ProjectManager())
    mocker.patch.object(manager.return_value, 'find_model', return_value=conf)
    mocker.patch('ice_rest.rest.services.parse.predict.get_requested_services',
                 return_value=[('MedicalAssistant-test', 'ner', True),
                               ('MedicalAssistant-test', 'ir', None)])
    mocker.patch('ice_rest.rest.services.parse.predict.cache_model', return_value=None)
    config = validate_service_id_and_cache(doc)
    assert config == conf


def test_update_last_access_to_predict_api(mocker):
    manager = mocker.patch('ice_rest.rest.services.parse.predict.ProjectManager', return_value=ProjectManager())
    mocker.patch.object(manager.return_value, 'update_config', return_value=None)
    assert update_last_access_to_predict_api("") == None


def test_validate_prediction_request_data():
    doc = dict(text="Aswathi uses Zeecold for headache", serviceid="MedicalAssistant-test")
    a = validate_prediction_request(doc)
    assert a is None


def test_validate_prediction_request_null():
    doc = {}
    with pytest.raises(falcon.HTTPBadRequest):
        assert validate_prediction_request(doc)


def test_predict_api_BOTANALYTICS_FLAG_OFF(client_predict, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_predict)
    app_config= mocker.patch('ice_rest.rest.services.parse.predict.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'OFF'
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.predict.validate_prediction_request', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.predict.validate_service_id_and_cache', return_value = {})
    mocker.patch('ice_rest.rest.services.parse.predict.predict_impl', return_value="{'entities':[],'intent':''}")
    mocker.patch('ice_rest.rest.services.parse.predict.update_last_access_to_predict_api', return_value=None)
    resp = client_predict.simulate_post('/api/parse/predict', headers=headers)
    assert resp.status_code == 200


def test_predict_api_BOTANALYTICS_FLAG_ON(client_predict, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_predict)
    app_config= mocker.patch('ice_rest.rest.services.parse.predict.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'ON'
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.predict.validate_prediction_request', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.predict.validate_service_id_and_cache', return_value = {})
    mocker.patch('ice_rest.rest.services.parse.predict.predict_impl', return_value=[])
    mocker.patch('ice_rest.rest.services.parse.predict.update_last_access_to_predict_api', return_value=None)
    resp = client_predict.simulate_post('/api/parse/predict', headers=headers)
    assert resp.status_code == 200

def test_predict_api__exception(client_predict, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_predict)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.predict.validate_prediction_request', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.predict.validate_service_id_and_cache', return_value = {})
    mocker.patch('ice_rest.rest.services.parse.predict.predict_impl', return_value=[])
    mocker.patch('ice_rest.rest.services.parse.predict.update_last_access_to_predict_api', return_value=None)
    resp = client_predict.simulate_post('/api/parse/predict', headers=headers)
    assert resp.status_code == 503


def test_v1_predict_api_BOTANALYTICS_FLAG_OFF(client_predictv1, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_predict)
    app_config= mocker.patch('ice_rest.rest.services.parse.predict.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'OFF'
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.predict.predict_impl', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.predict.modify_response_v1', return_value="")
    resp = client_predictv1.simulate_post('/api/parse/v1/predict', headers=headers)
    assert resp.status_code == 200



def test_v1_predict_api_BOTANALYTICS_FLAG_ON(client_predictv1, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_predict)
    app_config= mocker.patch('ice_rest.rest.services.parse.predict.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'ON'
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.predict.predict_impl', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.predict.modify_response_v1', return_value="")
    resp = client_predictv1.simulate_post('/api/parse/v1/predict', headers=headers)


def test_v1_predict_exception(client_predictv1, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_predict)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.predict.predict_impl', return_value=None)
    resp = client_predictv1.simulate_post('/api/parse/v1/predict', headers=headers)
    assert resp.status_code == 503