import logging
import requests
import falcon
import ast
from falcon import HTTPBadRequest
from ice_commons.data.dl.manager import DatasourceManager
from ice_rest.decorators import route
from ice_rest.rest.exception.notfound import InsufficientDataError
from ice_commons.utils import dict_contains
from pydash import get
from ice_commons.config_settings import app_config

logger = logging.getLogger(__name__)


@route('/api/parse/generate_variations')
class GenerateVariationsResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['serviceid','text']
        assert dict_contains(doc, mandatory_fields) is True, GenerateVariationsResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req, resp):
        doc = req.context['doc'] or {}
        try:
            config = DatasourceManager().find_datasource_by_service_id(doc['serviceid'])
            utterances = get(config, "utterances", [])
            response = requests.post(url=app_config['VARIATIONS_END_POINT'], json={'text': doc['text']},
                          headers={'Content-type': 'application/json'})

            if response.status_code == 200:
                paraphrases = ast.literal_eval(response.text)
                for i in utterances:
                    if i['utterance'] in paraphrases:
                        paraphrases.remove(i['utterance'])
                paraphrases = list(set(paraphrases[1:]))
                if doc['text'] in paraphrases:
                    paraphrases.remove(doc['text'])
                resp.data = paraphrases
            else:
                resp.data = []

        except requests.exceptions.RequestException:
            resp.data = []
        except InsufficientDataError as ide:
            raise ide
        except AssertionError as ae:
            logger.exception(str(ae))
            raise falcon.HTTPBadRequest('Invalid Configuration', str(ae))
        except Exception as ex:
            logger.exception(str(ex))
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal Verbis')
        resp.status = falcon.HTTP_200