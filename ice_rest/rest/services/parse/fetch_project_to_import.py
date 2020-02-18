import logging
import traceback
import os

import falcon
from falcon import HTTPBadRequest
from ice_rest.decorators import route
from ice_rest.rest.services.parse.validate_project_org import validate_project_organisation
from ice_commons.data.dl.manager import ProjectManager, DatasourceManager, ProjectconfigsManager
from bson.objectid import ObjectId

home_dir = os.path.expanduser('~')

logger = logging.getLogger(__name__)


def user_trained_projects(userid):
    """
    :param userid:
    :return:
    """
    manager = ProjectManager()
    query = {"$and": [{"createdBy": ObjectId(userid)}, {"ner.status": "trained"}, {"ir.status": "trained"},
                      {"visibility": "private"}, {"masterBot": False}]}
    # query = {"$and": [{"createdBy": ObjectId(userid)}, {"ner.status": "trained"}, {"ir.status": "trained"},
    #                   {"visibility": "private"}]}
    projection = {"name": 1, "serviceid": 1}
    data = manager.exists(query)
    if data:
        projects_to_import = manager.find(query, projection)
        logger.info("user trained projects found in PR DB.")
        return projects_to_import
    else:
        return False


def public_trained_projects(organisation_name):
    """
    :param organisation_name:
    :return:
    """
    manager = ProjectManager()
    query = {"$and": [{"organisation_name": organisation_name}, {"visibility": "public"}, {"ner.status": "trained"}, {"ir.status": "trained"},
                      {"masterBot": False}]}
    # query = {"$and": [{"visibility": "public"}, {"ner.status": "trained"}, {"ir.status": "trained"},
    # {"masterBot": False}]}
    projection = {"name": 1, "serviceid": 1}
    data = manager.exists(query)
    if data:
        projects_to_import = manager.find(query, projection)
        logger.info("public trained projects found in PR DB")
        return projects_to_import
    else:
        return False


@route('/api/parse/fetchprojecttoimport')
class FetchProjectToImport(object):
    @staticmethod
    def on_post(req, resp):
        logger.info(req.context)
        doc = req.context['doc'] or {}
        try:
            organisation_name = req.get_header('organisation-name', True)
            # user_id = doc['created_by']
            # assert user_id != ""
            public_projects = public_trained_projects(organisation_name)
            # user_projects = user_trained_projects(user_id)
            # user_projects = user_trained_projects(organisation_name)

        # except AssertionError as ae:
        #     logger.exception(ae.message, exc_info=True)
        #     logger.info(type(traceback.format_exc()))
        #     raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        # no need of exception because we already have an exception on req.get_header
        except Exception as ex:
            logger.exception(ex.message)
            raise falcon.HTTPServiceUnavailable('Service Outage', str(ex), 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200
        # resp.data = {"data": {"UserTrainedProjects": user_projects, "PublicTrainedProjects": public_projects}}
        resp.data = {"data": {"PublicTrainedProjects": public_projects}}
