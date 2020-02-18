import pytest
from ice_commons.data.dl.manager import IceEntitiesModelManager
from ice_commons.er.engines.spacy_ner import SpacyDefaultNER
from ice_commons.core.resolution.measurements_er import MeasurementsResolutionNER
from pydash import concat
from ice_commons.store.models import ModelStore


def test_tag_with_exception(mocker):
    store = mocker.patch.object(ModelStore, 'get_model', ModelStore())
    mocker.patch('ice_commons.store.models.get_entities_for_default_model',return_value = None)
    mocker.patch.object(SpacyDefaultNER ,'predict', return_value =(None))
    mocker.patch.object(store, 'filter_prediction_results', return_value =None)
    mocker.patch.object(IceEntitiesModelManager,'get_ice_entities', return_value =None)
    mocker.patch.object(store,'get_resolved_mappings',return_value = None)
    mocker.patch.object(store, 'handle_resolution_overlap', return_value =[])
    mocker.patch.object(store,'get_entities_for_ds', return_value =None)
    mocker.patch.object(store,'filter_tag_results', return_value =([], []))

    resp = store.tag(None, '', '', None, None, None, {},{})
    expected= {
                "utterance": '',
                "case_converted_utterance": '',
                "tokens": ''.split(),
                "custom_tags": [],
                "default_tags": []
            }
    assert resp == expected



def test_tag_with_default_none(mocker):
    model = mocker.patch.object(ModelStore, 'get_model', return_value = SpacyDefaultNER())
    store = ModelStore()
    mocker.patch('ice_commons.store.models.get_entities_for_default_model',return_value = [])
    mocker.patch.object(model.return_value ,'predict', return_value =([],[]))
    mocker.patch.object(store, 'filter_prediction_results', return_value =[])
    mocker.patch.object(IceEntitiesModelManager,'get_ice_entities', return_value =None)
    mocker.patch.object(store,'get_resolved_mappings',return_value = [])
    mocker.patch.object(store, 'handle_resolution_overlap', return_value =[])
    mocker.patch.object(store,'filter_tag_results', return_value =([], []))

    resp = store.tag(None, 'Hello How are you ?', 'hello how are you?', None, None, None, {},{})
    expected= {
                "utterance": 'hello how are you?',
                "case_converted_utterance": 'Hello How are you ?',
                "tokens": ['Hello', 'How','are','you','?'],
                "custom_tags": [],
                "default_tags": []
            }
    assert resp == expected


def test_tag_with_serviceid(mocker):
    model = mocker.patch.object(ModelStore, 'get_model', return_value = SpacyDefaultNER())
    store = ModelStore()
    mocker.patch('ice_commons.store.models.get_entities_for_default_model',return_value = [])
    mocker.patch.object(model.return_value ,'predict', return_value =([],[]))
    mocker.patch.object(store, 'filter_prediction_results', return_value =[])
    mocker.patch.object(IceEntitiesModelManager,'get_ice_entities', return_value =None)
    mocker.patch.object(store,'get_resolved_mappings',return_value = [])
    mocker.patch.object(store, 'handle_resolution_overlap', return_value =[])
    mocker.patch.object(store,'get_entities_for_ds', return_value =[])
    mocker.patch.object(store,'filter_tag_results', return_value =([], []))

    resp = store.tag('abc', 'Hello How are you ?', 'hello how are you?', None, None, None, {},{})
    expected= {
                "utterance": 'hello how are you?',
                "case_converted_utterance": 'Hello How are you ?',
                "tokens": ['Hello', 'How','are','you','?'],
                "custom_tags": [],
                "default_tags": []
            }
    assert resp == expected


def test_handle_resolution_overlap_with_empty_list():
    store = ModelStore()
    resp = store.handle_resolution_overlap([])
    expected = []
    assert resp == expected


def test_handle_resolution_overlap_without_overlap():
    store = ModelStore()
    resp = store.handle_resolution_overlap([{'start' : 4, 'end':6}, {'start' : 6, 'end':7}, {'start' : 8, 'end':10}])
    expected = [{'start' : 4, 'end':6}, {'start' : 6, 'end':7}, {'start' : 8, 'end':10}]
    assert resp == expected

