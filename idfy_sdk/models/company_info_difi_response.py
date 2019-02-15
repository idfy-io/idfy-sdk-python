# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class CompanyInfoDifiResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'org_nr': 'str',
        'org_name': 'str',
        'address': 'str',
        'postal_code': 'str',
        'city': 'str',
        'website': 'str',
        'country': 'str'
    }

    attribute_map = {
        'org_nr': 'OrgNr',
        'org_name': 'OrgName',
        'address': 'Address',
        'postal_code': 'PostalCode',
        'city': 'City',
        'website': 'Website',
        'country': 'Country'
    }

    def __init__(self, org_nr=None, org_name=None, address=None, postal_code=None, city=None, website=None, country=None):  
        """CompanyInfoDifiResponse"""  

        self._org_nr = None
        self._org_name = None
        self._address = None
        self._postal_code = None
        self._city = None
        self._website = None
        self._country = None
        self.discriminator = None

        if org_nr is not None:
            self.org_nr = org_nr
        if org_name is not None:
            self.org_name = org_name
        if address is not None:
            self.address = address
        if postal_code is not None:
            self.postal_code = postal_code
        if city is not None:
            self.city = city
        if website is not None:
            self.website = website
        if country is not None:
            self.country = country

    @property
    def org_nr(self):
        """Gets the org_nr of this CompanyInfoDifiResponse.  


        :return: The org_nr of this CompanyInfoDifiResponse.  
        :rtype: str
        """
        return self._org_nr

    @org_nr.setter
    def org_nr(self, org_nr):
        """Sets the org_nr of this CompanyInfoDifiResponse.


        :param org_nr: The org_nr of this CompanyInfoDifiResponse.  
        :type: str
        """

        self._org_nr = org_nr

    @property
    def org_name(self):
        """Gets the org_name of this CompanyInfoDifiResponse.  


        :return: The org_name of this CompanyInfoDifiResponse.  
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this CompanyInfoDifiResponse.


        :param org_name: The org_name of this CompanyInfoDifiResponse.  
        :type: str
        """

        self._org_name = org_name

    @property
    def address(self):
        """Gets the address of this CompanyInfoDifiResponse.  


        :return: The address of this CompanyInfoDifiResponse.  
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CompanyInfoDifiResponse.


        :param address: The address of this CompanyInfoDifiResponse.  
        :type: str
        """

        self._address = address

    @property
    def postal_code(self):
        """Gets the postal_code of this CompanyInfoDifiResponse.  


        :return: The postal_code of this CompanyInfoDifiResponse.  
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this CompanyInfoDifiResponse.


        :param postal_code: The postal_code of this CompanyInfoDifiResponse.  
        :type: str
        """

        self._postal_code = postal_code

    @property
    def city(self):
        """Gets the city of this CompanyInfoDifiResponse.  


        :return: The city of this CompanyInfoDifiResponse.  
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CompanyInfoDifiResponse.


        :param city: The city of this CompanyInfoDifiResponse.  
        :type: str
        """

        self._city = city

    @property
    def website(self):
        """Gets the website of this CompanyInfoDifiResponse.  


        :return: The website of this CompanyInfoDifiResponse.  
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this CompanyInfoDifiResponse.


        :param website: The website of this CompanyInfoDifiResponse.  
        :type: str
        """

        self._website = website

    @property
    def country(self):
        """Gets the country of this CompanyInfoDifiResponse.  


        :return: The country of this CompanyInfoDifiResponse.  
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CompanyInfoDifiResponse.


        :param country: The country of this CompanyInfoDifiResponse.  
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
        if not isinstance(other, CompanyInfoDifiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
