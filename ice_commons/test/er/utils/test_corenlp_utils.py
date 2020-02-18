from ice_commons.er.utils.corenlp_utils import stanfordcorenlp_defaultner, stanfordcorenlp_customner


def test_stanfordcorenlp_customner_null(mocker):
    snlp = mocker.patch('ice_commons.er.utils.corenlp_utils.StanfordNLP')
    mocker.patch('ice_commons.er.utils.corenlp_utils.get_corenlp_modelname')
    snlp.return_value.annotate.return_value = '{}'
    entities, pos = stanfordcorenlp_customner('', '', '', '')
    mocker.patch('ice_commons.er.utils.corenlp_utils.get_all_custom_entities')
    assert entities == [] and pos == []


def test_stanfordcorenlp_customner_data_english(mocker):
    snlp = mocker.patch('ice_commons.er.utils.corenlp_utils.StanfordNLP')
    mocker.patch('ice_commons.er.utils.corenlp_utils.get_corenlp_modelname')
    snlp.return_value.annotate.return_value = '{"sentences":[{"index":0,"entitymentions":[],"tokens":[{"index":1,' \
                                              '"word":"Can","originalText":"Can","lemma":"can",' \
                                              '"characterOffsetBegin":0,"characterOffsetEnd":3,"pos":"MD",' \
                                              '"ner":"O"},{"index":2,"word":"I","originalText":"I","lemma":"I",' \
                                              '"characterOffsetBegin":4,"characterOffsetEnd":5,"pos":"PRP",' \
                                              '"ner":"O"},{"index":3,"word":"have","originalText":"have",' \
                                              '"lemma":"have","characterOffsetBegin":6,"characterOffsetEnd":10,' \
                                              '"pos":"VB","ner":"O"},{"index":4,"word":"an","originalText":"an",' \
                                              '"lemma":"a","characterOffsetBegin":11,"characterOffsetEnd":13,' \
                                              '"pos":"DT","ner":"O"},{"index":5,"word":"appointment",' \
                                              '"originalText":"appointment","lemma":"appointment",' \
                                              '"characterOffsetBegin":14,"characterOffsetEnd":25,"pos":"NN",' \
                                              '"ner":"O"},{"index":6,"word":"with","originalText":"with",' \
                                              '"lemma":"with","characterOffsetBegin":26,"characterOffsetEnd":30,' \
                                              '"pos":"IN","ner":"O"},{"index":7,"word":"dr","originalText":"dr",' \
                                              '"lemma":"dr","characterOffsetBegin":31,"characterOffsetEnd":33,' \
                                              '"pos":"NN","ner":"O"},{"index":8,"word":"Remya?",' \
                                              '"originalText":"Remya?","lemma":"remya?","characterOffsetBegin":34,' \
                                              '"characterOffsetEnd":40,"pos":"NN","ner":"O"}]}]} '
    mocker.patch('ice_commons.er.utils.corenlp_utils.get_all_custom_entities')
    entities, pos = stanfordcorenlp_customner('MedicalAssistant-test', 'Can I have an appointment with dr Remya?',
                                              'Can I have an appointment with dr Remya?', 'EN')
    assert entities == [] and pos == []


