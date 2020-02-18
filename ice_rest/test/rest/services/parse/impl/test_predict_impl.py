import datetime
from collections import OrderedDict

from bson import ObjectId
from ice_commons.data.dl.manager import DatasourceManager
from ice_commons.store.models import ModelStore
from ice_rest.rest.services.parse.impl.predict_impl import updateDatasource, predict_impl, ner_entities, ir_entity_tags, \
    fetch_data_mappings, predict_preprocessing, replace_synonym, modify_entities, get_synonym_words, find_indexes, \
    modify_response_v1, get_proba


def test_predict_impl_with_no_intent_no_entity_no_pos(mocker):
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.fetch_data_mappings', return_value=({}, {}, {}))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.predict_preprocessing',
                 return_value=("", "", "", "", "", ""))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_requested_services', return_value=[])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_engine', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ner_entities',
                 return_value=([], [], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ir_entity_tags', return_value=([], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.missedUtterences', return_value="")
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.updateDatasource', return_value=None)
    doc = {'serviceid': '', 'text': ''}
    config = {'custom_entity_model': '',
              'predefined_entity_model': ''}
    resp = predict_impl(doc, config, None)
    expected = dict(entities=[], parts_of_speech=[], text='')
    assert resp == expected


def test_predict_impl_ir_and_ner_true_without_pos_in_input_(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch(
        'ice_rest.rest.services.parse.impl.predict_impl.fetch_data_mappings', return_value=[{}, {}, {}])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.predict_preprocessing',
                 return_value=("", "", "", "", "", ""))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_requested_services',
                 return_value=[('MedicalAssistant-test', 'ner', False), ('MedicalAssistant-test', 'ir', False)])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_engine', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ner_entities',
                 return_value=([], [], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ir_entity_tags', return_value=([], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.missedUtterences', return_value="")
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.updateDatasource', return_value=None)
    doc = {'serviceid': 'MedicalAssistant-test', 'text': 'hiii', 'entity': True, 'intent': True}
    config = {'custom_entity_model': '',
              'predefined_entity_model': ''}
    resp = predict_impl(doc, config, None)
    expected = dict(text='hiii', parts_of_speech=[], intent={'top_intent': [], 'confidence_level': []}, entities=[])
    assert resp == expected


def test_predict_impl_with_entity_true(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch(
        'ice_rest.rest.services.parse.impl.predict_impl.fetch_data_mappings', return_value=[{}, {}, {}])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.predict_preprocessing',
                 return_value=("", "", "", "", "", ""))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_requested_services',
                 return_value=[('MedicalAssistant-test', 'ner', 'yes')])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_engine', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ner_entities',
                 return_value=([], [], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ir_entity_tags', return_value=([], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.missedUtterences', return_value="")
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.updateDatasource', return_value=None)
    doc = {'serviceid': 'MedicalAssistant-test', 'text': 'hiii', 'entity': True, 'intent': False}

    config = {'custom_entity_model': '',
              'predefined_entity_model': ''}
    resp = predict_impl(doc, config, None)
    expected = dict(text='hiii', parts_of_speech=[], entities=[])
    assert resp == expected


def test_predict_impl_with_intent_true(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch(
        'ice_rest.rest.services.parse.impl.predict_impl.fetch_data_mappings', return_value=[{}, {}, {}])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.predict_preprocessing',
                 return_value=("", "", "", "", "", ""))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_requested_services',
                 return_value=[('MedicalAssistant-test', 'ir', None)])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_engine', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ner_entities',
                 return_value=([], [], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ir_entity_tags', return_value=([], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.missedUtterences', return_value="")
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.updateDatasource', return_value=None)
    doc = {'serviceid': 'MedicalAssistant-test', 'text': 'hiii', 'entity': False, 'intent': True}
    config = {'custom_entity_model': '',
              'predefined_entity_model': ''}
    resp = predict_impl(doc, config, None)
    expected = dict(text='hiii', parts_of_speech=[], intent={'top_intent': [], 'confidence_level': []}, entities=[])
    assert resp == expected


def test_predict_impl_with_pos_true_entity_false(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch(
        'ice_rest.rest.services.parse.impl.predict_impl.fetch_data_mappings', return_value=[{}, {}, {}])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.predict_preprocessing',
                 return_value=("", "", "", "", "", ""))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_requested_services',
                 return_value=[])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_engine', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ner_entities',
                 return_value=([], [], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ir_entity_tags', return_value=([], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.missedUtterences', return_value="")
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.updateDatasource', return_value=None)
    doc = {'serviceid': 'MedicalAssistant-test', 'text': 'hiii', 'pos': True, 'entity': False, 'intent': False}

    config = {'custom_entity_model': '',
              'predefined_entity_model': ''}
    resp = predict_impl(doc, config, None)
    expected = dict(text='hiii', parts_of_speech=[], entities=[])
    assert resp == expected


def test_predict_impl_with_pos_true_entity_true(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch(
        'ice_rest.rest.services.parse.impl.predict_impl.fetch_data_mappings', return_value=[{}, {}, {}])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.predict_preprocessing',
                 return_value=("", "", "", "", "", ""))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_requested_services',
                 return_value=[('MedicalAssistant-test', 'ner', True), ('MedicalAssistant-test', 'ir', None)])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_engine', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ner_entities',
                 return_value=([], [], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ir_entity_tags', return_value=([], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.missedUtterences', return_value="")
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.updateDatasource', return_value=None)
    doc = {'serviceid': 'MedicalAssistant-test1234', 'text': 'hiii', 'pos': True, 'entity': True,
           'intent': False}

    config = {'custom_entity_model': '',
              'predefined_entity_model': ''}
    resp = predict_impl(doc, config, None)
    expected = dict(text='hiii', parts_of_speech=[], intent={'top_intent': [], 'confidence_level': []}, entities=[])
    assert resp == expected


