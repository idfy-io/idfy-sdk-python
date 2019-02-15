# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class CompanyInformationResponse(object):

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
        'country': 'str',
        'raw_json': 'str',
        'phone': 'str',
        'mobile': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'org_nr': 'OrgNr',
        'org_name': 'OrgName',
        'address': 'Address',
        'postal_code': 'PostalCode',
        'city': 'City',
        'country': 'Country',
        'raw_json': 'RawJson',
        'phone': 'Phone',
        'mobile': 'Mobile',
        'request_id': 'RequestId'
    }

    def __init__(self, org_nr=None, org_name=None, address=None, postal_code=None, city=None, country=None, raw_json=None, phone=None, mobile=None, request_id=None):  
        """CompanyInformationResponse"""  

        self._org_nr = None
        self._org_name = None
        self._address = None
        self._postal_code = None
        self._city = None
        self._country = None
        self._raw_json = None
        self._phone = None
        self._mobile = None
        self._request_id = None
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
        if country is not None:
            self.country = country
        if raw_json is not None:
            self.raw_json = raw_json
        if phone is not None:
            self.phone = phone
        if mobile is not None:
            self.mobile = mobile
        if request_id is not None:
            self.request_id = request_id

    @property
    def org_nr(self):
        """Gets the org_nr of this CompanyInformationResponse.  


        :return: The org_nr of this CompanyInformationResponse.  
        :rtype: str
        """
        return self._org_nr

    @org_nr.setter
    def org_nr(self, org_nr):
        """Sets the org_nr of this CompanyInformationResponse.


        :param org_nr: The org_nr of this CompanyInformationResponse.  
        :type: str
        """

        self._org_nr = org_nr

    @property
    def org_name(self):
        """Gets the org_name of this CompanyInformationResponse.  


        :return: The org_name of this CompanyInformationResponse.  
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this CompanyInformationResponse.


        :param org_name: The org_name of this CompanyInformationResponse.  
        :type: str
        """

        self._org_name = org_name

    @property
    def address(self):
        """Gets the address of this CompanyInformationResponse.  


        :return: The address of this CompanyInformationResponse.  
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CompanyInformationResponse.


        :param address: The address of this CompanyInformationResponse.  
        :type: str
        """

        self._address = address

    @property
    def postal_code(self):
        """Gets the postal_code of this CompanyInformationResponse.  


        :return: The postal_code of this CompanyInformationResponse.  
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this CompanyInformationResponse.


        :param postal_code: The postal_code of this CompanyInformationResponse.  
        :type: str
        """

        self._postal_code = postal_code

    @property
    def city(self):
        """Gets the city of this CompanyInformationResponse.  


        :return: The city of this CompanyInformationResponse.  
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CompanyInformationResponse.


        :param city: The city of this CompanyInformationResponse.  
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this CompanyInformationResponse.  


        :return: The country of this CompanyInformationResponse.  
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CompanyInformationResponse.


        :param country: The country of this CompanyInformationResponse.  
        :type: str
        """

        self._country = country

    @property
    def raw_json(self):
        """Gets the raw_json of this CompanyInformationResponse.  


        :return: The raw_json of this CompanyInformationResponse.  
        :rtype: str
        """
        return self._raw_json

    @raw_json.setter
    def raw_json(self, raw_json):
        """Sets the raw_json of this CompanyInformationResponse.


        :param raw_json: The raw_json of this CompanyInformationResponse.  
        :type: str
        """

        self._raw_json = raw_json

    @property
    def phone(self):
        """Gets the phone of this CompanyInformationResponse.  


        :return: The phone of this CompanyInformationResponse.  
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CompanyInformationResponse.


        :param phone: The phone of this CompanyInformationResponse.  
        :type: str
        """

        self._phone = phone

    @property
    def mobile(self):
        """Gets the mobile of this CompanyInformationResponse.  


        :return: The mobile of this CompanyInformationResponse.  
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this CompanyInformationResponse.


        :param mobile: The mobile of this CompanyInformationResponse.  
        :type: str
        """

        self._mobile = mobile

    @property
    def request_id(self):
        """Gets the request_id of this CompanyInformationResponse.  


        :return: The request_id of this CompanyInformationResponse.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CompanyInformationResponse.


        :param request_id: The request_id of this CompanyInformationResponse.  
        :type: str
        """

        self._request_id = request_id

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
        if not isinstance(other, CompanyInformationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
