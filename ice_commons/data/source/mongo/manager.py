import logging

from ice_commons.data.source.mongo import Mongo


class DocumentManager(object):
    def __init__(self, db, document, uri=None, logger=None):
        """
        :param db:
        :param document:
        :param uri:
        :param logger:
        """
        self.logger = logger or logging.getLogger(__name__)
        self.connector = Mongo(uri=uri, default_db=db, default_collection=document)
       # self.logger.info("Initializing DocumentManager", extra={
       #     'uri': uri,
       #     'default_db': db,
       #     'default_collection': document
       # })

    def insert(self, document):
       # self.logger.info("inserting to collection", extra={
       #     'document': document
       # })
        collection = self.connector.get_collection()
        if collection:
            result = collection.insert_one(document)
            return result

    def batch_insert(self, documents):
      #  self.logger.info("batch insertion on collection ", extra={
      #      'documents': documents
      #  })
       # self.logger.debug(documents)
        collection = self.connector.get_collection()
        if collection:
            results = collection.insert_many(documents)
            return results

    def update(self, query, document, **options):
       # self.logger.info("updating collection", extra={
        #    'query': query,
       #     'document': document
       # })
        collection = self.connector.get_collection()
        if collection:
            collection.update(query, document, **options)

    def delete(self, query):
      #  self.logger.info("deleting from collection", extra={
       #     'query': query
       # })
        collection = self.connector.get_collection()
        if collection:
            collection.delete_one(query)

    def delete_many(self, query):
        #  self.logger.info("deleting from collection", extra={
        #     'query': query
        # })
        collection = self.connector.get_collection()
        if collection:
            collection.delete_many(query)

    def drop(self):
        #self.logger.info("dropping collection")
        collection = self.connector.get_collection()
        if collection:
            collection.drop()

    def find(self, query, projection=None):
      #  self.logger.info("finding from collection", extra={
      #      'query': query
       # })
        return list(self.connector.find(query, projection))

    def aggregate(self, query):
      #  self.logger.info("finding from collection", extra={
      #      'query': query
      #  })
        return list(self.collection.aggregate(query))

    def find_one(self, query):
      #  self.logger.info("finding one from collection", extra={
      #      'query': query
      #  })
        return self.connector.find_one(query)
