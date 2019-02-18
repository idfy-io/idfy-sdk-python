from __future__ import absolute_import

import mimetypes
from multiprocessing.pool import ThreadPool
import os
import datetime
import tempfile
import asyncio
from json import dumps

# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import quote

# internal imports
from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.infrastructure.serialization import deserialize, serialize
from idfy_sdk.infrastructure import http_requests as http, AuthManager as auth


class IdfyBaseService(object):
    def __init__(self, client_id=None, client_secret=None, scopes=None): # Should only the creation of the service fail if the parameters are invalid, or the whole process?

        if(client_id or client_secret or scopes):
            self.independant = True
        else:
            self.independant = False

        self.default_headers = {}
        self.user_agent = 'Eivind was here.'
        self._oauth_token = None if self.independant else config.OAuthToken
        self._client_id = client_id
        self._client_secret = client_secret
        self._scopes = scopes
        self._threaded = None
        self.configuration = config
    
    @property
    def client_id(self):
        if self._client_id is not None:
            return self._client_id
        return config.ClientId
    
    @client_id.setter
    def client_id(self, value):
        if self.independant and value is None:
            raise Exception()

        self._client_id = value
    
    @property
    def client_secret(self):
        if self._client_secret is not None:
            return self._client_secret
        return config.ClientSecret
    
    @client_secret.setter
    def client_secret(self, value):
        if self.independant and value is None:
            raise Exception()

        self._client_secret = value
    
    @property
    def scopes(self):
        if self._scopes is not None:
            return self.scopes
        return config.Scopes
    
    @scopes.setter
    def scopes(self, value):
        if self.independant and value is None:
            raise Exception()

        self._scopes = value
    


    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    @property
    def threaded_default(self):
        """Should calls be async by default or not?"""
        return self._threaded if not None else config.Threaded

    @threaded_default.setter
    def threaded_default(self, threaded: bool):
        if threaded is bool:
            self._threaded = threaded
        else:
            raise TypeError("threaded_default was passed a non-boolean value")

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value


    def Get(self, url, model=None, params=None): 
        return deserialize(http.Get(url, token = self.GetToken(), params = params), model)
    
    def Post(self, url, model=None, params=None, data=None):
        return deserialize(http.Post(url, data=dumps(serialize(data)), token=self.GetToken(), params=params), model)
    
    def Put(self, url, model=None, params=None, data=None): #returns response from the server as opposed to a Python object.
        return http.Put(url, token=self.GetToken(), params=params, data=dumps(serialize(data)))
    
    def Patch(self, url, model=None, data=None):
        return deserialize(http.Patch(url, data=dumps(serialize(data)), token=self.GetToken()), model)
    
    def Delete(self, url):
        http.Delete(url, self.GetToken())
    
    def GetToken(self): #This needs to be tested properly.
        if (self._oauth_token is not None) and (self._oauth_token.expiry > datetime.datetime.utcnow()):
            return self._oauth_token.access_token
            # Is anyone going to want to fetch a new token even if the old one still has a valid expiration date?

        self._oauth_token = auth.AuhorizeWithData(self.client_id, self.client_secret, self.scopes) \
            if self.independant else auth.Authorize()

        return self._oauth_token.access_token