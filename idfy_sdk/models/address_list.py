# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class AddressList(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'country_name': 'str',
        'country_code': 'str',
        'street': 'str',
        'post_code': 'str',
        'city': 'str'
    }

    attribute_map = {
        'country_name': 'countryName',
        'country_code': 'countryCode',
        'street': 'street',
        'post_code': 'postCode',
        'city': 'city'
    }

    def __init__(self, country_name=None, country_code=None, street=None, post_code=None, city=None):  
        """AddressList"""  

        self._country_name = None
        self._country_code = None
        self._street = None
        self._post_code = None
        self._city = None
        self.discriminator = None

        if country_name is not None:
            self.country_name = country_name
        if country_code is not None:
            self.country_code = country_code
        if street is not None:
            self.street = street
        if post_code is not None:
            self.post_code = post_code
        if city is not None:
            self.city = city

    @property
    def country_name(self):
        """Gets the country_name of this AddressList.  


        :return: The country_name of this AddressList.  
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this AddressList.


        :param country_name: The country_name of this AddressList.  
        :type: str
        """

        self._country_name = country_name

    @property
    def country_code(self):
        """Gets the country_code of this AddressList.  


        :return: The country_code of this AddressList.  
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this AddressList.


        :param country_code: The country_code of this AddressList.  
        :type: str
        """

        self._country_code = country_code

    @property
    def street(self):
        """Gets the street of this AddressList.  


        :return: The street of this AddressList.  
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this AddressList.


        :param street: The street of this AddressList.  
        :type: str
        """

        self._street = street

    @property
    def post_code(self):
        """Gets the post_code of this AddressList.  


        :return: The post_code of this AddressList.  
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this AddressList.


        :param post_code: The post_code of this AddressList.  
        :type: str
        """

        self._post_code = post_code

    @property
    def city(self):
        """Gets the city of this AddressList.  


        :return: The city of this AddressList.  
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AddressList.


        :param city: The city of this AddressList.  
        :type: str
        """

        self._city = city

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
        if not isinstance(other, AddressList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
