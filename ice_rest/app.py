from ice_rest.rest.appengine import AppEngine
from ice_commons.store.models import ModelStore

model_store = ModelStore()
model_store.load_default_models()
model_store.store.load_ngrams()
app = AppEngine().get_app()

