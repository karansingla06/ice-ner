import logging
from falcon import testing
import pytest,falcon
logger = logging.getLogger()
from ice_rest.rest.appengine import AppEngine
from ice_commons.data.dl.manager import ProjectManager
from ice_rest.rest.services.parse import train 
import json
from ice_rest.rest.services.parse.impl.common import markdown_generator
from ice_commons.celery_jobs.train.ner.train import TrainNERHelper
from ice_commons.data.dl.manager import ProjectManager
from ice_rest.rest.services.parse.train import TrainParseResource, BotAnalyticsAPI
from ice_commons.data.dl.manager import ProjectconfigsManager
from falcon import HTTPBadRequest
from ice_commons.celery_jobs.train import tasks,train_impl


@pytest.fixture()
def client():
    api = falcon.API()
    api.add_route('/api/parse/train', TrainParseResource())
    client = falcon.testing.TestClient(api)
    return client


req_init = falcon.request.Request.__init__


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
                        "serviceid": "WKVA",
                        "train_ner":True,
                        "train_ir":True
                        }}
def test_get_prediction_api(client,mocker):
      mocker.patch('falcon.request.Request.__init__', mock_init)
      class req:
            url = 'http://localhost:8080/api/parse/predict'
            relative_uri = "http://localhost:8080/api/parse/train"
      x=train.get_prediction_api_url(req)
      assert x == 'http://localhost:8080/api/parse/predict'


