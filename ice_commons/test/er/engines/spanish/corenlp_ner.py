from ice_commons.er.engines.spanish.corenlp_ner import CorenlpSpanishCustomNER, CorenlpSpanishDefaultNER


def test_predict_null_custom_spanish_null(mocker):
    text = original_text = pos = ""
    obj = CorenlpSpanishCustomNER()
    mocker.patch('ice_commons.er.engines.spanish.corenlp_ner.stanfordcorenlp_customner', return_value=[])
    assert obj.predict(text, original_text, pos) == []


def test_predict_null_custom_spanish_data(mocker):
    text = original_text = "I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza"
    pos = True
    obj = CorenlpSpanishCustomNER()
    resp = [
        dict(resolvedTo=dict(baseEntity="Dr Merin"), end=10, score=0.8371767453680246, entity="Dr Merin", start=8,
             tag="DOCTOR_NAME"),
        dict(resolvedTo=dict(baseEntity="Eliza"), end=18, score=0.8337980627932957, entity="Eliza", start=17,
             tag="PATIENT_NAME")
    ]
    mocker.patch('ice_commons.er.engines.spanish.corenlp_ner.stanfordcorenlp_customner', return_value=resp)
    assert obj.predict(text, original_text, pos) == resp


def test_predict_null_default_spanish_null(mocker):
    text = original_text = pos = ""
    obj = CorenlpSpanishDefaultNER()
    mocker.patch('ice_commons.er.engines.spanish.corenlp_ner.stanfordcorenlp_defaultner', return_value=[])
    assert obj.predict(text, original_text, pos) == []


def test_predict_null_default_spanish_data(mocker):
    text = original_text = "I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza"
    pos = True
    obj = CorenlpSpanishDefaultNER()
    resp = [
        dict(resolvedTo=dict(baseEntity="Dr Merin"), end=10, score=0.8371767453680246, entity="Dr Merin", start=8,
             tag="DOCTOR_NAME"),
        dict(resolvedTo=dict(baseEntity="Eliza"), end=18, score=0.8337980627932957, entity="Eliza", start=17,
             tag="PATIENT_NAME")
    ]
    mocker.patch('ice_commons.er.engines.spanish.corenlp_ner.stanfordcorenlp_defaultner', return_value=resp)
    assert obj.predict(text, original_text, pos) == resp
