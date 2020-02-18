import logging
import traceback
import datetime,json

import falcon
from falcon import HTTPBadRequest

from ice_rest.decorators import route
from ice_rest.rest.services.parse.impl.predict_impl import predict_impl, modify_response_v1
from ice_commons.utils import dict_contains
from pydash import get
from ice_rest.rest.services.parse.impl.common.store_utils import get_requested_services
from ice_commons.data.dl.manager import ProjectManager
from ice_rest.rest.services.parse.load_model import cache_model
from ice_commons.config_settings import app_config
from dateutil.relativedelta import relativedelta
import uuid
from ice_rest.manager.analytics.botanalyticsapi import BotAnalyticsAPI

logger = logging.getLogger(__name__)


def validate_service_id_and_cache(doc):
    """
    # cache model for respective project if not cached during prediction call.
    :param doc:
    :return:
    """
    manager = ProjectManager()
    query = {
        "serviceid": get(doc, "serviceid")
    }
    config = manager.find_model(query)
    if config is None:
        raise Exception("Invalid Service ID.")
    else:
        serviceid_info = get_requested_services(doc)
        cache_model(config, serviceid_info)
    return config


def update_last_access_to_predict_api(serviceid):
    query = {
        "serviceid": serviceid
    }
    document = {
        "$set": {
            "lastAccessed": datetime.datetime.utcnow(),
        }
    }
    manager = ProjectManager()
    manager.update_config(query, document)


def validate_prediction_request(doc):
    """
    :param doc:
    :return:
    """

    mandatory_fields = ['text', 'serviceid']
    if not dict_contains(doc, mandatory_fields):
        error = 'Mandatory params missing from the request. ' \
                'Please check your request params and retry'
        logger.exception(error)
        raise HTTPBadRequest("HTTP Bad Request", error)


@route('/api/parse/predict')
class PredictionResource(object):
    def on_post(self, req, resp):
        log_flag = False
        if app_config['BOTANALYTICS_LOG_FLAG'].upper() == "ON":
            log_flag, req_id, botanalytics, start_time = True, str(
                uuid.uuid4()), BotAnalyticsAPI(), datetime.datetime.now()
        doc = req.context['doc']
        validate_prediction_request(doc)
        config = validate_service_id_and_cache(doc)
        try:
            if log_flag:
                results = predict_impl(doc, config, req_id)
                botanalytics.log(requesttype="nerpredictdetails", serviceid=doc['serviceid'], req_id=req_id,
                                 predict_entities=[i['tag'] for i in results['entities']],
                                 predict_intent=get(results, 'intent.top_intent'),
                                 ner_req_timestamp=start_time.replace(microsecond=0).isoformat())
            else:
                results = predict_impl(doc, config)
            resp.data = results
        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())
        except Exception as ex:
            logger.exception(ex, exc_info=True)
            if not ex:
                description = 'Internal Server Error, Please try again later'
            else:
                description = ex
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)
        finally:
            update_last_access_to_predict_api(get(doc, 'serviceid'))
            if log_flag:
                end_time = datetime.datetime.now()
                total_time = relativedelta(end_time, start_time)
                botanalytics.log(requesttype="nerrequests", serviceid=doc['serviceid'], req_id=req_id, action="PREDICT",
                                 ner_req_timestamp=start_time.replace(microsecond=0).isoformat(),
                                 ner_req_end_timestamp=end_time.replace(microsecond=0).isoformat(), total_action_time=(total_time.hours * 60 * 60 * 1000 + total_time.minutes * 60 * 1000 + total_time.seconds * 1000) + (total_time.microseconds / 1000))

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200


@route('/api/parse/v1/predict')
class PredictionResource_V1(object):
    def on_post(self, req, resp):
        doc = req.context['doc']
        requested_services = validate_prediction_request(doc)
        try:
            reponse = predict_impl(doc)
            results = modify_response_v1(reponse)
            resp.data = results
        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200
