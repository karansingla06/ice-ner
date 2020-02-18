from ice_rest.rest.services.parse.impl.common.missed_utterances_impl import missedUtterences


def test_missedUtterancs_null(mocker):
    mocker.patch('ice_rest.rest.services.parse.impl.common.missed_utterances_impl.encrypt', return_value="")
    text = "I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza"
    resp = missedUtterences({"text": "", "entities": [], "intent": {"top_intent": "", "confidence_level": []}}, "", "",
                            missed_text=text)
    assert resp == text


def test_missedUtterences_data(mocker):
    response = dict(text="I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza",
                    parts_of_speech=[
                        dict(text="I", tag="PRP", pos="PRON", lemma="-PRON-"),
                        dict(text="would", tag="MD", pos="VERB", lemma="would"),
                        dict(text="like", tag="VB", pos="VERB", lemma="like"),
                        dict(text="to", tag="TO", pos="PART", lemma="to"),
                        dict(text="have", tag="VB", pos="VERB", lemma="have"),
                        dict(text="an", tag="DT", pos="DET", lemma="an"),
                        dict(text="appointment", tag="NN", pos="NOUN", lemma="appointment"),
                        dict(text="of", tag="IN", pos="ADP", lemma="of"),
                        dict(text="Dr", tag="NNP", pos="PROPN", lemma="dr"),
                        dict(text="Merin", tag="NNP", pos="PROPN", lemma="merin"),
                        dict(text="on", tag="IN", pos="ADP", lemma="on"),
                        dict(text="15", tag="CD", pos="NUM", lemma="15"),
                        dict(text="/", tag="SYM", pos="SYM", lemma="/"),
                        dict(text="10", tag="CD", pos="NUM", lemma="10"),
                        dict(text="/", tag="SYM", pos="SYM", lemma="/"),
                        dict(text="2018", tag="CD", pos="NUM", lemma="2018"),
                        dict(text="for", tag="IN", pos="ADP", lemma="for"),
                        dict(text="Eliza", tag="NNP", pos="PROPN", lemma="eliza")
                    ], intent=dict(top_intent="appointment", confidence_level=[
            {
                "No intent": "0.0%",
                "prescribtions": "5.0%",
                "consultation": "45.0%",
                "appointment": "45.0%",
                "greetings": "5.0%"
            }
        ]), entities=[])
    serviceid = "MedicalAssistant-test"
    req_id = "1234556789"
    missed_text_resp = mocker.patch('ice_rest.rest.services.parse.impl.common.missed_utterances_impl.encrypt',
                                    return_value="PW5VOlkuyrRekAkHvukHs15SNxIZOMZZSgK4UAsPCQ2Oa+WxD2HdthH"
                                                 "+ksCa5bsiZBbNa2iB366PrqttPrnXwIoHOmeRG78PBElx5zH2x7O/KETlqDufeKX4kbakcvPG")
    resp = missedUtterences(response, serviceid, req_id,
                            missed_text="I would like to have an appointment of Dr Merin on 15 / 10 / 2018 for Eliza")
    assert resp == missed_text_resp.return_value
