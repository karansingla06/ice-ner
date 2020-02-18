from falcon import testing
import pytest, falcon
from ice_rest.rest.services.parse.update_datasource import UpdateDatasource
from ice_commons.data.dl.manager import DatasourceManager

class TestUpdateDatasourceMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client():
    api = falcon.API(middleware=TestUpdateDatasourceMiddleware())
    api.add_route('/api/parse/update_datasource', UpdateDatasource())
    client = falcon.testing.TestClient(api)
    return client

req_init = falcon.request.Request.__init__


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': 
        {
            "input": {
                "clientMutationId": "random",
                "entities": [],
                "utterances": [
                    {
                        "utterance": "hi",
                        "case_converted_utterance": "Hi",
                        "mapping": "{\"tokens\":[\"Hi\"],\"tags\":[\"intent\":\"Nointent\"}",
                        "ir_trained": "false",
                        "ner_trained": "false"
                    }
                ],
                "patterns": [],
                "trainIntent": "true",
                "trainEntity": "true",
                "serviceid": "MedicalAssistant-En",
                "intents": [
                    {
                        "name": "qqq",
                        "description": "",
                        "createdAt": "2019-06-19T09:25:21.136Z",
                        "modifiedAt": "2019-06-19T09:25:21.136Z"
                    }
                ],
                "synonyms": [],
                "phrases": [],
                "predefined_entities": [],
                "id": "RGF0YXNvdXJjZTo1Y2UyNzRhZDllOWNmNzFlY2RhMDIzNmI="
            },
            "projectId": "5ce274ac9e9cf71ecda02365",
            "userId": "5a7d6b6992a9f054c2bad645"
        }
    }

   


def test_update_datasource_api1(client,mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    manager = mocker.patch('ice_rest.rest.services.parse.update_datasource.DatasourceManager', return_value=DatasourceManager())
    mocker.patch('ice_rest.rest.services.parse.update_datasource.DatasourceManager.update_datasource', return_value = None)
    resp = client.simulate_post('/api/parse/update_datasource', headers=headers)
    assert resp.status_code == 200


def test_update_datasource_api2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.update_datasource.DatasourceManager.update_datasource',side_effect=AssertionError('foo'))
    resp = client.simulate_post('/api/parse/update_datasource', headers=headers)
    assert resp.status_code == 400

def test_update_datasource_api3(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.update_datasource.DatasourceManager.update_datasource',side_effect= Exception('foooo'))
    resp = client.simulate_post('/api/parse/update_datasource', headers=headers)
    assert resp.status_code == 503