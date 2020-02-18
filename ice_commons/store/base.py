import pickle as pickle
import logging
import os
import shutil
from os.path import basename
import datetime
import dateutil.parser
import urllib3
from ice_commons.core.class_utils import create_instance
from ice_commons.core.model_utils import get_all_corenlp_engines
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists, NoSuchKey, InvalidAccessKeyId, InvalidSecurity)

from ice_commons.config_settings import app_config
from ice_commons.core.project_utils import get_corenlp_modelname
from ice_commons.patterns.singleton import Borg
from ice_commons.utils import (make_dir, get_model_name, MODEL_TYPE_NER,
                               MODEL_TYPE_IR, remove_dir, get_file_name)
from ice_commons.utils import timeit
import ice_commons.app_cache as app_cache
from ice_commons.utils import get_file_name
import threading

http_client = urllib3.PoolManager(timeout=60, maxsize=10, retries=urllib3.Retry(total=5, backoff_factor=0.2,
                                                                                status_forcelist=[500, 502, 503, 504]))
minio_secure = True if int(app_config['MINIO_SECURE']) else False
minio_client = Minio(str(app_config['MINIO_END_POINT']),access_key= str(app_config['MINIO_ACCESS_KEY']),secret_key= str(app_config['MINIO_SECRET_KEY']),
                     secure=minio_secure, http_client=http_client)

