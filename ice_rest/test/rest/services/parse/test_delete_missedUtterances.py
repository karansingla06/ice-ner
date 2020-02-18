from falcon import testing
import pytest, falcon
from ice_rest.rest.services.parse.delete_missedUtterances import DeleteMissedUtterances


class TestDeleteMissedUtterancesMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client():
    api = falcon.API(middleware=TestDeleteMissedUtterancesMiddleware())
    api.add_route('/api/parse/delete_missed_utterances', DeleteMissedUtterances())
    client = falcon.testing.TestClient(api)
    return client

req_init = falcon.request.Request.__init__


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "serviceid": "abc",
        'text' : 'xyz'
    }}

def mock_init2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "serviceid": "abc",
        'text' : 'xyz'
    }}


def mock_init3(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "any_other_field": "hello"
    }}

def test_delete_missed_utterances_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.delete_missedUtterances.DatasourceManager.find_datasource_by_service_id', return_value= {'missedUtterances' : ['c','b']})
    mocker.patch('ice_rest.rest.services.parse.delete_missedUtterances.decrypt', side_effect= ['a','b'])
    resp = client.simulate_post('/api/parse/delete_missed_utterances', headers=headers)
    assert resp.status_code == 200


def test_delete_missed_utterances_api2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    m = mocker.patch('ice_rest.rest.services.parse.delete_missedUtterances.manager')
    mocker.patch.object(m , 'find_datasource_by_service_id', return_value= {'missedUtterances' : ['a','f']})
    mocker.patch('ice_rest.rest.services.parse.delete_missedUtterances.decrypt', side_effect= ['c','xyz'])
    resp = client.simulate_post('/api/parse/delete_missed_utterances', headers=headers)
    assert resp.status_code == 200


def test_delete_missed_utterances_api3(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init3)
    headers = {"Content-Type": "application/json"}
    resp = client.simulate_post('/api/parse/delete_missed_utterances', headers=headers)
    assert resp.status_code == 500