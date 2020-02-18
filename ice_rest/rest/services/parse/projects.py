import logging
import traceback
import os

import falcon
from ice_rest.decorators import route

from ice_commons.data.dl.manager import ProjectManager, ProjectconfigsManager
from bson.objectid import ObjectId
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

def fetch_project_if_exists(serviceid):
    '''
    fetch project if exists
    '''
    manager = ProjectManager()
    query = {"serviceid": serviceid}
    data = manager.exists(query)
    if data:
        fetched_project = manager.find_one(query)
        logger.info("project fetched from DB") 
        return fetched_project
    else:
        return False


@route('/api/parse/projects/fetch_project')
class FetchProject(object):
    def on_post(self, req, resp):
        logger.info(req.context)
        doc = req.context['doc'] or {} 
        try:
            json = doc["json"]
            serviceid = json["serviceid"]
            # fetching project object
            fetched_project = fetch_project_if_exists(serviceid, json)
            if fetched_project:
                resp.data = fetched_project
            else:
                resp.data = {"status":"Project not found"}
        except AssertionError as ae:
            logger.exception(ae.message, exc_info=True)
            logger.info(type(traceback.format_exc()))
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())
        except Exception as ex:
            logger.exception(ex.message)
            raise falcon.HTTPServiceUnavailable('Service Outage', str(ex), 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200


def save_project(json):
    manager = ProjectManager()    
    if json:
        manager.save_config(json)
        logger.info("Project added in ProjectManager DB.")
        return True
    else:
        logger.info("Project data was empty. Insert failed")
        return False


@route('/api/parse/projects/create_project')
class CreateProject(object):
    def on_post(self, req, resp):
        logger.info(req.context)
        doc = req.context['doc'] or {}

        try:
            json = doc["data"]["addProject"]["changedProjectEdge"]["node"]
            save_project(json)
            resp.data = {'status': 'Project added successfully.'}
        except AssertionError as ae:
            logger.exception(ae.message, exc_info=True)
            logger.info(type(traceback.format_exc()))
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())
        except Exception as ex:
            logger.exception(ex.message)
            raise falcon.HTTPServiceUnavailable('Service Outage', str(ex), 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200



def delete_project_if_exists(project_id):
    """
    :param project_id:
    :return:
    """
    manager = ProjectManager()
    config_manager = ProjectconfigsManager()
    query = {"_id": ObjectId(project_id)}
    config_project_query = {"project": ObjectId(project_id)}
    data = manager.exists(query)
    if data:
        manager.delete(query)
        config_manager.delete(config_project_query)
        logger.info("project deleted from PR DB.")
        logger.info("project deleted from PR CONFIG DB")

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
        return True
    else:
        return False



def update_project_if_exists(serviceid, json):
    """
    :param serviceid:
    :param json:
    :return:
    """
    manager = ProjectManager()
    query = {"serviceid": serviceid}


def update_project_if_exists(serviceid, json):
    '''
    update_project_if_exists
    '''

    manager = ProjectManager()
    query = {"serviceid":serviceid}
    data = manager.exists(query)
    if data:
        newvalues = { "$set": json }
        manager.update(query, newvalues)
        logger.info("project update in PR DB.")
        return True
    else:
        return False


@route('/api/parse/projects/update_project')
class UpdateProject(object):
    def on_post(self, req, resp):
        logger.info(req.context)
        doc = req.context['doc'] or {} 
        try:

            service_id = doc["serviceid"]
            assert service_id != ""
            json = doc["json"]
            service_id = doc[u"serviceid"]
            assert service_id != ""
            json = doc[u"json"]
            # update project object
            bool_value = update_project_if_exists(service_id, json)
            if bool_value:
                resp.data = {'status': 'project updated successfully.'}
            else:
                resp.data = {'status': 'project not found'}
        except AssertionError as ae:
            logger.exception(ae.message, exc_info=True)
            logger.info(type(traceback.format_exc()))
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())
        except Exception as ex:
            logger.exception(ex.message)
            raise falcon.HTTPServiceUnavailable('Service Outage', str(ex), 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200

@route('/api/parse/projects/delete_project')
class DeleteProject(object):
    def on_post(self, req, resp):
        logger.info(req.context)
        doc = req.context['doc'] or {} 
        try:
            project_id = doc["id"]
            assert project_id != ""
            # delete project object
            bool_value = delete_project_if_exists(project_id)
            service_id = doc["serviceid"]
            assert service_id != ""
            # delete project object
            bool_value = delete_project_if_exists(service_id)
            if bool_value:
                resp.data = {'status': 'project deleted successfully.'}
            else:
                resp.data = {'status': 'No project found with the given id'}
        except AssertionError as ae:
            logger.exception(ae.message, exc_info=True)
            logger.info(type(traceback.format_exc()))
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())
        except Exception as ex:
            logger.exception(ex.message)
            raise falcon.HTTPServiceUnavailable('Service Outage', str(ex), 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200
        resp.data = {"data": {"deleteProject": {"ok": "true"}, "delProjectConfig": {"ok": "true"}}}

