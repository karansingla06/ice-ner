import pytest
from ice_commons.er.engines.spanish.crf_ner import CRFSpanishCustomNER



def test_predict_with_null(mocker):
    obj = mocker.patch('ice_commons.er.engines.spanish.crf_ner.CRFSpanishCustomNER', CRFSpanishCustomNER())
    obj.model = mocker.patch('ice_commons.er.engines.spanish.crf_ner.CRF')
    mocker.patch('ice_commons.er.engines.spanish.crf_ner.pos_tags_predict', return_value= [])
    mocker.patch('ice_commons.er.engines.spanish.crf_ner.sent2features', return_value=[])
    mocker.patch.object(obj.model,'predict_marginals_single', return_value = [])
    entities, pos_mapping = obj.predict('','', None)
    assert entities == []
    assert pos_mapping == None