def test_predict_impl_with_pos_true_entity_true(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch(
        'ice_rest.rest.services.parse.impl.predict_impl.fetch_data_mappings', return_value=[{}, {}, {}])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.predict_preprocessing',
                 return_value=("", "", "", "", "", ""))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_requested_services',
                 return_value=[('MedicalAssistant-test', 'ir', None)])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_engine', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ner_entities',
                 return_value=([], [], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ir_entity_tags', return_value=([], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.missedUtterences', return_value="")
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.updateDatasource', return_value=None)
    doc = {'serviceid': 'MedicalAssistant-test', 'text': 'hiii', 'pos': True, 'entity': False, 'intent': True}

    config = {'custom_entity_model': '',
              'predefined_entity_model': ''}
    resp = predict_impl(doc, config, None)
    expected = dict(text='hiii', parts_of_speech=[], intent={'top_intent': [], 'confidence_level': []}, entities=[])
    assert resp == expected


def test_predict_impl_with_pos_true_entity_true_intent_true(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch(
        'ice_rest.rest.services.parse.impl.predict_impl.fetch_data_mappings', return_value=[{}, {}, {}])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.predict_preprocessing',
                 return_value=("", "", "", "", "", ""))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_requested_services',
                 return_value=[('MedicalAssistant-test', 'ner', True)])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_engine', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ner_entities',
                 return_value=([], [], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ir_entity_tags', return_value=([], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.missedUtterences', return_value="")
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.updateDatasource', return_value=None)
    doc = {'serviceid': 'MedicalAssistant-test', 'text': 'hiii', 'pos': True, 'entity': True, 'intent': True}

    config = {'custom_entity_model': '',
              'predefined_entity_model': ''}
    resp = predict_impl(doc, config, None)
    expected = dict(text='hiii', parts_of_speech=[], entities=[])
    assert resp == expected


def test_predict_impl_with_pos_false_entity_true_intent_true(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch(
        'ice_rest.rest.services.parse.impl.predict_impl.fetch_data_mappings', return_value=[{}, {}, {}])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.predict_preprocessing',
                 return_value=("", "", "", "", "", ""))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_requested_services',
                 return_value=[('MedicalAssistant-test', 'ner', True)])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_engine', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ner_entities',
                 return_value=([], [], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.ir_entity_tags', return_value=([], []))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.missedUtterences', return_value="")
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.updateDatasource', return_value=None)
    doc = {'serviceid': 'MedicalAssistant-test', 'text': 'hiii', 'pos': False, 'entity': True, 'intent': True}

    config = {'custom_entity_model': '',
              'predefined_entity_model': ''}
    resp = predict_impl(doc, config, None)
    expected = dict(text='hiii', parts_of_speech=[], entities=[])
    assert resp == expected


def test_ner_entities_with_null(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch.object(store.return_value, 'get_entities', return_value=([], []))
    mocker.patch.object(store.return_value, 'get_pos_tags', return_value=([]))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.modify_entities', return_value=[])
    mocker.patch.object(store.return_value, 'tag_for_intent', return_value=([]))
    serviceid = "MedicalAssistant-test"
    model_type = "ner"
    config = dict(custom_entity_model="ice_commons.er.engines.mitie_ner.MitieCustomNER",
                  predefined_entity_model="ice_commons.er.engines.spacy_ner.SpacyDefaultNER")
    datasources_map = dict(
        predefined_entities=["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART",
                             "LANGUAGE", "ORDINAL"], entities=["CATEGORY", "DISEASE", "DOCTOR", "PATIENT"], patterns=[
            dict(entity="custom_date", pattern="\\d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}"),
            dict(entity="custom_email", pattern="[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}")],
        distinct_token_list=[], intents=[], synonymMappings=[])
    default_engine = "ice_commons.er.engines.spacy_ner.SpacyDefaultNER"
    engine = "ice_commons.er.engines.mitie_ner.MitieCustomNER"
    pos = True
    projects_map = dict(custom_entity_model="ice_commons.er.engines.mitie_ner.MitieCustomNER", ner_status="trained",
                        language="EN", predefined_entity_model="ice_commons.er.engines.spacy_ner.SpacyDefaultNER")

    syn_indexes = {}
    text = "Is Dr . Manu Nair , Cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM "
    syn_processed_retokenized_text = syn_processed_truecased_text = retokenized_text = text
    truecased_text = "Is Dr . Manu Nair , cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM"
    entities, entity_tags, parts_of_speech = ner_entities(store.return_value, config, serviceid, model_type, engine,
                                                          truecased_text, retokenized_text,
                                                          syn_processed_truecased_text, syn_processed_retokenized_text,
                                                          syn_indexes, default_engine,
                                                          datasources_map, projects_map, pos)
    assert entities == [] and entity_tags == [] and parts_of_speech == []


def test_ner_entities_with_entities(mocker):
    expected_response = dict(entities=[
        dict(start=12, resolvedTo={'baseEntity': '21 / 10 / 2018'}, tag='custom_date', end=17,
             entity='21 / 10 / 2018')], entity_tags=[], parts_of_speech=[])
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch.object(store.return_value, 'get_entities', return_value=(expected_response["entities"], []))
    mocker.patch.object(store.return_value, 'get_pos_tags', return_value=(expected_response["parts_of_speech"]))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.modify_entities',
                 return_value=expected_response["entities"])
    mocker.patch.object(store.return_value, 'tag_for_intent', return_value=(expected_response["entity_tags"]))
    serviceid = "MedicalAssistant-test12345"
    model_type = "ner"
    config = dict(custom_entity_model="ice_commons.er.engines.mitie_ner.MitieCustomNER",
                  predefined_entity_model="ice_commons.er.engines.spacy_ner.SpacyDefaultNER")
    datasources_map = dict(
        predefined_entities=["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART",
                             "LANGUAGE", "ORDINAL"], entities=["CATEGORY", "DISEASE", "DOCTOR", "PATIENT"], patterns=[
            dict(entity="custom_date", pattern="\\d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}"),
            dict(entity="custom_email", pattern="[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}")], distinct_token_list=[],
        intents=[], synonymMappings=[])
    default_engine = "ice_commons.er.engines.spacy_ner.SpacyDefaultNER"
    engine = "ice_commons.er.engines.mitie_ner.MitieCustomNER"
    pos = True
    projects_map = dict(custom_entity_model="ice_commons.er.engines.mitie_ner.MitieCustomNER", ner_status="trained",
                        language="EN", predefined_entity_model="ice_commons.er.engines.spacy_ner.SpacyDefaultNER")

    syn_indexes = {}
    text = "Is Dr . Manu Nair , Cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM "
    syn_processed_retokenized_text = syn_processed_truecased_text = retokenized_text = text
    truecased_text = "Is Dr . Manu Nair , cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM"
    entities, entity_tags, parts_of_speech = ner_entities(store.return_value, config, serviceid, model_type, engine,
                                                          truecased_text, retokenized_text,
                                                          syn_processed_truecased_text, syn_processed_retokenized_text,
                                                          syn_indexes, default_engine,
                                                          datasources_map, projects_map, pos)

    assert entities == expected_response["entities"] and entity_tags == expected_response[
        "entity_tags"] and parts_of_speech == expected_response["parts_of_speech"]


