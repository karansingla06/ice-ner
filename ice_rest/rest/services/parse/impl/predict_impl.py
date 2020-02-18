import logging
from pydash import get
from ice_commons.data.dl.manager import DatasourceManager, ProjectManager
from ice_rest.rest.services.parse.impl.common.missed_utterances_impl import missedUtterences
from ice_rest.rest.services.parse.impl.common.store_utils import get_model_store, get_requested_services
from ice_commons.utility.custom_tokenizer import tokenize_utterance
from ice_commons.core.model_utils import get_engine
from ice_commons.utils import MODEL_TYPE_IR, MODEL_TYPE_NER
import re
from collections import OrderedDict

logger = logging.getLogger(__name__)
project_manager = ProjectManager()
datasource_manager = DatasourceManager()


def get_proba(intent_list):
    prob = {}
    for intent_each in intent_list:
        if intent_each['name'] != "No intent":
            prob[intent_each['name']] = "0.0%"
    prob["No intent"] = "100.0%"
    return prob


def updateDatasource(serviceid, missed_text):
    """

    :param serviceid:
    :param missed_text:
    :return:
    """
    try:
        document = {
            "$addToSet": {
                "missedUtterances": missed_text,
            }
        }
        datasource_manager.update_datasource_by_service_id(serviceid, document)
        logger.info('Utterance mapped to DB successfully')

    except Exception as e:
        logger.exception(e)
        return {
            "serviceid": serviceid,
            "MissedUtterance": missed_text,
            "Error": e

        }

def replace_synonym(text, synonym_dic):
    logger.info("Replace synonynm function -------------")
    text = re.sub(' +', ' ', text.strip())
    synonym_found = OrderedDict()
    syn_indexes = OrderedDict()
    tokens = text.split()
    for item in synonym_dic:
        synonym_list = item['synonym']
        word = item['word']
        for each_synonym in synonym_list:
            m=-1
            text3 = text
            index_list =[]
            while m!=None:
                r = re.compile(r'\b%s\b' % each_synonym.upper(), re.I)
                m = r.search(text.upper())
                if(m==None):
                    x=1
                else:
                    index_list.append(m.start())
                    len1= len(each_synonym.upper())
                    space=" "
                    for i in range(0,len1):
                        space+=' '
                    text2 = text[0:m.start()]+space
                    text2 += text[len(text2):len(text)]
                    text = text2
            text = text3
            for index in index_list:
                if index != -1:
                    spaceCount = 0
                    for counter in range(0, index):
                        if text[counter] == " ":
                            spaceCount += 1
                    spacesInSynonym = each_synonym.count(" ")
                    synonym_found[str(" ".join(tokens[spaceCount:spaceCount + spacesInSynonym + 1])) + "$%^&*" + str(
                        spaceCount) + "$%^&*" + str(spaceCount + spacesInSynonym + 1)] = [word, spaceCount,
                                                                                          spaceCount + spacesInSynonym + 1]
    temp_values=[]
    for k,v in list(synonym_found.items()):
        temp_values.append(v)
    def takesecond(elem):
        return elem[1]
    temp_values = sorted(temp_values,key=takesecond)
    synonym_found3 = OrderedDict()
    for z in temp_values:
        for k,v in list(synonym_found.items()):
            if(z==v):
                synonym_found3[k]=v
    key_list=[]
    value_list=[]

    for k,v in list(synonym_found3.items()):
        key_list.append(k)
        value_list.append(v)
    i=1
    while(i<len(value_list)):
        
        if(value_list[i][1]<value_list[i-1][2]):
            if(value_list[i][2]-value_list[i][1]>value_list[i-1][2]-value_list[i-1][1]):
                del synonym_found3[key_list[i-1]]
                value_list =[]
                key_list=[]
                for k,v in list(synonym_found3.items()):
                    value_list.append(v)
                    key_list.append(k)
            else:
                del synonym_found3[key_list[i]]
                value_list =[]
                key_list=[]
                for k,v in list(synonym_found3.items()):
                    key_list.append(k)
                    value_list.append(v)
        else:
            i+=1
    synonym_found = synonym_found3
    prev_diff = 0

    firstlenchange = 0
    for i in synonym_found:
        word = i.split("$%^&*")[0]
        start = int(i.split("$%^&*")[1])
        diff = len(synonym_found[i][0].split()) - len(word.split())

        if prev_diff == 0:
            syn_indexes[synonym_found[i][1]] = [synonym_found[i][2], start,
                                                start + len(synonym_found[i][0].split()), word, synonym_found[i][0]]
            if abs(diff) > 0:
                firstlenchange = 1
        else:
            if firstlenchange == 0:
                end = start + len(synonym_found[i][0].split())
                syn_indexes[synonym_found[i][1]] = [synonym_found[i][2], start,
                                                    end, word, synonym_found[i][0]]
                firstlenchange = 1
            #
            else:
                start += prev_diff
                syn_indexes[synonym_found[i][1]] = [synonym_found[i][2], start,
                                                    start + len(synonym_found[i][0].split()), word,
                                                    synonym_found[i][0]]
        prev_diff += diff
    tokens = text.split()
    for key in syn_indexes:
        diff = abs(syn_indexes[key][0] - key) - 1
        del tokens[key: syn_indexes[key][0]]
        tokens.insert(key, syn_indexes[key][4])
        for _ in range(diff):
            tokens.insert(key, "$%^&*")
    tokens = [x for x in tokens if x != "$%^&*"]
    text = " ".join(tokens)
    logger.info("new text after synonym replacement is-----------***********-------  %s" % text)
    logger.info("dictionary with synonym indexes  -------- *** ---------   %s" % syn_indexes)
    return text, syn_indexes



