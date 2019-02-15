# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonOfficialPersonRegistryResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'first_name': 'str',
        'last_name': 'str',
        'middle_name': 'str',
        'fullname': 'str',
        'address': 'str',
        'address2': 'str',
        'city': 'str',
        'postal_code': 'str',
        'gender': 'str',
        'raw_json': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'middle_name': 'MiddleName',
        'fullname': 'Fullname',
        'address': 'Address',
        'address2': 'Address2',
        'city': 'City',
        'postal_code': 'PostalCode',
        'gender': 'Gender',
        'raw_json': 'RawJson',
        'request_id': 'RequestId'
    }

    def __init__(self, first_name=None, last_name=None, middle_name=None, fullname=None, address=None, address2=None, city=None, postal_code=None, gender=None, raw_json=None, request_id=None):  
        """PersonOfficialPersonRegistryResponse"""  

        self._first_name = None
        self._last_name = None
        self._middle_name = None
        self._fullname = None
        self._address = None
        self._address2 = None
        self._city = None
        self._postal_code = None
        self._gender = None
        self._raw_json = None
        self._request_id = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if middle_name is not None:
            self.middle_name = middle_name
        if fullname is not None:
            self.fullname = fullname
        if address is not None:
            self.address = address
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if postal_code is not None:
            self.postal_code = postal_code
        if gender is not None:
            self.gender = gender
        if raw_json is not None:
            self.raw_json = raw_json
        if request_id is not None:
            self.request_id = request_id

    @property
    def first_name(self):
        """Gets the first_name of this PersonOfficialPersonRegistryResponse.  


        :return: The first_name of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PersonOfficialPersonRegistryResponse.


        :param first_name: The first_name of this PersonOfficialPersonRegistryResponse.  
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PersonOfficialPersonRegistryResponse.  


        :return: The last_name of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PersonOfficialPersonRegistryResponse.


        :param last_name: The last_name of this PersonOfficialPersonRegistryResponse.  
        :type: str
        """

        self._last_name = last_name

    @property
    def middle_name(self):
        """Gets the middle_name of this PersonOfficialPersonRegistryResponse.  


        :return: The middle_name of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this PersonOfficialPersonRegistryResponse.


        :param middle_name: The middle_name of this PersonOfficialPersonRegistryResponse.  
        :type: str
        """

        self._middle_name = middle_name

    @property
    def fullname(self):
        """Gets the fullname of this PersonOfficialPersonRegistryResponse.  


        :return: The fullname of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """Sets the fullname of this PersonOfficialPersonRegistryResponse.


        :param fullname: The fullname of this PersonOfficialPersonRegistryResponse.  
        :type: str
        """

        self._fullname = fullname

    @property
    def address(self):
        """Gets the address of this PersonOfficialPersonRegistryResponse.  


        :return: The address of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PersonOfficialPersonRegistryResponse.


        :param address: The address of this PersonOfficialPersonRegistryResponse.  
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this PersonOfficialPersonRegistryResponse.  


        :return: The address2 of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this PersonOfficialPersonRegistryResponse.


        :param address2: The address2 of this PersonOfficialPersonRegistryResponse.  
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this PersonOfficialPersonRegistryResponse.  


        :return: The city of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PersonOfficialPersonRegistryResponse.


        :param city: The city of this PersonOfficialPersonRegistryResponse.  
        :type: str
        """

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this PersonOfficialPersonRegistryResponse.  


        :return: The postal_code of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this PersonOfficialPersonRegistryResponse.


        :param postal_code: The postal_code of this PersonOfficialPersonRegistryResponse.  
        :type: str
        """

        self._postal_code = postal_code

    @property
    def gender(self):
        """Gets the gender of this PersonOfficialPersonRegistryResponse.  


        :return: The gender of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this PersonOfficialPersonRegistryResponse.


        :param gender: The gender of this PersonOfficialPersonRegistryResponse.  
        :type: str
        """

        self._gender = gender

    @property
    def raw_json(self):
        """Gets the raw_json of this PersonOfficialPersonRegistryResponse.  


        :return: The raw_json of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._raw_json

    @raw_json.setter
    def raw_json(self, raw_json):
        """Sets the raw_json of this PersonOfficialPersonRegistryResponse.


        :param raw_json: The raw_json of this PersonOfficialPersonRegistryResponse.  
        :type: str
        """

        self._raw_json = raw_json

    @property
    def request_id(self):
        """Gets the request_id of this PersonOfficialPersonRegistryResponse.  


        :return: The request_id of this PersonOfficialPersonRegistryResponse.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PersonOfficialPersonRegistryResponse.


        :param request_id: The request_id of this PersonOfficialPersonRegistryResponse.  
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
        if not isinstance(other, PersonOfficialPersonRegistryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
