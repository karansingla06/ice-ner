import logging
import traceback
import os

import falcon
from ice_rest.decorators import route
from ice_rest.rest.services.parse.validate_project_org import validate_project_organisation
from ice_commons.data.dl.manager import DatasourceManager, ProjectconfigsManager
from bson.objectid import ObjectId

home_dir = os.path.expanduser('~')

logger = logging.getLogger(__name__)

def get_datasource_id(project_id):
    """
    :param project_id:
    :return:
    """
    config_manager = ProjectconfigsManager()
    logger.info(project_id)
    query = {"$and": [{"project": ObjectId(project_id)}]}
    logger.info(config_manager.find_one(query))
    return config_manager.find_one(query)


def get_datasource(project_id):
    """
    :param project_id:
    :return:
    """
    manager = DatasourceManager()
    query = {"_id": get_datasource_id(project_id)['datasource']}
    projection = {"_id": 0, "serviceid": 1, "utterances": 1, "entities": 1, "intents": 1, "patterns": 1,
                  "phrases": 1, "synonyms": 1}
    return manager.find(query, projection)


@route('/api/parse/getDataSourceConfig')
class GetDataSourceConfig(object):
    @staticmethod
    def on_post(req, resp):
        logger.info(req.context)
        doc = req.context['doc'] or {}
        data_dict = {}
        organisation_name = req.get_header('organisation-name', True)
        try:
            count = 0
            for item in doc.values():
                if validate_project_organisation(item, organisation_name):
                    data_dict["import" + str(count)] = [{"datasource": get_datasource(item)[0]}]
                    count += 1
                else:
                    data_dict["import" + str(count)] = [{"datasource": "given Project Id is not "
                                                                       "mapped to organisation_id"}]
                    count += 1
        except AssertionError as ae:
            logger.exception(ae.message, exc_info=True)
            logger.info(type(traceback.format_exc()))
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex.message)
            raise falcon.HTTPServiceUnavailable('Service Outage', str(ex), 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200
        resp.data = {"data": data_dict}