def find_indexes(text, word, start=0):
    index_list = [match.start() for match in re.finditer(re.escape(word.upper()), text.upper())]
    closest = 999999
    end = 0
    new_start = 0
    for index in index_list:
        if index != -1:
            spaceCount = 0
            for counter in range(0, index):
                if text[counter] == " ":
                    spaceCount += 1
            spacesInSynonym = word.count(" ")

            diff2 = abs(start - spaceCount)
            if diff2 < closest:
                new_start = spaceCount
                end = spaceCount + spacesInSynonym + 1
                closest = diff2
    if end != 0:
        return True, new_start, end
    else:
        return False, None, None


def get_synonym_words(synonym_dic):
    synonym_words = {}
    for item in synonym_dic:
        synonym_words[str(item['word']).lower()] = item['synonym']
    return synonym_words


def modify_entities(entities_sorted, syn_indexes, retokenized_text, synonym_dic):
    synonym_words = get_synonym_words(synonym_dic)
    for entity in entities_sorted:
        if 'resolvedTo' not in entity:
            entity['resolvedTo'] = {}
        check = True
        if len(list(syn_indexes.keys())) > 0:
            for item in syn_indexes:
                if entity['start'] >= syn_indexes[item][1] and entity['end'] <= syn_indexes[item][2]:
                    entity['end'] = syn_indexes[item][0]
                    entity['start'] = item
                    entity['resolvedTo']['baseEntity'] = syn_indexes[item][4]
                    entity['entity'] = syn_indexes[item][3]
                    check = False
                    break

            if check:
                flag, start, end = find_indexes(retokenized_text, str(entity['entity']), entity['start'])
                entity['resolvedTo']['baseEntity'] = entity['entity']
                if flag:
                    entity['start'] = start
                    entity['end'] = end
                else:
                    entity_tokens = entity['entity'].split()
                    syn_found = []
                    for ind, tok in enumerate(entity_tokens):
                        if tok.lower() in synonym_words:
                            for syn in synonym_words[tok]:
                                flag, start, end = find_indexes(retokenized_text, syn)
                                if flag:
                                    syn_found.append(" ".join(retokenized_text.split()[start:end]))
                            for syn in syn_found:
                                entity_tokens[ind] = syn
                                entity['entity'] = " ".join(entity_tokens)
                                flag, start, end = find_indexes(retokenized_text, str(entity['entity']))
                                if flag:
                                    entity['start'] = start
                                    entity['end'] = end
                                    break
            else:
                continue

        else:
            entity['resolvedTo']['baseEntity'] = entity['entity']
    return entities_sorted


