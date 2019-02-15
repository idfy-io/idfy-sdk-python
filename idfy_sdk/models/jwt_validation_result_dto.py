# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class JwtValidationResultDto(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'valid': 'bool',
        'expires': 'datetime',
        'payload': 'object',
        'error': 'str'
    }

    attribute_map = {
        'valid': 'valid',
        'expires': 'expires',
        'payload': 'payload',
        'error': 'error'
    }

    def __init__(self, valid=None, expires=None, payload=None, error=None):  
        """JwtValidationResultDto"""  

        self._valid = None
        self._expires = None
        self._payload = None
        self._error = None
        self.discriminator = None

        if valid is not None:
            self.valid = valid
        if expires is not None:
            self.expires = expires
        if payload is not None:
            self.payload = payload
        if error is not None:
            self.error = error

    @property
    def valid(self):
        """Gets the valid of this JwtValidationResultDto.  

        Whether the JWT is valid.  

        :return: The valid of this JwtValidationResultDto.  
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this JwtValidationResultDto.

        Whether the JWT is valid.  

        :param valid: The valid of this JwtValidationResultDto.  
        :type: bool
        """

        self._valid = valid

    @property
    def expires(self):
        """Gets the expires of this JwtValidationResultDto.  

        The expiration time on or after which the JWT will not be accepted for processing.  

        :return: The expires of this JwtValidationResultDto.  
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this JwtValidationResultDto.

        The expiration time on or after which the JWT will not be accepted for processing.  

        :param expires: The expires of this JwtValidationResultDto.  
        :type: datetime
        """

        self._expires = expires

    @property
    def payload(self):
        """Gets the payload of this JwtValidationResultDto.  

        The JWT payload.  

        :return: The payload of this JwtValidationResultDto.  
        :rtype: object
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this JwtValidationResultDto.

        The JWT payload.  

        :param payload: The payload of this JwtValidationResultDto.  
        :type: object
        """

        self._payload = payload

    @property
    def error(self):
        """Gets the error of this JwtValidationResultDto.  

        Error message explaining reason for a failed validation.  

        :return: The error of this JwtValidationResultDto.  
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this JwtValidationResultDto.

        Error message explaining reason for a failed validation.  

        :param error: The error of this JwtValidationResultDto.  
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
        if not isinstance(other, JwtValidationResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
