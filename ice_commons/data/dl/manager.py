import datetime
import logging

from bson.objectid import ObjectId

from ice_commons.data.source.mongo import DocumentManager

from ice_commons.config_settings import app_config

DB = app_config['MONGO_DB_NAME']
URI = app_config['MONGO_END_POINT']

logger = logging.getLogger(__name__)

class ProjectconfigsManager(DocumentManager):
    def __init__(self):
        super(ProjectconfigsManager, self).__init__(db=DB,document="projectconfigs",uri=URI)

    def update_config_by_service_id(self, serviceid, document):
        """
        :param _id:
        :param document:
        :return:
        """
        query = {"serviceid": serviceid}
        self.update(query, document)


class ProjectManager(DocumentManager):
    STATUS_NEW = "new"
    STATUS_HOLD = "pending"
    STATUS_TRAINING = "training"
    STATUS_TRAINING_FAILED = "training_failed"
    STATUS_TRAINED = "trained"
    STATUS_VALIDATING = "validating"
    STATUS_VALIDATED = "validated"

    STATUS_PUBLISHING = "publishing"
    STATUS_PUBLISH_FAILED = "publish_failed"
    STATUS_PUBLISHED = "published"

    def __init__(self):
        super(ProjectManager, self).__init__(db=DB, document="projects",uri=URI)

    def save_config(self, document):
        """

        :param document:
        :return:
        """
        document.update(created_at=datetime.datetime.utcnow())
        document.update(updated_at=datetime.datetime.utcnow())
        return self.insert(document)

    def update_config(self, query, document, options={}):
        """

        :param query:
        :param document:
        :param options:
        :return:
        """
        assert type(options) == dict, "Invalid options for model config update %s" % str(options)
        self.update(query, document, **options)

    def exists(self, query):
        result = self.find_one(query)
        return True if result is not None else False

    def find_config_by_id(self, serviceid):
        """

        :param serviceid:
        :return:
        """
        query = {"serviceid": {"$in": [serviceid]}}
        logger.debug(query)
        return self.find_one(query)

    def find_all_model(self, query={}):
        """

        :param query:
        :return:
        """

        return self.find(query)

    def find_model(self, query):
        """

        :param query:
        :return:
        """

        return self.find_one(query)

    def delete_model(self, query):
        """

        :param query:
        :return:
        """

        return self.delete(query)

    def get_models_by_status(self, status):
        query = [
            {"$or": [{"ner.status": status}, {"ir.status": status}]},
            {"serviceid": 1, "engine": 1, "ner.status": 1, "ir.status": 1, "_id": 0}
        ]
        return self.find(query)

    def update_ir_ner_status(self, serviceid, ner_status, ir_status):
        query= {'serviceid' : serviceid}
        return self.update(query,{"$set":{"ner.status":ner_status,"ir.status":ir_status}})

    def get_model_language(self, serviceid):
        query = { "serviceid" : serviceid}
        return self.find_one(query)

    def update_entity_model_ice_commons(self, serviceid, predefined_entity_model, custom_entity_model):
        query= {'serviceid' : serviceid}
        self.update(query,{"$set":{"predefined_entity_model": predefined_entity_model,"custom_entity_model" : custom_entity_model}})





class DatasourceManager(DocumentManager):
    def __init__(self):
        super(DatasourceManager, self).__init__(db=DB, document="datasources",uri=URI)

    def save_datasource(self, document):
        """

        :param document:
        :return:
        """
        document.update(createdAt=datetime.datetime.utcnow())
        document.update(updatedAt=datetime.datetime.utcnow())
        return self.insert(document)

    def find_config_by_id(self, datasource_id):
        """

        :param datasource_id:
        :return:
        """
        query = {"_id": ObjectId(datasource_id)}
        return self.find_one(query)

    def exists(self, query):
        result = self.find_one(query)
        return True if result is not None else False

    def find_all_model(self, query={}):
        """

        :param query:
        :return:
        """

        return self.find(query)

    def find_model(self, query):
        """

        :param query:
        :return:
        """

        return self.find_one(query)

    def delete_model(self, query):
        """

        :param query:
        :return:
        """

        return self.delete(query)

    def update_datasource(self, db_filter, document, **kwrgs):
        """

        :param db_filter:
        :param document:
        :return:
        """
        # document["$set"]["updatedAt"] = datetime.datetime.utcnow()
        self.update(db_filter, document, **kwrgs)

    def update_datasource_by_id(self, _id, document):
        """

        :param _id:
        :param document:
        :return:
        """
        document["$set"]["updatedAt"] = datetime.datetime.utcnow()
        query = {"_id": ObjectId(_id)}


    def update_datasource_by_service_id(self, serviceid, document):
        """
        :param _id:
        :param document:
        :return:
        """
        query = {"serviceid": serviceid}
        self.update(query, document)

    def find_datasource_by_service_id(self, serviceid):
        """
        :param _id:
        :param document:
        :return:
        """
        query = {"serviceid": serviceid}
        return self.find_one(query)


    def encrypt_missed_utterances(self,serviceid, encrypted_utterances):
        query= {'serviceid':serviceid}
        return self.update(query,{"$set":{'missedUtterances': encrypted_utterances}})

    def remove_missed_utterance(self,serviceid, utterance):
        query= { "serviceid" : serviceid}
        return self.update(query, {"$pull":{"missedUtterances" : utterance}})

    def upload_synonyms(self, serviceid, synonyms_dic= {}):
        query = {"serviceid": serviceid}
        return self.update(query, {"$set":{"synonymMappings": [{word: synonyms} for word, synonyms in list(synonyms_dic.items())] }})

    def update_datasource(self,serviceid,document):       
        query= {'serviceid':serviceid} 
        #document.update(updatedAt=datetime.datetime.utcnow())       
        return self.update(query,document)




