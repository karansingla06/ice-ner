from falcon import testing
import pytest,falcon
from ice_rest.rest.services.parse.retag_predefinedtags import RetagWithPredefinedModel, BotAnalyticsAPI, replace_predefined_entities
from ice_rest.rest.services.parse.retag_predefinedtags import remove_overlapping, remove_from_minio, update_projects_collection,retag,untag_predefined


class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/retag', RetagWithPredefinedModel())
    client = falcon.testing.TestClient(api)
    return client


req_init = falcon.request.Request.__init__


def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "predefined_model": "xy",
        "custom_model": "yz",
        "serviceid": "abc"
    }}


def test_retag_api1(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.DatasourceManager.find_datasource_by_service_id', return_value= {})
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.untag_predefined', return_value= [])
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.replace_predefined_entities', return_value= [])
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.DatasourceManager.update_datasource_by_service_id', return_value= None)
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.update_projects_collection', return_value= None)
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.retag', return_value= [])
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.remove_from_minio', return_value= None)
    app_config= mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'OFF'
    resp = client.simulate_post('/api/parse/retag', headers=headers)
    assert resp.status_code == 200



def test_predict_api2(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.DatasourceManager.find_datasource_by_service_id',
                 return_value={})
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.untag_predefined', return_value=[])
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.replace_predefined_entities', return_value=[])
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.DatasourceManager.update_datasource_by_service_id',
                 return_value=None)
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.update_projects_collection', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.retag', return_value=[])
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.remove_from_minio', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.app_config', {'BOTANALYTICS_LOG_FLAG':'ON'})
    m = mocker.patch.object(BotAnalyticsAPI, "log")
    m.side_effect = [None,None]
    resp = client.simulate_post('/api/parse/retag', headers=headers)
    assert resp.status_code == 200



def mock_init2(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
         "predefined_model": "xy",
        "serviceid": "abc"
    }}

def test_retag_api_with_exception(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init2)
    headers = {"Content-Type": "application/json"}
    resp = client.simulate_post('/api/parse/retag', headers=headers)
    assert resp.status_code == 500


def test_remove_overlapping():
    def_tags= [{'start':1, 'end': 3},{'start':4, 'end': 5}]
    cus_tags= [{'start' :2, 'end':3}]
    res = remove_overlapping(def_tags, cus_tags)
    assert res==[{'start': 2, 'end': 3}, {'start': 4, 'end': 5}]


def test_remove_from_minio(mocker):
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.get_ner_status', return_value='trained')
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.ProjectManager.update_config', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.VerbisStore.remove_models_from_remote', return_value=None)
    assert remove_from_minio('abc') == None


def test_update_projects_collection(mocker):
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.ProjectManager.update_config', return_value=None)
    assert update_projects_collection('abc', 'a', 'b') == None


def test_replace_predefined_entities1(mocker):
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.get_default_models', return_value=['a','B','c'])
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.get_entities_for_default_model', return_value=['x','y','z'])
    res = replace_predefined_entities('b')
    assert res== ['x','y','z']


def test_replace_predefined_entitiesw(mocker):
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.get_default_models', return_value=['a','B','c'])
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.get_entities_for_default_model', return_value=['x','y','z'])
    res = replace_predefined_entities('d')
    assert res== []


