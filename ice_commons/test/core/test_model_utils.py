import pytest
from ice_commons.core.model_utils import DEFAULT_MODELS, get_entities_for_default_model


def test_get_entities_for_default_model1():
    models = get_entities_for_default_model(None)
    assert []== models


def test_get_entities_for_default_model2():
    models = get_entities_for_default_model('abcd')
    assert []== models


def test_get_entities_for_default_model3():
    models = get_entities_for_default_model('ice_commons.er.engines.spacy_ner.SpacyDefaultNER')
    assert ["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT",
            "EVENT", "WORK_OF_ART", "LANGUAGE","ORDINAL"]== models

