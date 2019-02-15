# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.jwt_payload import JwtPayload  


class JwtValidationResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'jwt_valid': 'bool',
        'expired': 'bool',
        'jwt_payload': 'JwtPayload',
        'error': 'str'
    }

    attribute_map = {
        'jwt_valid': 'jwtValid',
        'expired': 'expired',
        'jwt_payload': 'jwtPayload',
        'error': 'error'
    }

    def __init__(self, jwt_valid=None, expired=None, jwt_payload=None, error=None):  
        """JwtValidationResponse"""  

        self._jwt_valid = None
        self._expired = None
        self._jwt_payload = None
        self._error = None
        self.discriminator = None

        if jwt_valid is not None:
            self.jwt_valid = jwt_valid
        if expired is not None:
            self.expired = expired
        if jwt_payload is not None:
            self.jwt_payload = jwt_payload
        if error is not None:
            self.error = error

    @property
    def jwt_valid(self):
        """Gets the jwt_valid of this JwtValidationResponse.  

        True if jwt is valid  

        :return: The jwt_valid of this JwtValidationResponse.  
        :rtype: bool
        """
        return self._jwt_valid

    @jwt_valid.setter
    def jwt_valid(self, jwt_valid):
        """Sets the jwt_valid of this JwtValidationResponse.

        True if jwt is valid  

        :param jwt_valid: The jwt_valid of this JwtValidationResponse.  
        :type: bool
        """

        self._jwt_valid = jwt_valid

    @property
    def expired(self):
        """Gets the expired of this JwtValidationResponse.  

        True if expired  

        :return: The expired of this JwtValidationResponse.  
        :rtype: bool
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this JwtValidationResponse.

        True if expired  

        :param expired: The expired of this JwtValidationResponse.  
        :type: bool
        """

        self._expired = expired

    @property
    def jwt_payload(self):
        """Gets the jwt_payload of this JwtValidationResponse.  

        Payload (valid data if jwt is valid)  

        :return: The jwt_payload of this JwtValidationResponse.  
        :rtype: JwtPayload
        """
        return self._jwt_payload

    @jwt_payload.setter
    def jwt_payload(self, jwt_payload):
        """Sets the jwt_payload of this JwtValidationResponse.

        Payload (valid data if jwt is valid)  

        :param jwt_payload: The jwt_payload of this JwtValidationResponse.  
        :type: JwtPayload
        """

        self._jwt_payload = jwt_payload

    @property
    def error(self):
        """Gets the error of this JwtValidationResponse.  

        Error message if not valid jwt  

        :return: The error of this JwtValidationResponse.  
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this JwtValidationResponse.

        Error message if not valid jwt  

        :param error: The error of this JwtValidationResponse.  
        :type: str
        """

        self._error = error

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
        if not isinstance(other, JwtValidationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
