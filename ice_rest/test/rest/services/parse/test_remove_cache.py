
import logging
from falcon import testing
import pytest,falcon
logger = logging.getLogger()

from ice_rest.rest.appengine import AppEngine
from ice_rest.rest.services.parse.remove_cache import RemoveCacheResource


@pytest.fixture()
def client():
    api = falcon.API()
    api.add_route('/api/parse/cache/remove', RemoveCacheResource())
    client = falcon.testing.TestClient(api)
    return client


req_init = falcon.request.Request.__init__


def mock_init1(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
                        "serviceid": None,
                        }}

def test_remove_cache_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init1)
    headers = {"Content-Type": "application/json"}
    model_store = mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_store')
    model_store.get_active_models.return_value= ""
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.find_model', return_value = None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.update_config', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_name', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.sep', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.join', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.exists', return_value=None)
    resp = client.simulate_post('/api/parse/cache/remove', headers=headers)
    assert resp.status_code == 200



def mock_init2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
                        "serviceid": "XYZ",
                        }}

def test_remove_cache_api2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    model_store = mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_store')
    model_store.get_active_models.return_value= ['a','b','c','d']
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.find_model', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.update_config', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_name', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.sep', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.join', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.exists', return_value=None)
    resp = client.simulate_post('/api/parse/cache/remove', headers=headers)
    assert resp.status_code == 200

def test_remove_cache_api3_without_null(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    model_store = mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_store')
    model_store.return_value.get_active_models.return_value= ['a','b','c']
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.find_model', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.update_config', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_name', return_value='a')
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.sep', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.join', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.exists', return_value=True)
    resp = client.simulate_post('/api/parse/cache/remove', headers=headers)
    assert resp.status_code == 503

def test_remove_cache_api_with_exception2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init1)
    headers = {"Content-Type": "application/json"}
    model_store = mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_store')
    model_store.get_active_models.return_value= ""
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.find_model', side_effect = Exception('foo'))
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.update_config', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_name', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.sep', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.join', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.exists', return_value=None)
    resp = client.simulate_post('/api/parse/cache/remove', headers=headers)
    assert resp.status_code == 503

def test_remove_cache_api_with_exception1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init1)
    headers = {"Content-Type": "application/json"}
    model_store = mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_store')
    model_store.get_active_models.return_value= ""
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.find_model', return_value = None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.update_config', return_value = None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_name', side_effect = Exception('foo'))
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.sep', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.join', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.exists', return_value=None)
    resp = client.simulate_post('/api/parse/cache/remove', headers=headers)
    assert resp.status_code == 503

def test_remove_cache_api_with_AssertionError(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init1)
    headers = {"Content-Type": "application/json"}
    model_store = mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_store')
    model_store.get_active_models.return_value= ""
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.find_model', return_value = None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.ProjectManager.update_config', return_value = None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.get_model_name', side_effect = AssertionError('new'))
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.sep', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.join', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.remove_cache.os.path.exists', return_value=None)
    resp = client.simulate_post('/api/parse/cache/remove', headers=headers)
    assert resp.status_code == 412