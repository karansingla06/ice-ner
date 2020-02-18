# import sys
# sys.path.append('/home/nivedithahn/ner/verbis/')
from falcon import testing
import pytest,falcon
from ice_rest.rest.appengine import AppEngine 
from ice_rest.rest.services.parse.impl.map import remove_duplicates, check, tag_phrase, tag_pattern, MapUtterances
from bson.objectid import ObjectId



class TestMiddleware:
    def process_request(self, req, resp):
        resp.body = 'Pass'

@pytest.fixture()
def client():
    api = falcon.API(middleware=TestMiddleware())
    api.add_route('/api/parse/bulktag', MapUtterances())
    client = falcon.testing.TestClient(api)
    return client

req_init = falcon.request.Request.__init__

def mock_init(req, *args, **kwargs):
    req_init(req, *args, **kwargs)
    req.context = {'doc': {
        "type": "phrases",
        "serviceid": "MedicalAssistant-test"
    }}


def test_bulktag_api(client, mocker):
    mocker.patch('falcon.request.Request.__init__', mock_init)
    headers = {"Content-Type": "application/json"}
    mocker.patch('ice_rest.rest.services.parse.impl.map.DatasourceManager.find_datasource_by_service_id', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.map.DatasourceManager.update_datasource_by_service_id', return_value="hh")
    mocker.patch('ice_rest.rest.services.parse.impl.map.tag_phrase', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.map.tag_pattern', return_value=None)
    app_config= mocker.patch('ice_rest.rest.services.parse.impl.map.app_config')
    app_config['BOTANALYTICS_LOG_FLAG'] = 'OFF'
    resp = client.simulate_post('/api/parse/bulktag', headers=headers)
    assert resp.status_code == 200


def test_remove_duplicates_with_null(mocker):
    input_data = []
    resp = remove_duplicates(input_data)
    expected = []
    assert resp == expected
    
def test_remove_duplicates_with_text(mocker):
    input_data = [{'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}, {'start': 3, 'tag': 'pink', 'end': 4, 'entity': 'pink'}, {'start': 7, 'tag': 'pink', 'end': 8, 'entity': 'pink'}, {'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}, {'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, {'start': 3, 'tag': 'pink', 'end': 4, 'entity': 'pink'}, {'start': 7, 'tag': 'pink', 'end': 8, 'entity': 'pink'}, {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}]
    resp = remove_duplicates(input_data)
    expected = [{'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, {'start': 3, 'tag': 'pink', 'end': 4, 'entity': 'pink'}, {'start': 7, 'tag': 'pink', 'end': 8, 'entity': 'pink'}, {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}] 
    assert resp == expected

def test_check_with_null(mocker):
    existing_tags = []
    current_tag = dict()
    resp = check(existing_tags, current_tag)
    expected  = dict()
    assert resp == expected

def test_check_with_text(mocker):
    existing_tags = [{'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}, {'start': 3, 'tag': 'pink', 'end': 4, 'entity': 'pink'}, {'start': 7, 'tag': 'pink', 'end': 8, 'entity': 'pink'}, {'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}] 
    current_tag = {'start': 1, 'tag': 'pink', 'end': 2, 'entity': 'pink'}
    resp = check(existing_tags, current_tag)
    expected = {'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'} 
    assert resp == expected

def test_tag_phrase_with_null(mocker):
    phrases = []
    utterances = []
    resp = tag_phrase(phrases, utterances)
    expected = []
    assert resp == expected


def test_tag_phrase_with_text_case1(mocker):

    mocker.patch('ice_rest.rest.services.parse.impl.map.phrase_checker', return_value = [{'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}, {'start': 1, 'tag': 'pink', 'end': 2, 'entity': 'pink'}, {'start': 3, 'tag': 'pink', 'end': 4, 'entity': 'pink'}, {'start': 7, 'tag': 'pink', 'end': 8, 'entity': 'pink'}, {'start': 10, 'tag': 'pink', 'end': 11, 'entity': 'pink'}])
    mocker.patch('ice_rest.rest.services.parse.impl.map.remove_duplicates', return_value = [{'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, {'start': 3, 'tag': 'pink', 'end': 4, 'entity': 'pink'}, {'start': 7, 'tag': 'pink', 'end': 8, 'entity': 'pink'}, {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}] )
    forloop = mocker.patch('ice_rest.rest.services.parse.impl.map.check')
    forloop.side_effect = [
        {'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'},
        {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'},
        {'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, 
        {'start': 3, 'tag': 'pink', 'end': 4, 'entity': 'pink'}, 
        {'start': 7, 'tag': 'pink', 'end': 8, 'entity': 'pink'},
        {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}]
    phrases = [{'phrase': ['Asia', 'Africa', 'Antarctica', 'Australia', 'Europe', 'North America', 'South America'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c51'), 'entity': 'continents'}, {'phrase': ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Portuguese', 'Bengali', 'Russian', 'Japanese', 'Punjabi', 'German', 'Malay', 'Telugu', 'Vietnamese', 'Persian', 'Kannada', 'Malayalam', 'Sundanese'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c50'), 'entity': 'common languages'}, {'phrase': ['blue', 'sky blue', 'navy blue', 'royal blue', 'dark blue'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c4f'), 'entity': 'colors'}, {'phrase': ['rose pink', 'dark pink', 'pink', 'pinky pink'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c4e'), 'entity': 'pink'}, {'phrase': ['dark red', 'red', 'light red', 'crimson red'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c4d'), 'entity': 'red'}, {'phrase': ['black', 'dark black'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c4c'), 'entity': 'black'}]
    utterances = [{'utterance': 'pinky pink , pink , rose , pink , dark pink', 'mapping': '{"tokens": ["Pinky", "pink", ",", "pink", ",", "rose", ",", "pink", ",", "dark", "pink"], "text": null, "intent": "colors", "tags": [{"start": 0, "tag": "pink", "end": 2, "entity": "pinky pink"}, {"start": 3, "tag": "pink", "end": 4, "entity": "pink"}, {"start": 7, "tag": "pink", "end": 8, "entity": "pink"}, {"start": 9, "tag": "pink", "end": 11, "entity": "dark pink"}]}', 'case_converted_utterance': 'Pinky pink , pink , rose , pink , dark pink'}] 
    resp = tag_phrase(phrases, utterances)
    expected = [{'utterance': 'pinky pink , pink , rose , pink , dark pink', 'mapping': '{"tokens": ["Pinky", "pink", ",", "pink", ",", "rose", ",", "pink", ",", "dark", "pink"], "text": null, "intent": "colors", "tags": [{"start": 0, "tag": "pink", "end": 2, "entity": "pinky pink"}, {"start": 9, "tag": "pink", "end": 11, "entity": "dark pink"}, {"start": 3, "tag": "pink", "end": 4, "entity": "pink"}, {"start": 7, "tag": "pink", "end": 8, "entity": "pink"}]}', 'case_converted_utterance': 'Pinky pink , pink , rose , pink , dark pink'}]
    assert resp == expected





def test_tag_phrase_with_text_case2(mocker):

    phrase_checker_fn = mocker.patch('ice_rest.rest.services.parse.impl.map.phrase_checker')
    phrase_checker_fn.side_effect = [
        [
            {'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, 
            {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}, 
            {'start': 1, 'tag': 'pink', 'end': 2, 'entity': 'pink'}, 
            {'start': 3, 'tag': 'pink', 'end': 4, 'entity': 'pink'}, 
            {'start': 7, 'tag': 'pink', 'end': 8, 'entity': 'pink'}, 
            {'start': 10, 'tag': 'pink', 'end': 11, 'entity': 'pink'}
        ],
        [
            {'start': 8, 'tag': 'colors', 'end': 10, 'entity': 'royal blue'}, 
            {'start': 5, 'tag': 'colors', 'end': 7, 'entity': 'navy blue'}, 
            {'start': 21, 'tag': 'colors', 'end': 23, 'entity': 'navy blue'}, 
            {'start': 16, 'tag': 'colors', 'end': 18, 'entity': 'dark blue'},
            {'start': 2, 'tag': 'colors', 'end': 4, 'entity': 'sky blue'},
            {'start': 0, 'tag': 'colors', 'end': 1, 'entity': 'blue'}, 
            {'start': 3, 'tag': 'colors', 'end': 4, 'entity': 'blue'}, 
            {'start': 6, 'tag': 'colors', 'end': 7, 'entity': 'blue'}, 
            {'start': 9, 'tag': 'colors', 'end': 10, 'entity': 'blue'}, 
            {'start': 12, 'tag': 'colors', 'end': 13, 'entity': 'blue'}, 
            {'start': 14, 'tag': 'colors', 'end': 15, 'entity': 'blue'}, 
            {'start': 17, 'tag': 'colors', 'end': 18, 'entity': 'blue'}, 
            {'start': 22, 'tag': 'colors', 'end': 23, 'entity': 'blue'}
        ]
    ]
    
    remove_duplicates_fn = mocker.patch('ice_rest.rest.services.parse.impl.map.remove_duplicates' )
    remove_duplicates_fn.side_effect = [
        [
            {'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, 
            {'start': 3, 'tag': 'pink', 'end': 4, 'entity': 'pink'},
            {'start': 7, 'tag': 'pink', 'end': 8, 'entity': 'pink'}, 
            {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'}
        ],
        [
            {'start': 0, 'tag': 'colors', 'end': 1, 'entity': 'blue'}, 
            {'start': 2, 'tag': 'colors', 'end': 4, 'entity': 'sky blue'}, 
            {'start': 5, 'tag': 'colors', 'end': 7, 'entity': 'navy blue'}, 
            {'start': 8, 'tag': 'colors', 'end': 10, 'entity': 'royal blue'}, 
            {'start': 12, 'tag': 'colors', 'end': 13, 'entity': 'blue'}, 
            {'start': 14, 'tag': 'colors', 'end': 15, 'entity': 'blue'}, 
            {'start': 16, 'tag': 'colors', 'end': 18, 'entity': 'dark blue'}, 
            {'start': 21, 'tag': 'colors', 'end': 23, 'entity': 'navy blue'}
        ] 
    ]
    check_fn = mocker.patch('ice_rest.rest.services.parse.impl.map.check')
    check_fn.side_effect = [
        {'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'},
        {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'},
        {'start': 0, 'tag': 'pink', 'end': 2, 'entity': 'pinky pink'}, 
        {'start': 3, 'tag': 'pink', 'end': 4, 'entity': 'pink'}, 
        {'start': 7, 'tag': 'pink', 'end': 8, 'entity': 'pink'},
        {'start': 9, 'tag': 'pink', 'end': 11, 'entity': 'dark pink'},
        {'start': 8, 'tag': 'colors', 'end': 10, 'entity': 'royal blue'}, 
        {'start': 5, 'tag': 'colors', 'end': 7, 'entity': 'navy blue'}, 
        {'start': 21, 'tag': 'colors', 'end': 23, 'entity': 'navy blue'}, 
        {'start': 16, 'tag': 'colors', 'end': 18, 'entity': 'dark blue'}, 
        {'start': 2, 'tag': 'colors', 'end': 4, 'entity': 'sky blue'}, 
        {'start': 0, 'tag': 'colors', 'end': 1, 'entity': 'blue'}, 
        {'start': 2, 'tag': 'colors', 'end': 4, 'entity': 'sky blue'}, 
        {'start': 5, 'tag': 'colors', 'end': 7, 'entity': 'navy blue'}, 
        {'start': 8, 'tag': 'colors', 'end': 10, 'entity': 'royal blue'}, 
        {'start': 12, 'tag': 'colors', 'end': 13, 'entity': 'blue'}, 
        {'start': 14, 'tag': 'colors', 'end': 15, 'entity': 'blue'}, 
        {'start': 16, 'tag': 'colors', 'end': 18, 'entity': 'dark blue'}, 
        {'start': 21, 'tag': 'colors', 'end': 23, 'entity': 'navy blue'}
    ]
    phrases = [{'phrase': ['Asia', 'Africa', 'Antarctica', 'Australia', 'Europe', 'North America', 'South America'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c51'), 'entity': 'continents'}, {'phrase': ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Portuguese', 'Bengali', 'Russian', 'Japanese', 'Punjabi', 'German', 'Malay', 'Telugu', 'Vietnamese', 'Persian', 'Kannada', 'Malayalam', 'Sundanese'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c50'), 'entity': 'common languages'}, {'phrase': ['blue', 'sky blue', 'navy blue', 'royal blue', 'dark blue'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c4f'), 'entity': 'colors'}, {'phrase': ['rose pink', 'dark pink', 'pink', 'pinky pink'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c4e'), 'entity': 'pink'}, {'phrase': ['dark red', 'red', 'light red', 'crimson red'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c4d'), 'entity': 'red'}, {'phrase': ['black', 'dark black'], '_id': ObjectId('5c5d5fda2a4a3c24036c4c4c'), 'entity': 'black'}]
    utterances =  [{'utterance': 'pinky pink , pink , rose , pink , dark pink', 'mapping': '{"tokens": ["Pinky", "pink", ",", "pink", ",", "rose", ",", "pink", ",", "dark", "pink"], "text": null, "intent": "colors", "tags": [{"start": 0, "tag": "pink", "end": 2, "entity": "pinky pink"}, {"start": 3, "tag": "pink", "end": 4, "entity": "pink"}, {"start": 7, "tag": "pink", "end": 8, "entity": "pink"}, {"start": 9, "tag": "pink", "end": 11, "entity": "dark pink"}]}', 'case_converted_utterance': 'Pinky pink , pink , rose , pink , dark pink'}, {'utterance': 'blue , sky blue , navy blue , royal blue , light blue , blue , dark blue , blues , navy blue', 'mapping': '{"tokens": ["Blue", ",", "sky", "blue", ",", "navy", "blue", ",", "royal", "blue", ",", "light", "blue", ",", "blue", ",", "dark", "blue", ",", "blues", ",", "navy", "blue"], "text": null, "intent": "colors", "tags": [{"start": 0, "tag": "colors", "end": 1, "entity": "blue"}, {"start": 2, "tag": "colors", "end": 4, "entity": "sky blue"}, {"start": 5, "tag": "colors", "end": 7, "entity": "navy blue"}, {"start": 8, "tag": "colors", "end": 10, "entity": "royal blue"}, {"start": 12, "tag": "colors", "end": 13, "entity": "blue"}, {"start": 14, "tag": "colors", "end": 15, "entity": "blue"}, {"start": 16, "tag": "colors", "end": 18, "entity": "dark blue"}, {"start": 21, "tag": "colors", "end": 23, "entity": "navy blue"}]}', 'case_converted_utterance': 'Blue , sky blue , navy blue , royal blue , light blue , blue , dark blue , blues , navy blue'}] 
    resp = tag_phrase(phrases, utterances)
    expected = [{'utterance': 'pinky pink , pink , rose , pink , dark pink', 'mapping': '{"tokens": ["Pinky", "pink", ",", "pink", ",", "rose", ",", "pink", ",", "dark", "pink"], "text": null, "intent": "colors", "tags": [{"start": 0, "tag": "pink", "end": 2, "entity": "pinky pink"}, {"start": 9, "tag": "pink", "end": 11, "entity": "dark pink"}, {"start": 3, "tag": "pink", "end": 4, "entity": "pink"}, {"start": 7, "tag": "pink", "end": 8, "entity": "pink"}]}', 'case_converted_utterance': 'Pinky pink , pink , rose , pink , dark pink'}, {'utterance': 'blue , sky blue , navy blue , royal blue , light blue , blue , dark blue , blues , navy blue', 'mapping': '{"tokens": ["Blue", ",", "sky", "blue", ",", "navy", "blue", ",", "royal", "blue", ",", "light", "blue", ",", "blue", ",", "dark", "blue", ",", "blues", ",", "navy", "blue"], "text": null, "intent": "colors", "tags": [{"start": 8, "tag": "colors", "end": 10, "entity": "royal blue"}, {"start": 5, "tag": "colors", "end": 7, "entity": "navy blue"}, {"start": 16, "tag": "colors", "end": 18, "entity": "dark blue"}, {"start": 21, "tag": "colors", "end": 23, "entity": "navy blue"}, {"start": 2, "tag": "colors", "end": 4, "entity": "sky blue"}, {"start": 0, "tag": "colors", "end": 1, "entity": "blue"}, {"start": 12, "tag": "colors", "end": 13, "entity": "blue"}, {"start": 14, "tag": "colors", "end": 15, "entity": "blue"}]}', 'case_converted_utterance': 'Blue , sky blue , navy blue , royal blue , light blue , blue , dark blue , blues , navy blue'}]
    assert resp == expected


def test_tag_pattern_with_null(mocker):
    patterns = []
    utterances = []
    resp = tag_pattern(patterns, utterances)
    expected = []
    assert resp == expected


def test_tag_pattern_with_text(mocker):
    regex_checker_fn = mocker.patch('ice_rest.rest.services.parse.impl.map.regex_checker')
    regex_checker_fn.side_effect = [
        [
            {'start': 7, 'tag': 'date', 'end': 12, 'entity': '12 / 02 / 2018'}, 
            {'start': 13, 'tag': 'date', 'end': 18, 'entity': '15 / 03 / 2018'}
         ],
        [ ],
        [
            {'start': 11, 'tag': 'email', 'end': 12, 'entity': 'neethu123@gmail.com'}
        ]
    ]

    remove_duplicates_fn = mocker.patch('ice_rest.rest.services.parse.impl.map.remove_duplicates' )
    remove_duplicates_fn.side_effect = [
        [
            {'start': 3, 'tag': 'medicine', 'end': 4, 'entity': 'zincovit'}, 
            {'start': 7, 'tag': 'date', 'end': 12, 'entity': '12 / 02 / 2018'},
            {'start': 13, 'tag': 'date', 'end': 18, 'entity': '15 / 03 / 2018'}
        ],
        [
            {'start': 4, 'tag': 'medicine', 'end': 5, 'entity': 'Cetirizine'},
            {'start': 9, 'tag': 'DISEASE', 'end': 11, 'entity': 'running nose'}
        ],
        [
            {'start': 5, 'tag': 'DOCTOR_NAME', 'end': 7, 'entity': 'Dr Reena'}, 
            {'start': 11, 'tag': 'email', 'end': 12, 'entity': 'neethu123@gmail.com'}
        ]  
    ]

    check_fn = mocker.patch('ice_rest.rest.services.parse.impl.map.check')
    check_fn.side_effect = [
        {'start': 7, 'tag': 'date', 'end': 12, 'entity': '12 / 02 / 2018'},
        {'start': 13, 'tag': 'date', 'end': 18, 'entity': '15 / 03 / 2018'},
        {'start': 11, 'tag': 'email', 'end': 12, 'entity': 'neethu123@gmail.com'}
    ]


    patterns = [{'pattern': '[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}', 'entity': 'email'}, {'pattern': '\\d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}', 'entity': 'date'}] 
    utterances = [{'utterance': 'i was having zincovit through the days 12 / 02 / 2018 to 15 / 03 / 2018', 'mapping': '{"tokens": ["I", "was", "having", "Zincovit", "through", "the", "days", "12", "/", "02", "/", "2018", "to", "15", "/", "03", "/", "2018"], "text": null, "intent": "PRESCRIPTIONS", "tags": [{"start": 3, "tag": "medicine", "end": 4, "entity": "zincovit"}, {"start": 7, "tag": "date", "end": 12, "entity": "12 / 02 / 2018"}, {"start": 13, "tag": "date", "end": 18, "entity": "15 / 03 / 2018"}]}', 'case_converted_utterance': 'I was having Zincovit through the days 12 / 02 / 2018 to 15 / 03 / 2018'}, {'utterance': 'I use to take Cetirizine tablets while I have running nose', 'mapping': '{"tokens": ["I", "use", "to", "take", "Cetirizine", "tablets", "while", "I", "have", "running", "nose"], "text": null, "intent": "PRESCRIPTIONS", "tags": [{"start": 4, "tag": "medicine", "end": 5, "entity": "Cetirizine"}, {"start": 9, "tag": "DISEASE", "end": 11, "entity": "running nose"}]}', 'case_converted_utterance': 'I use to take Cetirizine tablets while I have running nose'}, {'utterance': 'get me an appointment of Dr Reena and mail it to neethu123@gmail.com', 'mapping': '{"tokens": ["Get", "me", "an", "appointment", "of", "Dr", "Reena", "and", "mail", "it", "to", "neethu123@gmail.com"], "text": null, "intent": "APPOINTMENT", "tags": [{"start": 5, "tag": "DOCTOR_NAME", "end": 7, "entity": "Dr Reena"}, {"start": 11, "tag": "email", "end": 12, "entity": "neethu123@gmail.com"}]}', 'case_converted_utterance': 'Get me an appointment of Dr Reena and mail it to neethu123@gmail.com'}]
    resp = tag_pattern(patterns, utterances)
    expected = [{'utterance': 'i was having zincovit through the days 12 / 02 / 2018 to 15 / 03 / 2018', 'mapping': '{"tokens": ["I", "was", "having", "Zincovit", "through", "the", "days", "12", "/", "02", "/", "2018", "to", "15", "/", "03", "/", "2018"], "text": null, "intent": "PRESCRIPTIONS", "tags": [{"start": 3, "tag": "medicine", "end": 4, "entity": "zincovit"}, {"start": 7, "tag": "date", "end": 12, "entity": "12 / 02 / 2018"}, {"start": 13, "tag": "date", "end": 18, "entity": "15 / 03 / 2018"}]}', 'case_converted_utterance': 'I was having Zincovit through the days 12 / 02 / 2018 to 15 / 03 / 2018'}, {'utterance': 'I use to take Cetirizine tablets while I have running nose', 'mapping': '{"tokens": ["I", "use", "to", "take", "Cetirizine", "tablets", "while", "I", "have", "running", "nose"], "text": null, "intent": "PRESCRIPTIONS", "tags": [{"start": 4, "tag": "medicine", "end": 5, "entity": "Cetirizine"}, {"start": 9, "tag": "DISEASE", "end": 11, "entity": "running nose"}]}', 'case_converted_utterance': 'I use to take Cetirizine tablets while I have running nose'}, {'utterance': 'get me an appointment of Dr Reena and mail it to neethu123@gmail.com', 'mapping': '{"tokens": ["Get", "me", "an", "appointment", "of", "Dr", "Reena", "and", "mail", "it", "to", "neethu123@gmail.com"], "text": null, "intent": "APPOINTMENT", "tags": [{"start": 5, "tag": "DOCTOR_NAME", "end": 7, "entity": "Dr Reena"}, {"start": 11, "tag": "email", "end": 12, "entity": "neethu123@gmail.com"}]}', 'case_converted_utterance': 'Get me an appointment of Dr Reena and mail it to neethu123@gmail.com'}] 
    assert resp == expected

