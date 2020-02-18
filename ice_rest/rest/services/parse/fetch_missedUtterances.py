import falcon
import logging
from pydash import get
from ice_rest.decorators import route
from ice_commons.utility.cipher import decrypt
from ice_commons.data.dl.manager import DatasourceManager

logger = logging.getLogger(__name__)
manager = DatasourceManager()


@route('/api/parse/fetch_missed_utterances')
class DecryptMissedUtterances(object):
    def on_post(self, req, resp):
        doc = req.context['doc'] or {}
        try:
            serviceid = doc["serviceid"]
            datasource = manager.find_datasource_by_service_id(serviceid)
            logger.info("Fetching missed utterances from datasource")
            encrypted_missed_utterances = get(datasource, "missedUtterances",[])
            missed_utterances = []
            for missed_utterance_each in encrypted_missed_utterances:
                decrypted_text = decrypt(missed_utterance_each)
                missed_utterances.append(decrypted_text)
            logger.info("Missed utterances fetched successfully")
            resp.data = {"missed_utterances": missed_utterances}
            resp.set_header('X-Powered-By', 'USTGlobal ICE')
            resp.status = falcon.HTTP_200
        except Exception as ex:
            logger.exception(ex)
            resp.data = {"msg": ex}
            resp.set_header('X-Powered-By', 'USTGlobal ICE')
            resp.status = falcon.HTTP_500
