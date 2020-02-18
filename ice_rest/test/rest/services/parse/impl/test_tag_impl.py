import pytest
from ice_rest.rest.services.parse.impl.tag_impl import tag, remove_resolved_to
from ice_commons.store.models import ModelStore
from ice_commons.data.dl.manager import ProjectManager, DatasourceManager
from pydash import get



def test_tag_with_null(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_model_store', return_value=ModelStore())
    mocker.patch.object(store.return_value , 'change_case', return_value= (None, None))
    mocker.patch.object(ProjectManager, 'find_model', return_value= None)
    mocker.patch.object(DatasourceManager, 'find_datasource_by_service_id', return_value= None)
    mocker.patch.object(store.return_value,'tag', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_engine', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_model_name', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_all_corenlp_engines', return_value=[])
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.remove_resolved_to', return_value=[])
    doc = {'serviceid':'abc', 'text': ''}
    resp = tag(doc)
    assert resp == []


def test_tag_with_data1(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_model_store', return_value=ModelStore())
    mocker.patch.object(store.return_value , 'change_case', return_value= (None, None))
    mocker.patch.object(ProjectManager, 'find_model', return_value= None)
    mocker.patch.object(DatasourceManager, 'find_datasource_by_service_id', return_value= None)
    mocker.patch.object(store.return_value,'tag', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_engine', return_value='ICE')
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_model_name', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_all_corenlp_engines', return_value=['CoreNLP','CoreNLP-es'])
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.remove_resolved_to', return_value=[])
    doc = {'serviceid':None, 'text': ''}
    resp = tag(doc)
    assert resp == []


def test_tag_with_data2(mocker):
    store = mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_model_store', return_value=ModelStore())
    mocker.patch.object(store.return_value , 'change_case', return_value= ('Hello How are you ?', 'hello how are you?'))
    mocker.patch.object(ProjectManager, 'find_model', return_value= None)
    mocker.patch.object(DatasourceManager, 'find_datasource_by_service_id', return_value= None)
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_engine', return_value='CoreNLP')
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_model_name', return_value=None)
    mocker.patch('ice_rest.rest.services.parse.impl.tag_impl.get_all_corenlp_engines', return_value=['CoreNLP','CoreNLP-es'])
    expected = mocker.patch.object(store.return_value, 'tag', return_value= None)
    expected.return_value = {
        "utterance": 'hello how are you?',
        "case_converted_utterance": 'Hello How are you ?',
        "tokens": ['hello', 'how', 'are', 'you', '?'],
        "custom_tags": [],
        "default_tags": []
    }
    doc = {'serviceid': 'abc', 'text': 'hello how are you?'}
    resp = tag(doc)
    assert resp == expected.return_value


def test_remove_resolve_to1():
    resp = remove_resolved_to({})
    assert resp == {
                "custom_tags": [],
                "default_tags": []
            }


def test_remove_resolve_to2():
    resp = remove_resolved_to({
        "utterance": 'hello how are you?',
        "case_converted_utterance": 'Hello How are you ?',
        "tokens": ['hello', 'how', 'are', 'you', '?'],
        "custom_tags": [{'entity':'hello','resolvedTo': 'abcd'}, {'abcd':'abcd'}],
        "default_tags": [{'entity':'how are you'}, {'abcd':'abcd'}]
    })
    assert resp == {
        "utterance": 'hello how are you?',
        "case_converted_utterance": 'Hello How are you ?',
        "tokens": ['hello', 'how', 'are', 'you', '?'],
        "custom_tags": [{'entity':'hello'},{'abcd':'abcd'}],
        "default_tags": [{'entity':'how are you'},{'abcd':'abcd'}]
    }
