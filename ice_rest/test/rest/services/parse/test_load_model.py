import pytest
from ice_rest.rest.services.parse.load_model import cache_model



def test_cache_model1(mocker):
    mocker.patch('ice_rest.rest.services.parse.load_model.get_engine', return_value= '')
    mocker.patch('ice_rest.rest.services.parse.load_model.get_model_store')
    config = {'ner':{'status' : 'trained', 'last_trained':''}, 'ir':{'status' : 'trained','last_trained':''}, 'custom_entity_model': '', }
    req_ser= ('a','ner','c'),('x','ir','z')
    resp = cache_model(config,req_ser)
    assert resp==None
