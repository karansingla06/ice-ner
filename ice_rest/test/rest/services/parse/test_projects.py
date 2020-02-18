from falcon import testing
import pytest,falcon
from ice_rest.rest.services.parse.projects import FetchProject, fetch_project_if_exists
from ice_rest.rest.services.parse.projects import CreateProject, save_project
from ice_commons.data.dl.manager import ProjectManager, ProjectconfigsManager
from ice_rest.rest.services.parse.projects import DeleteProject, UpdateProject, delete_project_if_exists, update_project_if_exists

class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client_fetch():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/projects/fetch_project', FetchProject())
    client = falcon.testing.TestClient(api)
    return client

@pytest.fixture()
def client():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/projects/create_project', CreateProject())
    client = falcon.testing.TestClient(api)
    return client

req_init = falcon.request.Request.__init__

def mock_init_fetch(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        u"json":{u"serviceid": u"abc"}
    }}

def mock_init_fetch1(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
    }}

def mock_init_fetch2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': { u"serviceid":""
    }}

def test_fetch_project_api(client_fetch, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_fetch)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.fetch_project_if_exists', return_value={"abc":"123"})
    resp = client_fetch.simulate_post('/api/parse/projects/fetch_project', headers=headers)
    assert resp.status_code == 200

def test_fetch_project_api1(client_fetch, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_fetch1)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.fetch_project_if_exists', return_value=False)
    resp = client_fetch.simulate_post('/api/parse/projects/fetch_project', headers=headers)
    assert resp.status_code == 503

def test_fetch_project_api2(client_fetch, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_fetch)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.fetch_project_if_exists', side_effect= AssertionError('foooo'))
    resp = client_fetch.simulate_post('/api/parse/projects/fetch_project', headers=headers)
    assert resp.status_code == 412

def test_fetch_project_api3(client_fetch, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_fetch)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.fetch_project_if_exists', side_effect= Exception('foooo'))
    resp = client_fetch.simulate_post('/api/parse/projects/fetch_project', headers=headers)
    assert resp.status_code == 503

def test_fetch_project_api4(client_fetch, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_fetch)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.fetch_project_if_exists', return_value=None)
    resp = client_fetch.simulate_post('/api/parse/projects/fetch_project', headers=headers)
    assert resp.status_code == 200

def test_fetch_project_if_exists1(mocker):
    res = fetch_project_if_exists('12345789')
    assert res == False

def test_fetch_project_if_exists2(mocker):
    mocker.patch.object(ProjectManager, 'exists', return_value=True)
    mocker.patch.object(ProjectManager, 'find_one', return_value=True)
    res = fetch_project_if_exists('123456789')
    assert res


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {"doc":{
                        "data": {
                            "addProject": {
                                "changedProjectEdge": {
                                    "node": {
                                        "serviceid": "test",
                                        "name": "devtesting1",
                                        "desc": "dev testing1"
                                    }
                                }
                            }
                        }
                    }
                }

test_project_data = {
                        "serviceid": "testid123",
                        "name": "devtesting1",
                        "desc": "dev testing1"
                    }

# test cases for create project

def test_create_project_success(client, mocker):        
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.save_project', return_value=None)
    resp = client.simulate_post('/api/parse/projects/create_project',headers=headers)
    assert resp.status_code == 200

def test_create_project_asserterr(client, mocker):   
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.save_project', side_effect=AssertionError('Generate assertion error'))
    resp = client.simulate_post('/api/parse/projects/create_project',headers=headers)
    assert resp.status_code == 412

def test_create_project_excep(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.save_project', side_effect=Exception('Generate exception'))
    resp = client.simulate_post('/api/parse/projects/create_project', headers=headers)
    assert resp.status_code == 503

def test_save_project_success(mocker):
    res = save_project(test_project_data)    
    assert res

def test_save_project_fail(mocker):
    res = save_project({})    
    assert res == False

# test cases for  update/delete project
@pytest.fixture()
def client_delete():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/projects/delete_project', DeleteProject())
    client = falcon.testing.TestClient(api)
    return client

@pytest.fixture()
def client_update():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/projects/update_project', UpdateProject())
    client = falcon.testing.TestClient(api)
    return client


req_init = falcon.request.Request.__init__


def mock_init_delete(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        u"serviceid": u"abc"
    }}

def mock_init_delete1(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        u"serviceid": ""
    }}

def mock_init_delete2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
    }}

def mock_init_update(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        u"serviceid": u"abc",u"json":{u"name" : u"abc"}
    }}

def test_delete_project_api1(client_delete, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_delete)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.delete_project_if_exists', return_value=False)
    resp = client_delete.simulate_post('/api/parse/projects/delete_project', headers=headers)
    assert resp.status_code == 200

def test_delete_project_api2(client_delete, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_delete)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.delete_project_if_exists', return_value=True)
    resp = client_delete.simulate_post('/api/parse/projects/delete_project', headers=headers)
    assert resp.status_code == 200

def test_delete_project_api3(client_delete, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_delete2)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.delete_project_if_exists', return_value=False)
    resp = client_delete.simulate_post('/api/parse/projects/delete_project', headers=headers)
    assert resp.status_code == 503

def test_delete_project_api4(client_delete, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_delete1)
    headers = {"Content-Type": "application/json"}
    resp = client_delete.simulate_post('/api/parse/projects/delete_project', headers=headers)
    assert resp.status_code == 412


def test_delete_project_if_exists1(mocker):
    mocker.patch.object(ProjectManager, 'exists', return_value=True)
    mocker.patch.object(ProjectManager, 'delete', return_value=True)
    mocker.patch.object(ProjectconfigsManager, 'delete', return_value=True)
    res = delete_project_if_exists('123456987456')
    assert res


def test_delete_project_if_exists2(mocker):
    mocker.patch.object(ProjectManager, 'exists', return_value=False)
    res = delete_project_if_exists('123456987456')
    assert not res


def test_update_project_api1(client_update, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_update)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.update_project_if_exists', return_value=True)
    resp = client_update.simulate_post('/api/parse/projects/update_project', headers=headers)
    assert resp.status_code == 200

def test_update_project_api2(client_update, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_update)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.update_project_if_exists', return_value=False)
    resp = client_update.simulate_post('/api/parse/projects/update_project', headers=headers)
    assert resp.status_code == 200

def test_update_project_api3(client_update, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_delete)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.update_project_if_exists', return_value=None)
    resp = client_update.simulate_post('/api/parse/projects/update_project', headers=headers)
    assert resp.status_code == 503

def test_update_project_api4(client_update, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_delete1)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.projects.update_project_if_exists', return_value=True)
    resp = client_update.simulate_post('/api/parse/projects/update_project', headers=headers)
    assert resp.status_code == 412

def test_update_project_if_exists1(mocker):
    json = {'name': 'Rahul Tripathi'}
    mocker.patch.object(ProjectManager, 'exists', return_value=True)
    mocker.patch.object(ProjectManager, 'update', return_value=True)
    res = update_project_if_exists('126789', json)
    assert res

def test_update_project_if_exists2(mocker):
    json = {'name': 'Rahul Tripathi'}
    mocker.patch.object(ProjectManager, 'exists', return_value=False)
    res = update_project_if_exists('123456789', json)
    assert not res