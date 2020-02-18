import falcon
import json
from falcon import HTTPBadRequest
from ice_rest.decorators import route, service
from ice_commons.data.dl.manager import PredefinedIntentManager, PatternPhraseManager, CustomEntityModelManager, PreTrainedEntityModelManager, IceEntitiesModelManager
import logging
import traceback
from ice_commons.utils import dict_contains
import pandas as pd
from ice_rest.rest.services.parse.impl.common.store_utils import get_model_store
from pydash import get


logger = logging.getLogger(__name__)


default_predefined_modelClass_dic = {"EN": "ice_commons.er.engines.spacy_ner.SpacyDefaultNER", "ES": "ice_commons.er.engines.spanish.spacy_ner.SpacySpanishDefaultNER"}
default_custom_modelClass_dic = {"EN": "ice_commons.er.engines.crf_ner.CRFCustomNER", "ES": "ice_commons.er.engines.spanish.mitie_ner.MitieSpanishCustomNER"}


def utterance_recase(utterances):
    store = get_model_store()
    utterances_updated = []
    for text in utterances:
        text, original_text = store.change_case(text)
        utterances_updated.append(text)

    return utterances_updated


@route('/api/parse/category/intent/add')
class CategoryIntentAddResource(object):

    def on_post(self,req,resp):
        category = req.get_param(name='category', required=True)
        data = req.get_param(name='file', required=True)

        try:
            df = pd.read_excel(io=data.file, header=None)
            df.dropna(inplace=True)
            utterances = list(df.iloc[:, 0])
            utterances_updated = utterance_recase(utterances)
            names = list(df.iloc[:, 1])
            logger.info(df.columns)
            if 2 not in df.columns:
                desc = [""]*len(utterances_updated)
            else:
                desc = list(df.iloc[:, 2])

            data = {}
            for i in range(len(names)):
                if names[i] in list(data.keys()):
                    data[names[i]][0].append(utterances_updated[i])
                else:
                    data[names[i]] = [[utterances_updated[i]], desc[i]]

            obj = PredefinedIntentManager()
            obj.add_intent_by_category(data, category)

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200




@route('/api/parse/category/intent/fetch')
class CategoryIntentFetchResource(object):
    def on_get(self, req, resp):
        category = req.get_param(name="category", default= None)
        try:
            obj= PredefinedIntentManager()
            if category is None:
                results = obj.get_all_intent()
            else:
                results = obj.get_intent_by_category(category)
            resp.data = results
        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200





@route('/api/parse/category/intent/remove')
class CategoryIntentRemoveResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['category']
        assert dict_contains(doc, mandatory_fields) is True, CategoryIntentRemoveResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req, resp):
        doc = req.context['doc']
        try:
            obj= PredefinedIntentManager()
            results = obj.remove_category(doc)
            resp.data = results

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)
        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200





@route('/api/parse/intent/add')
class IntentAddResource(object):
    def on_post(self, req,resp):
        category = req.get_param(name='category',required=True)
        name = req.get_param(name='name', required=True)
        desc = req.get_param(name='desc', required=True)
        utterance_file = req.get_param(name='file',required=True)

        try:
            df = pd.read_excel(io=utterance_file.file,header=None)
            df.dropna(inplace=True)
            utterances= list(df.iloc[:,0])
            doc = {}
            doc['categoryName']=category
            doc['intentName']=name
            doc['intentDesc']=desc
            utterances_updated = utterance_recase(utterances)
            doc['utterances'] = utterances_updated
            obj = PredefinedIntentManager()
            results = {"message": ""}
            if not obj.add_intent(doc):
                results['message'] = "A record with the same intent name exists under the %s category" % doc['categoryName']
                resp.status = falcon.HTTP_BAD_REQUEST
            else:
                results['message'] = "Added successfully"
                resp.status = falcon.HTTP_200
            resp.data = results


        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)
        resp = json.dumps({"msg": "Successfully Added"})
        resp.set_header('X-Powered-By', 'USTGlobal ICE')





