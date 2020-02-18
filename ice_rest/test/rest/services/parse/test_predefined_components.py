import json
import logging
from falcon import testing
import pytest,falcon
logger = logging.getLogger()
from ice_commons.store.models import ModelStore
from ice_rest.rest.appengine import AppEngine
from ice_rest.rest.services.parse import predefined_components
from ice_rest.rest.services.parse.predefined_components import utterance_recase,CategoryIntentAddResource,CategoryIntentFetchResource,CategoryIntentRemoveResource,PatternPhraseFetchResource, IntentFetchResource, IntentRemoveResource,PatternAddResource, PatternUpdateResource, PatternRemoveResource,PhraseAddResource,PhraseUpdateResource, PhraseFetchResource,PhraseRemoveResource
from ice_commons.patterns.singleton import Borg
import json


req_init = falcon.request.Request.__init__
class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'


def test_utterance_recase_with_text(mocker):
      store = mocker.patch('ice_rest.rest.services.parse.predefined_components.get_model_store', return_value=ModelStore())
      mock_remove_overlap_duplicate = mocker.patch.object(store,'change_case')
      mock_remove_overlap_duplicate.side_effects = ["hi","Hi","hello","Hello"]
      resp = utterance_recase(['Hi',"Hello","HoW ArE YoU"])
      print(resp)
      ex = ['hi','hello','how are you']
      assert ex==resp

@pytest.fixture()
def client2():
    api = falcon.API()
    api.add_route('/api/parse/category/intent/remove', CategoryIntentRemoveResource())
    client2 = falcon.testing.TestClient(api)
    return client2
def mock_init_bad_request2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
	"category_":"testing3"}}
def test_predefined_components_category_intent_remove_bad_request(client2, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init_bad_request2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PredefinedIntentManager')
    obj.return_value.remove_category.return_value = {}
    resp = client2.simulate_post('/api/parse/category/intent/remove', headers=headers)
    assert resp.status_code == 400
def mock_init2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
	"category":"testing3"}}
def test_predefined_components_category_intent_remove_normal(client2, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PredefinedIntentManager')
    obj.return_value.remove_category.return_value = ""
    resp = client2.simulate_post('/api/parse/category/intent/remove', headers=headers)
    assert resp.status_code == 200
def test_predefined_components_category_intent_remove_Exception(client2, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PredefinedIntentManager')
    obj.return_value.remove_category.side_effect = Exception('new')
    resp = client2.simulate_post('/api/parse/category/intent/remove', headers=headers)
    assert resp.status_code == 503
def test_predefined_components_category_intent_remove_AssertionError(client2, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PredefinedIntentManager')
    obj.return_value.remove_category.side_effect = AssertionError('new')
    resp = client2.simulate_post('/api/parse/category/intent/remove', headers=headers)
    assert resp.status_code == 412











@pytest.fixture()
def client3():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/patternphrase/fetch', PatternPhraseFetchResource())
    client3 = falcon.testing.TestClient(api)
    return client3
def mock_init3(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {"language":["EN","ES"]}}
def test_parse_patternphrase_fetch_if(client3, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init3)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.fetch_all_patterns_by_language.return_value = [{'name':'x','entity':'x'}]
    obj.return_value.fetch_all_phrases_by_language.return_value = [{'name':'x','entity':'x'}]
    resp = client3.simulate_post('/api/parse/patternphrase/fetch', headers=headers)
    assert resp.status_code == 200
def mock_init3_2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {"language":None}}
def test_parse_patternphrase_fetch_else(client3, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init3_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.fetch_all_patterns_by_language.return_value = []
    obj.return_value.fetch_all_phrases_by_language.return_value = []
    resp = client3.simulate_post('/api/parse/patternphrase/fetch', headers=headers)
    assert resp.status_code == 503
def test_parse_patternphrase_fetch_Exception(client3, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init3)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.fetch_all_patterns_by_language.return_value = []
    obj.return_value.fetch_all_phrases_by_language.side_effect = Exception('new')
    resp = client3.simulate_post('/api/parse/patternphrase/fetch', headers=headers)
    assert resp.status_code == 503
def test_parse_patternphrase_fetch_Assertion(client3, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init3)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.fetch_all_patterns_by_language.return_value = []
    obj.return_value.fetch_all_phrases_by_language.side_effect = AssertionError('new')
    resp = client3.simulate_post('/api/parse/patternphrase/fetch', headers=headers)
    assert resp.status_code == 412








@pytest.fixture()
def client5():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/intent/remove', IntentRemoveResource())
    client5 = falcon.testing.TestClient(api)
    return client5
def mock_init5(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
	"category":"testing2",
	"name":"test1"	}}
def test_intent_remove_normal(client5, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init5)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PredefinedIntentManager')
    obj.return_value.remove_intent.return_value = {}
    resp = client5.simulate_post('/api/parse/intent/remove', headers=headers)
    assert resp.status_code == 200
def mock_init5_2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
	"category":"testing2",
		}}
