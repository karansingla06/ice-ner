import logging
import traceback
import os
import falcon
from falcon import HTTPBadRequest
from ice_rest.decorators import route
import sys
import shutil
from pydash import get
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.normpath(os.getcwd() + os.sep + os.pardir))

from ice_commons.data.dl.manager import ProjectManager
from ice_commons.utils import MODEL_TYPE_NER, MODEL_TYPE_IR, FILE_EXTENSION, get_model_name
from ice_rest.rest.services.parse.impl.common.store_utils import get_model_store
from ice_commons.store.base import VerbisStore
from ice_commons.utils import dict_contains

logger = logging.getLogger(__name__)



@route('/api/parse/cache/remove')
class RemoveCacheResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['serviceid']
        assert dict_contains(doc, mandatory_fields) is True, RemoveCacheResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req, resp):
        doc = req.context['doc'] or {}

        try:
            home_dir = os.path.expanduser('~')
            model_store_path = os.path.join(home_dir + os.sep + '.verbis/store')
            model_store = get_model_store()
            manager = ProjectManager()
            serviceid = doc['serviceid']
            query={'serviceid': serviceid}
            data = manager.find_model(query)
            engine = get(data, "engine", "ICE")
            model_name = get_model_name(serviceid, MODEL_TYPE_NER, engine)

            model_lists = model_store.get_active_models()
            logger.info("model lists -  %s" %model_lists)
            if model_name in model_lists:
                model_store.unpublish(serviceid, MODEL_TYPE_NER, engine)

            model_name = get_model_name(serviceid, MODEL_TYPE_IR, engine=None)
            logger.info(model_name)
            if model_name in model_lists:
                model_store.unpublish(serviceid, MODEL_TYPE_IR, engine=None)

            logger.info("path is %s" % os.path.join(model_store_path + os.sep + serviceid))
            # delete model file from local
            if os.path.exists(os.path.join(model_store_path + os.sep + serviceid)):
                # print "path exists, so do rm."
                shutil.rmtree(os.path.join(model_store_path + os.sep + serviceid))
                # delete model file from minio
                VerbisStore().remove_models_from_remote(serviceid)
                logger.info("files removed successfully")

            # update DB
            document = {
                "$set": {
                    "ner.status": 'new',
                    "ir.status": 'new'
                }
            }
            manager.update_config(query, document)

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())
        except Exception as ex:
            logger.exception(ex, exc_info=True)
            logger.error(traceback.format_exc())
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal Verbis')
        resp.status = falcon.HTTP_200