def test_ner_entities_with_entity_tag(mocker):
    expected_response = dict(entities=[],
                             entity_tags=[dict(start=12, tag='custom_date', end=17, entity='21 / 10 / 2018')],
                             parts_of_speech=[])
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch.object(store.return_value, 'get_entities', return_value=(expected_response["entities"], []))
    mocker.patch.object(store.return_value, 'get_pos_tags', return_value=(expected_response["parts_of_speech"]))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.modify_entities',
                 return_value=expected_response["entities"])
    mocker.patch.object(store.return_value, 'tag_for_intent', return_value=(expected_response["entity_tags"]))
    serviceid = "MedicalAssistant-test"
    model_type = "ner"
    config = dict(custom_entity_model="ice_commons.er.engines.mitie_ner.MitieCustomNER",
                  predefined_entity_model="ice_commons.er.engines.spacy_ner.SpacyDefaultNER")
    datasources_map = dict(
        predefined_entities=["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART",
                             "LANGUAGE", "ORDINAL"], entities=["CATEGORY", "DISEASE", "DOCTOR", "PATIENT"], patterns=[
            dict(entity="custom_date", pattern="\\d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}"),
            dict(entity="custom_email", pattern="[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}")], distinct_token_list=[],
        intents=[], synonymMappings=[])
    default_engine = "ice_commons.er.engines.spacy_ner.SpacyDefaultNER"
    engine = "ice_commons.er.engines.mitie_ner.MitieCustomNER"
    pos = True
    projects_map = dict(custom_entity_model="ice_commons.er.engines.mitie_ner.MitieCustomNER", ner_status="trained",
                        language="EN", predefined_entity_model="ice_commons.er.engines.spacy_ner.SpacyDefaultNER")

    syn_indexes = {}
    text = "Is Dr . Manu Nair , Cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM "
    syn_processed_retokenized_text = syn_processed_truecased_text = retokenized_text = text
    truecased_text = "Is Dr . Manu Nair , cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM"
    entities, entity_tags, parts_of_speech = ner_entities(store.return_value, config, serviceid, model_type, engine,
                                                          truecased_text, retokenized_text,
                                                          syn_processed_truecased_text, syn_processed_retokenized_text,
                                                          syn_indexes, default_engine,
                                                          datasources_map, projects_map, pos)

    assert entities == expected_response["entities"] and entity_tags == expected_response[
        "entity_tags"] and parts_of_speech == expected_response["parts_of_speech"]


