import logging

from pydash import get
from ice_commons.utility.cipher import encrypt
import datetime
from ice_commons.config_settings import app_config
from ice_rest.manager.analytics.botanalyticsapi import BotAnalyticsAPI

logger = logging.getLogger(__name__)


def missedUtterences(response,serviceid, req_id, missed_text=None):
    """
    :param missed_text:
    :param response:
    :return:
    """
    response_intent = get(response, "intent", default={})
    response_entity = get(response, "entities", default=[])

    '''
    Checking for Null values in intent and entity, if Null then adding the values to field 
    missedUtterances in the database verbis/datasources  
    '''
    if bool(response_entity) is False:
        response_confidence_level = get(response_intent, "confidence_level", default=[])
        response_confidence_level = response_confidence_level[0] if len(response_confidence_level) > 0 else {}
        probalibity_values = list(response_confidence_level.values())

        logger.info("len of probalibity_values %s" % (len(probalibity_values)))
        if (len(probalibity_values) > 1):
            temp_list = []
            for items in probalibity_values:
                items = items.strip('%')
                items = float(items)
                temp_list.append(items)

            temp_list.sort(key=float, reverse=True)
            p1 = temp_list[0]
            p2 = temp_list[1]

            diff_cal = lambda p1, p2: p1 - p2
            final_value = diff_cal(p1, p2)

            if final_value < 10:
                encrypted_text = encrypt(missed_text)
                if app_config['BOTANALYTICS_LOG_FLAG'].upper() == "ON":
                    BotAnalyticsAPI().log(requesttype="nermisseddetails", serviceid= serviceid, req_id=req_id, ner_req_timestamp=datetime.datetime.now().replace(microsecond=0).isoformat())
                return encrypted_text
    else:
        logger.info('Utterance already mapped')

    return missed_text
