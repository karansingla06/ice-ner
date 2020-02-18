from celery import Celery
from ice_commons.config_settings import app_config

redis_url = app_config['REDIS_END_POINT']
app = Celery('train',
             broker=redis_url,
             backend=redis_url,
             include=['ice_commons.celery_jobs.train.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=60 * 60 * 24,
)


def get_app():
    return app