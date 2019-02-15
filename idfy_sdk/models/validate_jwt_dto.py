# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class ValidateJwtDto(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'jwt': 'str'
    }

    attribute_map = {
        'jwt': 'jwt'
    }

    def __init__(self, jwt=None):  
        """ValidateJwtDto"""  

        self._jwt = None
        self.discriminator = None

        self.jwt = jwt

    @property
    def jwt(self):
        """Gets the jwt of this ValidateJwtDto.  

        The JWT to validate.  

        :return: The jwt of this ValidateJwtDto.  
        :rtype: str
        """
        return self._jwt

    @jwt.setter
    def jwt(self, jwt):
        """Sets the jwt of this ValidateJwtDto.

        The JWT to validate.  

        :param jwt: The jwt of this ValidateJwtDto.  
        :type: str
        """
        if jwt is None:
            raise ValueError("Invalid value for `jwt`, must not be `None`")  

        self._jwt = jwt

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
        if not isinstance(other, ValidateJwtDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
