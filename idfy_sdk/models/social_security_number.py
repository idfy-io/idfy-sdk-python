# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class SocialSecurityNumber(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'value': 'str',
        'country_code': 'str'
    }

    attribute_map = {
        'value': 'value',
        'country_code': 'countryCode'
    }

    def __init__(self, value=None, country_code=None):  
        """SocialSecurityNumber"""  

        self._value = None
        self._country_code = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if country_code is not None:
            self.country_code = country_code

    @property
    def value(self):
        """Gets the value of this SocialSecurityNumber.  

        The social security number.  

        :return: The value of this SocialSecurityNumber.  
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SocialSecurityNumber.

        The social security number.  

        :param value: The value of this SocialSecurityNumber.  
        :type: str
        """

        self._value = value

    @property
    def country_code(self):
        """Gets the country_code of this SocialSecurityNumber.  

        ISO 3166-1 Alfa-2 (2 letters) country code.  

        :return: The country_code of this SocialSecurityNumber.  
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this SocialSecurityNumber.

        ISO 3166-1 Alfa-2 (2 letters) country code.  

        :param country_code: The country_code of this SocialSecurityNumber.  
        :type: str
        """

        self._country_code = country_code

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
        if not isinstance(other, SocialSecurityNumber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
