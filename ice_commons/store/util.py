import pandas as pd
import json
from pydash import get
import re
import logging
from ice_commons.utils import MODEL_TYPE_NER, MODEL_TYPE_IR
from ice_commons.data.dl.manager import ProjectManager
logger = logging.getLogger(__name__)


def get_published_models():
    manager = ProjectManager()
    ids = manager.get_models_by_status(manager.STATUS_PUBLISHED)

    df = pd.DataFrame(ids)
    results = []
    for index, row in df.iterrows():
        service_id = row['serviceid']
        ner_status = get(row, "ner.status")
        engine = get(row, "engine")
        if ner_status == ProjectManager.STATUS_PUBLISHED:
            results.append((service_id, 'ner', engine))
        ir_status = get(row, "ir.status")
        if ir_status == ProjectManager.STATUS_PUBLISHED:
            results.append((service_id, 'ir', None))
    return results

def remove_duplicates(tag_list):
    b = []
    for i in range(0, len(tag_list)):
        if tag_list[i] not in tag_list[i + 1:]:
            b.append(tag_list[i])
    return b

def validate_regex(pattern):
    if pattern is not None:
        try:
            return re.compile(pattern)
        except re.error as e:
            return False
    else:
        return False
        
def regex_checker(text, pattern_entities):
    pattern_response = []
    text2= ' '+text+' '
    for item in pattern_entities:
        pattern = item.get('pattern')
        pattern = pattern.replace('^', '^(\s)')
        pattern = pattern.replace('$', '(\s)$')
        entity = item.get("entity")
        response = validate_regex(pattern)
        logger.info(" RESPONSE :::::::::::::::::::::  %s \n\n " %pattern)
        if response:
            match = []
            for m in re.finditer(pattern, text2, re.IGNORECASE):
                match.append(m.string[m.start():m.end()].strip())
            index=0
            for (loop_num,each_value) in enumerate(match):
                spaceCount = 0
                old_index = index
                if(loop_num==0):
                   index = text.find(each_value)
                else:
                   index = text.find(each_value,old_index+1)
                temp_dict={}
                if index != -1:
                    for counter in range(0, old_index):
                        if text[counter] == " ":
                            spaceCount += 1
                    for counter in range(old_index, index):
                        if text[counter] == " ":
                            spaceCount += 1
                    spacesInPhrase = each_value.count(" ")
                    end = spaceCount+spacesInPhrase+1
                    temp_dict = {
                        "tag": entity,
                        "start": spaceCount,
                        "entity": " ".join(text.split()[spaceCount:end]),
                        "end": end
                    }
                pattern_response.append(temp_dict)
    pattern_response = remove_duplicates(pattern_response)
    return pattern_response


def phrase_checker(text, pharase_entities):
    response_list = []
    for item in pharase_entities:
        phrase = item.get("phrase")
        phrase.sort(key=len, reverse = True) 
        entity = item.get("entity")
        for each_phrase in phrase:
             spaceCount = 0
             cur_pharse_count = (" "+ text.upper()+ " ").count(" "+each_phrase.upper()+ " ")
             index = 0
             for phrase_counter in range(cur_pharse_count):
                old_index = index
                if(phrase_counter==0):
                    index = (" "+text.upper()+" ").find(" "+each_phrase.upper()+" ")
                else:
                    index = (" "+text.upper()+" ").find(" "+each_phrase.upper()+" ",old_index+1)
                if index != -1:
                   for counter in range(old_index, index):
                      if text[counter] == " ":
                         spaceCount += 1
                   spacesInPhrase = each_phrase.count(" ")
                   end = spaceCount+spacesInPhrase+1
                   start = spaceCount
                   temp_dict = {
                     "tag": entity,
                     "start": spaceCount,
                     "entity": " ".join(text.split()[start:end]),
                     "end": end
                   }
                   response_list.append(temp_dict)
    return response_list

def get_requested_services(doc):
    serviceid = get(doc,'serviceid')
    intent = get(doc, 'intent', default=True)
    ner = get(doc, 'entity', default=True)
    pos = get (doc, 'pos', default='yes')
    requested_services = []
    if ner is True:
        requested_services.append((serviceid, MODEL_TYPE_NER,pos))
    if intent is True:
        requested_services.append((serviceid, MODEL_TYPE_IR, None))
    return requested_services

def get_model_name(serviceid, model_type, engine):
    model_name = serviceid + "-" + model_type
    if (model_type == "ner"):
        model_name = model_name + "-" + engine

    return model_name
