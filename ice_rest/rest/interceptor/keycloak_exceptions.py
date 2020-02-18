

import logging

logger = logging.getLogger(__name__)
import requests


class KeycloakError(Exception):
    def __init__(self, error_message="", response_code=None,
                 response_body=None):

        Exception.__init__(self, error_message)

        self.response_code = response_code
        self.response_body = response_body
        self.error_message = error_message

    def __str__(self):
        if self.response_code is not None:
            return "{0}: {1}".format(self.response_code, self.error_message)
        else:
            return "{0}".format(self.error_message)


class KeycloakOperationError(KeycloakError):
    pass

class KeycloakAuthenticationError(KeycloakError):
    pass


class AccessTokenInvalidException(KeycloakOperationError):
    def __init__(self):
        pass

class RefreshTokenInvalidException(KeycloakOperationError):
    def __init__(self):
        pass

def raise_error_from_response(response, error, expected_code=200):

    if expected_code == response.status_code:
        if expected_code == requests.codes.no_content:
            return {}
        try:
            return response.json()
        except ValueError:
            return response.content

    try:
        message = response.json()['message']
    except (KeyError, ValueError):
        message = response.content

    if isinstance(error, dict):
        error = error.get(response.status_code, KeycloakOperationError)
    else:
        if response.status_code == 401:
            error = KeycloakAuthenticationError()

    raise error(error_message=message,
                response_code=response.status_code,
                response_body=response.content)

