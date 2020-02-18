import pytest
from ice_commons.er.engines.crf_ner import CRFCustomNER
from sklearn_crfsuite import CRF



def test_predict_with_null(mocker):
    obj = mocker.patch('ice_commons.er.engines.crf_ner.CRFCustomNER', CRFCustomNER())
    obj.model = mocker.patch('ice_commons.er.engines.crf_ner.CRF')
    mocker.patch('ice_commons.er.engines.crf_ner.pos_tags_predict', return_value= [])
    mocker.patch('ice_commons.er.engines.crf_ner.sent2features', return_value=[])
    mocker.patch.object(obj.model,'predict_marginals_single', return_value = [])
    mocker.patch('ice_commons.er.engines.crf_ner.format_response', return_value=[])
    entities, pos_mapping = obj.predict('','', None)
    assert entities == []
    assert pos_mapping == None


def test_predict_with_data(mocker):
    obj = mocker.patch('ice_commons.er.engines.crf_ner.CRFCustomNER', CRFCustomNER())
    obj.model = mocker.patch('ice_commons.er.engines.crf_ner.CRF')
    mocker.patch('ice_commons.er.engines.crf_ner.pos_tags_predict', return_value= [])
    mocker.patch('ice_commons.er.engines.crf_ner.sent2features', return_value=[('I', 'PRON', '-PRON-'), ('have', 'VERB', 'have'), ('a', 'DET', 'a'), ('meeting', 'NOUN', 'meeting'), ('in', 'ADP', 'in'), ('Delhi', 'PROPN', 'delhi'), ('?', 'PUNCT', '?')])
    mocker.patch.object(obj.model,'predict_marginals_single', return_value = [])
    mocker.patch('ice_commons.er.engines.crf_ner.format_response',return_value= [{'start': 5, 'tag': 'LOCATION', 'end': 6, 'entity': 'Delhi'}])

    entities, pos_mapping = obj.predict('I have a meeting in Delhi ?', 'I have a meeting in Delhi ?', None)
    assert entities == [{'start': 5, 'tag': 'LOCATION', 'end': 6, 'entity': 'Delhi'}]
    assert pos_mapping == None