#print(minio_client.list_buckets())
class VerbisStore(Borg):
    _lock = threading.Lock()

    def __init__(self):
        """

        :param root:
        :return:
        """
        self.logger = logging.getLogger(__name__)

        self.logger.info("Inside VerbisStore: Init")
        # self.models = dict()
        self.root = self.__get_default_root()
        self.logger.info("VerbisStore: root dir %s" % self.root)
        # make_dir(self.root)
        self.minio_client = minio_client  # Minio(MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_SECURE)

    def __get__file_paths(self, serviceid, file_name):
        """

        :param serviceid:
        :param model_type:
        :return:
        """

        root_dir = os.path.join(self.root, serviceid)
        abs_file_name = os.path.join(root_dir, file_name)

        return root_dir, abs_file_name

    @staticmethod
    def __get_default_root():
        """

        :return:
        """
        user_dir = os.path.expanduser('~')
        default_root = os.path.join(user_dir, '.verbis', 'store')
        return default_root

    # @timeit
    def put(self, model, serviceid=None, model_type=None, engine=None):
        """

        :param model:
        :param serviceid:
        :param model_type:
        :param engine:
        :return:
        """
        if model_type is None and serviceid is None:
            raise AssertionError("Either model_id or model type should be specified for put action")
        self.logger.info("Loading model with id: %s & type: %s" % (serviceid, model_type))
        model_id = basename(get_model_name(serviceid, model_type, engine))
        app_cache.put_model(model_id, model)
        self.logger.info(app_cache.get_registered_ids())

    @timeit
    def publish(self, serviceid, model_type, engine=None, class_name=None):
        """

        :param serviceid:
        :param name:
        :return:
        """
        try:
            self.logger.info("Loading model with id: %s & type: %s & engine: %s and class_name: %s" % (
                serviceid, model_type, engine, class_name))
            model = self.load(serviceid, model_type, engine, class_name)
            assert model is not None, "Unable to load model with id %s and type %s" % (serviceid, model_type)
            self.put(model, serviceid, model_type, engine)
        except AssertionError:
            msg = "Unable to load model with id %s and type %s" % (serviceid, model_type)
            self.logger.warn(msg)

    @timeit
    def unpublish(self, serviceid, model_type, engine=None):
        """

        :param serviceid:
        :param model_type:
        :param engine:
        :return:
        """
        self.logger.info("Loading model with id: %s & type: %s" % (serviceid, model_type))
        model_id = basename(get_model_name(serviceid, model_type, engine))
        app_cache.unpublish(model_id)

    def load_ngrams(self):
        user_dir = os.path.expanduser('~')
        default_root = os.path.join(user_dir, '.verbis')
        root_dir = os.path.join(default_root, "ngrams_english")
        abs_file_name = os.path.join(root_dir, "distributions.obj")
        f = open(abs_file_name, 'rb')
        uniDist = pickle.load(f)
        backwardBiDist = pickle.load(f)
        forwardBiDist = pickle.load(f)
        trigramDist = pickle.load(f)
        wordCasingLookup = pickle.load(f)
        f.close()
        self.put(uniDist, serviceid="uniDist", model_type="NGRAM", engine=None)
        self.put(backwardBiDist, serviceid="backwardBiDist", model_type="NGRAM", engine=None)
        self.put(forwardBiDist, serviceid="forwardBiDist", model_type="NGRAM", engine=None)
        self.put(trigramDist, serviceid="trigramDist", model_type="NGRAM", engine=None)
        self.put(wordCasingLookup, serviceid="wordCasingLookup", model_type="NGRAM", engine=None)
        print((app_cache.get_registered_ids()))
        # print(app_cache.model_cache)

    def get(self, serviceid, model_type, engine=None):
        """

        :param serviceid:
        :param model_type:
        :param engine:
        :return:
        """

        clf_id = basename(get_model_name(serviceid, model_type, engine))
        if clf_id in self.get_registered_ids():
            return app_cache.get_model(clf_id)
        return None

    def get_registered_ids(self):
        """

        :return:
        """
        return app_cache.get_registered_ids()

    def save_ner(self, model, model_type):
        """

        :param model:
        :param model_type:
        :return:
        """
        model_name = get_file_name(model.serviceid, model_type, model.get_engine(), model.get_extension())
        self.logger.info("NER File Name is::::::::::::::; %s" % model_name)
        self.logger.info("Engie isssssssssssssssssssssss %s" % model.get_engine())
        file_paths = self.__get__file_paths(model.serviceid, model_name)
        if not os.path.exists(file_paths[0]):
            make_dir(file_paths[0])
        elif os.path.exists(file_paths[1]):
            remove_dir(file_paths[1])

        make_dir(file_paths[0])
        model.save(file_paths[1])

    def save_ner_minio(self, model, model_type):
        """

        :param model:
        :param model_type:
        :return:
        """
        model_name = get_file_name(model.serviceid, model_type, model.get_engine(), model.get_extension())
        self.logger.info("NER File Name is::::::::::::::; %s" % model_name)
        self.logger.info("Engie isssssssssssssssssssssss %s" % model.get_engine())
        if model.get_engine() in get_all_corenlp_engines():
            model_name = object_name = get_corenlp_modelname(model.serviceid).split("/")[-1]
        else:
            object_name = model_name
        file_paths = self.__get__file_paths(model.serviceid, model_name)
        file_load_from_local_path = file_paths[1]

        # Make a bucket
        try:
            self.minio_client.make_bucket(app_config['MINIO_BUCKET_NAME'])
        except urllib3.exceptions.MaxRetryError as err:
            raise
        except BucketAlreadyOwnedByYou as err:
            print("BucketAlreadyOwnedByYou")
        except BucketAlreadyExists as err:
            print("BucketAlreadyExists")
        except ResponseError as err:
            raise
        except Exception as err:
            raise err

        # Put an object
        try:
            self.logger.info("Object name :::::::%s" % object_name)
            self.logger.info("File is :::::::%s" % file_load_from_local_path)
            self.minio_client.fput_object(app_config['MINIO_BUCKET_NAME'], object_name, file_load_from_local_path)
        except ResponseError as err:
            raise

    def load(self, serviceid, model_type, engine=None, class_name=None):
        """

        :param serviceid:
        :param model_type:
        :param engine:
        :return:
        """
        if (model_type == MODEL_TYPE_NER):
            er = create_instance(class_name, serviceid=serviceid)
            extension = er.get_extension()
        else:
            extension = "dat"
        model_name = get_file_name(serviceid, model_type, engine, extension)
        self.logger.info("Params %s,%s,%s,%s - %s" % (serviceid, model_type, engine, extension, model_name))
        file_paths = self.__get__file_paths(serviceid, model_name)

        logging.getLogger(__name__).info(file_paths)
        try:
            if os.path.exists(file_paths[0]):
                if model_type == MODEL_TYPE_NER:
                    er.load(file_paths[1])
                    return er
                elif model_type == MODEL_TYPE_IR:
                    f = open(file_paths[1], 'rb')
                    model = pickle.load(f)
                    f.close()
                    return model
        except:
            self.logger.warn("Unable to load %s model for service %s" % (model_type, serviceid))
        return None

    def save_ir(self, model):
        """

        :param model:
        :return:
        """
        model_name = get_file_name(model.serviceid, MODEL_TYPE_IR, None, "dat")
        file_paths = self.__get__file_paths(model.serviceid, model_name)

        self.logger.info(file_paths)

        if not os.path.exists(file_paths[0]):
            make_dir(file_paths[0])
        elif os.path.exists(file_paths[1]):
            remove_dir(file_paths[1])

        fh = open(file_paths[1], "wb")
        pickle.dump(model, fh)
        fh.close()

    def save_ir_minio(self, model):
        """

        :param model:
        :return:
        """
        model_name = get_file_name(model.serviceid, MODEL_TYPE_IR, None, "dat")
        file_paths = self.__get__file_paths(model.serviceid, model_name)
        self.logger.info(file_paths)

        object_name = model_name
        file_load_from_local_path = file_paths[1]

        # Make a bucket
        try:
            self.minio_client.make_bucket(app_config['MINIO_BUCKET_NAME'])
        except urllib3.exceptions.MaxRetryError as err:
            raise
        except InvalidAccessKeyId as err:
            raise
        except InvalidSecurity as err:
            raise
        except BucketAlreadyOwnedByYou as err:
            print("BucketAlreadyOwnedByYou")
        except BucketAlreadyExists as err:
            print("BucketAlreadyExists")
        except ResponseError as err:
            raise
        except Exception as err:
            raise err

        # Put an object
        try:
            self.minio_client.fput_object(app_config['MINIO_BUCKET_NAME'], object_name, file_load_from_local_path)
        except ResponseError as err:
            raise

    def remove_previous_model_from_store(self, serviceid):
        previous_model = get_corenlp_modelname(serviceid)
        if previous_model is None:
            self.logger.info("No previous models found!!")
        else:
            root_dir = os.path.join(self.root, serviceid)
            if os.path.exists(root_dir):
                os.remove(os.path.join(root_dir, previous_model))

    def get_model_from_remote(self, file_name, serviceid):
        self.logger.info("getting model file from minio")
        # obj_vs = VerbisStore()
        root_dir = os.path.join(self.root, serviceid)
        file_path = os.path.join(root_dir, file_name)
        try:
            # check bucket exists or not.
            if not self.minio_client.bucket_exists(app_config['MINIO_BUCKET_NAME']):
                raise Exception("bucket of respective object-{} doesn't exists.".format(
                    app_config['MINIO_BUCKET_NAME']))
            # get object
            stream_data = self.minio_client.get_object(app_config['MINIO_BUCKET_NAME'], file_name)
            # copy object to local dir.
            if not os.path.exists(root_dir):
                os.makedirs(root_dir)

            with open(file_path, 'wb+') as file_data:
                shutil.copyfileobj(stream_data, file_data)
        except urllib3.exceptions.MaxRetryError as err:
            raise
        except InvalidAccessKeyId as err:
            raise
        except InvalidSecurity as err:
            raise
        except ResponseError as err:
            raise
        except NoSuchKey as err:
            raise
        except Exception as e:
            raise

    def remove_models_from_remote(self, serviceid):
        # Remove a prefix recursively.
        try:
            get_name = lambda object: object.object_name
            names = list(map(get_name,
                        self.minio_client.list_objects_v2(app_config['MINIO_BUCKET_NAME'], serviceid, recursive=True)))
            for err in self.minio_client.remove_objects(app_config['MINIO_BUCKET_NAME'], names):
                print(("Deletion Error: {}".format(err)))
        except urllib3.exceptions.MaxRetryError as err:
            raise
        except InvalidAccessKeyId as err:
            raise
        except InvalidSecurity as err:
            raise
        except ResponseError as err:
            print(err)
        except NoSuchKey as err:
            print(err)
        except Exception as e:
            raise

    def should_reload_cache(self, model_name, last_trained):
        last_trained = dateutil.parser.parse(str(last_trained))
        if (model_name in app_cache.cached_ts_map and model_name in app_cache.get_registered_ids()):
            cached_ts = app_cache.cached_ts_map[model_name]
            # logger.info("Cache check for model %s" % model_name)
            # logger.info("last_trained %s" % (last_trained))
            # logger.info("cached_ts %s" % (cached_ts))
            if (last_trained > cached_ts):
                return True
            else:
                return False
        else:
            return True

    def reload_cache(self, serviceid, model_type, engine, model_class, model_name):
        if (model_type == "ner"):
            extension = create_instance(model_class, serviceid=serviceid).get_extension()
        else:
            extension = "dat"
        if engine in get_all_corenlp_engines():
            model_file_name = get_corenlp_modelname(serviceid)
        else:
            model_file_name = get_file_name(serviceid, model_type, engine, extension)
        self.get_model_from_remote(model_file_name, serviceid)
        self.publish(serviceid, model_type, engine, model_class)
        app_cache.cached_ts_map[model_name] = datetime.datetime.utcnow()

    def check_trained_time_and_reload(self, model_name, last_trained, service_id, model_type, engine, model_class):
        reload = self.should_reload_cache(model_name, last_trained)
        if (reload):
            with VerbisStore._lock:
                reload = self.should_reload_cache(model_name, last_trained)
                if (reload):
                    self.reload_cache(service_id, model_type, engine, model_class, model_name)
