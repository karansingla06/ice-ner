import pytest
import falcon
from falcon import testing
from ice_rest.rest.services.parse.datasource_config import get_datasource, get_datasource_id, GetDataSourceConfig
from ice_commons.data.dl.manager import DatasourceManager

class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'


@pytest.fixture()
def client_datasource():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/getDataSourceConfig', GetDataSourceConfig())
    client = falcon.testing.TestClient(api)
    return client


req_init = falcon.request.Request.__init__


def mock_init_datasource(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {"id0": "5a9d085cbc34e9f64513cd82", "id1": "5a9e819abc34e9f64513fe62"}}


def test_get_datasource_config_api1(client_datasource, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_datasource)
    headers = {"Content-Type": "application/json", "organisation-name": "USTGlobal"}
    mocker.patch('ice_rest.rest.services.parse.datasource_config.get_datasource', return_value=[True])
    resp = client_datasource.simulate_post('/api/parse/getDataSourceConfig', headers=headers)
    assert resp.status_code == 200

def test_get_datasource(mocker):
    mocker.patch.object(DatasourceManager, 'find', return_value=True)
    return_value = {"datasource": "123456"}
    mocker.patch('ice_rest.rest.services.parse.datasource_config.get_datasource_id', return_value=return_value)
    res = get_datasource("123456987456")
    assert res

