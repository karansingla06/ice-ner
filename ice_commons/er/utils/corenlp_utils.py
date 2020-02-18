import configparser as CP
import json
import os
import logging
from stanfordcorenlp import StanfordCoreNLP
from pydash import get
from ice_commons.core.class_utils import create_instance
from ice_commons.core.model_utils import get_corenlp_default_model, get_corenlp_custom_model
from ice_commons.core.project_utils import get_corenlp_modelname, put_corenlp_modelname, get_custom_entities, \
    get_pattern_entities, get_phrase_entities
import datetime
from ice_commons.config_settings import app_config
from ice_commons.store.base import VerbisStore
from ice_commons.utils import make_dir

logger = logging.getLogger(__name__)


class StanfordNLP(object):
    def __init__(self):
        self.nlp = StanfordCoreNLP(app_config['CORENLP_END_POINT'], port=int(app_config['CORENLP_PORT']),
                                   timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)

    def word_tokenize(self, sentence):
        return self.nlp.word_tokenize(sentence)

    def pos(self, sentence):
        return self.nlp.pos_tag(sentence)

    def ner(self, sentence):
        return self.nlp.ner(sentence)

    def parse(self, sentence):
        return self.nlp.parse(sentence)

    def dependency_parse(self, sentence):
        return self.nlp.dependency_parse(sentence)

    def annotate(self, sentence, prop):
        return self.nlp.annotate(sentence, properties=prop)


def get_all_custom_entities(serviceid):
    custom_entities = get_custom_entities(serviceid)
    patterns = get_pattern_entities(serviceid)
    phrases = get_phrase_entities(serviceid)
    for pattern_each in patterns:
        custom_entities.append(pattern_each["entity"])
    for phrase_each in phrases:
        custom_entities.append(phrase_each["entity"])
    return custom_entities


def stanfordcorenlp_customner(serviceid, text, original_text, language):
    sNLP = StanfordNLP()
    model_name = get_corenlp_modelname(serviceid)
    path = (os.path.join(os.path.expanduser('~'), '.verbis', 'store/' + serviceid) + "/" + model_name).encode("utf-8")
    props = {
        "annotators": "tokenize,ssplit,pos,lemma,ner",
        "pipelineLanguage": language,
        "tokenize.whitespace": "true",
        "ner.model": path
    }
    text = text.encode("utf-8")
    original_text = original_text.encode("utf-8")
    results = sNLP.annotate(text, props)
    result = json.loads(results)
    sentence = result['sentences'] if 'sentences' in result else []
    entity_mention = []
    for item in sentence:
        entity = get(item, 'entitymentions', [])
        for entity_each in entity:
            entity_mention.append(entity_each)
    entities = []
    pos = []
    for entity_mention_each in entity_mention:
        custom_entities = get_all_custom_entities(serviceid)
        print(custom_entities)
        if entity_mention_each['ner'] in custom_entities:
            ent = " ".join(original_text.split()[entity_mention_each['docTokenBegin']:entity_mention_each['docTokenEnd']])
            entity = dict(start=entity_mention_each['docTokenBegin'], end=entity_mention_each['docTokenEnd'],
                          entity=ent, score=".25", tag=entity_mention_each['ner'], resolvedTo={'baseEntity': ent})
            entities.append(entity)
    return entities, pos


def stanfordcorenlp_defaultner(text, original_text, language):
    sNLP = StanfordNLP()
    props = {
        "annotators": "tokenize,ssplit,pos,lemma,ner",
        "pipelineLanguage": language,
        "tokenize.whitespace": "true"
    }
    text = text.encode("utf-8")
    original_text = original_text.encode("utf-8")
    results = sNLP.annotate(text, props)
    result = json.loads(results)
    sentence = result['sentences'] if 'sentences' in result else []
    entity_mention = []
    tokens = []
    for item in sentence:
        entity = get(item, 'entitymentions', [])
        tok = get(item, 'tokens', [])
        for entity_each in entity:
            entity_mention.append(entity_each)
        for tok_each in tok:
            tokens.append(tok_each)
    entities = []
    for entity_mention_each in entity_mention:
        ent = " ".join(original_text.split()[entity_mention_each['docTokenBegin']:entity_mention_each['docTokenEnd']])
        entity = dict(start=entity_mention_each['docTokenBegin'], end=entity_mention_each['docTokenEnd'], entity=ent,
                      tag=entity_mention_each['ner'], resolvedTo={'baseEntity': ent})
        entities.append(entity)
    pos = []
    for token_each in tokens:
        pos_each = {'text': token_each['originalText'], 'tag': token_each['pos'], 'pos': token_each['pos'],
                    'lemma': token_each['lemma']}
        pos.append(pos_each)
    return entities, pos


