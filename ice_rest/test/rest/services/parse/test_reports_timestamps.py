from falcon import testing
import pytest,falcon
from ice_rest.rest.services.parse.reports_timestamps import ReportFetchResource, TimestampFetchResource
from datetime import datetime

import json

class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/report', ReportFetchResource())
    api.add_route('/api/parse/report/ts', TimestampFetchResource())
    client = falcon.testing.TestClient(api)
    return client


req_init = falcon.request.Request.__init__


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "serviceid": "hello",
        "timestamp": "abc"
    }}


def test_fetch_report_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.reports_timestamps.TestRunsManager.fetch_all_reports', return_value={'runs': [{'run_time': datetime.now()}]})
    resp = client.simulate_post('/api/parse/report', headers=headers)
    assert resp.status_code == 200


def mock_init2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "serviceid": "hello"
    }}



def test_fetch_report_api2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.reports_timestamps.TestRunsManager.fetch_all_reports', return_value={})
    resp = client.simulate_post('/api/parse/report', headers=headers)
    assert resp.status_code == 400


def test_fetch_report_api3(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.reports_timestamps.TestRunsManager.fetch_all_reports', return_value=None)
    resp = client.simulate_post('/api/parse/report', headers=headers)
    assert resp.status_code == 503


def mock_init3(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "serviceid": "hello"
    }}


def test_fetch_timestamp_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init3)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.reports_timestamps.TestRunsManager.fetch_timestamps', return_value={'runs': [{'run_time': datetime.now()}]})
    mocker.patch('ice_rest.rest.services.parse.reports_timestamps.TestRunsManager.fetch_all_reports', return_value={'runs': [{'run_time': datetime.now()}]})
    resp = client.simulate_post('/api/parse/report/ts', headers=headers)
    assert resp.status_code == 200


def mock_init4(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "textabc": "hello"
    }}

def test_fetch_timestamp_api2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init4)
    headers = {"Content-Type": "application/json"}
    resp = client.simulate_post('/api/parse/report', headers=headers)
    assert resp.status_code == 400


def test_fetch_timestamp_api3(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init3)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.reports_timestamps.TestRunsManager.fetch_timestamps', return_value={})
    mocker.patch('ice_rest.rest.services.parse.reports_timestamps.TestRunsManager.fetch_all_reports', return_value={})
    resp = client.simulate_post('/api/parse/report/ts', headers=headers)
    assert resp.status_code == 503