def test_handle_resolution_overlap_with_overlap():
    store = ModelStore()
    resp = store.handle_resolution_overlap([{'start' : 0, 'end':2, 'entity' : 'karan singla'}, {'start' : 1, 'end':3, 'entity' :'singla is' },
                                            {'start' : 2, 'end':6,'entity' :'is famous in Delhi' }])
    expected = [{'start' : 0, 'end':2, 'entity' : 'karan singla'}, {'start' : 2, 'end':6,'entity' :'is famous in Delhi' }]
    assert resp == expected


def test_get_resolved_mappings_with_null(mocker):
    store = ModelStore()
    mocker.patch('ice_commons.store.models.create_instance', return_value= None)
    resp= store.get_resolved_mappings([], None)
    assert resp == []


def test_get_resolved_mappings_emptylist(mocker):
    store = ModelStore()
    obj = mocker.patch('ice_commons.store.models.create_instance', return_value= MeasurementsResolutionNER())
    expected= mocker.patch.object(obj.return_value, 'resolve', return_value= [])
    resp = store.get_resolved_mappings([{'resolutionClass': 'i', 'name': 'Weight'}], 'karan weighs around 68 kgs')
    assert resp == expected.return_value


def test_get_resolved_mappings(mocker):
    store = ModelStore()
    obj = mocker.patch('ice_commons.store.models.create_instance', return_value= MeasurementsResolutionNER())
    expected= mocker.patch.object(obj.return_value, 'resolve', return_value= [{'entity' : '68 kgs', 'tag':'weight'}])
    resp = store.get_resolved_mappings([{'resolutionClass': 'i', 'name': 'Weight'}], 'karan weighs around 68 kgs')
    assert resp == expected.return_value


def test_filter_prediction_results1():
    store = ModelStore()
    default= [{'start' : 0, 'end':2, 'entity' : 'karan singla', 'tag':'PERSON'}, {'start' : 1, 'end':3, 'entity' :'singla is' ,'tag':'MISC'},
                {'start' : 2, 'end':6,'entity' :'is famous in Delhi','tag':'LOCATION'}]
    resp = store.filter_prediction_results(default, ['PERSON','LOCATION'])
    expected = [{'start' : 0, 'end':2, 'entity' : 'karan singla', 'tag':'PERSON'},
                {'start' : 2, 'end':6,'entity' :'is famous in Delhi','tag':'LOCATION'}]
    assert resp==expected


def test_filter_prediction_results2():
    store = ModelStore()
    default= []
    resp = store.filter_prediction_results(default, [])
    expected = []
    assert resp==expected


def test_change_case_with_null(mocker):
    tokens= mocker.patch('ice_commons.store.models.tokenize_utterance', return_value=[])
    store = ModelStore()
    mocker.patch.object(store, 'get_model', None)
    case_conve = mocker.patch('ice_commons.store.models.convert_case', return_value=[])
    store = ModelStore()
    text= ''
    text, original_text = store.change_case(text)
    assert text == " ".join(case_conve.return_value)
    assert original_text == " ".join(tokens.return_value)


def test_change_case_with_text(mocker):
    tokens= mocker.patch('ice_commons.store.models.tokenize_utterance', return_value=['hello','how','are','you','?'])
    store = ModelStore()
    mocker.patch.object(store, 'get_model', None)
    case_conve = mocker.patch('ice_commons.store.models.convert_case', return_value=['Hello', 'How','Are', 'You', '?'])
    store = ModelStore()
    text= 'hello how are you?'
    text, original_text = store.change_case(text)

    assert text == " ".join(case_conve.return_value)
    assert original_text == " ".join(tokens.return_value)


def test_get_entities_for_ds_with_null(mocker):
    store = ModelStore()
    mocker.patch('ice_commons.store.models.regex_checker', return_value=[])
    mocker.patch('ice_commons.store.models.phrase_checker', return_value=[])
    pattern_response, phrase_response, predefined_tags = store.get_entities_for_ds(None, None ,{})
    assert pattern_response==[]
    assert phrase_response==[]
    assert predefined_tags==[]


