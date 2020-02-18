from ice_commons.data.dl.manager import ProjectManager, DatasourceManager, ProjectconfigsManager
from bson.objectid import ObjectId


def validate_project_organisation(project_id, organisation_name):
    manager = ProjectManager()
    query = {"$and": [{"_id": ObjectId(project_id)}, {"organisation_name": organisation_name}]}
    if manager.exists(query):
        return True
    else:
        return False

