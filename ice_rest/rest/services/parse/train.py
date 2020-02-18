import logging

import falcon
from falcon import HTTPBadRequest

from ice_rest.decorators import route
from ice_rest.rest.exception.notfound import InsufficientDataError
from ice_commons.celery_jobs.train.tasks import train_parse
from ice_commons.utils import dict_contains
from pydash import get
from ice_rest.rest.services.parse.impl.common.markdown_generator import markdown_creater
from ice_commons.data.dl.manager import ProjectManager, ProjectconfigsManager
import datetime
from dateutil.relativedelta import relativedelta
import uuid
from ice_rest.manager.analytics.botanalyticsapi import BotAnalyticsAPI
from ice_commons.config_settings import app_config

logger = logging.getLogger(__name__)


def get_prediction_api_url(req):
    relative_uri = "/api/parse/predict"
    url = req.url
    return url.replace(req.relative_uri, relative_uri)


def updateStatus(serviceid, train_ner, train_ir):
    manager = ProjectManager()
    query = {
        "serviceid": serviceid
    }
    config = manager.find_model(query)
    if config is not None:
        if train_ner is True:
            document = {
                "$set": {
                    "ner.status": ProjectManager.STATUS_HOLD,
                    "ner.status_message": "Awaiting the completion of entity training."
                }
            }
            manager.update_config(query, document)
        if train_ir is True:
            document = {
                "$set": {
                    "ir.status": ProjectManager.STATUS_HOLD,
                    "ir.status_message": "Awaiting the completion of intent training."
                }
            }
            manager.update_config(query, document)


@route('/api/parse/train')
class TrainParseResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['serviceid']
        assert dict_contains(doc, mandatory_fields) is True, TrainParseResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req, resp):
        log_flag = False
        if app_config['BOTANALYTICS_LOG_FLAG'].upper() == "ON":
            log_flag, req_id, botanalytics, start_time = True, str(uuid.uuid4()), BotAnalyticsAPI(), datetime.datetime.now()

        manager = ProjectconfigsManager()
        doc = req.context['doc'] or {}
        serviceid = get(doc, "serviceid")
        train_ner = get(doc, "train_ner", default=True)
        train_ir = get(doc, "train_ir", default=True)

        try:
            updateStatus(doc['serviceid'], train_ner, train_ir)
            train_parse.delay(doc['serviceid'], train_ner, train_ir)
            predict_url = get_prediction_api_url(req)
            logger.info("get prediction url is %s" % str(predict_url))
            markdown = markdown_creater(serviceid, predict_url)
            logger.info("markdown is %s" % str(markdown))
            document = {
                "$set": {
                    "integration_markdown": markdown.get("mark_down_ui_client")
                }
            }
            manager.update_config_by_service_id(serviceid, document)
            if log_flag:
                botanalytics.log(requesttype="nertraindetails", serviceid=doc['serviceid'], req_id=req_id, train_entity=train_ner,train_intent=train_ir, ner_req_timestamp=start_time.replace(microsecond=0).isoformat())
        except InsufficientDataError as ide:
            raise ide
        except AssertionError as ae:
            logger.exception(ae)
            raise falcon.HTTPBadRequest('Invalid Configuration', ae)
        except Exception as ex:
            logger.exception(ex)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        finally:
            if log_flag:
                end_time = datetime.datetime.now()
                total_time = relativedelta(end_time, start_time)
                botanalytics.log(requesttype="nerrequests", serviceid=doc['serviceid'], req_id=req_id, action="TRAIN", ner_req_timestamp=start_time.replace(microsecond=0).isoformat(), ner_req_end_timestamp=end_time.replace(microsecond=0).isoformat(), total_action_time=(total_time.hours * 60 * 60 * 1000 + total_time.minutes * 60 * 1000 +total_time.seconds * 1000) + (total_time.microseconds / 1000))

        resp.set_header('X-Powered-By', 'USTGlobal Verbis')
        resp.status = falcon.HTTP_200