def test_get_entities_for_ds_with_data1(mocker):
    store = ModelStore()
    mocker.patch('ice_commons.store.models.regex_checker', return_value=[])
    mocker.patch('ice_commons.store.models.phrase_checker', return_value=[{
                     "tag": 'name',
                     "start": 0,
                     "entity": 'Karan',
                     "end": 1
                   }])
    pattern_response, phrase_response, predefined_tags = store.get_entities_for_ds(None, 'Karan singla' ,
    {'phrases':[
		{
			"phrase" : [
				"Karan"
			],
		"entity" : "name"
		}
	]})
    assert pattern_response==[]
    assert phrase_response==[{
                     "tag": 'name',
                     "start": 0,
                     "entity": 'Karan',
                     "end": 1
                   }]
    assert predefined_tags==[]



def test_get_entities_for_ds_with_data2(mocker):
    store = ModelStore()
    mocker.patch('ice_commons.store.models.regex_checker', return_value=[{
                     "tag": 'email',
                     "start": 0,
                     "entity": 'Karan@gmail.com',
                     "end": 1
                   }])
    mocker.patch('ice_commons.store.models.phrase_checker', return_value=[])
    pattern_response, phrase_response, predefined_tags = store.get_entities_for_ds(None, 'Karan singla' ,
    {'patterns':[
		{
			"entity" : "email",
			"pattern" : "[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-z.A-Z]{2,6}"
		}
	], 'predefined_entities':['a','b']})
    assert pattern_response==[{
                     "tag": 'email',
                     "start": 0,
                     "entity": 'Karan@gmail.com',
                     "end": 1
                   }]
    assert phrase_response==[]
    assert predefined_tags==['a','b']



def test_filter_tag_results_null(mocker):
    store = ModelStore()
    m1= mocker.patch.object(store,'remove_overlaps_and_duplicates', return_value=([],[]))
    assert m1.return_value == ([],[])
    m2=mocker.patch.object(store,'remove_overlaps_and_duplicates', return_value=([],[]))
    assert m2.return_value == ([], [])
    m3=mocker.patch.object(store,'remove_overlaps_and_duplicates', return_value=([],[]))
    assert m3.return_value == ([], [])
    mocker.patch.object(store, 'filter_model_tags', return_value=([], []))
    m4=mocker.patch.object(store, 'remove_overlaps_and_duplicates', return_value=([],[]))
    assert m4.return_value == ([], [])
    m5 = mocker.patch.object(store, 'remove_overlaps_and_duplicates', return_value=([], []))
    assert m5.return_value == ([], [])
    resp1, resp2 = store.filter_tag_results([], [],[], [], [], [], [])
    assert resp1==[]
    assert resp2==[]


def test_filter_tag_results_data1(mocker):
    store = ModelStore()
    m = mocker.patch.object(store, 'remove_overlaps_and_duplicates')
    m.side_effect = [([], []), ([], []), ([], []), ([], []), ([], [])]
    resp1, resp2 = store.filter_tag_results([], [], [], [], [], [], [])
    assert resp1 == concat([], [])
    assert resp2 == concat([], [], [])


def test_filter_tag_results_data2(mocker):
    store = ModelStore()
    # text = 'Karan has a meeting with Dr. Neeru in Delhi next thursday'
    m = mocker.patch.object(store, 'remove_overlaps_and_duplicates')
    m.side_effect = [([{'start':9, 'end':11, 'entity':'next thursday', 'tag':'TIMESTAMP'}], [9,10]),
                     ([], [9,10]),
                     ([], [9,10]),
                     ([{'start':8, 'end':9, 'entity':'Delhi', 'tag':'LOCATION'}, {'start':0, 'end':1, 'entity':'Karan', 'tag':'PERSON'}], [9,10,8,0]),
                     ([{'start':5, 'end':7, 'entity':'Dr. Neeru', 'tag':'DOCTOR'}], [9,10,8,0,5,6])]
    resp1, resp2 = store.filter_tag_results([{'start':8, 'end':9, 'entity':'Delhi', 'tag':'LOCATION'}, {'start':0, 'end':1, 'entity':'Karan', 'tag':'PERSON'}],
                                            [{'start':5, 'end':7, 'entity':'Dr. Neeru', 'tag':'DOCTOR','score':0.66},{'start':0, 'end':1, 'entity':'Karan', 'tag':'PATIENT','score':0.4}],
                                            [], [],
                                            ['LOCATION','PERSON'], ['DOCTOR','PATIENT'],
                                            [{'start':9, 'end':11, 'entity':'next thursday', 'tag':'TIMESTAMP'}])
    assert resp1 == concat([{'start': 8, 'tag': 'LOCATION', 'end': 9, 'entity': 'Delhi'},
                             {'start': 0, 'tag': 'PERSON', 'end': 1, 'entity': 'Karan'},
                             {'start': 9, 'tag': 'TIMESTAMP', 'end': 11, 'entity': 'next thursday'}])
    assert resp2 == concat([{'start': 5, 'tag': 'DOCTOR', 'end': 7, 'entity': 'Dr. Neeru'}], [], [])



