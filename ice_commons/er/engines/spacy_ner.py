# from __future__ import unicode_literals
from ice_commons.er.engines.base_ner import BaseDefaultEntityRecognizer,AbstractIceEngine
import spacy
from ice_commons.utility.custom_tokenizer import tokenize_utterance
from pydash import compact
from spacy.tokens import Doc

import logging

logger = logging.getLogger(__name__)


class SpacyNER(AbstractIceEngine):
    def get_engine(self):
        return "SPACY"


class SpacyDefaultNER(BaseDefaultEntityRecognizer,SpacyNER):

    def __init__(self, serviceid="DEFAULT"):
        super(SpacyDefaultNER,self).__init__(serviceid)

    def load(self):
        spacy_model = spacy.load('en')
        def replace_tokenizer(my_split_function):
            spacy_model.tokenizer = lambda string: Doc(spacy_model.vocab, words=my_split_function(string))

        replace_tokenizer(tokenize_utterance)
        return spacy_model

    def predict(self, text, original_text, pos):
        if not isinstance(text, str):
            text = str(text, "utf-8")
        doc = self.model(text)
        logger.info("english predict")
        def default_entity_mapping(entity):
            return {
                "tag": entity.label_,
                "entity": " ".join(original_text.split()[entity.start:entity.end]),
                "start": entity.start,
                "end": entity.end,
                "resolvedTo" : {'baseEntity' : " ".join(original_text.split()[entity.start:entity.end])}
            }

        default_entities = compact(list(map(default_entity_mapping, doc.ents)))
        pos_mapping = []
        if pos is not None:
            def default_pos_mapping(word):
                original_text_tokens= original_text.split()
                text_tokens = text.split()
                word_text = word.text
                word_index = text_tokens.index(word_text)
                return {
                    "text": original_text_tokens[word_index] if word_index < len(original_text_tokens) else word_text,
                    "lemma": word.lemma_,
                    "tag": word.tag_,
                    "pos": word.pos_
                }

            pos_mapping = list(map(default_pos_mapping, doc))
        return default_entities, pos_mapping