def test_intent_remove_bad_request(client5, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init5_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PredefinedIntentManager')
    obj.return_value.remove_intent.return_value = {}
    resp = client5.simulate_post('/api/parse/intent/remove', headers=headers)
    assert resp.status_code == 400
def test_intent_remove_bad_Exception(client5, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init5)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PredefinedIntentManager')
    obj.return_value.remove_intent.side_effect = Exception('new')
    resp = client5.simulate_post('/api/parse/intent/remove', headers=headers)
    assert resp.status_code == 503
def test_intent_remove_bad_AssertionError(client5, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init5)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PredefinedIntentManager')
    obj.return_value.remove_intent.side_effect = AssertionError('new')
    resp = client5.simulate_post('/api/parse/intent/remove', headers=headers)
    assert resp.status_code == 412












@pytest.fixture()
def client6():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/pattern/add', PatternAddResource())
    client6 = falcon.testing.TestClient(api)
    return client6
def mock_init6(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
	"category":"testing2"	}}
def test_parse_pattern_add_bad_request(client6, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init6)
    headers = {"Content-Type": "application/json"}
    
    resp = client6.simulate_post('/api/parse/pattern/add', headers=headers)
    assert resp.status_code == 400
def mock_init6_2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
		"name" : "eee",
		"value": "ff"}}
