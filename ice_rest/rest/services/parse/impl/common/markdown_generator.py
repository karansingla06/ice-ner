from ice_commons.data.dl.manager import DatasourceManager
import logging
import json

logger = logging.getLogger()

integration = """
## Integration
To integrate {service_id} with your application use the following rest endpoint

{api}

#### Sample Request JSON
```json
{{
   "text": {data},
   "serviceid":"{service_id}",
   "pos":false,
   "intent":true,
   "entity":true
}}
```
#### Sample Response JSON
```json
"text": {response},

"intent":{{
    "top_intent":top intent,
    "confidence_level":[
    {{
        intent1:percentage,
        intent2:percenatge
    }}
    
    ] 
}}

"entities":
[ {{
    "start": start_index,
    "tag": "entity_value",
    "end": end_index,
    "score": score,
    "entity": "entity_type"
}} ]

```
"""


def markdown_creater(serviceid,get_prediction_api_url):
    data = data_generator(serviceid)
    markdown = markdown_integration(data, serviceid, get_prediction_api_url)
    return markdown

def data_generator(serviceid = None):
    try:

        fetched_value = DatasourceManager().find_datasource_by_service_id(serviceid)
        temp_value =  fetched_value.get('utterances')
        data = []

        for items in temp_value:
            data.append(items.get('utterance'))

        return data

    except Exception as e:
        logger.exception(e)


def markdown_integration(data = None, serviceid = None ,get_prediction_api_url = None):
    if data is not None and len(data)!=0:
        data = data[0]
    data_input = {
        "api": get_prediction_api_url,
        "service_id": serviceid,
        "data": json.dumps(data, indent=4),
        "response": json.dumps(data, indent=4),

    }
    mark_down=dict();
    mark_down["mark_down_ui_client"]=integration.format(**data_input)
    return mark_down























