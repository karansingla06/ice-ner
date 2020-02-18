import logging
import time
import falcon
from falcon import HTTPBadRequest

from ice_rest.decorators import route
from ice_rest.rest.exception.notfound import InsufficientDataError
from ice_commons.celery_jobs.train.tasks import validate_test_data
from ice_commons.utils import dict_contains
from pydash import get
from ice_commons.data.dl.manager import ProjectManager


logger = logging.getLogger(__name__)

manager = ProjectManager()



def get_predict_api_url(req):
    relative_uri = "/api/parse/predict"
    url = req.url
    return url.replace(req.relative_uri, relative_uri)


def updateStatus(serviceid):

    query = {
        "serviceid": serviceid
    }
    config = manager.find_model(query)
    if config is not None:
        document = {
            "$set": {
                "ner.status": ProjectManager.STATUS_VALIDATING,
                "ner.status_message": "Awaiting the completion of validation"
            }
        }
        manager.update_config(query, document)

        document = {
            "$set": {
                "ir.status": ProjectManager.STATUS_VALIDATING,
                "ir.status_message": "Awaiting the completion of validation"
            }
        }
        manager.update_config(query, document)
        time.sleep(6)


@route('/api/parse/validate')
class ValidateParseResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc'] or {}
        mandatory_fields = ['serviceid']
        assert dict_contains(doc, mandatory_fields) is True, ValidateParseResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req, resp):
        doc = req.context['doc'] or {}
        serviceid = get(doc, "serviceid", None)
        predict_url = get_predict_api_url(req)
        try:
            conf = manager.find_config_by_id(doc['serviceid'])
            if get(conf, "ner.status",None) in ["trained", "validated"]:
                updateStatus(serviceid)
                validate_test_data.delay(serviceid, predict_url)
            else:
                resp.data = {"message" : "Cannot validate if project is not trained"}

        except InsufficientDataError as ide:
            raise ide
        except AssertionError as ae:
            logger.exception(ae)
            raise falcon.HTTPBadRequest('Invalid Configuration', ae)
        except Exception as ex:
            logger.exception(ex)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal Verbis')
        resp.status = falcon.HTTP_200