def test_untag_predefined():
    utterances= [
        {
            "case_converted_text": "Get me the trend for last 5 hours ",
            "mapping": "{\"tokens\": [\"Get\", \"me\", \"the\", \"trend\", \"for\", \"last\", \"5\", \"hours\"], \"text\": null, \"intent\": \"trendgraph\", \"tags\": [{\"tag\": \"DATE\", \"start\": 5, \"score\": \".5\", \"end\": 8, \"entity\": \"last 5 hours\"}]}",
            "case_converted_utterance": "Get me the trend for last 5 hours ",
            "utterance": "Get me the trend for last 5 hours "
        },
        {
            "case_converted_text": "Share the trend graph for last 15 hours ",
            "mapping": "{\"tokens\": [\"Share\", \"the\", \"trend\", \"graph\", \"for\", \"last\", \"15\", \"hours\"], \"text\": null, \"intent\": \"trendgraph\", \"tags\": [{\"tag\": \"DATE\", \"start\": 5, \"score\": \".5\", \"end\": 8, \"entity\": \"last 15 hours\"}]}",
            "case_converted_utterance": "Share the trend graph for last 15 hours ",
            "utterance": "Share the trend graph for last 15 hours "
        }
	]
    res = untag_predefined(utterances, ['DATE', 'TIME'])
    assert res== [{'utterance': 'Get me the trend for last 5 hours ', 'case_converted_text': 'Get me the trend for last 5 hours ',
                   'mapping': '{"tokens": ["Get", "me", "the", "trend", "for", "last", "5", "hours"], '
                              '"text": null, "intent": "trendgraph", "tags": '
                              '[{"start": 5, "tag": "DATE", "end": 8, "score": ".5", "entity": "last 5 hours"}]}',
                   'case_converted_utterance': 'Get me the trend for last 5 hours '},
                  {'utterance': 'Share the trend graph for last 15 hours ',
                   'case_converted_text': 'Share the trend graph for last 15 hours ',
                   'mapping': '{"tokens": ["Share", "the", "trend", "graph", "for", "last", "15", "hours"], '
                              '"text": null, "intent": "trendgraph", "tags": '
                              '[{"start": 5, "tag": "DATE", "end": 8, "score": ".5", "entity": "last 15 hours"}]}',
                   'case_converted_utterance': 'Share the trend graph for last 15 hours '}]


def test_retag(mocker):
    utterances = [
        {
            "case_converted_text": "Get me the trend for last 5 hours ",
            "mapping": "{\"tokens\": [\"Get\", \"me\", \"the\", \"trend\", \"for\", \"last\", \"5\", \"hours\"], \"text\": null, \"intent\": \"trendgraph\", \"tags\": [{\"tag\": \"DATE\", \"start\": 5, \"score\": \".5\", \"end\": 8, \"entity\": \"last 5 hours\"}]}",
            "case_converted_utterance": "Get me the trend for last 5 hours ",
            "utterance": "Get me the trend for last 5 hours "
        },
        {
            "case_converted_text": "Share the trend graph for last 15 hours ",
            "mapping": "{\"tokens\": [\"Share\", \"the\", \"trend\", \"graph\", \"for\", \"last\", \"15\", \"hours\"], \"text\": null, \"intent\": \"trendgraph\", \"tags\": [{\"tag\": \"DATE\", \"start\": 5, \"score\": \".5\", \"end\": 8, \"entity\": \"last 15 hours\"}]}",
            "case_converted_utterance": "Share the trend graph for last 15 hours ",
            "utterance": "Share the trend graph for last 15 hours "
        }
    ]
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.get_model_store')
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.get_engine', return_value= None)
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.get_model_store.tag_predefined', return_value= [])
    mocker.patch('ice_rest.rest.services.parse.retag_predefinedtags.remove_overlapping', return_value= [])
    res = retag('abc', utterances, 'new_engine')
    assert res == [{'case_converted_text': 'Get me the trend for last 5 hours ', 'ir_trained': False, 'mapping': '{"tokens": ["Get", "me", "the", "trend", "for", "last", "5", "hours"], "text": null, "intent": "trendgraph", "tags": []}', 'case_converted_utterance': 'Get me the trend for last 5 hours ', 'ner_trained': False, 'utterance': 'Get me the trend for last 5 hours '}, {'case_converted_text': 'Share the trend graph for last 15 hours ', 'ir_trained': False, 'mapping': '{"tokens": ["Share", "the", "trend", "graph", "for", "last", "15", "hours"], "text": null, "intent": "trendgraph", "tags": []}', 'case_converted_utterance': 'Share the trend graph for last 15 hours ', 'ner_trained': False, 'utterance': 'Share the trend graph for last 15 hours '}]




