from falcon import testing
import pytest,falcon
from ice_rest.rest.services.parse.tokenize import TokenizeParseResource


class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/tokenize', TokenizeParseResource())
    client = falcon.testing.TestClient(api)
    return client

req_init = falcon.request.Request.__init__


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "text": "hello my name is karan"
    }}


def test_tokenize_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.tokenize', return_value= [])
    resp = client.simulate_post('/api/parse/tokenize', headers=headers)
    assert resp.status_code == 200


def test_tokenize_api2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.tokenize.tokenize_utterance', side_effect=Exception('foo'))
    resp = client.simulate_post('/api/parse/tokenize', headers=headers)
    assert resp.status_code == 503


def mock_init2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "any_other_field": "hello"
    }}

def test_tokenize_api3(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    resp = client.simulate_post('/api/parse/tokenize', headers=headers)
    assert resp.status_code == 400