# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Mobile(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'country_code': 'str',
        'number': 'str'
    }

    attribute_map = {
        'country_code': 'countryCode',
        'number': 'number'
    }

    def __init__(self, country_code=None, number=None):  
        """Mobile"""  

        self._country_code = None
        self._number = None
        self.discriminator = None

        if country_code is not None:
            self.country_code = country_code
        if number is not None:
            self.number = number

    @property
    def country_code(self):
        """Gets the country_code of this Mobile.  

        The country code.  

        :return: The country_code of this Mobile.  
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Mobile.

        The country code.  

        :param country_code: The country_code of this Mobile.  
        :type: str
        """

        self._country_code = country_code

    @property
    def number(self):
        """Gets the number of this Mobile.  

        The mobile number.  

        :return: The number of this Mobile.  
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Mobile.

        The mobile number.  

        :param number: The number of this Mobile.  
        :type: str
        """

        self._number = number

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
        if not isinstance(other, Mobile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