def test_train_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.train.updateStatus', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.train.markdown_creater', return_value={'mark_down_ui_client': '\n## Integration\nTo integrate WKVA with your application use the following rest endpoint\n\nhttp://localhost:8021/api/parse/predict\n\n#### Sample Request JSON\n```json\n{\n   "text": "Hi",\n   "serviceid":"WKVA",\n   "pos":false,\n   "intent":true,\n   "entity":true\n}\n```\n#### Sample Response JSON\n```json\n"text": "Hi",\n\n"intent":{\n    "top_intent":top intent,\n    "confidence_level":[\n    {\n        intent1:percentage,\n        intent2:percenatge\n    }\n    \n    ] \n}\n\n"entities":\n[ {\n    "start": start_index,\n    "tag": "entity_value",\n    "end": end_index,\n    "score": score,\n    "entity": "entity_type"\n} ]\n\n```\n'})
    mocker.patch('ice_rest.rest.services.parse.train.ProjectconfigsManager.update_config_by_service_id', return_value=None)
    app_config= mocker.patch('ice_rest.rest.services.parse.train.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'ON'
    resp = client.simulate_post('/api/parse/train', headers=headers)
    assert resp.status_code == 200

def test_train_api_with_exception(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.train.updateStatus', side_effect = Exception('xyz'))
    mocker.patch('ice_rest.rest.services.parse.train.markdown_creater', return_value={'mark_down_ui_client': '\n## Integration\nTo integrate WKVA with your application use the following rest endpoint\n\nhttp://localhost:8021/api/parse/predict\n\n#### Sample Request JSON\n```json\n{\n   "text": "Hi",\n   "serviceid":"WKVA",\n   "pos":false,\n   "intent":true,\n   "entity":true\n}\n```\n#### Sample Response JSON\n```json\n"text": "Hi",\n\n"intent":{\n    "top_intent":top intent,\n    "confidence_level":[\n    {\n        intent1:percentage,\n        intent2:percenatge\n    }\n    \n    ] \n}\n\n"entities":\n[ {\n    "start": start_index,\n    "tag": "entity_value",\n    "end": end_index,\n    "score": score,\n    "entity": "entity_type"\n} ]\n\n```\n'})
    mocker.patch('ice_rest.rest.services.parse.train.ProjectconfigsManager.update_config_by_service_id', return_value=None)
    app_config= mocker.patch('ice_rest.rest.services.parse.train.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'ON'
    resp = client.simulate_post('/api/parse/train', headers=headers)
    assert resp.status_code == 503
def test_train_api_with_AssertionError(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.train.updateStatus', side_effect = AssertionError('xyz'))
    mocker.patch('ice_rest.rest.services.parse.train.markdown_creater', return_value={'mark_down_ui_client': '\n## Integration\nTo integrate WKVA with your application use the following rest endpoint\n\nhttp://localhost:8021/api/parse/predict\n\n#### Sample Request JSON\n```json\n{\n   "text": "Hi",\n   "serviceid":"WKVA",\n   "pos":false,\n   "intent":true,\n   "entity":true\n}\n```\n#### Sample Response JSON\n```json\n"text": "Hi",\n\n"intent":{\n    "top_intent":top intent,\n    "confidence_level":[\n    {\n        intent1:percentage,\n        intent2:percenatge\n    }\n    \n    ] \n}\n\n"entities":\n[ {\n    "start": start_index,\n    "tag": "entity_value",\n    "end": end_index,\n    "score": score,\n    "entity": "entity_type"\n} ]\n\n```\n'})
    mocker.patch('ice_rest.rest.services.parse.train.ProjectconfigsManager.update_config_by_service_id', return_value=None)
    app_config= mocker.patch('ice_rest.rest.services.parse.train.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'ON'
    resp = client.simulate_post('/api/parse/train', headers=headers)
    assert resp.status_code == 400


def test_train_api_inside_if(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.train.updateStatus', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.train.get_prediction_api_url', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.train.train_parse', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.train.markdown_creater', return_value={'mark_down_ui_client': '\n## Integration\nTo integrate WKVA with your application use the following rest endpoint\n\nhttp://localhost:8021/api/parse/predict\n\n#### Sample Request JSON\n```json\n{\n   "text": "Hi",\n   "serviceid":"WKVA",\n   "pos":false,\n   "intent":true,\n   "entity":true\n}\n```\n#### Sample Response JSON\n```json\n"text": "Hi",\n\n"intent":{\n    "top_intent":top intent,\n    "confidence_level":[\n    {\n        intent1:percentage,\n        intent2:percenatge\n    }\n    \n    ] \n}\n\n"entities":\n[ {\n    "start": start_index,\n    "tag": "entity_value",\n    "end": end_index,\n    "score": score,\n    "entity": "entity_type"\n} ]\n\n```\n'})
    manager = mocker.patch('ice_rest.rest.services.parse.train.ProjectconfigsManager')
    manager.return_value.update_config_by_service_id.return_value = {}    
    mocker.patch('ice_rest.rest.services.parse.train.app_config', {'BOTANALYTICS_LOG_FLAG':'ON'})
    resp = client.simulate_post('/api/parse/train', headers=headers)
    assert resp.status_code == 200


def mock_init_bad_request(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
                        
                        "train_ner":True,
                        
                        }}
            
def test_train_api_bad_request(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_bad_request)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.train.updateStatus', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.train.markdown_creater', return_value={'mark_down_ui_client': '\n## Integration\nTo integrate WKVA with your application use the following rest endpoint\n\nhttp://localhost:8021/api/parse/predict\n\n#### Sample Request JSON\n```json\n{\n   "text": "Hi",\n   "serviceid":"WKVA",\n   "pos":false,\n   "intent":true,\n   "entity":true\n}\n```\n#### Sample Response JSON\n```json\n"text": "Hi",\n\n"intent":{\n    "top_intent":top intent,\n    "confidence_level":[\n    {\n        intent1:percentage,\n        intent2:percenatge\n    }\n    \n    ] \n}\n\n"entities":\n[ {\n    "start": start_index,\n    "tag": "entity_value",\n    "end": end_index,\n    "score": score,\n    "entity": "entity_type"\n} ]\n\n```\n'})
    mocker.patch('ice_rest.rest.services.parse.train.ProjectconfigsManager.update_config_by_service_id', return_value=None)
    app_config= mocker.patch('ice_rest.rest.services.parse.train.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'OFF'
    resp = client.simulate_post('/api/parse/train', headers=headers)
    assert resp.status_code == 400

def test_updatestatus_with_null(mocker):
      manager = mocker.patch('ice_rest.rest.services.parse.train.ProjectManager')
      manager.find_model.return_value = {}
      exp = train.updateStatus(None,None,None)
      assert exp==None
def test_updatestatus_with_train_ner_true(mocker):
      manager = mocker.patch('ice_rest.rest.services.parse.train.ProjectManager')
      manager.find_model.return_value = {}
      mocker.patch('ice_rest.rest.services.parse.train.ProjectManager.find_model',return_value = ['config'])
      mocker.patch('ice_rest.rest.services.parse.train.ProjectManager.STATUS_HOLD',return_value = {})
      mocker.patch('ice_rest.rest.services.parse.train.ProjectManager.update_config',return_value = {})
      exp = train.updateStatus(None,True,None)
      assert exp==None
def test_updatestatus_with_train_ir_true(mocker):
      manager = mocker.patch('ice_rest.rest.services.parse.train.ProjectManager')
      manager.find_model.return_value = {}
      mocker.patch('ice_rest.rest.services.parse.train.ProjectManager.find_model',return_value = ['config'])
      mocker.patch('ice_rest.rest.services.parse.train.ProjectManager.STATUS_HOLD',return_value = {})
      mocker.patch('ice_rest.rest.services.parse.train.ProjectManager.update_config',return_value = {})
      exp = train.updateStatus(None,None,True)
      assert exp==None
def test_updatestatus_all_true(mocker):
      manager = mocker.patch('ice_rest.rest.services.parse.train.ProjectManager')
      manager.find_model.return_value = {}
      mocker.patch('ice_rest.rest.services.parse.train.ProjectManager.find_model',return_value = ['config'])
      mocker.patch('ice_rest.rest.services.parse.train.ProjectManager.STATUS_HOLD',return_value = {})
      mocker.patch('ice_rest.rest.services.parse.train.ProjectManager.update_config',return_value = {})
      exp = train.updateStatus(True,True,True)
      assert exp== None