def test_ner_entities_with_pos(mocker):
    expected_response = dict(entities=[], entity_tags=[],
                             parts_of_speech=[dict(text="Is", tag="VBZ", pos="VERB", lemma="be"),
                                              dict(text="Dr", tag="NNP", pos="PROPN", lemma="dr"),
                                              dict(text=".", tag=".", pos="PUNCT", lemma="."),
                                              dict(text="Manu", tag="NNP", pos="PROPN", lemma="manu"),
                                              dict(text="Nair", tag="NNP", pos="PROPN", lemma="nair"),
                                              dict(text=",", tag=",", pos="PUNCT", lemma=","),
                                              dict(text="Cardiologist", tag="NN", pos="NOUN", lemma="cardiologist"),
                                              dict(text="available", tag="JJ", pos="ADJ", lemma="available"),
                                              dict(text="for", tag="IN", pos="ADP", lemma="for"),
                                              dict(text="a", tag="DT", pos="DET", lemma="a"),
                                              dict(text="consultation", tag="NN", pos="NOUN", lemma="consultation"),
                                              dict(text="on", tag="IN", pos="ADP", lemma="on"),
                                              dict(text="21", tag="CD", pos="NUM", lemma="21"),
                                              dict(text="/", tag="SYM", pos="SYM", lemma="/"),
                                              dict(text="10", tag="CD", pos="NUM", lemma="10"),
                                              dict(text="/", tag="SYM", pos="SYM", lemma="/"),
                                              dict(text="2018", tag="CD", pos="NUM", lemma="2018"),
                                              dict(text="at", tag="IN", pos="ADP", lemma="at"),
                                              dict(text="2", tag="CD", pos="NUM", lemma="2"),
                                              dict(text="PM", tag="NN", pos="NOUN", lemma="pm")])
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch.object(store.return_value, 'get_entities', return_value=(expected_response["entities"], []))
    mocker.patch.object(store.return_value, 'get_pos_tags', return_value=(expected_response["parts_of_speech"]))
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.modify_entities',
                 return_value=expected_response["entities"])
    mocker.patch.object(store.return_value, 'tag_for_intent', return_value=(expected_response["entity_tags"]))
    serviceid = "MedicalAssistant-test"
    model_type = "ner"
    config = dict(custom_entity_model="ice_commons.er.engines.mitie_ner.MitieCustomNER",
                  predefined_entity_model="ice_commons.er.engines.spacy_ner.SpacyDefaultNER")
    datasources_map = dict(
        predefined_entities=["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART",
                             "LANGUAGE", "ORDINAL"], entities=["CATEGORY", "DISEASE", "DOCTOR", "PATIENT"], patterns=[
            dict(entity="custom_date", pattern="\\d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}"),
            dict(entity="custom_email", pattern="[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}")], distinct_token_list=[],
        intents=[], synonymMappings=[])
    default_engine = "ice_commons.er.engines.spacy_ner.SpacyDefaultNER"
    engine = "ice_commons.er.engines.mitie_ner.MitieCustomNER"
    pos = True
    projects_map = dict(custom_entity_model="ice_commons.er.engines.mitie_ner.MitieCustomNER", ner_status="trained",
                        language="EN", predefined_entity_model="ice_commons.er.engines.spacy_ner.SpacyDefaultNER")

    syn_indexes = {}
    text = "Is Dr . Manu Nair , Cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM "
    syn_processed_retokenized_text = syn_processed_truecased_text = retokenized_text = text
    truecased_text = "Is Dr . Manu Nair , cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM"
    entities, entity_tags, parts_of_speech = ner_entities(store.return_value, config, serviceid, model_type, engine,
                                                          truecased_text, retokenized_text,
                                                          syn_processed_truecased_text, syn_processed_retokenized_text,
                                                          syn_indexes, default_engine,
                                                          datasources_map, projects_map, pos)

    assert entities == expected_response["entities"] and entity_tags == expected_response[
        "entity_tags"] and parts_of_speech == expected_response["parts_of_speech"]


