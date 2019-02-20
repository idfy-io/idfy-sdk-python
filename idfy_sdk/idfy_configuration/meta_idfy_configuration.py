from idfy_sdk import urls as urls
from idfy_sdk import version as ver

class MetaIdfyConfiguration(type):

    @property
    def Threaded(self):
        return self._threaded

    @Threaded.setter
    def Threaded(self, threaded):
        self._threaded = threaded

    @property
    def BaseUrl(self):
        return self._baseUrl if self._baseUrl is not None else urls.DefaultBaseUrl

    @BaseUrl.setter
    def BaseUrl(self, baseUrl):
        self._baseUrl = baseUrl

    @property
    def OAuthBaseUrl(self):
        return self._oauthBaseUrl if self._oauthBaseUrl is not None else urls.DefaultOAuthBaseUrl
    
    @OAuthBaseUrl.setter
    def OAuthBaseUrl(self, oauthBaseUrl):
        self._oauthBaseUrl = oauthBaseUrl
    
    @property
    def SdkVersion(self):
        return ver

    @property
    def ClientId(self):
        return self._clientId
    
    @ClientId.setter
    def ClientId(self, clientId):
        self._clientId = clientId
    
    @property
    def ClientSecret(self):
        return self._clientSecret
    
    @ClientSecret.setter
    def ClientSecret(self, clientSecret):
        self._clientSecret = clientSecret
    
    @property
    def Scopes(self):
        return self._scopes
    
    @Scopes.setter
    def Scopes(self, scopes):
        self._scopes = scopes
    
    @property
    def OAuthToken(self):
        return self._oauthToken
    
    @OAuthToken.setter
    def OAuthToken(self, oauthToken):
        self._oauthToken = oauthToken
    
