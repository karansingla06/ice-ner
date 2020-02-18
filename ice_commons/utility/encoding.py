import json

from bson.objectid import ObjectId
from datetime import datetime


class JSONEncoder(json.JSONEncoder):
    """

    """

    def default(self, o):
        """

        :param o:
        :return:
        """
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        return json.JSONEncoder.default(self, o)


def json_encode(data):
    return JSONEncoder().encode(data)


def jsonify(obj):
    from bson import json_util
    return json.dumps(obj, default=json_util.default)


def convert(config):
    """
    Converts a dict with unicode chars to ascii representation
    :param config:
    :return:
    """
    if isinstance(config, dict):
        return {convert(key): convert(value) for key, value in config.items()}
    elif isinstance(config, list):
        return [convert(element) for element in config]
    elif isinstance(config, str):
        return config.encode('utf-8')
    else:
        return config
