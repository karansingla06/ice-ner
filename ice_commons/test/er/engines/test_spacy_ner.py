import pytest
from ice_commons.er.engines.spacy_ner import SpacyDefaultNER


def test_predict_with_null(mocker):
    # obj = mocker.patch('ice_commons.er.engines.spanish.spacy_ner.SpacyDefaultNER', SpacyDefaultNER())
    mocker.patch('ice_commons.er.engines.spacy_ner.SpacyDefaultNER.load')
    default_entities, pos_mapping = SpacyDefaultNER().predict('', '' ,None)
    assert default_entities== []
    assert pos_mapping== []



def test_predict_with_pos(mocker):
    # obj = mocker.patch('ice_commons.er.engines.spanish.spacy_ner.SpacyDefaultNER', SpacyDefaultNER())
    mocker.patch('ice_commons.er.engines.spacy_ner.SpacyDefaultNER.load')
    default_entities, pos_mapping = SpacyDefaultNER().predict('I have a meeting in Delhi ?','i have a meeting in delhi', True)
    assert default_entities== []
    assert pos_mapping== []