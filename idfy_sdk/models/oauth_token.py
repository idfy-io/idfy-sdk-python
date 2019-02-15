import pprint
import re  

import six

class OAuthToken:
    """
    Nts: The token contains a DateTime object.
    """
    swagger_types = {
        'access_token': 'str',
        'expires_in': 'int',
        'token_type': 'str'
        #'expiry': 'datetime'
    }

    attribute_map = {
        'access_token': 'access_token',
        'expires_in': 'expires_in',
        'token_type': 'token_type',
    }

    def __init__(self, access_token=None, expires_in=None, token_type=None):  

        self._access_token = None
        self._expires_in = None
        self._token_type = None
        self._expiry = None


        if access_token is not None:
            self._access_token = access_token
        if expires_in is not None:
            self._expires_in = expires_in
        if token_type is not None:
            self._token_type = token_type



    @property
    def access_token(self):
        return self._access_token
    
    @access_token.setter
    def access_token(self, token):
        self._access_token = token
    
    @property
    def expires_in(self):
        return self._expires_in
    
    @expires_in.setter
    def expires_in(self, expires):
        self._expires_in = expires
    
    @property
    def token_type(self):
        return self._token_type
    
    @token_type.setter
    def token_type(self, token_type):
        self._token_type = token_type
    
    @property
    def expiry(self):
        return self._expiry
    
    @expiry.setter
    def expiry(self, expiry):
        self._expiry = expiry

def to_dict(self):
    """Returns the model properties as a dict"""
    result = {}

    for attr, _ in six.iteritems(self.swagger_types):
        value = getattr(self, attr)
        if isinstance(value, list):
            result[attr] = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result[attr] = value.to_dict()
        elif isinstance(value, dict):
            result[attr] = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result[attr] = value

    return result

def to_str(self):
    """Returns the string representation of the model"""
    return pprint.pformat(self.to_dict())

def __repr__(self):
    """For `print` and `pprint`"""
    return self.to_str()

def __eq__(self, other):
    """Returns true if both objects are equal"""
    if not isinstance(other, OAuthToken):
        return False

    return self.__dict__ == other.__dict__

def __ne__(self, other):
    """Returns true if both objects are not equal"""
    return not self == other
