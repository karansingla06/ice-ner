from properties.p import Property
import os
import json


class Commons(object):

    @staticmethod
    def parsejson(jsonobj, name=None):
        body = json.loads(json.dumps(jsonobj))
        if name in body:
            return body[name]
        else:
            return None

    @staticmethod
    def parserequest(jsonobj):
        body = json.loads(json.dumps(jsonobj))
        return body