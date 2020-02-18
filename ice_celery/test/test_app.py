import pytest

def test_app(mocker):
    m = mocker.patch('ice_celery.app.model_store')
    m.return_value.load_default_models_celery.return_value = 'a'
    m2 = mocker.patch('ice_celery.app.get_app')
    m2.return_value.start.return_value= None

