import json
import falcon
from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakAuthenticationError,KeycloakInvalidTokenError
import re
from ice_commons.utility.keyOAuth import KeycloakConfig
from ice_rest.rest.interceptor.keycloak_exceptions import *




class RequestAuthenticationMiddleware(object):
    obj = KeycloakConfig()
    security = obj.get_security()
    server = obj.get_serverurl()
    client_public_id = obj.get_clientid_public()
    client_bearer_id = obj.get_clientid_bearer()
    #realm = obj.get_realm()

    if (security is None or len(security.strip()) == 0):
        security = "OFF"

    def keycloak_details(self, realm):

        keycloak_openid = KeycloakOpenID(server_url=self.server, client_id=self.client_bearer_id,
                                         realm_name=realm, verify=False)

        keycloak_refresh = KeycloakOpenID(server_url=self.server, client_id=self.client_public_id,
                                          realm_name=realm, verify=False)

        return keycloak_openid, keycloak_refresh

    def process_request(self, req, resp):
        logger.info("In process_request")

        if (req.method in ['GET', 'POST', 'PUT', 'DELETE'] and self.security == "ON"):
            access_token = req.get_header('Authorization')
            realm = req.get_header('Organization-name')
            keycloak_openid, keycloak_refresh = self.keycloak_details(realm)

            if (access_token != None):
                try:
                    user_info = self.access_token_handler(keycloak_openid, access_token)
                    if (user_info == None):
                        description = 'User not found'
                        self.throwerror(description, "Authentication failed")

                except AccessTokenInvalidException:

                    access_token = req.get_header('refresh-token')
                    if (access_token != None):
                        try:
                            self.refresh_token_handler(keycloak_refresh, access_token)

                        except RefreshTokenInvalidException:
                            description = 'Both access token and refresh token are invalid.'
                            self.throwerror(description)
                    else:
                        description = 'The provided auth token is invalid. Request a new token and try again.'
                        self.throwerror(description)
            else:
                description = 'Please provide a valid token. The auth token provided is invalid.'
                self.throwerror(description)

    def access_token_handler(self, keycloak_openid, token):
        # challenges = ['Token type="Fernet"']
        try:
            user_info = keycloak_openid.userinfo(token)
            return user_info
        #except Exception as ex:
          #  logger.error(ex)
        except (KeycloakAuthenticationError, KeycloakInvalidTokenError):
           raise AccessTokenInvalidException()

    def refresh_token_handler(self, keycloak_refresh, token):
        try:
            token = keycloak_refresh.refresh_token(token)
            user_info = keycloak_refresh.userinfo(token['access_token'])
            if (user_info == None):
                description = ('The provided auth token is not valid. Please request a new token and try again.')
                self.throwerror(description)

        except KeycloakAuthenticationError as ex:
            error = "Authentication Error occurred while refreshing"
            description = ex
            self.throwerror(description, error)

        except KeycloakInvalidTokenError as ex:
            description = ex
            error = 'Invalid token'
            self.throwerror(description, error)

        except Exception as ex:
            description = ex
            error = 'Invalid token'
            self.throwerror(description, error)

    def throwerror(self, description, error='Authentication required'):
        raise falcon.HTTPUnauthorized(error, description)