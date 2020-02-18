import json
from ice_rest.rest.services.parse.impl.common import markdown_generator



def test_markdown_integration_with_null():
      data=None
      serviceid=None
      get_prediction_api_url=None
      m2 = markdown_generator.markdown_integration(data,serviceid,get_prediction_api_url)
      try:
            data=data[0]
      except Exception as e:
            print(e)

      data_input = {
        "api": get_prediction_api_url,
        "service_id": serviceid,
        "data": json.dumps(data, indent=4),
        "response": json.dumps(data, indent=4),
      }
      integration = """\n## Integration\nTo integrate {service_id} with your application use the following rest endpoint\n\n{api}\n\n#### Sample Request JSON\n```json\n{{\n   "text": {data},\n   "serviceid":"{service_id}",\n   "pos":false,\n   "intent":true,\n   "entity":true\n}}\n```\n#### Sample Response JSON\n```json\n"text": {response},\n\n"intent":{{\n    "top_intent":top intent,\n    "confidence_level":[\n    {{\n        intent1:percentage,\n        intent2:percenatge\n    }}\n    \n    ] \n}}\n\n"entities":\n[ {{\n    "start": start_index,\n    "tag": "entity_value",\n    "end": end_index,\n    "score": score,\n    "entity": "entity_type"\n}} ]\n\n```\n"""
      m1=dict()
      m1["mark_down_ui_client"]=integration.format(**data_input) 
      
      assert m1 == m2


def test_markdown_integration_with_text1():
      data=['Hi', "What'S up ?", 'Who is this ?', 'Good evening', 'Hey', 'Hai', 'You there', 'Good day', 'Good morning', 'How is it going ?', 'Looking good eve', "What'S new ?", 'Ok take me back', 'How R U ?', 'How are you today ?', 'Hi advisor', 'How are things going ?', 'How have you been ?', 'Hi there', 'Hey you', 'Hey there', 'Hey there all', 'Hey how are you doing', 'Hey twin', 'Hello agent', 'Hello', 'Good to see you', 'Hello I am looking for some help here', 'Have you been well ?', 'Greetings', 'my name is Rachel', 'just testing', 'how di i clear ind-444', 'I cant seem to clear e-file rejection Abc-567 ', "I can't seem to clear diagnostic 12345 ", 'I am getting rejection Ind-517 ', 'I am getting diagnostic 46125 ', 'How do I clear rejection Ind-517 ', 'How do I clear rejection Ind-517 ? ', 'What are some of the causes for a schema validation error ']
      serviceid="WKVA"
      get_prediction_api_url="http://localhost:8021/api/parse/predict"
      m2 = markdown_generator.markdown_integration(data,serviceid,get_prediction_api_url)
      try:
            data=data[0]
      except Exception as e:
            print(e)
               
      data_input = {
        "api": get_prediction_api_url,
        "service_id": serviceid,
        "data": json.dumps(data, indent=4),
        "response": json.dumps(data, indent=4),
      }
      integration = """\n## Integration\nTo integrate {service_id} with your application use the following rest endpoint\n\n{api}\n\n#### Sample Request JSON\n```json\n{{\n   "text": {data},\n   "serviceid":"{service_id}",\n   "pos":false,\n   "intent":true,\n   "entity":true\n}}\n```\n#### Sample Response JSON\n```json\n"text": {response},\n\n"intent":{{\n    "top_intent":top intent,\n    "confidence_level":[\n    {{\n        intent1:percentage,\n        intent2:percenatge\n    }}\n    \n    ] \n}}\n\n"entities":\n[ {{\n    "start": start_index,\n    "tag": "entity_value",\n    "end": end_index,\n    "score": score,\n    "entity": "entity_type"\n}} ]\n\n```\n"""
      m1=dict()
      m1["mark_down_ui_client"]=integration.format(**data_input) 
      assert m1 == m2

def test_markdown_integration_with_text2():
      data="taco"
      serviceid={'sa':1231}
      get_prediction_api_url={'dasd':4}
      m2 = markdown_generator.markdown_integration(data,serviceid,get_prediction_api_url)
      try:
            data=data[0]
      except Exception as e:
            print(e)
               
      data_input = {
        "api": get_prediction_api_url,
        "service_id": serviceid,
        "data": json.dumps(data, indent=4),
        "response": json.dumps(data, indent=4),
      }
      integration = """\n## Integration\nTo integrate {service_id} with your application use the following rest endpoint\n\n{api}\n\n#### Sample Request JSON\n```json\n{{\n   "text": {data},\n   "serviceid":"{service_id}",\n   "pos":false,\n   "intent":true,\n   "entity":true\n}}\n```\n#### Sample Response JSON\n```json\n"text": {response},\n\n"intent":{{\n    "top_intent":top intent,\n    "confidence_level":[\n    {{\n        intent1:percentage,\n        intent2:percenatge\n    }}\n    \n    ] \n}}\n\n"entities":\n[ {{\n    "start": start_index,\n    "tag": "entity_value",\n    "end": end_index,\n    "score": score,\n    "entity": "entity_type"\n}} ]\n\n```\n"""
      m1=dict()
      m1["mark_down_ui_client"]=integration.format(**data_input) 
      assert m1 == m2


