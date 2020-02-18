import falcon
import logging
import os
import sys
import traceback
from datetime import datetime, timedelta

import requests

from ice_commons.config_settings import app_config
from ice_commons.data.dl.manager import ProjectManager

sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.normpath(os.getcwd() + os.sep + os.pardir))


logger = logging.getLogger(__name__)


def uncache_project_if_exists():
    '''
    uncache model if their last date of access more than X days.
    '''
    try:
        manager = ProjectManager()
        query = {}
        data = manager.find_all_model(query)
        for document in data:
            try:
                serviceid = document['serviceid']
                last_accessed = document['lastAccessed']
                days_diff = datetime.today() - timedelta(days=int(app_config['MINIO_DAYS']))
                ner_status = document['ner']['status']
                ir_status = document['ir']['status']

                if last_accessed < days_diff and ner_status in ['trained', 'validated'] and ir_status in ['trained',
                                                                                                          'validated']:
                    logger.info("removal process starts")
                    requests.post(url="http://localhost:8021/api/parse/cache/remove", json={'serviceid': serviceid},
                                  headers={'Content-type': 'application/json'})
                    logger.info("Model with service id: %s  is removed from minio cache since it was last accessed 90 "
                                "days back. Please retrain." % serviceid)

            except Exception as ex:
                logger.exception(ex, exc_info=True)
                logger.error(traceback.format_exc())
                description = 'Internal Server Error, Please try again later'
                raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)
    except Exception as ex:
        logger.exception(ex, exc_info=True)
        logger.error(traceback.format_exc())
        description = 'Internal Server Error, Please try again later'
        raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)


if __name__ == "__main__":
    logger.info("--- uncaching minio models script run --- ")
    uncache_project_if_exists()