def test_ir_entity_tags_with_null(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch.object(store.return_value, 'get_intent', return_value=([], []))
    serviceid = model_type = engine = syn_processed_truecased_text = ""
    datasources_map = {}
    entity_tags = []
    prediction, probabilities = ir_entity_tags(store.return_value, serviceid, model_type, engine,
                                               syn_processed_truecased_text, entity_tags, datasources_map)
    assert prediction == [] and probabilities == []


def test_ir_entity_tags_with_prediction(mocker):
    expected_response = dict(prediction="PRESCRIPTIONS",
                             probabilities=[{"CONSULTATION": "0.0%", "APPOINTMENT": "0.0%", "PRESCRIPTIONS": "100.0%"}])
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch.object(store.return_value, 'get_intent',
                        return_value=(expected_response["prediction"], []))
    serviceid = "MedicalAssistant-test"
    model_type = "ir"
    engine = "ice_commons.er.engines.mitie_ner.MitieCustomNER"
    syn_processed_truecased_text = "Is Dr . Manu Nair , Cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM "
    datasources_map = dict(
        predefined_entities=["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART",
                             "LANGUAGE", "ORDINAL"], entities=["CATEGORY", "DISEASE", "DOCTOR", "PATIENT"], patterns=[
            dict(entity="custom_date", pattern="\\  d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}"),
            dict(entity="custom_email", pattern="[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}")],
        distinct_token_list=["Thank", "Consumption", "swelling", "mild", "cardiologist", "Bye", "Forair", "Today", "20",
                             "21", "Berlin", "nose", "2018", "bye", "Aswathi", "evening", "appointment", "Manu",
                             "Hellons", "get", "GPE", "preferred", "She", "advised", "not", "using", "day", "Asthalin",
                             "shoulder", "like", "Suppliment", "morning", "twice", "Thanks", "tablets", "He", "right",
                             "pediatrician", "habit", "Eliza", "see", "inHAler", "meet", "Good", "07", "DOCTOR", "08",
                             "while", "per", "EMAIL", "pen", "Hi", "Salbutamol", "LOCATION", "Baby", "Cough", "PM",
                             "available", "use", "Neena", "USING", "inhaler", "Hello", "abcdefg@gmail.com", "CATEGORY",
                             "on", "Cetirizine", "Monday", "taking", "days", "Nair", "CARDINAL", "afternoon", "TIME",
                             "Aconsultation", "Nicy", "Zincovit", "suppliment", "CUSTOM_DATE_SLASHED", "There", "Hey",
                             "CUSTOM_EMAIL", "CAUSE_OF_DEATH", "PATIENT", "would", "consultation", "forward",
                             "ORGANIZATION", "syrup", "friend", "QUANTITY", "nutrition", "PERSON", "mL", "taken",
                             "dentist", "baby", "Dolo", "with", "me", "physician", "mg", "15", "last", "ml",
                             "MEDICINE_TAB", "See", "CUSTOM_DATE", "500", "ORG", "headache", "my", "NUMBER", "general",
                             "good", "in", "DATE", "Zeecold", "she", "any", "sinusitis", "book", "take", "you", "Dr",
                             "10", "Intake", "fever", "pain", "felt", "DISEASE", "running", "uses", "knee", "Antony",
                             "MEDICINE", "CITY", "light", "Is", "Remya", "daily", "more", "Merin", "Paracetamol",
                             "left", "Can"],
        intents=[], synonymMappings=[])
    entity_tags = [dict(start=12, tag='custom_date', end=17, entity='21 / 10 / 2018')]
    prediction, probabilities = ir_entity_tags(store.return_value, serviceid, model_type, engine,
                                               syn_processed_truecased_text, entity_tags,
                                               datasources_map)
    assert prediction == expected_response["prediction"]


def test_ir_entity_tags_with_probabilities(mocker):
    expected_response = dict(prediction="PRESCRIPTIONS",
                             probabilities=[{"CONSULTATION": "0.0%", "APPOINTMENT": "0.0%", "PRESCRIPTIONS": "100.0%"}])
    store = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_model_store', return_value=ModelStore())
    mocker.patch.object(store.return_value, 'get_intent',
                        return_value=([], expected_response["probabilities"]))
    serviceid = "MedicalAssistant-test"
    model_type = "ir"
    engine = "ice_commons.er.engines.mitie_ner.MitieCustomNER"
    syn_processed_truecased_text = "Is Dr . Manu Nair , Cardiologist available for a consultation on 21 / 10 / 2018 at 2 PM "
    datasources_map = dict(
        predefined_entities=["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART",
                             "LANGUAGE", "ORDINAL"], entities=["CATEGORY", "DISEASE", "DOCTOR", "PATIENT"],
        patterns=[
            dict(entity="custom_date", pattern="\\  d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}"),
            dict(entity="custom_email", pattern="[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}")],
        distinct_token_list=["Thank", "Consumption", "swelling", "mild", "cardiologist", "Bye", "Forair", "Today", "20",
                             "21", "Berlin", "nose", "2018", "bye", "Aswathi", "evening", "appointment", "Manu",
                             "Hellons", "get", "GPE", "preferred", "She", "advised", "not", "using", "day", "Asthalin",
                             "shoulder", "like", "Suppliment", "morning", "twice", "Thanks", "tablets", "He", "right",
                             "pediatrician", "habit", "Eliza", "see", "inHAler", "meet", "Good", "07", "DOCTOR", "08",
                             "while", "per", "EMAIL", "pen", "Hi", "Salbutamol", "LOCATION", "Baby", "Cough", "PM",
                             "available", "use", "Neena", "USING", "inhaler", "Hello", "abcdefg@gmail.com", "CATEGORY",
                             "on", "Cetirizine", "Monday", "taking", "days", "Nair", "CARDINAL", "afternoon", "TIME",
                             "Aconsultation", "Nicy", "Zincovit", "suppliment", "CUSTOM_DATE_SLASHED", "There", "Hey",
                             "CUSTOM_EMAIL", "CAUSE_OF_DEATH", "PATIENT", "would", "consultation", "forward",
                             "ORGANIZATION", "syrup", "friend", "QUANTITY", "nutrition", "PERSON", "mL", "taken",
                             "dentist", "baby", "Dolo", "with", "me", "physician", "mg", "15", "last", "ml",
                             "MEDICINE_TAB", "See", "CUSTOM_DATE", "500", "ORG", "headache", "my", "NUMBER", "general",
                             "good", "in", "DATE", "Zeecold", "she", "any", "sinusitis", "book", "take", "you", "Dr",
                             "10", "Intake", "fever", "pain", "felt", "DISEASE", "running", "uses", "knee", "Antony",
                             "MEDICINE", "CITY", "light", "Is", "Remya", "daily", "more", "Merin", "Paracetamol",
                             "left", "Can"],
        intents=[], synonymMappings=[])
    entity_tags = [dict(start=12, tag='custom_date', end=17, entity='21 / 10 / 2018')]
    prediction, probabilities = ir_entity_tags(store.return_value, serviceid, model_type, engine,
                                               syn_processed_truecased_text, entity_tags,
                                               datasources_map)
    assert probabilities == expected_response["probabilities"]


def test_updateDatasource(mocker):
    data_manager = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.datasource_manager')
    data_manager.return_value.update_datasource_by_service_id.return_value = "Updated Successfully!!!!!!!"
    serviceid = "MedicalAssistant-test"
    missed_text = "+ksCa5bsiZBbNa2iB366PrqttPrnXwIoHOmeRG78PBElx5zH2x7O / KETlqDufeKX4kbakcvPG"
    assert updateDatasource(serviceid, missed_text) is None


def test_fetch_data_mappings_with_null_serviceid(mocker):
    doc = {'serviceid': '', 'text': ''}
    data_map = dict(intents=[], patterns=[], phrases=[], distinct_token_list=[], entities=[], synonymMappings=[],
                    predefined_entities=[])
    proj_map = dict(ner_status=[], custom_entity_model='ice_commons.er.engines.crf_ner.CRFCustomNER',
                    predefined_entity_model='ice_commons.er.engines.spacy_ner.SpacyDefaultNER', language='EN')
    data_manager = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.datasource_manager')
    data_manager.find_datasource_by_service_id.return_value = {}
    proj_manager = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.project_manager')
    proj_manager.find_model.return_value = {}
    corpus, datasources_map, projects_map = fetch_data_mappings(doc)
    assert corpus == {} and datasources_map == data_map and projects_map == proj_map


def test_fetch_data_mappings_with_serviceid(mocker):
    doc = dict(serviceid='123456', text='')
    data_map = dict(intents=[], patterns=[], phrases=[], distinct_token_list=[], entities=[], synonymMappings=[],
                    predefined_entities=[])
    proj_map = dict(ner_status=[], custom_entity_model='ice_commons.er.engines.crf_ner.CRFCustomNER',
                    predefined_entity_model='ice_commons.er.engines.spacy_ner.SpacyDefaultNER', language='EN')
    data_manager = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.datasource_manager')
    data_manager.find_datasource_by_service_id.return_value = {}
    proj_manager = mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.project_manager')
    proj_manager.find_model.return_value = {}
    corpus, datasources_map, projects_map = fetch_data_mappings(doc)
    assert corpus == {} and datasources_map == data_map and projects_map == proj_map


def test_predict_preprocessing_null(mocker):
    datasources_map = dict(intents=[], patterns=[], phrases=[], distinct_token_list=[], entities=[], synonymMappings=[],
                           predefined_entities=[])
    text = ""
    store = ModelStore()
    truecased_text, retokenized_text, syn_processed_text, syn_processed_truecased_text, syn_processed_retokenized_text, syn_indexes = predict_preprocessing(
        text, store, datasources_map)
    assert (truecased_text, retokenized_text, syn_processed_text, syn_processed_truecased_text,
            syn_processed_retokenized_text, syn_indexes) == ('', '', '', '', '', OrderedDict())


def test_predict_preprocessing_data(mocker):
    datasources_map = dict(intents=[
        dict(_id=ObjectId('5c668ce664d92d382998edd7'), modifiedAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             name=dict(_id=ObjectId('5ba09ed8c7974c459e35288b'),
                       modifiedAt=datetime.datetime(2018, 8, 28, 11, 23, 54, 324000), description='',
                       createdAt=datetime.datetime(2018, 8, 28, 11, 23, 54, 324000), name='junk'),
             createdAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             description=dict(_id=ObjectId('5ba09ed8c7974c459e35288b'),
                              modifiedAt=datetime.datetime(2018, 8, 28, 11, 23, 54, 324000), description='',
                              createdAt=datetime.datetime(2018, 8, 28, 11, 23, 54, 324000), name='junk')),
        dict(_id=ObjectId('5c668ce664d92d382998edd8'), modifiedAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             name=dict(_id=ObjectId('5ba09ed8c7974c459e35288a'),
                       modifiedAt=datetime.datetime(2018, 8, 28, 11, 20, 37, 244000), description='',
                       createdAt=datetime.datetime(2018, 8, 28, 11, 20, 37, 244000), name='prescriptions'),
             createdAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             description=dict(_id=ObjectId('5ba09ed8c7974c459e35288a'),
                              modifiedAt=datetime.datetime(2018, 8, 28, 11, 20, 37, 244000), description='',
                              createdAt=datetime.datetime(2018, 8, 28, 11, 20, 37, 244000), name='prescriptions')),
        dict(_id=ObjectId('5c668ce664d92d382998edd9'), modifiedAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             name=dict(_id=ObjectId('5ba09ed8c7974c459e352889'),
                       modifiedAt=datetime.datetime(2018, 8, 28, 11, 18, 48, 964000), description='',
                       createdAt=datetime.datetime(2018, 8, 28, 11, 18, 48, 964000), name='appointment'),
             createdAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             description=dict(_id=ObjectId('5ba09ed8c7974c459e352889'),
                              modifiedAt=datetime.datetime(2018, 8, 28, 11, 18, 48, 964000), description='',
                              createdAt=datetime.datetime(2018, 8, 28, 11, 18, 48, 964000), name='appointment')),
        dict(_id=ObjectId('5c668ce664d92d382998edda'), modifiedAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             name=dict(_id=ObjectId('5ba09ed8c7974c459e352888'),
                       modifiedAt=datetime.datetime(2018, 8, 28, 11, 18, 7, 172000), description='',
                       createdAt=datetime.datetime(2018, 8, 28, 11, 18, 7, 172000), name='consultation'),
             createdAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             description=dict(_id=ObjectId('5ba09ed8c7974c459e352888'),
                              modifiedAt=datetime.datetime(2018, 8, 28, 11, 18, 7, 172000), description='',
                              createdAt=datetime.datetime(2018, 8, 28, 11, 18, 7, 172000), name='consultation')),
        dict(_id=ObjectId('5c668ce664d92d382998eddb'), modifiedAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             name=dict(_id=ObjectId('5ba09ed8c7974c459e352887'),
                       modifiedAt=datetime.datetime(2018, 8, 28, 11, 17, 6, 212000), description='',
                       createdAt=datetime.datetime(2018, 8, 28, 11, 17, 6, 212000), name='conclusion'),
             createdAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             description=dict(_id=ObjectId('5ba09ed8c7974c459e352887'),
                              modifiedAt=datetime.datetime(2018, 8, 28, 11, 17, 6, 212000), description='',
                              createdAt=datetime.datetime(2018, 8, 28, 11, 17, 6, 212000), name='conclusion')),
        dict(_id=ObjectId('5c668ce664d92d382998eddc'), modifiedAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             name=dict(_id=ObjectId('5ba09ed8c7974c459e352886'),
                       modifiedAt=datetime.datetime(2018, 8, 28, 11, 15, 25, 269000), description='',
                       createdAt=datetime.datetime(2018, 8, 28, 11, 15, 25, 269000), name='greeting'),
             createdAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             description=dict(_id=ObjectId('5ba09ed8c7974c459e352886'),
                              modifiedAt=datetime.datetime(2018, 8, 28, 11, 15, 25, 269000), description='',
                              createdAt=datetime.datetime(2018, 8, 28, 11, 15, 25, 269000), name='greeting')),
        dict(_id=ObjectId('5c668ce664d92d382998eddd'), modifiedAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000),
             description='no intent', createdAt=datetime.datetime(2019, 2, 15, 9, 56, 54, 993000), name='No intent')],
        patterns=[
            dict(pattern='\\d{4}\\s/\\s\\d{2}\\s/\\s\\d{2}|\\d{2}\\s/\\s\\d{2}\\s/\\s\\d{4}',
                 _id=ObjectId('5ba09ed8c7974c459e35288d'), entity='custom_date'),
            dict(pattern='[a-z0-9A-Z_.-]+@[da-zA-Z.-]+.[a-zA-Z.]{2,6}', _id=ObjectId('5ba09ed8c7974c459e35288c'),
                 entity='custom_email')], phrases=[dict(phrase=['Zeecold', 'Salbutamol', 'Asthalin', 'Paracetamol',
                                                                 'Zincovit', 'Cetirizine', 'Forair', 'Dolo'],
                                                         _id=ObjectId('5ba09ed8c7974c459e35288e'),
                                                         entity='medicine_tab')],
        distinct_token_list=['Thank', 'Consumption', 'swelling', 'mild', 'cardiologist', 'Bye',
                             'Forair', 'Today', '20', '21', 'Berlin', 'nose', '2018', 'bye',
                             'Aswathi', 'evening', 'appointment', 'Manu', 'Hellons', 'get', 'GPE',
                             'preferred', 'She', 'advised', 'not', 'using', 'day', 'Asthalin',
                             'shoulder', 'like', 'Suppliment', 'morning', 'twice', 'Thanks',
                             'tablets', 'He', 'right', 'pediatrician', 'habit', 'Eliza', 'see',
                             'inHAler', 'meet', 'Good', '07', 'DOCTOR', '08', 'while', 'per',
                             'EMAIL', 'pen', 'Hi', 'Salbutamol', 'LOCATION', 'Baby', 'Cough', 'PM',
                             'available', 'use', 'Neena', 'USING', 'inhaler', 'Hello',
                             'abcdefg@gmail.com', 'CATEGORY', 'on', 'Cetirizine', 'Monday', 'taking',
                             'days', 'Nair', 'CARDINAL', 'afternoon', 'TIME', 'Aconsultation',
                             'Nicy', 'Zincovit', 'suppliment', 'CUSTOM_DATE_SLASHED', 'There', 'Hey',
                             'CUSTOM_EMAIL', 'CAUSE_OF_DEATH', 'PATIENT', 'would', 'consultation',
                             'forward', 'ORGANIZATION', 'syrup', 'friend', 'QUANTITY', 'nutrition',
                             'PERSON', 'mL', 'taken', 'dentist', 'baby', 'Dolo', 'with', 'me',
                             'physician', 'mg', '15', 'last', 'ml', 'MEDICINE_TAB', 'See',
                             'CUSTOM_DATE', '500', 'ORG', 'headache', 'my', 'NUMBER', 'general',
                             'good', 'in', 'DATE', 'Zeecold', 'she', 'any', 'sinusitis', 'book',
                             'take', 'you', 'Dr', '10', 'Intake', 'fever', 'pain', 'felt',
                             'DISEASE', 'running', 'uses', 'knee', 'Antony', 'MEDICINE', 'CITY',
                             'light', 'Is', 'Remya', 'daily', 'more', 'Merin', 'Paracetamol',
                             'left', 'Can'], entities=['CATEGORY', 'DISEASE', 'DOCTOR', 'PATIENT'],
        synonymMappings=[],
        predefined_entities=['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT',
                             'WORK_OF_ART', 'LANGUAGE', 'ORDINAL'])
    text = "I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza"
    store = ModelStore()
    truecased_text, retokenized_text, syn_processed_text, syn_processed_truecased_text, syn_processed_retokenized_text, syn_indexes = predict_preprocessing(
        text, store, datasources_map)
    assert (truecased_text, retokenized_text, syn_processed_text, syn_processed_truecased_text,
            syn_processed_retokenized_text, syn_indexes) == (
               'i would like to have an appointment of dr merin on 15 / 10 / 2018 for eliza',
               'I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza',
               'I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza',
               'i would like to have an appointment of dr merin on 15 / 10 / 2018 for eliza',
               'I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza', OrderedDict())


