from falcon import testing
import pytest,falcon
from ice_rest.rest.services.parse.fetch_missedUtterances import DecryptMissedUtterances


class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/fetch_missed_utterances', DecryptMissedUtterances())
    client = falcon.testing.TestClient(api)
    return client

req_init = falcon.request.Request.__init__


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "serviceid": "abc"
    }}


def test_fetch_missed_utterances_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.fetch_missedUtterances.DatasourceManager.find_datasource_by_service_id', return_value= {'missedUtterances' : ['a','b']})
    mocker.patch('ice_rest.rest.services.parse.fetch_missedUtterances.decrypt', return_value= None)
    resp = client.simulate_post('/api/parse/fetch_missed_utterances', headers=headers)
    assert resp.status_code == 200


def mock_init2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "any_other_field": "hello"
    }}

def test_fetch_missed_utterances_api3(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    resp = client.simulate_post('/api/parse/fetch_missed_utterances', headers=headers)
    assert resp.status_code == 500