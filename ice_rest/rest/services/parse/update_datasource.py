import falcon
import logging
from pydash import get
from ice_rest.decorators import route
from ice_commons.utility.cipher import encrypt, decrypt
from ice_commons.data.dl.manager import DatasourceManager
import json

logger = logging.getLogger(__name__)
manager = DatasourceManager()


@route('/api/parse/update_datasource')
class UpdateDatasource(object):
    def on_post(self, req, resp):
        datasource = req.context['doc'] or {}
        doc = datasource["input"]
        try:

            serviceid = doc["serviceid"]
            document = {
                "$set": {
                    "clientMutationId":doc["clientMutationId"],
                    "entities": doc["entities"],
                    "utterances":doc["utterances"],
                    "patterns": doc["patterns"], 
                    "trainIntent":doc["trainIntent"],
                    "trainEntity":doc["trainEntity"], 
                    "intents": doc["intents"],
                    "synonyms": doc["synonyms"],
                    "phrases": doc["phrases"],
                    "predefined_entities": doc["predefined_entities"]
                }
            }

            manager.update_datasource(serviceid,document)
            logger.info('Utterance updated to DB successfully')
            resp.data = {"message": "Utterance updated to DB successfully"}
            resp.set_header('X-Powered-By', 'USTGlobal ICE')
            resp.status = falcon.HTTP_200          


        except AssertionError as ae:
            logger.exception(ae.message)
            raise falcon.HTTPBadRequest('Service publish condition failed', ae.message)
        except Exception as ex:
            logger.exception(ex.message)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

