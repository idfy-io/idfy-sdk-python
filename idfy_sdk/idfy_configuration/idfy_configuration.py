from idfy_sdk.idfy_configuration.meta_idfy_configuration import MetaIdfyConfiguration

class IdfyConfiguration(object, metaclass=MetaIdfyConfiguration): #There might mot be much point to this being here as opposed to in a seperate .py file
    _threaded = False
    _baseUrl = None
    _oauthBaseUrl = None
    _sdkVersion = None
    _clientId = None
    _clientSecret = None
    _scopes = None
    _oauthToken = None

    @classmethod
    def set_client_credentials(cls, clientId, clientSecret, scopes):
        cls._clientId = clientId
        cls._clientSecret = clientSecret
        cls._scopes = scopes
    
    #Classmethod: set_base_url():