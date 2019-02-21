from idfy_sdk.idfy_configuration.meta_idfy_configuration import MetaIdfyConfiguration

class IdfyConfiguration(object, metaclass=MetaIdfyConfiguration):
    """This class holds congifuration options common to the whole SDK.

    !!!Do not instantiate this class!!!
    This class is a container for the static methods and data which
    allow you to configure the SDK as a whole. If you set a base URL
    here for example, that URL will be used as the default for all
    services where you dont set it explicitly. If you want to
    configure one of the services individually, use the constructor
    in that service to set your desired options.
    """
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
        """Set the client credentials and scope.

        Sets the client credentials for all services where you haven't
        set them individually. These credentials are used to fetch the
        Oauth token used to authenticate you against our API.
        """
        cls._clientId = clientId
        cls._clientSecret = clientSecret
        cls._scopes = scopes
    
    #Classmethod: set_base_url():