def test_markdown_creater_with_null(mocker):
      mocker.patch('ice_rest.rest.services.parse.impl.common.markdown_generator.data_generator',return_value=[])
      mocker.patch('ice_rest.rest.services.parse.impl.common.markdown_generator.markdown_integration',return_value={})
      ans2 = markdown_generator.markdown_creater("WKVA",'http://localhost:8021/api/parse/predict')
      assert {} == ans2


def test_markdown_creater_with_text(mocker):
      mocker.patch('ice_rest.rest.services.parse.impl.common.markdown_generator.data_generator',return_value=['Hi','Henlo','chimkens'])
      mocker.patch('ice_rest.rest.services.parse.impl.common.markdown_generator.markdown_integration',return_value={'Hi'})
      ans2 = markdown_generator.markdown_creater("WKVA",'http://localhost:8021/api/parse/predict')
      assert {'Hi'} == ans2

def test_data_generator_with_null(mocker):
      data_manager = mocker.patch('ice_rest.rest.services.parse.impl.common.markdown_generator.DatasourceManager')
      data_manager.find_datasource_by_service_id.return_value= {}
      exp = []
      resp = markdown_generator.data_generator("WKVA")
      assert exp == resp

from ice_commons.data.dl.manager import DatasourceManager
def test_data_generator_with_text(mocker):
      send = {'trainEntity': True, 
      'intents': [{'modifiedAt': '2019-02-04T09:24:34.971Z', 'name': 'Greeting', 
      'createdAt': '2019-02-04T09:24:34.971Z', 
      'description': 'Marks the beginning of a conversation'},
      {'modifiedAt': '2019-02-04T09:20:33.731Z', 
      'name': 'test', 'createdAt': '2019-02-04T09:20:33.731Z', 'description': 'fgdgfd'},
      {'modifiedAt': '2018-10-25T09:21:34.481Z', 'name': 'getArticle', 
      'createdAt': '2018-10-25T09:21:34.481Z', 'description': 'getArticle'}, 
      {'modifiedAt': '2018-10-25T09:21:34.481Z', 'name': 'conclusion', 
      'createdAt': '2018-10-25T09:21:34.481Z', 'description': 'conclusion'}, 
      {'modifiedAt': '2018-10-25T09:21:34.481Z', 'name': 'getArticl', 
      'createdAt': '2018-10-25T09:21:34.481Z', 'description': 'getArticl'}, 
      {'modifiedAt': '2018-10-25T09:21:34.481Z', 'name': 'getAction', 'createdAt': '2018-10-25T09:21:34.481Z',
      'description': 'getAction'}, {'modifiedAt': '2018-10-25T09:21:34.481Z', 'name': 'greetings', 
      'createdAt': '2018-10-25T09:21:34.481Z', 'description': 'greetings'}, 
      {'modifiedAt': '2018-10-25T09:21:34.481Z', 'name': 'getArtcleForState',
      'createdAt': '2018-10-25T09:21:34.481Z', 'description': 'getArtcleForState'}, 
      {'modifiedAt': '2018-10-25T09:21:34.481Z', 'name': 'due_date', 'createdAt': '2018-10-25T09:21:34.481Z',
      'description': 'due_date'}, {'modifiedAt': '2018-10-25T09:21:34.481Z', 
      'name': 'successflow', 'createdAt': '2018-10-25T09:21:34.481Z', 'description': 'successflow'},
      {'modifiedAt': '2018-10-25T09:21:34.481Z', 'name': 'No intent', 
      'createdAt': '2018-10-25T09:21:34.481Z', 'description': 'no intent'}],
      'predefined_entities': ['PERSON', 'ORGANIZATION', 'LOCATION'],            
      'utterances': [{'utterance': 'Hi', 'mapping': '{"tokens": ["Hi"], "text": null, "intent": "Greeting", "tags": []}',
      'case_converted_utterance': 'Hi'}, 
      {'utterance': "What'S up?", 
      'mapping': '{"tokens": ["What\'S", "up", "?"], "text": null, "intent": "Greeting", "tags": [{"start": 0, "tag": "SUBJECT", "end": 2, "score": 0.6370884841484333, "entity": "What\'S up"}]}', 
      'case_converted_utterance': "What'S up ?"}]}
      mocker.patch('ice_rest.rest.services.parse.impl.common.markdown_generator.DatasourceManager.find_datasource_by_service_id',return_value = send)
      exp =  ['Hi',"What'S up?"]
      resp = markdown_generator.data_generator("WKVA")
      assert exp == resp

def test_data_generator_with_exception(mocker):
      mocker.patch('ice_rest.rest.services.parse.impl.common.markdown_generator.DatasourceManager.find_datasource_by_service_id',side_effect = Exception('error'))
      exp =  None
      resp = markdown_generator.data_generator("WKVA")
      assert exp == resp
