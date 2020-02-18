import traceback

from celery import Task
from celery.utils.log import get_task_logger

from ice_commons.celery_jobs.config import get_app
from ice_commons.celery_jobs.validate.validate_impl import validate
from ice_commons.celery_jobs.train.train_impl import train
from ice_commons.utils import now

logger = get_task_logger(__name__)

app = get_app()


class LogErrorsTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(('{0!r} failed: {1!r}'.format(task_id, exc)))
        self.save_failed_task(exc, task_id, args, kwargs, einfo)

    def save_failed_task(self, exc, task_id, args, kwargs, traceback):
        """
        :type exc: Exception
        """

        celery_task_id = task_id
        full_name = self.name
        name = self.name.split('.')[-1]
        exception_class = exc.__class__.__name__
        exception_msg = str(exc).strip()
        traceback = str(traceback).strip()
        updated_at = now()

        print(name)
        print(exception_msg)
        print(args[0])
        print(kwargs)


@app.task(base=LogErrorsTask)
def train_parse(serviceid, train_entity, train_intent):
    try:
        train(serviceid, train_entity, train_intent)
        print("Hiiii")
    except RuntimeError as e:
        logger.exception(e, exc_info=True)
        logger.error(traceback.format_exc())


@app.task(base=LogErrorsTask)
def validate_test_data(serviceid, predict_url):
    try:
        validate(serviceid, predict_url)

    except RuntimeError as e:
        logger.exception(e, exc_info=True)
        logger.error(traceback.format_exc())