def test_filter_tag_results_data3(mocker):
    store = ModelStore()
    # text = 'Karan has a meeting with Dr. Neeru in Delhi next thursday'
    m = mocker.patch.object(store, 'remove_overlaps_and_duplicates')
    m.side_effect = [([{'start':9, 'end':11, 'entity':'next thursday', 'tag':'TIMESTAMP'}], [9,10]),
                     ([], [9,10]),
                     ([], [9,10]),
                     ([{'start':8, 'end':9, 'entity':'Delhi', 'tag':'LOCATION'}], [9,10,8]),
                     ([{'start':5, 'end':7, 'entity':'Dr. Neeru', 'tag':'DOCTOR'},{'start':0, 'end':1, 'entity':'Karan', 'tag':'PATIENT','score':0.4}], [9,10,8,0,5,6])]
    resp1, resp2 = store.filter_tag_results([{'start':8, 'end':9, 'entity':'Delhi', 'tag':'LOCATION'}, {'start':0, 'end':1, 'entity':'Karan', 'tag':'PERSON'}],
                                            [{'start':5, 'end':7, 'entity':'Dr. Neeru', 'tag':'DOCTOR','score':0.66},{'start':0, 'end':1, 'entity':'Karan', 'tag':'PATIENT','score':0.4}],
                                            [], [],
                                            ['LOCATION','PERSON'], ['DOCTOR','PATIENT'],
                                            [{'start':9, 'end':11, 'entity':'next thursday', 'tag':'TIMESTAMP'}])
    assert resp1 == concat([{'start': 8, 'tag': 'LOCATION', 'end': 9, 'entity': 'Delhi'},
                             {'start': 9, 'tag': 'TIMESTAMP', 'end': 11, 'entity': 'next thursday'}])
    assert resp2 == concat([{'start': 5, 'tag': 'DOCTOR', 'end': 7, 'entity': 'Dr. Neeru'},{'start':0, 'end':1, 'entity':'Karan', 'tag':'PATIENT','score':0.4}],
                           [], [])




def test_remove_overlaps_and_duplicates():
    store = ModelStore()
    predictions, tagged_indexes = store.remove_overlaps_and_duplicates([],[])

    assert predictions==[]
    assert tagged_indexes==[]

def test_remove_overlaps_and_duplicates1():
    store = ModelStore()
    predictions, tagged_indexes = store.remove_overlaps_and_duplicates([{'start':8,'end':10}],[9])
    assert predictions==[]
    assert tagged_indexes==[9]

def test_remove_overlaps_and_duplicates2():
    store = ModelStore()
    predictions, tagged_indexes = store.remove_overlaps_and_duplicates([{'start':8,'end':10}, {'start':3,'end':5}],[9])
    assert predictions==[{'start':3,'end':5}]
    assert tagged_indexes==[9,3,4]


def test_get_entities_null(mocker):
    store = ModelStore()
    serviceid = model_type = custom_engine = text = original_text = pos = default_engine = ""
    datasources_map = projects_map = {}
    model = mocker.patch('ice_commons.store.models.ModelStore.get_model')
    model.return_value.predict.return_value = ([], [])
    mocker.patch('ice_commons.store.models.ModelStore.filter_prediction_results')
    ice_ent = mocker.patch('ice_commons.store.models.IceEntitiesModelManager')
    ice_ent.return_value.get_ice_entities.return_value = []
    mocker.patch('ice_commons.store.models.ModelStore.get_resolved_mappings', return_value=[])
    mocker.patch('ice_commons.store.models.ModelStore.get_entities_for_ds', return_value=[[], [], []])

    resp = (store.get_entities(serviceid, model_type, custom_engine, text, original_text, pos, default_engine,
                               datasources_map, projects_map))
    assert resp == ([], None)