def test_parse_pattern_add_normal_if(client6, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init6_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.add_pattern.return_value = 'xz'
    resp = client6.simulate_post('/api/parse/pattern/add', headers=headers)
    assert resp.status_code == 200
def test_parse_pattern_add_normal_else(client6, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init6_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.add_pattern.return_value = True
    resp = client6.simulate_post('/api/parse/pattern/add', headers=headers)
    assert resp.status_code == 200
def test_parse_pattern_add_Exception(client6, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init6_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.add_pattern.side_effect = Exception('new')
    resp = client6.simulate_post('/api/parse/pattern/add', headers=headers)
    assert resp.status_code == 503
def test_parse_pattern_add_AssertionError(client6, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init6_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.add_pattern.side_effect = AssertionError('new')
    resp = client6.simulate_post('/api/parse/pattern/add', headers=headers)
    assert resp.status_code == 412

def test_parse_pattern_add_normal_if2(client6, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init6_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.add_pattern.return_value = ''
    resp = client6.simulate_post('/api/parse/pattern/add', headers=headers)
    assert resp.status_code == 400




@pytest.fixture()
def client7():
    api = falcon.API()
    api.add_route('/api/parse/pattern/update', PatternUpdateResource())
    client7 = falcon.testing.TestClient(api)
    return client7
def mock_init6(req, *args, **kwargs):
      req_init(req, *args, **kwargs)
      req.context = {'doc': {
	"category":"testing2"	}}
def mock_init7(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
	"name":"{{any pattern name}}"}}
def test_parse_pattern_update_bad_request(client7, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init7)
    headers = {"Content-Type": "application/json"}
    resp = client7.simulate_post('/api/parse/pattern/update', headers=headers)
    assert resp.status_code == 400
def mock_init7_2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
		"name" : "eee",
		"value": "ff"}}
def test_parse_pattern_update_normal(client7, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init7_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.update_pattern.return_value = {}
    resp = client7.simulate_post('/api/parse/pattern/update', headers=headers)
    assert resp.status_code == 200
def test_parse_pattern_update_Exception(client7, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init7_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.update_pattern.side_effect = Exception('new')
    resp = client7.simulate_post('/api/parse/pattern/update', headers=headers)
    assert resp.status_code == 503
def test_parse_pattern_update_Assertion_Error(client7, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init7_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.update_pattern.side_effect = AssertionError('new')
    resp = client7.simulate_post('/api/parse/pattern/update', headers=headers)
    assert resp.status_code == 412







@pytest.fixture()
def client8():
    api = falcon.API()
    api.add_route('/api/parse/pattern/remove', PatternRemoveResource())
    client8 = falcon.testing.TestClient(api)
    return client8
def mock_init8(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {}}
def test_parse_pattern_remove_bad_request(client8, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init8)
    headers = {"Content-Type": "application/json"}
    resp = client8.simulate_post('/api/parse/pattern/remove', headers=headers)
    assert resp.status_code == 400
def mock_init8_2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {	"name":"test"}}
def test_parse_pattern_remove_normal(client8, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init8_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.remove_pattern.return_value = {}
    resp = client8.simulate_post('/api/parse/pattern/remove', headers=headers)
    assert resp.status_code == 200
def test_parse_pattern_remove_Exception(client8, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init8_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.remove_pattern.side_effect = Exception('new')
    resp = client8.simulate_post('/api/parse/pattern/remove', headers=headers)
    assert resp.status_code == 503
def test_parse_pattern_remove_Assertion_Error(client8, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init8_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.remove_pattern.side_effect = AssertionError('new')
    resp = client8.simulate_post('/api/parse/pattern/remove', headers=headers)
    assert resp.status_code == 412










@pytest.fixture()
def client9():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/phrase/add', PhraseAddResource())
    client9 = falcon.testing.TestClient(api)
    return client9
def mock_init9(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {}}
def test_parse_phrase_add_bad_request(client9, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init9)
    headers = {"Content-Type": "application/json"}
    resp = client9.simulate_post('/api/parse/phrase/add', headers=headers)
    assert resp.status_code == 400
def mock_init9_2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {'name':"xz",'value':"null"}}
def test_parse_phrase_add_normal_if(client9, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init9_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.add_phrase.return_value = False
    resp = client9.simulate_post('/api/parse/phrase/add', headers=headers)
    assert resp.status_code == 400
def test_parse_phrase_add_normal_else(client9, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init9_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.add_phrase.return_value = True
    resp = client9.simulate_post('/api/parse/phrase/add', headers=headers)
    assert resp.status_code == 200
def test_parse_phrase_add_Exception(client9, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init9_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.add_phrase.side_effect = Exception('new')
    resp = client9.simulate_post('/api/parse/phrase/add', headers=headers)
    assert resp.status_code == 503
def test_parse_phrase_add_Assertion_Error(client9, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init9_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.add_phrase.side_effect = AssertionError('new')
    resp = client9.simulate_post('/api/parse/phrase/add', headers=headers)
    assert resp.status_code == 412










@pytest.fixture()
def client11():
    api = falcon.API()
    api.add_route('/api/parse/phrase/update', PhraseUpdateResource())
    client11 = falcon.testing.TestClient(api)
    return client11
def mock_init11(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {}}
def test_parse_phrase_update_bad_request(client11, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init11)
    headers = {"Content-Type": "application/json"}
    resp = client11.simulate_post('/api/parse/phrase/update', headers=headers)
    assert resp.status_code == 400
def mock_init11_2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
	"name":"test1"	,
	"value": "success2"}}
def test_parse_phrase_update_normal(client11, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init11_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.update_phrase.return_value = False
    resp = client11.simulate_post('/api/parse/phrase/update', headers=headers)
    assert resp.status_code == 200
def test_parse_phrase_update_Exception(client11, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init11_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.update_phrase.side_effect = Exception('new')
    resp = client11.simulate_post('/api/parse/phrase/update', headers=headers)
    assert resp.status_code == 503
def test_parse_phrase_update_Assertion_Error(client11, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init11_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.update_phrase.side_effect = AssertionError('new')
    resp = client11.simulate_post('/api/parse/phrase/update', headers=headers)
    assert resp.status_code == 412









@pytest.fixture()
def client12():
    api = falcon.API()
    api.add_route('/api/parse/phrase/remove', PhraseRemoveResource())
    client12 = falcon.testing.TestClient(api)
    return client12
def mock_init12(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {}}
def test_parse_phrase_remove_bad_request(client12, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init12)
    headers = {"Content-Type": "application/json"}
    resp = client12.simulate_post('/api/parse/phrase/remove', headers=headers)
    assert resp.status_code == 400
def mock_init12_2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
	"name":"test"}}
def test_parse_phrase_remove_normal(client12, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init12_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.remove_phrase.return_value = []
    resp = client12.simulate_post('/api/parse/phrase/remove', headers=headers)
    assert resp.status_code == 200
def test_parse_phrase_remove_Exception(client12, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init12_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.remove_phrase.side_effect = Exception('new')
    resp = client12.simulate_post('/api/parse/phrase/remove', headers=headers)
    assert resp.status_code == 503
def test_parse_phrase_remove_Assertion_Error(client12, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init12_2)
    headers = {"Content-Type": "application/json"}
    obj = mocker.patch('ice_rest.rest.services.parse.predefined_components.PatternPhraseManager')
    obj.return_value.remove_phrase.side_effect = AssertionError('new')
    resp = client12.simulate_post('/api/parse/phrase/remove', headers=headers)
    assert resp.status_code == 412