def predict_preprocessing(text, store, datasources_map):
    text = text.replace('\xa0', ' ')
    logger.info("initialising datasource manager in predict_impl")
    logger.info("calling truecaser on store for user text %s" % store)
    truecased_text, retokenized_text = store.change_case(text)
    syn_processed_text, syn_indexes = replace_synonym(retokenized_text, datasources_map["synonymMappings"])

    logger.info("calling truecaser on store for replaced synonym text %s" % store)
    syn_processed_truecased_text, syn_processed_retokenized_text = store.change_case(syn_processed_text)
    logger.info("truecaser completed")
    return truecased_text, retokenized_text, syn_processed_text, syn_processed_truecased_text, syn_processed_retokenized_text, syn_indexes


def fetch_data_mappings(doc):
    query = {
        "serviceid": get(doc, "serviceid")
    }
    corpus = datasource_manager.find_datasource_by_service_id(doc["serviceid"])
    project_config = project_manager.find_model(query)
    datasources_map = {"predefined_entities": get(corpus, "predefined_entities", default=[]),
                       "entities": get(corpus, "entities", default=[]),
                       "patterns": get(corpus, "patterns", default=[]), "phrases": get(corpus, "phrases", default=[]),
                       "distinct_token_list": get(corpus, "distinct_token_list", default=[]),
                       "intents": get(corpus, "intents", default=[]),
                       "synonymMappings": get(corpus, "synonyms", [])}
    projects_map = {"custom_entity_model": get(project_config, "custom_entity_model",
                                               default="ice_commons.er.engines.crf_ner.CRFCustomNER"),
                    "ner_status": get(project_config, "ner.status", default=[]),
                    "language": get(project_config, "language", "EN"), "predefined_entity_model": get(project_config,
                                                                                                      "predefined_entity_model",
                                                                                                      default="ice_commons.er.engines.spacy_ner.SpacyDefaultNER")}

    return corpus, datasources_map, projects_map


def ner_entities(store, config, serviceid, model_type, engine, truecased_text, retokenized_text,
                 syn_processed_truecased_text, syn_processed_retokenized_text, syn_indexes, default_engine,
                 datasources_map, projects_map, pos):
    entities, _ = store.get_entities(serviceid, model_type, engine, syn_processed_truecased_text,
                                     syn_processed_retokenized_text, None,
                                     default_engine, datasources_map, projects_map)
    parts_of_speech = store.get_pos_tags(truecased_text, retokenized_text, projects_map['language'], pos)

    entities_sorted = sorted(entities, key=lambda k: k['start'])
    entities = modify_entities(entities_sorted, syn_indexes, retokenized_text, datasources_map['synonymMappings'])
    entity_tags = store.tag_for_intent(serviceid, syn_processed_truecased_text, syn_processed_retokenized_text, engine,
                                       default_engine, config['predefined_entity_model'], datasources_map, projects_map)
    return entities, entity_tags, parts_of_speech


