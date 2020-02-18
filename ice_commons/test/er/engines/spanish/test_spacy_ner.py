import pytest
from ice_commons.er.engines.spanish.spacy_ner import SpacySpanishDefaultNER


def test_predict_with_null(mocker):
    mocker.patch('ice_commons.er.engines.spanish.spacy_ner.SpacySpanishDefaultNER.load')
    default_entities, pos_mapping = SpacySpanishDefaultNER().predict('', '' ,None)
    assert default_entities== []
    assert pos_mapping== []




def test_predict_with_pos(mocker):
    mocker.patch('ice_commons.er.engines.spanish.spacy_ner.SpacySpanishDefaultNER.load')
    default_entities, pos_mapping = SpacySpanishDefaultNER().predict('I have a meeting in Delhi ?','i have a meeting in delhi', True)
    assert default_entities== []
    assert pos_mapping== []