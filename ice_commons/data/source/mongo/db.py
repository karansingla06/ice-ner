import logging

from bson.json_util import dumps, loads
from pymongo import MongoClient
from pymongo.errors import InvalidURI, ConnectionFailure, ServerSelectionTimeoutError
from pymongo.uri_parser import parse_uri


class Mongo(object):
    def __init__(self, uri=None, default_db=None, default_collection=None, logger=None):

        """
        :param uri:
        :param default_db:
        :param default_collection:
        :param logger:
        """
        self.logger = logger or logging.getLogger(__name__)
        try:
            if uri:
                parse_uri(uri, validate=True)
            self.db = default_db
            self.collection = default_collection
            self.connection = MongoClient(uri)
        except InvalidURI:
            self.logger.error("Invalid MongoDB URI: %s" % uri, exc_info=True)
            raise InvalidURI
        except ServerSelectionTimeoutError as e:
            self.logger.error("Connection refused to MongoDB with URI: %s" % uri, exc_info=True)
            raise e
        except ConnectionFailure as e:
            self.logger.error("Connection failed to MongoDB with URI: %s" % uri, exc_info=True)
            raise e

    def get_db(self, db=None):
        """
        :param db:
        :return:
        """
        db = db if db else self.db
       # self.logger.info("Accessing db: ", extra={
       #     'db': db
       # })
        if db:
            return self.connection[db]
        else:
            return None

    def get_collection(self, db=None, collection=None):
        """
        :param db:
        :param collection:
        :return:
        """
        database = self.get_db(db)
        collection = collection if collection else self.collection
      #  self.logger.info("Accessing collection", extra={
       #     'collection': collection
       # })
        if database and collection:
            return database[collection]
        else:
            return None

    def _fix_query_operator(self, query):
        """
        :param query:
        :return:
        """
       # self.logger.info("transforming json query to mongodb query object")
       # self.logger.debug(query)
        try:
            str_json = dumps(query)
            str_json = str_json.replace("__$", "$")
            transformed_query = loads(str_json)
            self.logger.debug("transformed query: ")
            self.logger.debug(transformed_query)
            return transformed_query
        except ValueError as ve:
            self.logger.error("Invalid JSON: %s" % str_json, exc_info=True)
            raise ve

    def find(self, db_filter, projection=None, db=None, collection=None):
        """
        :param db_filter:
        :param db:
        :param collection:
        :return:
        """

      #  self.logger.info("executing db.find", extra={
      #      'db_filter': db_filter,
      #      'db': db,
       #     'collection': collection
       # })

        collection = self.get_collection(db=db, collection=collection)
        db_filter = self._fix_query_operator(db_filter)
        return collection.find(db_filter, projection)

    def find_one(self, db_filter, db=None, collection=None):
        """
        :param db_filter:
        :param db:
        :param collection:
        :return:
        """
      #  self.logger.info("executing db.find_one", extra={
      #      'db_filter': db_filter,
       #     'db': db,
       #     'collection': collection
       # })
        collection = self.get_collection(db=db, collection=collection)
        db_filter = self._fix_query_operator(db_filter)
        return collection.find_one(db_filter)
