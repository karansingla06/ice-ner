import logging

import falcon
from falcon import HTTPBadRequest

from ice_rest.decorators import route
from ice_rest.rest.services.parse.impl.tokenize_impl import tokenize_utterance
from ice_commons.utils import dict_contains

logger = logging.getLogger(__name__)


@route('/api/parse/tokenize')
class TokenizeParseResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['text']
        assert dict_contains(doc, mandatory_fields) is True, TokenizeParseResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req, resp):
        doc = req.context['doc'] or {}
        try:
            tokens = tokenize_utterance(doc['text'])
            resp.data = tokens
        except Exception as ex:
            logger.exception(ex)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal Verbis')
        resp.status = falcon.HTTP_200
