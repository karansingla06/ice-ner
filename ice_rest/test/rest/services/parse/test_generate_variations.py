from falcon import testing
import pytest,falcon, requests
from ice_rest.rest.services.parse.generate_variations import GenerateVariationsResource


class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/generate_variations', GenerateVariationsResource())
    client = falcon.testing.TestClient(api)
    return client

req_init = falcon.request.Request.__init__


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "text": "hello my name is karan",
        "serviceid": "abc"
    }}


class MockPostRequest():
    def __init__(self, code):
        self.status_code = code
        self.content= '[]'


def test_generate_variations_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.generate_variations.DatasourceManager.find_datasource_by_service_id', return_value= {'utterances':[{'utterance':'hello'},{'utterance':'how are you?'}]})
    mocker.patch('ice_rest.rest.services.parse.generate_variations.requests.post', return_value= MockPostRequest(200))
    mocker.patch('ice_rest.rest.services.parse.generate_variations.ast.literal_eval', return_value= ['hiii','hola', 'hello'])
    resp = client.simulate_post('/api/parse/generate_variations', headers=headers)
    assert resp.status_code == 200


def test_generate_variations_api12(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.generate_variations.DatasourceManager.find_datasource_by_service_id', return_value= {'utterances':[{'utterance':'hello'},{'utterance':'how are you?'}]})
    mocker.patch('ice_rest.rest.services.parse.generate_variations.requests.post', return_value= MockPostRequest(404))
    mocker.patch('ice_rest.rest.services.parse.generate_variations.ast.literal_eval', return_value= ['hiii','hola', 'hello'])
    resp = client.simulate_post('/api/parse/generate_variations', headers=headers)
    assert resp.status_code == 200


def test_generate_variations_api2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.generate_variations.DatasourceManager.find_datasource_by_service_id',side_effect=Exception('foo'))

    resp = client.simulate_post('/api/parse/generate_variations', headers=headers)
    assert resp.status_code == 503


def test_generate_variations_api3(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.generate_variations.DatasourceManager.find_datasource_by_service_id',side_effect=AssertionError('foo'))
    resp = client.simulate_post('/api/parse/generate_variations', headers=headers)
    assert resp.status_code == 400

def test_generate_variations_api4(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.generate_variations.DatasourceManager.find_datasource_by_service_id',side_effect=requests.exceptions.RequestException('foo'))
    resp = client.simulate_post('/api/parse/generate_variations', headers=headers)
    assert resp.status_code == 200


def mock_init2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "any_other_field": "hello"
    }}

def test_generate_variations_api5(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    resp = client.simulate_post('/api/parse/generate_variations', headers=headers)
    assert resp.status_code == 400