class TestDataManager(DocumentManager):
    def __init__(self):
        super(TestDataManager, self).__init__(db=DB,document="testdatas",uri=URI)

    def update_config_by_service_id(self, serviceid, document):
        """
        :param _id:
        :param document:
        :return:
        """
        query = {"serviceid": serviceid}
        self.update(query, document)


    def fetch_by_serviceid(self, serviceid):
        query = {"serviceid": serviceid}
        return self.find_one(query)



class TestRunsManager(DocumentManager):
    def __init__(self):
        super(TestRunsManager, self).__init__(db=DB,document="testruns",uri=URI)

    def not_exists(self, query):
        result = self.find_one(query)
        return False if result is not None else True

    def fetch_timestamps(self, serviceid):
        query = {"serviceid": serviceid}
        config = self.find(query= query, projection= {"runs.run_time": 1, "_id":0})
        if len(config)!=0:
            return config[0]

    def fetch_all_reports(self, serviceid):
        query= {"serviceid" : serviceid}
        return self.find_one(query)

    def remove_older_reports(self, report_doc, test_run_doc):
        reports = report_doc['runs']
        len_reports = len(reports)
        if len_reports<=4:
            reports.append(test_run_doc)
            return reports
        else:
            reports.append(test_run_doc)
            newlist = sorted(reports, key=lambda k: k['run_time'], reverse= True)
            return newlist[0:5]


    def update_config_by_service_id(self, serviceid, test_run_doc):
        """
        :param _id:
        :param document:
        :return:
        """
        query = {"serviceid": serviceid}
        if self.not_exists(query):
            document = {
                    "serviceid" : serviceid,
                    "runs": [test_run_doc]
                }
            self.insert(document)
        else:
            report_doc = self.fetch_all_reports(serviceid)
            updated_report = self.remove_older_reports(report_doc, test_run_doc)
            document= {
                "$set" : {"runs" : updated_report}
            }
            self.update(query, document)



class PatternPhraseManager(DocumentManager):
    def __init__(self):
        super(PatternPhraseManager, self).__init__(db=DB, document="patternphrase",uri=URI)

    def get_pattern(self,pattern):
        query = {"type": "pattern",  "name": pattern}
        return self.find(query=query,projection= {"_id":0})

    def get_phrase(self,phrase):
        query = {"type": "phrase",  "name": phrase}
        return self.find(query=query, projection={"_id":0})

    def not_exists(self, query):
        result = self.find_one(query)
        logger.info(result)
        return False if result is not None else True

    def add_pattern(self,doc):

        doc.update(created_at=datetime.datetime.utcnow())
        doc.update(updated_at=datetime.datetime.utcnow())
        doc.update(type="pattern")
        query = {"type": "pattern", "name": doc["name"]}
        if self.not_exists(query):
            self.insert(doc)
            return True
        else:
            return False

    def add_phrase(self,doc):

        doc.update(created_at=datetime.datetime.utcnow())
        doc.update(updated_at=datetime.datetime.utcnow())
        doc.update(type="phrase")
        query = {"type": "phrase", "name": doc["name"]}
        if self.not_exists(query):
            self.insert(doc)
            return True
        else:
            return False

    def update_pattern(self, doc):

        query= {"type": "pattern", "name": doc["name"]}
        document = {
            "$set": {
                "value": doc["value"], "updated_at": datetime.datetime.utcnow(),
            }
        }
        return self.update(query,document)

    def update_phrase(self, doc):
        query = {"type": "phrase", "name": doc["name"]}
        document = {
            "$set": {
                "value": doc["value"], "updated_at": datetime.datetime.utcnow(),
            }
        }
        return self.update(query, document)

    def remove_pattern(self,doc):
        query= {"type":"pattern", "name":doc["name"]}
        return self.delete(query)

    def remove_phrase(self,doc):
        query= {"type":"phrase", "name":doc["name"]}
        return self.delete(query)

    def get_all_patterns(self):
        query = {'type': 'pattern'}
        return self.find(query=query, projection={"_id":0})

    def get_all_phrases(self):
        query = {'type': 'phrase'}
        return self.find(query=query, projection={"_id":0})

    def fetch_all_patterns_by_language(self, lang):
        query = {"language": lang, "type": "pattern"}
        return self.find(query=query, projection={"_id": 0})

    def fetch_all_phrases_by_language(self, lang):
        query = {"language": lang, "type": "phrase"}
        return self.find(query=query, projection={"_id": 0})



