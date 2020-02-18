
from ice_commons.celery_jobs.train import train_impl


def test_train_intrainimpl_with_null(mocker):
      mocker.patch('ice_commons.celery_jobs.train.train_impl.TrainNERHelper.train',return_value=None)
      mocker.patch('ice_commons.celery_jobs.train.train_impl.DeployIRHelper.deploy',return_value=None)
      exp = train_impl.train(None,None,None)
      assert exp == None
      
def test_train_intrainimpl_with_train_entity_true(mocker):
      mocker.patch('ice_commons.celery_jobs.train.train_impl.TrainNERHelper.train',return_value=None)
      mocker.patch('ice_commons.celery_jobs.train.train_impl.DeployIRHelper.deploy',return_value=None)
      serviceid=None
      if(serviceid!=None):
            exp = train_impl.train(serviceid,False,True)
      else:
            exp = train_impl.train("",False,True)
      assert exp == None
def test_train_intrainimpl_with_train_intent_true(mocker):
      mocker.patch('ice_commons.celery_jobs.train.train_impl.TrainNERHelper.train',return_value=None)
      mocker.patch('ice_commons.celery_jobs.train.train_impl.DeployIRHelper.deploy',return_value=None)
      serviceid=None
      if(serviceid!=None):
            exp = train_impl.train(serviceid,False,True)
      else:
            exp = train_impl.train("",False,True)
      assert exp == None
def test_train_intrainimpl_with_all_true(mocker):
      mocker.patch('ice_commons.celery_jobs.train.train_impl.TrainNERHelper.train',return_value=None)
      mocker.patch('ice_commons.celery_jobs.train.train_impl.DeployIRHelper.deploy',return_value=None)
      exp = train_impl.train("xyz",True,True)
      assert exp == None