def ir_entity_tags(store, serviceid, model_type, engine, syn_processed_truecased_text, entity_tags, datasources_map):
    if entity_tags is not None:
        text_tokens = syn_processed_truecased_text.split()
        indexes_to_delete = []
        text_tokens_final = []
        for entity_each in entity_tags:
            start = entity_each["start"]
            end = entity_each["end"]
            text_tokens[start] = entity_each["tag"]
            while (end - start > 1):
                start = start + 1
                indexes_to_delete.append(start)
        for index, token_each in enumerate(text_tokens):
            if index not in indexes_to_delete:
                text_tokens_final.append(token_each)
        text = " ".join(text_tokens_final)

    else:
        text = syn_processed_truecased_text
    tokens = tokenize_utterance(text)
    distinct_token_list = get(datasources_map, "distinct_token_list", default=[])
    if distinct_token_list is None:
        distinct_token_list = []
    tokens = list(set(tokens))
    synonym_config = get(datasources_map, "synonymMappings", default=[])
    for item in synonym_config:
        distinct_token_list.append(item['word'])
        distinct_token_list += [i for i in item['synonym']]
    distinct_token_list = list(set(distinct_token_list))
    distinct_token_list = [x.upper() for x in distinct_token_list]
    tokens = [x.upper() for x in tokens]

    flag = 0
    for i in range(len(tokens)):
        if tokens[i] in distinct_token_list:
            flag = 1
            break
    if (len(distinct_token_list) > 0) and (flag == 0):
        prediction = "No intent"
        intent_list = get(datasources_map, "intents", default=[])
        if len(intent_list) > 0:
            probabilities = [get_proba(intent_list)]
        else:
            probabilities = [
                {
                    "No intent": "100.0%"
                }
            ]
    else:
        prediction, probabilities = store.get_intent(serviceid, model_type, engine, text)
    return prediction, probabilities


def predict_impl(doc, config, req_id=None):
    text = doc["text"]
    store = get_model_store()
    entity_tags = None
    response = {
        "text": text
    }
    corpus, datasources_map, projects_map = fetch_data_mappings(doc)
    truecased_text, retokenized_text, syn_processed_text, syn_processed_truecased_text, syn_processed_retokenized_text, syn_indexes = predict_preprocessing(
        text, store, datasources_map)

    for index, (serviceid, model_type, pos) in enumerate(get_requested_services(doc)):
        logger.info((serviceid, model_type, pos))
        engine = get_engine(config['custom_entity_model'])
        default_engine = get_engine(config['predefined_entity_model'])

        if model_type == MODEL_TYPE_NER:
            entities, entity_tags, parts_of_speech = ner_entities(store, config, serviceid, model_type, engine,
                                                                  truecased_text, retokenized_text,
                                                                  syn_processed_truecased_text,
                                                                  syn_processed_retokenized_text, syn_indexes,
                                                                  default_engine, datasources_map, projects_map, pos)
            response["entities"] = entities
            if (parts_of_speech is not None) and (get (doc,'pos', default=True) is True):
                response["parts_of_speech"] = parts_of_speech

        elif model_type == MODEL_TYPE_IR:
            prediction, probabilities = ir_entity_tags(store, serviceid, model_type, engine,
                                                       syn_processed_truecased_text, entity_tags, datasources_map)
            logger.info("prediction......................%s" % prediction)
            logger.info("probabilities......................%s" % probabilities)
            response["intent"] = {
                "top_intent": prediction,
                "confidence_level": probabilities
            }
            missed_text = missedUtterences(response, doc['serviceid'], req_id, syn_processed_retokenized_text)
            if missed_text is not syn_processed_retokenized_text:
                updateDatasource(serviceid, missed_text)
    if 'entities' not in response:
        response['entities'] = []
    if 'parts_of_speech' not in response:
        response['parts_of_speech'] = []
    return response



def start_end_checker(entities):
    key_pairs = [list(items.keys()) for items in entities]
    for items in key_pairs:
        if 'start' and 'end' in items:
            return 1
        else:
            return 0


def modify_response_v1(results):
    text = results["text"]
    response = {"text": text}
    entities = results.get("entities")
    value = start_end_checker(entities)
    response["entities"] = entities

    if value == 1:
        for items in entities:
            del items['start']
            del items['end']
    else:
        pass

    if "intent" in list(results.keys()):
        top_intent = results["intent"]["top_intent"]
        response["intent"] = {
            "category": top_intent,
            "probabilities": []
        }

    return response
