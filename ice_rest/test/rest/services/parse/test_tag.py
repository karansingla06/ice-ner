from falcon import testing
import pytest,falcon
from ice_rest.rest.services.parse.tag import TagResource, BotAnalyticsAPI


@pytest.fixture()
def client():
    api = falcon.API()
    api.add_route('/api/parse/tag', TagResource())
    client = falcon.testing.TestClient(api)
    return client


req_init = falcon.request.Request.__init__


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "text": "hello",
        "serviceid": "abc"
    }}


def test_tag_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.tag.tag', return_value=None)
    app_config= mocker.patch('ice_rest.rest.services.parse.tag.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'OFF'
    resp = client.simulate_post('/api/parse/tag', headers=headers)
    assert resp.status_code == 200


def test_predict_api2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.tag.tag',return_value = None)
    mocker.patch('ice_rest.rest.services.parse.tag.app_config', {'BOTANALYTICS_LOG_FLAG':'ON'})
    m = mocker.patch.object(BotAnalyticsAPI, "log")
    m.side_effect = [None,None]
    resp = client.simulate_post('/api/parse/tag', headers=headers)
    assert resp.status_code == 503


def mock_init2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "text": "hello"
    }}

def test___validate_tag_request(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    expected = mocker.patch('ice_rest.rest.services.parse.tag._validate_tag_request', {'description': 'Mandatory params missing from the request. Please check your request params and retry',
          'title': 'HTTP Bad Request'})
    response = client.simulate_post('/api/parse/tag', headers=headers)

    assert response.status == falcon.HTTP_400
    assert response.json == expected


