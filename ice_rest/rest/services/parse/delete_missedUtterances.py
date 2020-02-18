import falcon
import logging
from pydash import get
from ice_rest.decorators import route
from ice_commons.utility.cipher import encrypt, decrypt
from ice_commons.data.dl.manager import DatasourceManager

logger = logging.getLogger(__name__)
manager = DatasourceManager()


@route('/api/parse/delete_missed_utterances')
class DeleteMissedUtterances(object):
    def on_post(self, req, resp):
        doc = req.context['doc'] or {}
        try:
            serviceid = doc["serviceid"]
            text = doc["text"]
            datasource = manager.find_datasource_by_service_id(serviceid)
            logger.info("checking if missed utterances in datasource model")
            encrypted_missed_utterances = get(datasource, "missedUtterances",[])
            resp.data = {"message": "text not present in missed utterances"}

            if len(encrypted_missed_utterances)!= 0:
                for utterance in encrypted_missed_utterances:
                    decrypted_utterance = decrypt(utterance)
                    if text == decrypted_utterance:
                        logger.info("removal process starting")
                        manager.remove_missed_utterance(serviceid, utterance)
                        resp.data = {"message" : "text successfully removed from missed utterances"}
                        break
            resp.set_header('X-Powered-By', 'USTGlobal ICE')
            resp.status = falcon.HTTP_200

        except Exception as ex:
            logger.exception(ex)
            resp.data = {"msg": ex}
            resp.set_header('X-Powered-By', 'USTGlobal ICE')
            resp.status = falcon.HTTP_500