def test_get_entities_data(mocker):
    store = ModelStore()

    serviceid = "MedicalAssistant-test"
    model_type = "ner"
    datasources_map = dict(
        predefined_entities=["PERSON", "NORP", "FACILITY", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART",
                             "LANGUAGE", "ORDINAL"], entities=["CATEGORY", "DISEASE", "DOCTOR", "PATIENT"], patterns=[
            dict(entity="custom_date", pattern="\\d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}"),
            dict(entity="custom_email", pattern="[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}")], distinct_token_list=[],
        intents=[], synonymMappings=[])
    default_engine = "ice_commons.er.engines.spacy_ner.SpacyDefaultNER"
    custom_engine = "ice_commons.er.engines.mitie_ner.MitieCustomNER"
    pos = True
    projects_map = dict(custom_entity_model="ice_commons.er.engines.mitie_ner.MitieCustomNER", ner_status="trained",
                        language="EN", predefined_entity_model="ice_commons.er.engines.spacy_ner.SpacyDefaultNER")

    original_text = "Is Dr . Manu Nair , Cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM "
    text = "Is Dr . Manu Nair , cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM"


    model = mocker.patch('ice_commons.store.models.ModelStore.get_model')
    model.return_value.predict.return_value = ([], [])
    mocker.patch('ice_commons.store.models.ModelStore.filter_prediction_results', return_value = [
        dict(start=12, tag='custom_date', end=17, entity='21 / 10 / 2018')])
    ice_ent = mocker.patch('ice_commons.store.models.IceEntitiesModelManager')
    ice_ent.return_value.get_ice_entities.return_value = []
    mocker.patch('ice_commons.store.models.ModelStore.get_resolved_mappings', return_value=[])
    mocker.patch('ice_commons.store.models.ModelStore.get_entities_for_ds', return_value=[[], [], []])


    resp = (store.get_entities(serviceid, model_type, custom_engine, text, original_text, pos, default_engine,
                               datasources_map, projects_map))
    assert resp == ([{'start': 12, 'tag': 'custom_date', 'end': 17, 'entity': '21 / 10 / 2018'}], [])


def test_get_pos_tags_null():
    store = ModelStore()
    text = original_text = ""
    assert store.get_pos_tags(text, original_text) == []


def test_get_pos_tags_data(mocker):
    store = ModelStore()
    text = original_text = "Is Dr . Manu Nair , Cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM"
    mocker.patch.object(store, 'get_model', return_value=None)
    assert store.get_pos_tags(text, original_text) == []


def test_get_model_null():
    store = ModelStore()
    serviceid = model_type = engine = ""
    assert store.get_model(serviceid, model_type, engine) is None


def test_get_model_data():
    store = ModelStore()
    serviceid = "MedicalAssistant-test"
    model_type = "ner"
    engine = "SPACY"
    assert store.get_model(serviceid, model_type, engine) is None


def test_get_intent_null():
    store = ModelStore()
    serviceid = model_type = engine = text = ""
    assert store.get_intent(serviceid, model_type, engine, text) == ([], [])


def test_get_intent_data(mocker):
    store = ModelStore()
    serviceid = "MedicalAssistant-test"
    model_type = "ir"
    engine = "ice_commons.er.engines.mitie_ner.MitieCustomNER"
    text = "I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza"
    mocker.patch.object(store, 'get_model', None)
    assert store.get_intent(serviceid, model_type, engine, text) is None


def test_tag_for_intent_null(mocker):
    store = ModelStore()
    service_id = text = original_text = engine = default_engine = default_model_class = ""
    datasources_map = projects_map = {}
    mocker.patch.object(store, 'tag', return_value={"custom_tags": [], "default_tags": []})
    resp = store.tag_for_intent(service_id, text, original_text, engine, default_engine, default_model_class,
                                datasources_map, projects_map)
    assert resp == []

def test_tag_for_intent_data(mocker):
    store = ModelStore()
    service_id = "MedicalAssistant-test"
    text = original_text = "Is Dr . Manu Nair , Cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM"
    engine = "ice_commons.er.engines.mitie_ner.MitieCustomNER"
    default_engine = default_model_class = "ice_commons.er.engines.spacy_ner.SpacyDefaultNER"
    datasources_map = projects_map = {}
    mocker.patch.object(store, 'tag', return_value={"custom_tags": [], "default_tags": []})
    resp = store.tag_for_intent(service_id, text, original_text, engine, default_engine, default_model_class,
                         datasources_map, projects_map)
    assert resp == []

