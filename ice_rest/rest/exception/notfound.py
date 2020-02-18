import falcon

from ice_rest.decorators import iceexception

__author__ = 'rakeshpaul'


@iceexception()
class RecordNotFoundError(Exception):
    @staticmethod
    def handle(ex, req, resp, params):
        """

        :param ex:
        :param req:
        :param resp:
        :param params:
        :return:
        """
        description = 'Requested resource not found. Please check your request params and retry'
        raise falcon.HTTPInvalidParam(description, params)


@iceexception()
class InsufficientDataError(Exception):
    @staticmethod
    def handle(ex, req, resp, params):
        """

        :param ex:
        :param req:
        :param resp:
        :param params:
        :return:
        """
        description = 'Not enough data to build the model.'
        raise falcon.HTTPNotAcceptable(description)


@iceexception()
class DataParseError(Exception):
    @staticmethod
    def handle(ex, req, resp, params):
        """

        :param ex:
        :param req:
        :param resp:
        :param params:
        :return:
        """
        description = 'Unable to parse uploaded file. Please check and retry'
        raise falcon.HTTPNotAcceptable(description)
