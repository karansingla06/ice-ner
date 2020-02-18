import logging

from ice_commons.er.engines.corenlp_ner import CorenlpCustomNER, CorenlpDefaultNER, CorenlpNER
from ice_commons.er.utils.corenlp_utils import stanfordcorenlp_defaultner, stanfordcorenlp_customner

logger = logging.getLogger(__name__)


class CorenlpSpanishNER(CorenlpNER):
    def get_engine(self):
        return "CoreNLP-es"


class CorenlpSpanishDefaultNER(CorenlpDefaultNER, CorenlpSpanishNER):
    def __init__(self, serviceid="DEFAULT"):
        super(CorenlpSpanishDefaultNER, self).__init__(serviceid)

    def predict(self, text, original_text, pos):
        return stanfordcorenlp_defaultner(text, original_text, language="es")


class CorenlpSpanishCustomNER(CorenlpCustomNER, CorenlpSpanishNER):
    def __init__(self, serviceid=None):
        super(CorenlpSpanishCustomNER, self).__init__(serviceid)

    def predict(self, text, original_text, pos):
        return stanfordcorenlp_customner(self.serviceid, text, original_text, language="es")
