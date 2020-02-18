from ice_commons.config_settings import app_config


class KeycloakConfig(object):
    def get_security(self):
        return app_config['KEYCLOAK_ON']
    def get_serverurl(self):
        return app_config['KEYCLOAK_END_POINT']
    def get_clientid_bearer(self):
        return app_config['KEYCLOAK_PUBLIC_CLIENT_ID']
    def get_clientid_public(self):
        return app_config['KEYCLOAK_BEARER_CLIENT_ID']
    def get_realm(self):
        return app_config['KEYCLOAK_REALM']