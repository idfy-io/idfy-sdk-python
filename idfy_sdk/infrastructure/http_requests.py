import requests
from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.infrastructure.idfy_exception import IdfyException

def Get(url, token, params=None) -> "http-response" :
    response = requests.get(url, headers = Headers(token), params = params)

    return response
    #if response.ok:
    #    return response
    #else:
    #    raise IdfyException(response)

def Post(url, token = None, params = None, data=None, auth = None): # Test whether the query option handles None values the way we want.
    response = requests.post(url, data=data, params=params, headers = Headers(token), auth = auth)

    return response
    #if response.ok:
    #    return response
    #else:
    #    raise IdfyException(response)

def Put(url, token, params=None, data=None):
    response = requests.put(url, headers=Headers(token), params=params, data=data) #test some Post methods. I changed "data=" to "data="

    return response
    #if response.ok:
    #    return response
    #else:
    #    raise IdfyException(response)

def Patch(url, token = None, data=None):
    response = requests.patch(url, data=data, headers = Headers(token))

    return response
    #if response.ok:
    #    return response
    #else:
    #    raise IdfyException(response)

def Delete(url, token=None):
    response = requests.delete(url, headers=Headers(token))

    return response

    #if response.ok:
    #    return response
    #else:
    #    raise IdfyException(response)


def Headers(token): # The headers need to be improved and the default_headers thing is not implemented.
    headers = {}

    headers['X-Idfy-SDK'] = "Python {}".format(config.SdkVersion)

    if token is not None:
        headers['Authorization'] = "Bearer {}".format(token) #The "bearer" part is the token type, it can be found in the token object.
        headers["Content-Type"] = "application/json"
    else:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    
    return headers

def create_exception(response): #TODO
    pass