def test_replace_synonym_null():
    text = ""
    synonym_dic = []
    resp = (replace_synonym(text, synonym_dic))
    assert resp == ('', OrderedDict())


def test_replace_synonym_data():
    text = "my pcp asked me to meet this sunday"
    synonym_dic = [dict(word="primary care physician", synonym=["pcp"]),
                   dict(word="doctor", synonym=["physician", "vet", "dentist"])]
    resp = (replace_synonym(text, synonym_dic))
    assert resp == ('my primary care physician asked me to meet this sunday',
                    OrderedDict([(1, [2, 1, 4, 'pcp', 'primary care physician'])]))


def test_replace_synonym_data_1():
    text = "my primary care physician asked me to meet this sunday"
    synonym_dic = [dict(word="pcp", synonym=["primary care physician"]),
                   dict(word="doctor", synonym=["physician", "vet", "dentist"])]
    resp = (replace_synonym(text, synonym_dic))
    assert resp == ('my doctor asked me to meet this sunday', OrderedDict(
        [(1, [4, 1, 2, 'primary care physician', 'pcp']), (3, [4, 1, 2, 'physician', 'doctor'])]))


def test_modify_entities_null():
    entities_sorted = []
    syn_indexes = {}
    retokenized_text = " "
    datasources_map = {'synonymMappings': []}
    entities = modify_entities(entities_sorted, syn_indexes, retokenized_text, datasources_map['synonymMappings'])
    assert entities == []


