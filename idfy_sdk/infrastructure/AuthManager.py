import datetime
from requests.auth import HTTPBasicAuth

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.infrastructure.serialization import deserialize
from idfy_sdk.infrastructure import http_requests as http
from idfy_sdk import urls as urls


def Authorize():
    #check if config object already has a token with a valid expiration date. If so. Return it.
    if (config.OAuthToken) and (config.OAuthToken.expiry > datetime.datetime.utcnow()): # Doing this check two different places seems sub-optimal.
            return config.OAuthToken
    config.OAuthToken = AuhorizeWithData(config.ClientId, config.ClientSecret, config.Scopes)
    return config.OAuthToken

def AuhorizeWithData(clientId, clientSecret, scopes):
    if clientId is None:
        raise AttributeError("Client credentials have not been set!") # NTS: have another look at this

    formData = {
        'grant_type': 'client_credentials',
        'scope': ' '.join(scopes)
    }

    basicAuth = HTTPBasicAuth(clientId, clientSecret) # Clean up this line and everything beneath it.

    url = config.OAuthBaseUrl + urls.OAuthTokens

    token = deserialize((http.Post(url, data=formData, auth=basicAuth)), 'OAuthToken')

#Put in try/catch around Post call to token API

    token.expiry = datetime.datetime.utcnow() + datetime.timedelta(seconds = token.expires_in)

    return token