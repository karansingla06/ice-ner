import falcon
import pytest
from falcon import testing, Request

from ice_rest.rest.exception.notfound import InsufficientDataError
from ice_rest.rest.services.parse.validation_test_data import ValidateParseResource, updateStatus, get_predict_api_url

req_init = falcon.request.Request.__init__


def mock_init_validate(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "serviceid": "abc"
    }}

def mock_init_validate_null(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
    }}


class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'


@pytest.fixture()
def client():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/validate', ValidateParseResource())
    client = falcon.testing.TestClient(api)
    return client


def test_validate_api_validated(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_validate)
    obj = ValidateParseResource()
    mocker.patch.object(obj, '_validate_model_config')
    manager = mocker.patch('ice_rest.rest.services.parse.validation_test_data.manager')
    manager.find_config_by_id.return_value = {"ner": {"status": "validated"}}
    mocker.patch('ice_rest.rest.services.parse.validation_test_data.updateStatus')
    mocker.patch('ice_rest.rest.services.parse.validation_test_data.validate_test_data.delay')
    headers = {"Content-Type": "application/json"}
    resp = client.simulate_post('/api/parse/validate', headers=headers)
    assert resp.status_code == 200


def test_validate_api_new(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_validate)
    obj = ValidateParseResource()
    mocker.patch.object(obj, '_validate_model_config')
    # mocker.patch('ice_rest.rest.services.parse.validation_test_data._validate_model_config')
    mocker.patch('ice_rest.rest.services.parse.validation_test_data.get_predict_api_url')
    manager = mocker.patch('ice_rest.rest.services.parse.validation_test_data.manager')
    manager.find_config_by_id.return_value = {"ner": {"status": "new"}}
    mocker.patch('ice_rest.rest.services.parse.validation_test_data.updateStatus')
    mocker.patch('ice_rest.rest.services.parse.validation_test_data.validate_test_data.delay')
    headers = {"Content-Type": "application/json"}
    resp = client.simulate_post('/api/parse/validate', headers=headers)
    assert resp.status_code == 200


def test_validate_api_exception(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_validate_null)
    obj = ValidateParseResource()
    mocker.patch.object(obj, '_validate_model_config')
    mocker.patch('ice_rest.rest.services.parse.validation_test_data.get_predict_api_url')
    manager = mocker.patch('ice_rest.rest.services.parse.validation_test_data.manager')
    manager.find_config_by_id.return_value = {}
    mocker.patch('ice_rest.rest.services.parse.validation_test_data.updateStatus')
    mocker.patch('ice_rest.rest.services.parse.validation_test_data.validate_test_data.delay')
    headers = {"Content-Type": "application/json"}
    resp = client.simulate_post('/api/parse/validate', headers=headers)
    assert resp.status_code == 400


def test_updateStatus(mocker):
    manager = mocker.patch('ice_rest.rest.services.parse.validation_test_data.manager')
    manager.find_model.return_value = {}
    manager.update_config.return_value = None
    resp = updateStatus("service_id")
    assert resp == None


def test_get_predict_api_url():
    env = testing.create_environ(
        path='/api/parse/validate',)
    req = Request(env)
    resp = get_predict_api_url(req)
    assert resp == 'http://falconframework.org/api/parse/predict'


def test_validate_api_exception1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_validate)
    obj = ValidateParseResource()
    mocker.patch.object(obj, '_validate_model_config')
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.validation_test_data.get_predict_api_url')
    mocker.patch('ice_rest.rest.services.parse.validation_test_data.ProjectManager.find_config_by_id', side_effect=Exception('foo'))
    resp = client.simulate_post('/api/parse/validate', headers=headers)
    print(resp.status_code)
    assert resp.status_code == 503