def test_modify_entities_data_flag_true(mocker):
    entities_sorted = [
        dict(start=7, tag='custom_date', end=8, entity='21/10/2018'),
        dict(start=1, tag='category', end=2, entity='physician')]
    syn_indexes = OrderedDict([(1, [2, 1, 2, 'physician', 'doctor'])])
    datasources_map = {'synonymMappings': [dict(word="PCP", synonym=["primary care physician"]),
                                           dict(word="doctor", synonym=["physician", "vet", "dentist"])]}
    retokenized_text = "my physician asked me to meet on 21/10/2018"
    syn_words = dict(pcp=['primary care physician'], doctor=['physician', 'vet', 'dentist'])
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_synonym_words', return_value=syn_words)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.find_indexes', return_value=(True, 1, 2))
    entities = modify_entities(entities_sorted, syn_indexes, retokenized_text, datasources_map['synonymMappings'])
    print(entities)
    assert entities == [{'start': 1, 'resolvedTo': {'baseEntity': '21/10/2018'}, 'tag': 'custom_date', 'end': 2,
                         'entity': '21/10/2018'},
                        {'start': 1, 'resolvedTo': {'baseEntity': 'doctor'}, 'tag': 'category', 'end': 2,
                         'entity': 'physician'}]


def test_modify_entities_data_flag_false(mocker):
    entities_sorted = [
        dict(start=7, tag='custom_date', end=8, entity='sunday'),
        dict(start=1, tag='category', end=2, entity='pcp')]
    syn_indexes = OrderedDict([(1, [2, 1, 2, 'pcp', 'primary care physician'])])
    datasources_map = {'synonymMappings': [dict(word="pcp", synonym=["primary care physician"]),
                                           dict(word="doctor", synonym=["physician", "vet", "dentist"])]}
    retokenized_text = "my pcp asked me to meet this sunday"
    syn_words = {'primary care physician': ['pcp'], 'doctor': ['general physician', 'vet', 'dentist'],
                 'sunday': ['holiday']}
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.get_synonym_words', return_value=syn_words)
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.find_indexes', return_value=(False, None, None))
    entities = modify_entities(entities_sorted, syn_indexes, retokenized_text, datasources_map['synonymMappings'])
    assert entities == [
        {'start': 7, 'resolvedTo': {'baseEntity': 'sunday'}, 'tag': 'custom_date', 'end': 8, 'entity': 'sunday'},
        {'start': 1, 'resolvedTo': {'baseEntity': 'primary care physician'}, 'tag': 'category', 'end': 2,
         'entity': 'pcp'}]