@route('/api/parse/intent/update')
class IntentUpdateResource(object):
    def on_post(self, req, resp):
        append = req.get_param(name="append", required=True)
        category = req.get_param(name='category', required=True)
        name = req.get_param(name='name', required=True)
        desc = req.get_param(name='desc', required=True)
        utterance_file = req.get_param(name='file', required=True)

        try:
            df = pd.read_excel(io=utterance_file.file, header=None)
            df.dropna(inplace=True)
            utterances = list(df.iloc[:, 0])
            doc = {}
            doc['categoryName'] = category
            doc['intentName'] = name
            doc['intentDesc'] = desc
            utterances_updated = utterance_recase(utterances)
            doc['utterances'] = utterances_updated

            obj = PredefinedIntentManager()
            if append.lower()=="true":
                obj.update_intent(doc)
            else:
                obj.replace_intent(doc)

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200



@route('/api/parse/patternphrase/fetch')
class PatternPhraseFetchResource(object):
    @staticmethod
    def format_result(entity_list):
        result = []
        for entity_each in entity_list:
            entity = {"name": entity_each["name"], "entity": entity_each["entity"]}
            result.append(entity)
        return result

    def on_post(self, req, resp):
        doc = req.context['doc']
        language = get(doc, "language","EN")
        results = {}
        try:
            obj = PatternPhraseManager()
            if language is not None:
                patterns = self.format_result(obj.fetch_all_patterns_by_language(language))
                phrases = self.format_result(obj.fetch_all_phrases_by_language(language))
                results['patterns'] = patterns
                results['phrases'] = phrases
            else:
                raise Exception("Model Language not specified...")
            resp.data = results
        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200


@route('/api/parse/intent/fetch')
class IntentFetchResource(object):
    def on_get(self, req, resp):
        intent = req.get_param(name="name", default=None)
        try:
            obj= PredefinedIntentManager()
            if intent is None:
                results = obj.get_all_intent()
            else:
                results = obj.get_intent(intent)
            resp.data = results
        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200





@route('/api/parse/intent/remove')
class IntentRemoveResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['name']
        assert dict_contains(doc, mandatory_fields) is True, IntentRemoveResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req, resp):
        doc = req.context['doc']
        try:
            obj= PredefinedIntentManager()
            results = obj.remove_intent(doc)
            resp.data = results

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)
        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200




@route('/api/parse/pattern/add')
class PatternAddResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['name','value']
        assert dict_contains(doc, mandatory_fields) is True, PatternAddResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req,resp):
        doc = req.context['doc']

        try:
            obj = PatternPhraseManager()
            results = {"message":""}
            if not obj.add_pattern(doc):
                results['message'] = "A record with the same name exists in the database"
                resp.status = falcon.HTTP_BAD_REQUEST

            else:
                results['message'] = "Added successfully"
                resp.status = falcon.HTTP_200

            resp.data = results

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)
        resp.set_header('X-Powered-By', 'USTGlobal ICE')




@route('/api/parse/pattern/fetch')
class PatternFetchResource(object):
    def on_get(self, req,resp):
        pattern = req.get_param(name="name", default=None)
        try:
            obj = PatternPhraseManager()
            if pattern is None:
                results = obj.get_all_patterns()
            else:
                results = obj.get_pattern(pattern)
            resp.data = results

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200




@route('/api/parse/pattern/update')
class PatternUpdateResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['name', 'value']
        assert dict_contains(doc, mandatory_fields) is True, PatternUpdateResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req,resp):
        doc = req.context['doc']
        try:
            obj = PatternPhraseManager()
            obj.update_pattern(doc)

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200





@route('/api/parse/pattern/remove')
class PatternRemoveResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['name']
        assert dict_contains(doc, mandatory_fields) is True, PatternRemoveResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req,resp):
        doc = req.context['doc']
        try:
            obj = PatternPhraseManager()
            obj.remove_pattern(doc)

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200






@route('/api/parse/phrase/add')
class PhraseAddResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = [ 'name', 'value']
        assert dict_contains(doc, mandatory_fields) is True, PhraseAddResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req,resp):
        doc = req.context['doc']
        try:
            obj= PatternPhraseManager()
            results = {"message":""}
            if not obj.add_phrase(doc):
                results['message'] = "A record with the same name exists in the database"
                resp.status = falcon.HTTP_BAD_REQUEST

            else:
                results['message'] = "Added successfully"
                resp.status = falcon.HTTP_200
            resp.data = results

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)
        resp.set_header('X-Powered-By', 'USTGlobal ICE')





