from ice_commons.celery_jobs.train import tasks

def test_train_parse_with_null(mocker):
      mocker.patch('ice_commons.celery_jobs.train.tasks.train',return_value=None)
      exp = tasks.train_parse(None,None,None)
      assert exp == None