def test_stanfordcorenlp_customner_data_spanish(mocker):
    snlp = mocker.patch('ice_commons.er.utils.corenlp_utils.StanfordNLP')
    mocker.patch('ice_commons.er.utils.corenlp_utils.get_corenlp_modelname')
    snlp.return_value.annotate.return_value = '{"sentences":[{"index":0,"entitymentions":[{"docTokenBegin":5,' \
                                              '"docTokenEnd":6,"tokenBegin":5,"tokenEnd":6,"text":"dentista",' \
                                              '"characterOffsetBegin":24,"characterOffsetEnd":32,"ner":"TITLE"}],' \
                                              '"tokens":[{"index":1,"word":"quiero","originalText":"quiero",' \
                                              '"lemma":"quiero","characterOffsetBegin":0,"characterOffsetEnd":6,' \
                                              '"pos":"VERB","ner":"O"},{"index":2,"word":"una","originalText":"una",' \
                                              '"lemma":"una","characterOffsetBegin":7,"characterOffsetEnd":10,' \
                                              '"pos":"DET","ner":"O"},{"index":3,"word":"cita",' \
                                              '"originalText":"cita","lemma":"cita","characterOffsetBegin":11,' \
                                              '"characterOffsetEnd":15,"pos":"NOUN","ner":"O"},{"index":4,' \
                                              '"word":"para","originalText":"para","lemma":"para",' \
                                              '"characterOffsetBegin":16,"characterOffsetEnd":20,"pos":"ADP",' \
                                              '"ner":"O"},{"index":5,"word":"un","originalText":"un","lemma":"un",' \
                                              '"characterOffsetBegin":21,"characterOffsetEnd":23,"pos":"DET",' \
                                              '"ner":"O"},{"index":6,"word":"dentista","originalText":"dentista",' \
                                              '"lemma":"dentista","characterOffsetBegin":24,"characterOffsetEnd":32,' \
                                              '"pos":"NOUN","ner":"TITLE"}]}]} '
    mocker.patch('ice_commons.er.utils.corenlp_utils.get_all_custom_entities')
    entities, pos = stanfordcorenlp_customner('MedicalAssistant-test', 'quiero una cita para un dentista',
                                              'quiero una cita para un dentista', 'ES')
    assert entities == [] and pos == []


def test_stanfordcorenlp_defaultner_null(mocker):
    snlp = mocker.patch('ice_commons.er.utils.corenlp_utils.StanfordNLP')
    snlp.return_value.annotate.return_value = '{}'
    entities, pos = stanfordcorenlp_defaultner('', '', '')
    assert entities == [] and pos == []


def test_stanfordcorenlp_defaultner_english(mocker):
    snlp = mocker.patch('ice_commons.er.utils.corenlp_utils.StanfordNLP')
    mocker.patch('ice_commons.er.utils.corenlp_utils.get_corenlp_modelname')
    snlp.return_value.annotate.return_value = '{"sentences":[{"index":0,"entitymentions":[],"tokens":[{"index":1,' \
                                              '"word":"Can","originalText":"Can","lemma":"can",' \
                                              '"characterOffsetBegin":0,"characterOffsetEnd":3,"pos":"MD",' \
                                              '"ner":"O"},{"index":2,"word":"I","originalText":"I","lemma":"I",' \
                                              '"characterOffsetBegin":4,"characterOffsetEnd":5,"pos":"PRP",' \
                                              '"ner":"O"},{"index":3,"word":"have","originalText":"have",' \
                                              '"lemma":"have","characterOffsetBegin":6,"characterOffsetEnd":10,' \
                                              '"pos":"VB","ner":"O"},{"index":4,"word":"an","originalText":"an",' \
                                              '"lemma":"a","characterOffsetBegin":11,"characterOffsetEnd":13,' \
                                              '"pos":"DT","ner":"O"},{"index":5,"word":"appointment",' \
                                              '"originalText":"appointment","lemma":"appointment",' \
                                              '"characterOffsetBegin":14,"characterOffsetEnd":25,"pos":"NN",' \
                                              '"ner":"O"},{"index":6,"word":"with","originalText":"with",' \
                                              '"lemma":"with","characterOffsetBegin":26,"characterOffsetEnd":30,' \
                                              '"pos":"IN","ner":"O"},{"index":7,"word":"dr","originalText":"dr",' \
                                              '"lemma":"dr","characterOffsetBegin":31,"characterOffsetEnd":33,' \
                                              '"pos":"NN","ner":"O"},{"index":8,"word":"Remya?",' \
                                              '"originalText":"Remya?","lemma":"remya?","characterOffsetBegin":34,' \
                                              '"characterOffsetEnd":40,"pos":"NN","ner":"O"}]}]} '
    entities, pos = stanfordcorenlp_defaultner('Can I have an appointment with dr Remya?', 'Can I have an appointment '
                                                                                           'with dr Remya?', 'EN')
    assert entities == [] and pos == [{'text': 'Can', 'tag': 'MD', 'pos': 'MD', 'lemma': 'can'},
                                      {'text': 'I', 'tag': 'PRP', 'pos': 'PRP', 'lemma': 'I'},
                                      {'text': 'have', 'tag': 'VB', 'pos': 'VB', 'lemma': 'have'},
                                      {'text': 'an', 'tag': 'DT', 'pos': 'DT', 'lemma': 'a'},
                                      {'text': 'appointment', 'tag': 'NN', 'pos': 'NN', 'lemma': 'appointment'},
                                      {'text': 'with', 'tag': 'IN', 'pos': 'IN', 'lemma': 'with'},
                                      {'text': 'dr', 'tag': 'NN', 'pos': 'NN', 'lemma': 'dr'},
                                      {'text': 'Remya?', 'tag': 'NN', 'pos': 'NN', 'lemma': 'remya?'}]


