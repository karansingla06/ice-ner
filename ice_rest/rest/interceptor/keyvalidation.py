import falcon
from ice_commons.utility.validation import Validator
from ice_commons.config_settings import app_config
import logging

logger = logging.getLogger(__name__)


class KeyValidator(object):

    def process_request(self, req, resp):
        relative_uri = req.relative_uri
        if "/api/parse/tag" in relative_uri and (req is not None and req.method != "GET") or \
                "/api/parse/predict" in relative_uri and (req is not None and req.method != "GET") or \
                "/api/parse/train" in relative_uri and (req is not None and req.method != "GET"):
            key = None
            try:
                key = app_config['LICENSE_KEY']
            except Exception as ex:
                print(ex)
                raise falcon.HTTPUnauthorized("Key error", "System error occurred")
            if key is None:
                raise falcon.HTTPUnauthorized("Key error", "License key is not set, or is NONE")
            keystatus = False
            try:
                validator = Validator()
                keystatus = validator.validate(key)
            except Exception as ex:
                print(ex)
                raise falcon.HTTPUnauthorized("Key error", "System error occurred")
            if keystatus is False:
                raise falcon.HTTPUnauthorized("Key error", "License key is expired")

    def process_resource(self, req, resp, resource, params):
        pass

    def process_response(self, req, resp, resource, req_succeeded):
        pass
