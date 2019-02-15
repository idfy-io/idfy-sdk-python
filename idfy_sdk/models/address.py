# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Address(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address1': 'str',
        'address2': 'str',
        'postal_code': 'str',
        'city': 'str',
        'country': 'str'
    }

    attribute_map = {
        'address1': 'Address1',
        'address2': 'Address2',
        'postal_code': 'PostalCode',
        'city': 'City',
        'country': 'Country'
    }

    def __init__(self, address1=None, address2=None, postal_code=None, city=None, country=None):  
        """Address"""  

        self._address1 = None
        self._address2 = None
        self._postal_code = None
        self._city = None
        self._country = None
        self.discriminator = None

        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if postal_code is not None:
            self.postal_code = postal_code
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country

    @property
    def address1(self):
        """Gets the address1 of this Address.  


        :return: The address1 of this Address.  
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Address.


        :param address1: The address1 of this Address.  
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Address.  


        :return: The address2 of this Address.  
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Address.


        :param address2: The address2 of this Address.  
        :type: str
        """

        self._address2 = address2

    @property
    def postal_code(self):
        """Gets the postal_code of this Address.  


        :return: The postal_code of this Address.  
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Address.


        :param postal_code: The postal_code of this Address.  
        :type: str
        """

        self._postal_code = postal_code

    @property
    def city(self):
        """Gets the city of this Address.  


        :return: The city of this Address.  
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.


        :param city: The city of this Address.  
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this Address.  


        :return: The country of this Address.  
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.


        :param country: The country of this Address.  
        :type: str
        """

        self._country = country

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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
