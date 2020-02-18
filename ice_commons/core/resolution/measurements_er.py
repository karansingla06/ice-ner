# coding=utf-8
import logging
import traceback

from ice_commons.core.resolution.base_er import BaseResolutionNER
from quantulum3 import parser

logger = logging.getLogger(__name__)


def get_word_position(char_span, text):
    """
    :param char_span: The starting and ending character position of the entity
    :param text: The text from which resolver should identify measurement
    :return: Starting and ending word positions based on character  span
    """
    char_pos = start = end = 0
    for word_position, word in enumerate(text.split()):
        if char_pos == char_span[0]:
            start = word_position
        if char_pos + len(word) == char_span[1]:
            end = word_position + 1
        char_pos = char_pos + len(word) + 1
    return start, end


class MeasurementsResolutionNER(BaseResolutionNER):
    def resolve(self, text):
        """
        :param text: The text from which resolver should identify measurement
        :return:list
        """

        try:
            resolved_mappings = []
            if type(text) is str or type(text) is str:
                quant = parser.parse(text)
                for quant_each in quant:
                    if quant_each.unit.entity.name not in ("dimensionless", "time", "unknown"):
                        start, end = get_word_position(quant_each.span, text)
                        resp = {'tag': quant_each.unit.entity.name.upper(), 'entity': quant_each.surface,
                                'resolvedTo': {'unit': quant_each.unit.name, 'quantity': quant_each.value,
                                               'baseEntity': quant_each.surface}, 'start': start, 'end': end}
                        if quant_each.surface in text:
                            resolved_mappings.append(resp)
            return resolved_mappings

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
            return []
