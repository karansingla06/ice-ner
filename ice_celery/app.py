

from ice_commons.store.models import ModelStore
from ice_commons.celery_jobs.config import get_app

model_store = ModelStore()
model_store.load_default_models_celery()
app = get_app()
if __name__ == '__main__':
    app.start()
