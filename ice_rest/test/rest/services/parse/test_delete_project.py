from falcon import testing
import pytest,falcon
from ice_rest.rest.services.parse.delete_project import DeleteProject, delete_project_if_exists, uncache_project_if_exists


class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/delete_project', DeleteProject())
    client = falcon.testing.TestClient(api)
    return client

req_init = falcon.request.Request.__init__


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "serviceid": "abc"
    }}


def test_delete_project_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.delete_project.uncache_project_if_exists', return_value= None)
    resp = client.simulate_post('/api/parse/delete_project', headers=headers)
    assert resp.status_code == 200

def test_delete_project_api2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.delete_project.uncache_project_if_exists', side_effect= AssertionError('foooo'))
    resp = client.simulate_post('/api/parse/delete_project', headers=headers)
    assert resp.status_code == 412

def test_delete_project_api3(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.delete_project.uncache_project_if_exists', side_effect= Exception('foooo'))
    resp = client.simulate_post('/api/parse/delete_project', headers=headers)
    assert resp.status_code == 503

def mock_init2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "any_other_field": "hello"
    }}

def test_delete_project_api4(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    resp = client.simulate_post('/api/parse/delete_project', headers=headers)
    assert resp.status_code == 400


def test_delete_project_if_exists(mocker):
    mocker.patch('ice_rest.rest.services.parse.delete_project.ProjectManager')
    mocker.patch('ice_rest.rest.services.parse.delete_project.DatasourceManager')
    res = delete_project_if_exists('aa')
    assert res == None


def test_uncache_project_if_exists1(mocker):
    mocker.patch('ice_rest.rest.services.parse.delete_project.uncache_project_if_exists')
    m= mocker.patch('ice_rest.rest.services.parse.delete_project.get_model_store')
    m.return_value.get_active_models.return_value = ['a','b']
    mocker.patch('ice_rest.rest.services.parse.delete_project.get_model_name',return_value = 'a')
    mocker.patch('ice_rest.rest.services.parse.delete_project.ProjectManager')
    mocker.patch('ice_rest.rest.services.parse.delete_project.DatasourceManager')
    mocker.patch('ice_rest.rest.services.parse.delete_project.os.path.exists', return_value= True)
    mocker.patch('ice_rest.rest.services.parse.delete_project.shutil.rmtree', return_value= None)
    res = uncache_project_if_exists('aa')
    assert res == None


def test_uncache_project_if_exists2(mocker):
    mocker.patch('ice_rest.rest.services.parse.delete_project.uncache_project_if_exists')
    m= mocker.patch('ice_rest.rest.services.parse.delete_project.get_model_store')
    m.return_value.get_active_models.return_value = ['a','b']
    mocker.patch('ice_rest.rest.services.parse.delete_project.get_model_name',return_value = 'a')
    mocker.patch('ice_rest.rest.services.parse.delete_project.ProjectManager.find_model', return_value= None)
    mocker.patch('ice_rest.rest.services.parse.delete_project.DatasourceManager')
    mocker.patch('ice_rest.rest.services.parse.delete_project.os.path.exists', return_value= True)
    mocker.patch('ice_rest.rest.services.parse.delete_project.shutil.rmtree', return_value= None)
    res = uncache_project_if_exists('aa')
    assert res == None