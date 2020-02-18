from ice_commons.celery_jobs.train.ir.train import DeployIRHelper
from ice_commons.celery_jobs.train.ner.train import TrainNERHelper

def train(serviceid, train_entity, train_intent):
    if train_entity is True:
        helper = TrainNERHelper(serviceid)
        helper.train(train_intent)
    if train_intent is True:
        helper = DeployIRHelper(serviceid)
        helper.deploy()
