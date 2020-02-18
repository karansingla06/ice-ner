import traceback

import requests
import json
import logging
from ice_commons.config_settings import app_config
import datetime
import falcon

logger = logging.getLogger(__name__)


class RequestApplicationAuthenticationMiddleware(object):
    license_status = {}

    def process_request(self, req, resp):
        logger.info('RequestApplicationAuthenticationMiddleware::process_request BEGIN')
        authentication_status = 0
        try:
            authentication_status = self.validate_authentication_from_cache()
            if authentication_status != 1:
               response = self.authenticate_requests()
               if response is not None and response.status_code == 200:
                   validationres = json.loads(response.text)
                   authentication_status = validationres["message"]
                   self.license_status.clear()
                   self.license_status[datetime.date.today()] = authentication_status
        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
        challenges = ['Error="LicenseAuthentication"']
        if authentication_status != 1:
            description = ('The provided license token is not valid. '
                           'Please request a new license token and try again.')
            raise falcon.HTTPUnauthorized('Authentication required',
                                          description,
                                          challenges,
                                          href='http://docs.example.com/auth')

    def validate_authentication_from_cache(self):
        logger.info('RequestApplicationAuthenticationMiddleware::validate_authentication_from_cache BEGIN')
        isvalid = 0
        try:
            if datetime.date.today() in list(self.license_status.keys()):
                isvalid = 1
            else:
                isvalid = -1
            #isvalid = self.license_status[datetime.date.today()]
        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
            isvalid = -1
        logger.info('RequestApplicationAuthenticationMiddleware::validate_authentication_from_cache END '+str(isvalid))
        return isvalid

    def authenticate_requests(self):
        logger.info('RequestApplicationAuthenticationMiddleware::authenticate_requests BEGIN')
        server_url = app_config['LICENSE_KEY_VALIDATION_URL'] + '/api/license/validate'
        # call get service with headers and params
        response ={}
        try:
            headers = {'content-type': 'application/json'}
            response = requests.post(server_url, data=json.dumps({}), headers=headers)
        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
        return response

