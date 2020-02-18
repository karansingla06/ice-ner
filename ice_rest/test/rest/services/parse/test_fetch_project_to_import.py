from falcon import testing
import pytest
import falcon
from ice_rest.rest.services.parse.fetch_project_to_import import FetchProjectToImport, user_trained_projects, \
    public_trained_projects
from ice_commons.data.dl.manager import ProjectManager


class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'


@pytest.fixture()
def client_fetchprojecttoimport():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/fetchprojecttoimport', FetchProjectToImport())
    client = falcon.testing.TestClient(api)
    return client


req_init = falcon.request.Request.__init__


def mock_init_fetch_project_import(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
            "created_by": "5aa66f6404f0aa0423f9dda6"
        }}


def mock_init_fetch_project_import1(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
            "created_by": ""
        }}


def mock_init_fetch_project_import2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        }}


def test_fetch_project_to_import_api1(client_fetchprojecttoimport, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_fetch_project_import)
    headers = {"Content-Type": "application/json", "organisation-name": "USTGlobal"}
    mocker.patch('ice_rest.rest.services.parse.fetch_project_to_import.user_trained_projects', return_value=True)
    mocker.patch('ice_rest.rest.services.parse.fetch_project_to_import.public_trained_projects', return_value=True)
    resp = client_fetchprojecttoimport.simulate_post('/api/parse/fetchprojecttoimport', headers=headers)
    assert resp.status_code == 200


# def test_fetch_project_to_import_api2(client_fetchprojecttoimport, mocker):
#     mocker.patch('falcon.request.Request.__init__', mock_init_fetch_project_import1)
#     headers = {"Content-Type": "application/json", "organisation-name": "USTGlobal"}
#     mocker.patch('ice_rest.rest.services.parse.fetch_project_to_import.user_trained_projects', return_value=None)
#     mocker.patch('ice_rest.rest.services.parse.fetch_project_to_import.public_trained_projects', return_value=None)
#     resp = client_fetchprojecttoimport.simulate_post('/api/parse/fetchprojecttoimport', headers=headers)
#     assert resp.status_code == 412


# def test_fetch_project_to_import_api3(client_fetchprojecttoimport, mocker):
#     mocker.patch('falcon.request.Request.__init__', mock_init_fetch_project_import2)
#     headers = {"Content-Type": "application/json", "organisation-name": "USTGlobal"}
#     mocker.patch('ice_rest.rest.services.parse.fetch_project_to_import.user_trained_projects', return_value=None)
#     mocker.patch('ice_rest.rest.services.parse.fetch_project_to_import.public_trained_projects', return_value=None)
#     resp = client_fetchprojecttoimport.simulate_post('/api/parse/fetchprojecttoimport', headers=headers)
#     assert resp.status_code == 503


def test_user_trained_projects(mocker):
    mocker.patch.object(ProjectManager, 'exists', return_value=True)
    mocker.patch.object(ProjectManager, 'find', return_value=True)
    res = user_trained_projects("000014125436")
    assert res


def test_user_trained_projects_negative(mocker):
    mocker.patch.object(ProjectManager, 'exists', return_value=False)
    res = user_trained_projects("000114654321")
    assert not res


def test_public_trained_projects(mocker):
    mocker.patch.object(ProjectManager, 'exists', return_value=True)
    mocker.patch.object(ProjectManager, 'find', return_value=True)
    res = public_trained_projects("organisation_name")
    assert res


def test_public_trained_projects_negative(mocker):
    mocker.patch.object(ProjectManager, 'exists', return_value=False)
    res = public_trained_projects("organisation_name")
    assert not res
