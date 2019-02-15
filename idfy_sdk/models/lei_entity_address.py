# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class LeiEntityAddress(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'city': 'str',
        'country': 'str',
        'first_address_line': 'str',
        'additional_address_line': 'list[str]',
        'postal_code': 'str',
        'region': 'str'
    }

    attribute_map = {
        'city': 'City',
        'country': 'Country',
        'first_address_line': 'FirstAddressLine',
        'additional_address_line': 'AdditionalAddressLine',
        'postal_code': 'PostalCode',
        'region': 'Region'
    }

    def __init__(self, city=None, country=None, first_address_line=None, additional_address_line=None, postal_code=None, region=None):  
        """LeiEntityAddress"""  

        self._city = None
        self._country = None
        self._first_address_line = None
        self._additional_address_line = None
        self._postal_code = None
        self._region = None
        self.discriminator = None

        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if first_address_line is not None:
            self.first_address_line = first_address_line
        if additional_address_line is not None:
            self.additional_address_line = additional_address_line
        if postal_code is not None:
            self.postal_code = postal_code
        if region is not None:
            self.region = region

    @property
    def city(self):
        """Gets the city of this LeiEntityAddress.  


        :return: The city of this LeiEntityAddress.  
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this LeiEntityAddress.


        :param city: The city of this LeiEntityAddress.  
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this LeiEntityAddress.  


        :return: The country of this LeiEntityAddress.  
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this LeiEntityAddress.


        :param country: The country of this LeiEntityAddress.  
        :type: str
        """

        self._country = country

    @property
    def first_address_line(self):
        """Gets the first_address_line of this LeiEntityAddress.  


        :return: The first_address_line of this LeiEntityAddress.  
        :rtype: str
        """
        return self._first_address_line

    @first_address_line.setter
    def first_address_line(self, first_address_line):
        """Sets the first_address_line of this LeiEntityAddress.


        :param first_address_line: The first_address_line of this LeiEntityAddress.  
        :type: str
        """

        self._first_address_line = first_address_line

    @property
    def additional_address_line(self):
        """Gets the additional_address_line of this LeiEntityAddress.  


        :return: The additional_address_line of this LeiEntityAddress.  
        :rtype: list[str]
        """
        return self._additional_address_line

    @additional_address_line.setter
    def additional_address_line(self, additional_address_line):
        """Sets the additional_address_line of this LeiEntityAddress.


        :param additional_address_line: The additional_address_line of this LeiEntityAddress.  
        :type: list[str]
        """

        self._additional_address_line = additional_address_line

    @property
    def postal_code(self):
        """Gets the postal_code of this LeiEntityAddress.  


        :return: The postal_code of this LeiEntityAddress.  
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this LeiEntityAddress.


        :param postal_code: The postal_code of this LeiEntityAddress.  
        :type: str
        """

        self._postal_code = postal_code

    @property
    def region(self):
        """Gets the region of this LeiEntityAddress.  


        :return: The region of this LeiEntityAddress.  
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this LeiEntityAddress.


        :param region: The region of this LeiEntityAddress.  
        :type: str
        """

        self._region = region

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
        if not isinstance(other, LeiEntityAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
