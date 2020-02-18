# coding=utf-8
import logging
import traceback

from ice_commons.core.resolution.base_er import BaseResolutionNER
from ice_commons.core.resolution.utils.numberToText import stringToNumHandlingFunc

logger = logging.getLogger(__name__)


class NumberResolutionNER(BaseResolutionNER):
    def resolve(self, text):
        """
        :type text: object
        :return : list
        """
        try:
            resolved_mappings = []
            if type(text) is str or type(text) is str:
                result = stringToNumHandlingFunc(str(text))
                if len(result) != 0:
                    for result_each in result:
                        resp = dict(tag='NUMBER', entity=result_each['text'], resolvedTo={
                            'digit': int(result_each['digit']) if (result_each['digit'] * 10) % 10 == 0 else
                            result_each['digit'], 'baseEntity': result_each['text']}, start=result_each['start_index'],
                                    end=result_each['end_index'] + 1)
                        resolved_mappings.append(resp)
            return resolved_mappings
        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
            return []

