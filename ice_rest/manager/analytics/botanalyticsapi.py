import json
from .connections import AsyncCall
import logging
import falcon
import  traceback
from ice_commons.config_settings import app_config
logger = logging.getLogger(__name__)

class BotAnalyticsAPI(object):

    def store(self, requesttype, requestjson):
        try:
            asynccall = AsyncCall()
            url = app_config['BOTANALYTICS_END_POINT']
            url = url + "/" + requesttype
            asynccall.invoke(url, requestjson, {'Content-Type': 'application/json'})

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

    def log(self, **kwargs):
        requestjson = locals()['kwargs']
        if 'requesttype' in requestjson:
            requesttype = requestjson['requesttype']
            self.store(requesttype,requestjson)