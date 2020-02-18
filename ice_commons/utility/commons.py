

keycloak_config= {
        "security" : "",
        "serverurl" : "http://clones.southindia.cloudapp.azure.com:8180/auth/",
        "clientid_bearer" : "ice-xd-backend",
        "clientid_public" : "ice-xd-frontend",
        "realm" : "ice-xd"
}

class Commons(object):


    def get_security(self):
        return keycloak_config['security']
    def get_serverurl(self):
        return keycloak_config['serverurl']
    def get_clientid_bearer(self):
        return keycloak_config['clientid_bearer']
    def get_clientid_public(self):
        return keycloak_config['clientid_public']
    def get_realm(self):
        return keycloak_config['realm']