@route('/api/parse/phrase/fetch')
class PhraseFetchResource(object):

    def on_get(self, req,resp):
        phrase = req.get_param(name="name", default=None)
        try:
            obj = PatternPhraseManager()
            if phrase is None:
                results = obj.get_all_phrases()
            else:
                results = obj.get_phrase(phrase)
            resp.data = results


        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200





@route('/api/parse/phrase/update')
class PhraseUpdateResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['name', 'value']
        assert dict_contains(doc, mandatory_fields) is True, PhraseUpdateResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req,resp):
        doc = req.context['doc']
        try:
            obj = PatternPhraseManager()
            obj.update_phrase(doc)

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200



@route('/api/parse/phrase/remove')
class PhraseRemoveResource(object):
    @staticmethod
    def _bad_request():
        description = 'Mandatory params missing from the request. ' \
                      'Please check your request params and retry'
        logger.exception(description)
        raise HTTPBadRequest("HTTP Bad Request", description)

    def _validate_model_config(req, resp, resource, params):
        doc = req.context['doc']
        mandatory_fields = ['name']
        assert dict_contains(doc, mandatory_fields) is True, PhraseRemoveResource._bad_request()

    @falcon.before(_validate_model_config)
    def on_post(self, req,resp):
        doc = req.context['doc']
        try:
            obj= PatternPhraseManager()
            obj.remove_phrase(doc)

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200



def group_entities(ice_entity_config, predefined_entity_mappings):
    ice_categories = {}
    for i in ice_entity_config:
        if i['category'] not in list(ice_categories.keys()):
            if i['category'] is not None:
                ice_categories[i['category']] = {'categoryDescription': i['categoryDescription'], 'entities': [{'name': i['name'], 'description': i['description']}]}
            else:
                ice_categories[i['name']] = {'categoryDescription': i['description'], 'entities': []}
        else:
            ice_categories[i['category']]['entities'].append({'name': i['name'], 'description': i['description']})

    for map in predefined_entity_mappings:
        default_entities_map = map['entities']
        entities = []
        if len(ice_categories)!=0:
            for category in list(ice_categories.keys()):
                sub_entities_list = ice_categories[category]['entities']
                group = {'name': category, 'description' : ice_categories[category]['categoryDescription'] ,'sub_entities': sub_entities_list}
                entities.append(group)

        for default_entity in default_entities_map:
            group = {'name': default_entity['name'], 'description': default_entity['description'], 'sub_entities': []}
            entities.append(group)
        map['entities'] = entities

    return predefined_entity_mappings


@route('/api/parse/entity_models')
class EntityModelResource(object):
    def on_post(self, req, resp):
        try:
            doc = req.context['doc']
            language = "EN"
            if dict_contains(doc, 'language'):
                language= doc['language']
            ice_entity_config = IceEntitiesModelManager().get_ice_entities(language)
            predefined_entity_mappings = PreTrainedEntityModelManager().get_entity_models(language)
            predefined_entity_models = group_entities(ice_entity_config, predefined_entity_mappings)
            results = {"predefined_entity_models": predefined_entity_models,
                       "custom_entity_models": CustomEntityModelManager().get_entity_models(language),
                       "default_predefined_modelClass": default_predefined_modelClass_dic[language],
                       "default_custom_modelClass": default_custom_modelClass_dic[language]}
            resp.data = results

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200



@route('/api/parse/entity_models/entities')
class EntityModelResource(object):
    def on_post(self, req, resp):
        name = req.get_param(name="name", required=True)
        language = req.get_param(name="language", default="EN")
        try:
            obj = PreTrainedEntityModelManager()
            query = {"name": name, "language": language.upper()}
            results = obj.get_entity(query)
            resp.data = results

        except AssertionError as ae:
            logger.exception(ae, exc_info=True)
            logger.error(traceback.format_exc())
            raise falcon.HTTPPreconditionFailed('Service publish condition failed', traceback.format_exc())

        except Exception as ex:
            logger.exception(ex, exc_info=True)
            description = 'Internal Server Error, Please try again later'
            raise falcon.HTTPServiceUnavailable('Service Outage', description, 30)

        resp.set_header('X-Powered-By', 'USTGlobal ICE')
        resp.status = falcon.HTTP_200
