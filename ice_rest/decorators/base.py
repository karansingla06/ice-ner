import logging
import time

from ice_commons.utils import dict_contains

logger = logging.getLogger(__name__)


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te - ts))
        return result

    return timed


class route(object):
    """ Decorates RequestHandlers and builds a list of routes """

    _routes = []

    def __init__(self, uri):
        """ Initializes route object
            Inputs:
                uri: uri of the Request Handler
        """
        self._uri = uri

    def __call__(self, _handler):
        """ Adds Handler instance and URI and append to the list of routes
            Input:
                _handler: falcon Request Handler object
        """
        self._routes.append([self._uri, _handler()])
        return _handler

    @classmethod
    def get_routes(cls):
        """ Returns list of routes """
        return cls._routes


class service(object):
    """ Decorates RequestHandlers and builds a list of routes """

    _services = dict()

    def __init__(self, _uri, _service, _validator):
        """ Initializes route object
            Inputs:
                uri: uri of the Request Handler
        """
        self._uri = _uri
        self._service = _service
        self._validator = _validator

    def __call__(self, _handler):
        """ Adds Handler instance and URI and append to the list of routes
            Input:
                _handler: falcon Request Handler object
        """
        self._services.update({
            self._uri: (self._service, self._validator)
        })
        return _handler

    @classmethod
    def get_service(cls, _name):
        """ Returns a local service """
        return cls._services[_name] if dict_contains(cls._services, _name) else None

    @classmethod
    def get_services(cls):
        """ Returns a local service """
        return cls._services


class iceexception(object):
    """ Decorates RequestHandlers and builds a list of exceptions """

    _exceptions = []

    def __call__(self, _handler):
        """ Adds Handler instance and URI and append to the list of exceptions
            Input:
                _handler: falcon Request Handler object
        """
        self._exceptions.append(_handler)
        return _handler

    @classmethod
    def get_exceptions(cls):
        """ Returns list of exceptions """
        return cls._exceptions


class middleware(object):
    """ Decorates RequestHandlers and builds a list of middlewares """

    _middlewares = []

    def __call__(self, _handler):
        """ Adds Handler instance and URI and append to the list of middlewares
            Input:
                _handler: falcon Request Handler object
        """
        self._middlewares.append(_handler())
        return _handler

    @classmethod
    def get_middlewares(cls):
        """ Returns list of middlewares """
        return cls._middlewares
