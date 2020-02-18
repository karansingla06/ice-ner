import pytest
from ice_commons.er.engines.mitie_ner import MitieDefaultNER, MitieCustomNER


def test_default_predict_with_null(mocker):
    mocker.patch('ice_commons.er.engines.mitie_ner.MitieDefaultNER.load')
    default_entities, pos_mapping = MitieDefaultNER().predict('', '' ,None)
    assert default_entities== []
    assert pos_mapping== None


def test_default_predict(mocker):
    mocker.patch('ice_commons.er.engines.mitie_ner.MitieDefaultNER.load')
    default_entities, pos_mapping = MitieDefaultNER().predict('Karan has a meeting in Delhi ?','karan has a meeting in delhi', None)
    assert default_entities== []
    assert pos_mapping== None



def test_custom_predict_with_model(mocker):
    obj=mocker.patch('ice_commons.er.engines.mitie_ner.MitieCustomNER', MitieCustomNER())
    obj.model= mocker.patch('ice_commons.er.engines.mitie_ner.named_entity_extractor')
    mocker.patch.object(obj.model, 'extract_entities', return_value=[])
    entities, pos_mapping = obj.predict('Remya has taken 3 Paracetamol tablets while she felt fever', 'Remya has taken 3 Paracetamol tablets while she felt fever', None)
    assert entities == []
    assert pos_mapping == None
