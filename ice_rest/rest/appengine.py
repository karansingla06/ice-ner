import logging
import pkgutil

import falcon
from ice_rest.rest.interceptor.authinterceptor import RequestAuthenticationMiddleware
import os

from falcon_cors import CORS

from ice_rest.decorators import route, middleware, iceexception
#from ice_rest.rest.interceptor.keyvalidation import KeyValidator
from ice_rest.rest.interceptor.application_validator import RequestApplicationAuthenticationMiddleware

logger = logging.getLogger(__name__)


class AppEngine(object):
    """
    """
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(AppEngine, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.autoload(os.path.dirname(__file__))
        self.__initialized = True

    @staticmethod
    def autoload(dirname):
        logging.getLogger(__name__).info("Autoload all modules in directory %s " % dirname)

        for path, directories, files in os.walk(dirname):
            for importer, package_name, _ in pkgutil.iter_modules([path]):
                # Supposedly, this means the module is already loaded, but that is
                # not the case for tests. It shouldn't hurt to reload them anyways.
                # if package_name not in sys.modules or True:
                importer.find_module(package_name).load_module(package_name)

    def get_app(self):
        cors = CORS(
            allow_all_origins=True,
            allow_methods_list=["POST", "GET", "OPTIONS", "PUT"],
            allow_headers_list=["Origin", "X-Requested-With", "Content-Type", "Accept", "Authorization"]
        )

        middlewares = [cors.middleware, RequestAuthenticationMiddleware()] # , RequestApplicationAuthenticationMiddleware()]
        middlewares.extend(middleware.get_middlewares())
        app = falcon.API(
            middleware=middlewares
        )

        app = self.register_routes(app)
        return self.register_error_handlers(app)

    @staticmethod
    def register_error_handlers(app):
        for handler in iceexception.get_exceptions():
            app.add_error_handler(handler, handler.handle)
        # app.add_error_handler(RecordNotFoundError, RecordNotFoundError.handle)
        return app

    @staticmethod
    def register_routes(app):
        """ Get all routes from handler decorator and add them to the app """
        routes = route.get_routes()

        for service, resource in routes:
            logging.getLogger(__name__).info("Registering service: " + service)
            app.add_route(service, resource)

        return app