def test_stanfordcorenlp_defaultner_spanish(mocker):
    snlp = mocker.patch('ice_commons.er.utils.corenlp_utils.StanfordNLP')
    mocker.patch('ice_commons.er.utils.corenlp_utils.get_corenlp_modelname')
    snlp.return_value.annotate.return_value = '{"sentences":[{"index":0,"entitymentions":[{"docTokenBegin":5,' \
                                              '"docTokenEnd":6,"tokenBegin":5,"tokenEnd":6,"text":"dentista",' \
                                              '"characterOffsetBegin":24,"characterOffsetEnd":32,"ner":"TITLE"}],' \
                                              '"tokens":[{"index":1,"word":"quiero","originalText":"quiero",' \
                                              '"lemma":"quiero","characterOffsetBegin":0,"characterOffsetEnd":6,' \
                                              '"pos":"VERB","ner":"O"},{"index":2,"word":"una","originalText":"una",' \
                                              '"lemma":"una","characterOffsetBegin":7,"characterOffsetEnd":10,' \
                                              '"pos":"DET","ner":"O"},{"index":3,"word":"cita",' \
                                              '"originalText":"cita","lemma":"cita","characterOffsetBegin":11,' \
                                              '"characterOffsetEnd":15,"pos":"NOUN","ner":"O"},{"index":4,' \
                                              '"word":"para","originalText":"para","lemma":"para",' \
                                              '"characterOffsetBegin":16,"characterOffsetEnd":20,"pos":"ADP",' \
                                              '"ner":"O"},{"index":5,"word":"un","originalText":"un","lemma":"un",' \
                                              '"characterOffsetBegin":21,"characterOffsetEnd":23,"pos":"DET",' \
                                              '"ner":"O"},{"index":6,"word":"dentista","originalText":"dentista",' \
                                              '"lemma":"dentista","characterOffsetBegin":24,"characterOffsetEnd":32,' \
                                              '"pos":"NOUN","ner":"TITLE"}]}]} '
    entities, pos = stanfordcorenlp_defaultner('quiero una cita para un dentista', 'quiero una cita para un dentista',
                                               'ES')
    assert entities == [
        dict(entity='dentista', resolvedTo={'baseEntity': 'dentista'}, tag='TITLE', end=6, start=5)] and pos == [
               dict(text='quiero', tag='VERB', pos='VERB', lemma='quiero'),
               dict(text='una', tag='DET', pos='DET', lemma='una'),
               dict(text='cita', tag='NOUN', pos='NOUN', lemma='cita'),
               dict(text='para', tag='ADP', pos='ADP', lemma='para'),
               dict(text='un', tag='DET', pos='DET', lemma='un'),
               dict(text='dentista', tag='NOUN', pos='NOUN', lemma='dentista')]