def test_get_synonym_words_null():
    synonym_dic = []
    assert get_synonym_words(synonym_dic) == {}


def test_get_synonym_words_data():
    synonym_dic = [dict(word="PCP", synonym=["primary care physician"]),
                   dict(word="doctor", synonym=["physician", "vet", "dentist"])]
    syn_words = dict(pcp=['primary care physician'], doctor=['physician', 'vet', 'dentist'])
    assert get_synonym_words(synonym_dic) == syn_words


def test_find_indexes_null():
    text = word = ""
    assert find_indexes(text, word, start=0) == (True, 0, 1)


def test_find_indexes_data1():
    text = "my physician asked me to meet on 21 / 10 / 2018"
    word = "physician"
    start = 1
    assert find_indexes(text, word, start=0) == (True, 1, 2)


def test_find_indexes_data2():
    text = "my primary care physician asked me to meet on 21 / 10 / 2018"
    word = "pcp"
    start = 1
    assert find_indexes(text, word, start=0) == (False, None, None)


def test_modify_response_v1(mocker):
    results = {"text": "my physician asked me to meet on 21 / 10 / 2018", "entities": [
        {'entity': '21 / 10 / 2018', 'resolvedTo': {'baseEntity': '21 / 10 / 2018'}, 'tag': 'custom_date', 'end': 8,
         'start': 7}], 'intent': dict(top_intent="CONSULTATION", confidence_level=[
        {"CONSULTATION": "100.0%", "APPOINTMENT": "0.0%", "PRESCRIPTIONS": "0.0%"}])}
    mocker.patch('ice_rest.rest.services.parse.impl.predict_impl.start_end_checker', return_value=1)
    resp = {'text': 'my physician asked me to meet on 21 / 10 / 2018',
            'intent': {'category': 'CONSULTATION', 'probabilities': []}, 'entities': [
            {'resolvedTo': {'baseEntity': '21 / 10 / 2018'}, 'tag': 'custom_date', 'entity': '21 / 10 / 2018'}]}
    assert modify_response_v1(results) == resp


def test_get_proba_null():
    intent_list = []
    assert get_proba(intent_list) == {'No intent': '100.0%'}


def test_get_proba_null_data():
    intent_list = [
        dict(name="prescribtions", description="prescribtions given by doctor"),
        dict(name="consultation", description="consultation messages"),
        dict(name="appointment", description="appointment requested"),
        dict(name="greetings", description="greetings"),
        dict(name="junk", description="non relevant data")
    ]
    assert get_proba(intent_list) == {'junk': '0.0%', 'appointment': '0.0%', 'consultation': '0.0%',
                                      'greetings': '0.0%', 'No intent': '100.0%', 'prescribtions': '0.0%'}
