from falcon import Request,testing

from ice_commons.celery_jobs.validate.validate_impl import get_predict_api_url, validate


class MockPostRequest():
    def __init__(self, code):
        self.status_code = code
        self.content = '{"text": "Is a table available for 6 persons at 5 PM monday ?", "parts_of_speech": [{"text": "Is", "tag": "VBZ", "pos": "VERB", "lemma": "be"}, {"text": "a", "tag": "DT", "pos": "DET", "lemma": "a"}, {"text": "table", "tag": "NN", "pos": "NOUN", "lemma": "table"}, {"text": "available", "tag": "JJ", "pos": "ADJ", "lemma": "available"}, {"text": "for", "tag": "IN", "pos": "ADP", "lemma": "for"}, {"text": "6", "tag": "CD", "pos": "NUM", "lemma": "6"}, {"text": "persons", "tag": "NNS", "pos": "NOUN", "lemma": "person"}, {"text": "at", "tag": "IN", "pos": "ADP", "lemma": "at"}, {"text": "5", "tag": "CD", "pos": "NUM", "lemma": "5"}, {"text": "PM", "tag": "NN", "pos": "NOUN", "lemma": "pm"}, {"text": "monday", "tag": "NNP", "pos": "PROPN", "lemma": "monday"}, {"text": "?", "tag": ".", "pos": "PUNCT", "lemma": "?"}], "intent": {"top_intent": "TableBooking", "confidence_level": [{"ShowMenu": "0.0%", "Positive Feedback": "0.0%", "Greeting": "0.0%", "Conclusion": "0.0%", "TableBooking": "100.0%", "Switch to Agent": "0.0%", "Negative Feedback": "0.0%"}]}, "entities": [{"resolvedTo": {"baseEntity": "6"}, "end": 6, "score": 0.7725474473812105, "entity": "6", "start": 5, "tag": "COUNT"}, {"resolvedTo": {"baseEntity": "5"}, "end": 9, "score": 0.9687916092166523, "entity": "5", "start": 8, "tag": "COUNT"}]}'

def test_get_predict_api_url():
    env = testing.create_environ(
        path='/api/parse/validate',)
    req = Request(env)
    resp = get_predict_api_url(req)
    assert resp == 'http://falconframework.org/api/parse/predict'


def test_validate(mocker):
    project_manager = mocker.patch('ice_commons.celery_jobs.validate.validate_impl.project_manager')
    test_data_manager = mocker.patch('ice_commons.celery_jobs.validate.validate_impl.test_data_manager')
    test_run_manager = mocker.patch('ice_commons.celery_jobs.validate.validate_impl.test_run_manager')
    test_data_manager.fetch_by_serviceid.return_value = {"serviceid":"0Aht4vuyU46Av4ZgQTHOmsTeCKpGOIFAka5UZxzkDTnip8q3ZsL6wHyeq6PMStIj","utterances":[{"tags":[{"end":6,"start":5,"tag":"COUNT","entity":"6"},{"end":10,"start":8,"tag":"SCHEDULE","entity":"5 PM"},{"end":11,"start":10,"tag":"CUSTOMDATE","entity":"monday"}],"intent":"TableBooking","utterance":"Is a table available for 6 persons at 5 PM monday ?"}]}
    mocker.patch('ice_commons.celery_jobs.validate.validate_impl.requests.post', return_value= MockPostRequest(200))
    test_run_manager.update_config_by_service_id.return_value = None
    project_manager.find_model.return_value = {"name":"autovalidation-test717","predefined_entity_model":"ice_commons.er.engines.spacy_ner.SpacyDefaultNER","custom_entity_model":"ice_commons.er.engines.crf_ner.CRFCustomNER","language":"EN","ir":{"status_message":"Validation completed successfully.","status":"validated"},"ner":{"status_message":"Validation completed successfully.","status":"validated"},"serviceid":"0Aht4vuyU46Av4ZgQTHOmsTeCKpGOIFAka5UZxzkDTnip8q3ZsL6wHyeq6PMStIj"}
    project_manager.update_config.return_value = None
    assert validate("service_id", 'http://falconframework.org/api/parse/predict') == None

