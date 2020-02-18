import datetime
import logging
import traceback

from pydash import get

from ice_commons.core.class_utils import create_instance
from ice_commons.core.model_utils import get_all_corenlp_engines
from ice_commons.data.dl.manager import ProjectManager, DatasourceManager
from ice_commons.store.base import VerbisStore
from ice_commons.utils import MODEL_TYPE_NER
from ice_commons.utils import token
from ice_commons.utility.logger import get_redis_handler, LogArrayHandler

class StreamingMixin(object):
    domain = 'verbis.streaming.notifications.model'

    @staticmethod
    def get_topic(serviceid, model_type):
        if serviceid is not None and model_type is not None:
            return StreamingMixin.domain + '.' + serviceid + '.' + model_type
        return StreamingMixin.domain


class TrainNERHelper(StreamingMixin):
    """

    """

    def __init__(self, serviceid):
        assert serviceid is not None, \
            "Invalid serviceid specified -> %s" % serviceid

        self.serviceid = serviceid
        self.logger = logging.getLogger(__name__)
        real_time_handler = get_redis_handler(self.get_topic(self.serviceid, 'ner'))
        self.logger.addHandler(real_time_handler)
        self.logger.addHandler(LogArrayHandler())

    def instantiate_trainer(self, custom_entity_model):
        serviceid = self.serviceid or token()
        entity_recognizer = create_instance(custom_entity_model, serviceid=serviceid)
        return entity_recognizer

    def train(self,train_intent):
        """
        :param doc:
        :param n_test_percent:
        :return:
        """
        manager = ProjectManager()
        query = {
            "serviceid": self.serviceid
        }
        config = manager.find_model(query)
        if config is not None:
            try:
                document = {
                    "$set": {
                        "ner.status": ProjectManager.STATUS_TRAINING,
                        "ner.status_message": "Entity training is in progress.",
                        "ner.last_trained": datetime.datetime.utcnow()}
                }
                if(train_intent is True):
                    document = {
                        "$set": {
                            "ner.status": ProjectManager.STATUS_TRAINING,
                            "ner.status_message": "Entity training is in progress.",
                            "ir.status": ProjectManager.STATUS_HOLD,
                            "ir.status_message": "Awaiting the completion of entity training.",
                            "ner.last_trained": datetime.datetime.utcnow()
                        }
                    }
                manager.update_config(query, document)

                # starting actual training
                data_manager = DatasourceManager()
                self.logger.info("Starting training of service %s" % self.serviceid)
                corpus = data_manager.find_model(query)
                custom_entity_model = get(config,"custom_entity_model")
                entity_recognizer = self.instantiate_trainer(custom_entity_model)
                trained_utterances = entity_recognizer.train(corpus)
                if entity_recognizer.get_engine() not in get_all_corenlp_engines():
                    VerbisStore().save_ner(entity_recognizer, model_type=MODEL_TYPE_NER)
                ###############MINIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO##################
                # send file to minio server
                VerbisStore().save_ner_minio(entity_recognizer, model_type=MODEL_TYPE_NER)
                document = {
                    "$set": {
                        "utterances": trained_utterances,
                   }
                }
                data_manager.update_datasource(query, document)

                document = {
                    "$set": {
                        "ner.status": ProjectManager.STATUS_TRAINED,
                        "ner.status_message": "Entity training completed successfully.",
                        "ner.logs.train":""
                    }
                }
                manager.update_config(query, document)

                self.logger.info("Completed training entity recognizer for service %s" % self.serviceid)
            except (RuntimeError, Exception) as ex:
                self.logger.exception(ex, exc_info=True)
                self.logger.error(traceback.format_exc())
                if ex== "Cannot have number of folds n_folds=3 greater than the number of samples: 2.":
                    ex = "Add more utterances for entity training"
                document = {
                    "$set": {
                        "ner.status": ProjectManager.STATUS_TRAINING_FAILED,
                        "ner.status_message": ex,
                        "ner.logs.train": self.logger.handlers[-1].logs
                    }
                }
                manager.update_config(query, document)
        else:
            description = 'Unable to find project_config with given id.' \
                          'Please check your request params and retry'
            self.logger.error(description)