def write_to_tsv(serviceid, tokens, tags):
    tsv_file = serviceid + ".tsv"
    logger.info("File saved to %s" % os.path.join(os.path.expanduser('~'), '.verbis', tsv_file))
    with open(os.path.join(os.path.expanduser('~'), '.verbis', tsv_file), "w") as out_file:
        for i in range(len(tokens)):
            token = tokens[i]
            tag = tags[i]
            for j in range(len(token)):
                out_file.write(token[j].encode("utf-8") + "\t" + tag[j].encode("utf-8") + "\n")
            out_file.write("\n")


def write_property_file(serviceid, engine):
    configparser = CP.RawConfigParser()
    property_file = serviceid + ".prop"
    input_file = serviceid + ".tsv"
    output_file = os.path.join(os.path.expanduser('~'), '.verbis', 'store/' + serviceid) + "/" + str(
        serviceid) + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + '-' + engine + '-ner.ser.gz'
    VerbisStore().remove_previous_model_from_store(serviceid)
    VerbisStore().remove_models_from_remote(serviceid)
    put_corenlp_modelname(serviceid, output_file)
    if not os.path.exists(os.path.join(os.path.expanduser('~'), '.verbis', 'store/' + serviceid)):
        make_dir(os.path.join(os.path.join(os.path.expanduser('~'), '.verbis', 'store/' + serviceid)))

    configparser.add_section('input')
    configparser.set('input', 'trainFile', os.path.join(os.path.expanduser('~'), '.verbis', input_file))

    configparser.add_section('output')
    configparser.set('input', 'serializeto', output_file)

    configparser.add_section('properties')
    configparser.set('properties', 'map', 'word=0,answer=1')
    configparser.set('properties', 'maxLeft', '1')
    configparser.set('properties', 'useClassFeature', 'true')
    configparser.set('properties', 'useWord', 'true')
    configparser.set('properties', 'useNGrams', 'true')
    configparser.set('properties', 'noMidNGrams', 'true')
    configparser.set('properties', 'maxNGramLeng', '6')
    configparser.set('properties', 'usePrev', 'true')
    configparser.set('properties', 'useNext', 'true')
    configparser.set('properties', 'useDisjunctive', 'true')
    configparser.set('properties', 'useSequences', 'true')
    configparser.set('properties', 'usePrevSequences', 'true')
    configparser.set('properties', 'useTypeSeqs', 'true')
    configparser.set('properties', 'useTypeSeqs2', 'true')
    configparser.set('properties', 'useTypeySequences', 'true')
    configparser.set('properties', 'wordShape', 'chris2useLC')

    with open(os.path.join(os.path.expanduser('~'), '.verbis', property_file), 'wb') as configfile:
        configparser.write(configfile)


def create_model_file(serviceid):
    property_file = os.path.join(os.path.expanduser('~'), '.verbis', serviceid + ".prop")
    coreNLP = app_config['CORENLP_PATH'] + "/" + app_config['CORENLP_VERSION'] + ".jar"
    cmd = "java -cp " + coreNLP + " edu.stanford.nlp.ie.crf.CRFClassifier -prop " + property_file
    logger.info("java command : %s" % cmd)
    os.system(cmd)
    os.remove(os.path.join(os.path.expanduser('~'), '.verbis', serviceid + ".prop"))
    os.remove(os.path.join(os.path.expanduser('~'), '.verbis', serviceid + ".tsv"))


def get_corenlp_instance(serviceid, engine):
    if serviceid is "DEFAULT":
        model = get_corenlp_default_model(engine)
    else:
        model = get_corenlp_custom_model(engine)
    instance = create_instance(model, serviceid=serviceid)
    return instance