class PredefinedIntentManager(DocumentManager):
    def __init__(self):
        super(PredefinedIntentManager, self).__init__(db=DB, document="predefinedintents",uri=URI)

    def not_exists(self, query):

        result = self.find_one(query)
        return False if result is not None else True

    def add_intent(self, doc):
        query = {"categoryName": doc["categoryName"], "intents.name":  doc["intentName"]}

        if self.not_exists(query):
            query2 = {"categoryName": doc["categoryName"]}

            if self.not_exists(query2):
                document = {
                    "categoryName": doc["categoryName"],
                    "categoryDesc": "",
                    "intents": [{"name": doc["intentName"], "utterances":[i for i in doc['utterances']] ,
                                 "desc": doc["intentDesc"], "createdAt": datetime.datetime.utcnow()}],
                    "createdAt": datetime.datetime.utcnow(),
                    "modifiedAt": datetime.datetime.utcnow()
                }
                self.insert(document)
            else:
                document = {
                    "$push": {"intents": {"name": doc['intentName'],
                                           "utterances": [i for i in doc['utterances']],
                                           "desc": doc["intentDesc"],
                                           "createdAt": datetime.datetime.utcnow()}}}
                self.update(query2, document)
            return True
        else:
            return False

    def add_intent_by_category(self, data, category):
        document = {
            "categoryName": category,
            "categoryDesc":"",
            "intents": [{"name": name, "utterances": listOfList[0],"desc": listOfList[1],"createdAt": datetime.datetime.utcnow()
                         } for name, listOfList in list(data.items())],
            "createdAt": datetime.datetime.utcnow(),
            "modifiedAt": datetime.datetime.utcnow()
        }
        self.insert(document)


    def get_intent(self, name):
        query = {"intents.name": name}
        return self.find(query=query, projection={"_id":0, "intents": {"$elemMatch": {"name": name}}})

    def get_intent_by_category(self, category):
        query = {"categoryName": category}
        return self.find(query=query, projection={"_id":0})

    def get_all_intent(self):
        return self.find(query={}, projection={"_id":0})

    def update_intent(self, doc):
        query = {"categoryName": doc["categoryName"], "intents.name": doc["intentName"]}
        return self.update(query, { "$addToSet":  { "intents.$.utterances": {"$each" : doc['utterances']}}})

    def replace_intent(self,doc):
        query = {"categoryName": doc["categoryName"], "intents.name": doc["intentName"]}
        return self.update(query, {"$set": {"intents.$.utterances" : doc['utterances']}})

    def add_language(self, language):
        return self.update({}, { "$set": {"language": language} }, multi=True)

    def remove_intent(self,doc):
        return self.update({"categoryName": doc["category"]},{"$pull":{"intents":{"name": doc["name"]}}})

    def remove_category(self,doc):
        return self.delete_many(query={"categoryName": doc["category"]})


class PreTrainedEntityModelManager(DocumentManager):
    def __init__(self):
        super(PreTrainedEntityModelManager, self).__init__(db=DB, document="pretrainedentitymodels",uri=URI)

    def get_entity_models(self, language):
        query = {"language": language}
        return self.find(query=query, projection={"_id": 0})

    def get_entity(self, query={}):
        entities = self.find(query=query, projection={"entities": 1, "_id": 0})
        if len(entities) != 0:
            return entities[0]['entities']
        else:
            return {"message":"Entities not found for the given input"}


class CustomEntityModelManager(DocumentManager):
    def __init__(self):
        super(CustomEntityModelManager, self).__init__(db=DB, document="customentitymodels",uri=URI)

    def get_entity_models(self, language):
        query = {"language": language}
        return self.find(query=query, projection={"_id": 0})


class IceEntitiesModelManager(DocumentManager):
    def __init__(self):
        super(IceEntitiesModelManager, self).__init__(db=DB, document="ice_entities", uri=URI)

    def get_ice_entities(self, language):
        return self.find(query={'language': language},projection={"_id": 0})

    def add_ice_entities(self,entity):
        return self.insert(entity)