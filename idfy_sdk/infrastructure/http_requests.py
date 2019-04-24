"""Uses the Requests module to send http requests to the API endpoints"""

import requests
from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.infrastructure.idfy_exception import IdfyException

def Get(url, token, params=None):
    response = requests.get(url, headers = Headers(token), params = params)

    if response.ok:
        return response
    else:
        raise IdfyException(response)

def Post(url, token = None, params = None, data=None, auth = None): # Test whether the query option handles None values the way we want.
    response = requests.post(url, data=data, params=params, headers = Headers(token), auth = auth)

    if response.ok:
        return response
    else:
        raise IdfyException(response)

def Put(url, token, params=None, data=None):
    response = requests.put(url, headers=Headers(token), params=params, data=data)

    if response.ok:
        return response
    else:
        raise IdfyException(response)

def Patch(url, token = None, data=None):
    response = requests.patch(url, data=data, headers = Headers(token))

    if response.ok:
        return response
    else:
        raise IdfyException(response)

def Delete(url, token=None):
    response = requests.delete(url, headers=Headers(token))

    if response.ok:
        return response
    else:
        raise IdfyException(response)

def Headers(token): # default_headers is not implemented.
    headers = {}

    headers['X-Idfy-SDK'] = "Python {}".format(config.SdkVersion)

    if token is not None:
        headers['Authorization'] = "Bearer {}".format(token)
        headers["Content-Type"] = "application/json"
    else:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    
    return headers

    

