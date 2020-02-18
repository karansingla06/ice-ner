import logging
import traceback
import os
import shutil

import falcon
from falcon import HTTPBadRequest
import sys

from ice_rest.decorators import route
from ice_commons.utils import dict_contains

from ice_commons.data.dl.manager import ProjectManager, DatasourceManager
from ice_commons.utils import MODEL_TYPE_NER, MODEL_TYPE_IR, FILE_EXTENSION, get_model_name
from pydash import get
from ice_rest.rest.services.parse.impl.common.store_utils import get_model_store

home_dir = os.path.expanduser('~')

logger = logging.getLogger(__name__)

def uncache_project_if_exists(serviceid):
    model_store = get_model_store()
    manager = ProjectManager()
    query = {"serviceid":serviceid}
    document = manager.find_model(query)
    model_lists = model_store.get_active_models()
    if document is not None:
        engine = get(document, "engine", "ICE")
    else:
        engine = "ICE"

    model_name = get_model_name(serviceid, MODEL_TYPE_NER, engine)
    if model_name in model_lists:
        model_store.unpublish(serviceid, MODEL_TYPE_NER, engine)

    model_name = get_model_name(serviceid, MODEL_TYPE_IR, engine=None)
    if model_name in model_lists:
        model_store.unpublish(serviceid, MODEL_TYPE_IR, engine=None)

    # delete model file
    model_store_path = os.path.join(home_dir + os.sep + '.verbis/store')

    if os.path.exists(os.path.join(model_store_path + os.sep + serviceid)):
        shutil.rmtree(os.path.join(model_store_path + os.sep + serviceid))

    logger.info("uncache_project_if_exists done.")

def delete_project_if_exists(given_serviceid):
    '''
    delete_project_if_exists
    '''

    manager = ProjectManager()
    query = {"serviceid":given_serviceid}
    data = manager.exists(query)
    if data:
        manager.delete(query)
        logger.info("project deleted from PR DB.")
    ds_manager = DatasourceManager()
    data = ds_manager.exists(query)
    if data:
        ds_manager.delete(query)
        logger.info("project deleted from DS DB.")

@route('/api/parse/delete_project')
class DeleteProject(object):
    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['serviceid']
        if not dict_contains(doc, mandatory_fields):
            description = 'Mandatory params missing from the request. ' \
                          'Please check your request params and retry'
            logger.exception(description)
            raise HTTPBadRequest("HTTP Bad Request", description)

    @falcon.before(_validate_model_config)
    def on_post(self, req, resp):
        doc = req.context['doc'] or {}
        try:
            serviceid = doc["serviceid"]
            # delete model file
            uncache_project_if_exists(serviceid)
            resp.data = {'status': 'project deletion successful.'}
        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.info(type(traceback.format_exc()))
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())
        except Exception as ex:
            logger.exception(ex)
            raise falcon.HTTPServiceUnavailable('Service Outage', str(ex), 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200
