import cachetools
model_cache=cachetools.LRUCache(maxsize=20)
default_models_cache={}
cached_ts_map = {}

def get_registered_ids():
    return list(model_cache.keys()) + list(default_models_cache.keys())

def get_model(model_name):
    if model_name in list(model_cache.keys()):
        return model_cache[model_name]
    elif model_name in list(default_models_cache.keys()):
        return default_models_cache[model_name]
    return None

def put_model(model_name,model):
    if("NGRAM" in model_name or 'DEFAULT' in model_name):
        default_models_cache[model_name] = model
    else:
        model_cache[model_name] = model

def unpublish(model_name):
    del model_cache[model_name]

