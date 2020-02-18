# coding=utf-8
import datetime
import logging
import traceback

import moment

from ice_commons.core.resolution.base_er import BaseResolutionNER
from ice_commons.core.resolution.utils.handleDatesTime import DateUtils

logger = logging.getLogger(__name__)

month_map = {'01': "January", '02': "February", '03': "March", '04': "April", '05': "May", '06': "June", '07': "July",
             '08': "August", '09': "September", '10': "October", '11': "November", '12': "December"}


class DateResolutionNER(BaseResolutionNER):
    def resolve(self, text):
        """
        :type text: object
        :return : list
        """
        try:
            resolved_mappings = []
            if type(text) is str or type(text) is str:
                dateobj = DateUtils()
                result = dateobj.parse_date(str(text))
                for result_each in result:
                    timestamp = result_each['timestamp']
                    temp = []
                    resp = {'baseEntity': result_each['words'], 'tag': 'TIMESTAMP', 'start': result_each['position'][0],
                            'end': result_each['position'][1],
                            'entity': result_each['words'], 'resolvedTo': {'values': []}}
                    for timestamp_each in  timestamp:
                        moment_obj = moment.date(datetime.datetime.strptime(timestamp_each[0:19], '%Y-%m-%d %H:%M:%S'))
                        day = moment_obj.format('DD')
                        month = moment_obj.format('MM')
                        year = moment_obj.format('YYYY')
                        hour = moment_obj.format('h')
                        minute = moment_obj.format('m')
                        second = moment_obj.format('s')
                        temp.append({'timestamp': timestamp_each[0:19],
                                               'year': year, 'month': month_map[month], 'day': day, 'hour': hour,
                                               'minute': minute, 'second': second })
                    resp['resolvedTo']['values']= temp
                    if result_each['words'] in text:
                        resolved_mappings.append(resp)
            return resolved_mappings
        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
            return []