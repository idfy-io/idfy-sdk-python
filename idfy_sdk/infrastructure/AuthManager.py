"""Contains the functions used to fetch Oauth tokens from the Authentication endpoint."""

import datetime
from requests.auth import HTTPBasicAuth

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.infrastructure.serialization import deserialize
from idfy_sdk.infrastructure import http_requests as http
from idfy_sdk import urls as urls


def Authorize():
    """Authorize a service using config class.

    If the service does not have client credentials set individually it
    calls this function, which fetches them from the configuration class.
    If the config object already has a token with a valid expiration date
    that token is re-used.
    """
    if (config.OAuthToken) and (config.OAuthToken.expiry > datetime.datetime.utcnow()):
            return config.OAuthToken
    config.OAuthToken = AuhorizeWithData(config.ClientId, config.ClientSecret, config.Scopes)
    return config.OAuthToken

def AuhorizeWithData(clientId, clientSecret, scopes):
    """Gets the Oauth token using client credentials"""
    if clientId is None:
        raise TypeError("Client credentials have not been set!")

    formData = {
        'grant_type': 'client_credentials',
        'scope': ' '.join(scopes)
    }
    
    basicAuth = HTTPBasicAuth(clientId, clientSecret)
    url = config.OAuthBaseUrl + urls.OAuthTokens
    try:
        token = deserialize((http.Post(url, data=formData, auth=basicAuth)), 'OAuthToken')
    except (Exception) as e:
        raise Exception("An error occurred while fetching the Oauth token.") from e

    token.expiry = datetime.datetime.utcnow() + datetime.timedelta(seconds = token.expires_in)

    return token