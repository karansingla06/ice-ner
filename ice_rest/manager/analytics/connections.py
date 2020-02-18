from threading import Thread
import requests
import logging
import falcon, traceback
logger = logging.getLogger(__name__)


class AsyncCall(object):
    def post(self,url, jsondata, requestheaders):
        try:
            response = requests.post(url=url, json=jsondata, headers=requestheaders)

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

    def invoke(self,x,y,requestheaders):
        try:
            thread = Thread(target=self.post, args=(x, y, requestheaders))
            thread.start()
        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)