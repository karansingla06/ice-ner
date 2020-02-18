import logging
import traceback

import falcon
from falcon import HTTPBadRequest

from ice_rest.decorators import route, service
from ice_rest.rest.services.parse.impl.tag_impl import tag
from ice_commons.config_settings import app_config
from ice_commons.utils import dict_contains
from ice_rest.manager.analytics.botanalyticsapi import BotAnalyticsAPI
logger = logging.getLogger(__name__)

import datetime
from dateutil.relativedelta import relativedelta
import uuid

def _validate_tag_request(req, resp, resource, params):
    """

    :param req:
    :param resp:
    :param resource:
    :param params:
    :return:
    """

    doc = req.context['doc']
    mandatory_fields = ['text','serviceid']
    if not dict_contains(doc, mandatory_fields):
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

@route('/api/parse/tag')
@service(
    '/api/parse/tag',
    tag,
    _validate_tag_request
)
class TagResource(object):
    @falcon.before(_validate_tag_request)
    def on_post(self, req, resp):
        log_flag = False
        if app_config['BOTANALYTICS_LOG_FLAG'].upper() == "ON":
            log_flag, req_id, botanalytics, start_time = True, str(uuid.uuid4()), BotAnalyticsAPI(), datetime.datetime.now()

        doc = req.context['doc']
        try:
            results = tag(doc)
            resp.data = results
            ###  BotAnalytics tag api results logging
            if log_flag:
                botanalytics.log(requesttype="nertagdetails", serviceid=doc['serviceid'], req_id=req_id, tag_custom_tags= [i['tag'] for i in results['custom_tags']], tag_default_tags= [i['tag'] for i in results['default_tags']])

        except AssertionError as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Assertion Error, Please contact admin for assistance',
                                                traceback.format_exc())
        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        finally:
            ###  BotAnalytics tag api call logging
            if log_flag:
                end_time = datetime.datetime.now()
                total_time = relativedelta(end_time, start_time)
                botanalytics.log(requesttype="nerrequests", serviceid=doc['serviceid'], req_id=req_id, action="TAG",ner_req_timestamp=start_time.replace(microsecond=0).isoformat(), ner_req_end_timestamp=end_time.replace(microsecond=0).isoformat(),total_action_time=(total_time.hours*60*60*1000+total_time.minutes*60*1000+total_time.seconds*1000)+(total_time.microseconds/1000))

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200
