# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonPersonInformation(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'firstname': 'str',
        'middlename': 'str',
        'lastname': 'str',
        'date_of_birth': 'str',
        'address': 'str',
        'zip_code': 'str',
        'city': 'str',
        'mobile': 'str',
        'phone': 'str',
        'gender': 'str',
        'raw_json': 'str',
        'request_id': 'str',
        'dead': 'datetime',
        'source': 'str'
    }

    attribute_map = {
        'firstname': 'Firstname',
        'middlename': 'Middlename',
        'lastname': 'Lastname',
        'date_of_birth': 'DateOfBirth',
        'address': 'Address',
        'zip_code': 'ZipCode',
        'city': 'City',
        'mobile': 'Mobile',
        'phone': 'Phone',
        'gender': 'Gender',
        'raw_json': 'RawJson',
        'request_id': 'RequestId',
        'dead': 'Dead',
        'source': 'Source'
    }

    def __init__(self, firstname=None, middlename=None, lastname=None, date_of_birth=None, address=None, zip_code=None, city=None, mobile=None, phone=None, gender=None, raw_json=None, request_id=None, dead=None, source=None):  
        """PersonPersonInformation"""  

        self._firstname = None
        self._middlename = None
        self._lastname = None
        self._date_of_birth = None
        self._address = None
        self._zip_code = None
        self._city = None
        self._mobile = None
        self._phone = None
        self._gender = None
        self._raw_json = None
        self._request_id = None
        self._dead = None
        self._source = None
        self.discriminator = None

        if firstname is not None:
            self.firstname = firstname
        if middlename is not None:
            self.middlename = middlename
        if lastname is not None:
            self.lastname = lastname
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if address is not None:
            self.address = address
        if zip_code is not None:
            self.zip_code = zip_code
        if city is not None:
            self.city = city
        if mobile is not None:
            self.mobile = mobile
        if phone is not None:
            self.phone = phone
        if gender is not None:
            self.gender = gender
        if raw_json is not None:
            self.raw_json = raw_json
        if request_id is not None:
            self.request_id = request_id
        if dead is not None:
            self.dead = dead
        if source is not None:
            self.source = source

    @property
    def firstname(self):
        """Gets the firstname of this PersonPersonInformation.  


        :return: The firstname of this PersonPersonInformation.  
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this PersonPersonInformation.


        :param firstname: The firstname of this PersonPersonInformation.  
        :type: str
        """

        self._firstname = firstname

    @property
    def middlename(self):
        """Gets the middlename of this PersonPersonInformation.  


        :return: The middlename of this PersonPersonInformation.  
        :rtype: str
        """
        return self._middlename

    @middlename.setter
    def middlename(self, middlename):
        """Sets the middlename of this PersonPersonInformation.


        :param middlename: The middlename of this PersonPersonInformation.  
        :type: str
        """

        self._middlename = middlename

    @property
    def lastname(self):
        """Gets the lastname of this PersonPersonInformation.  


        :return: The lastname of this PersonPersonInformation.  
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this PersonPersonInformation.


        :param lastname: The lastname of this PersonPersonInformation.  
        :type: str
        """

        self._lastname = lastname

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this PersonPersonInformation.  


        :return: The date_of_birth of this PersonPersonInformation.  
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this PersonPersonInformation.


        :param date_of_birth: The date_of_birth of this PersonPersonInformation.  
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def address(self):
        """Gets the address of this PersonPersonInformation.  


        :return: The address of this PersonPersonInformation.  
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PersonPersonInformation.


        :param address: The address of this PersonPersonInformation.  
        :type: str
        """

        self._address = address

    @property
    def zip_code(self):
        """Gets the zip_code of this PersonPersonInformation.  


        :return: The zip_code of this PersonPersonInformation.  
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this PersonPersonInformation.


        :param zip_code: The zip_code of this PersonPersonInformation.  
        :type: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """Gets the city of this PersonPersonInformation.  


        :return: The city of this PersonPersonInformation.  
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PersonPersonInformation.


        :param city: The city of this PersonPersonInformation.  
        :type: str
        """

        self._city = city

    @property
    def mobile(self):
        """Gets the mobile of this PersonPersonInformation.  


        :return: The mobile of this PersonPersonInformation.  
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this PersonPersonInformation.


        :param mobile: The mobile of this PersonPersonInformation.  
        :type: str
        """

        self._mobile = mobile

    @property
    def phone(self):
        """Gets the phone of this PersonPersonInformation.  


        :return: The phone of this PersonPersonInformation.  
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PersonPersonInformation.


        :param phone: The phone of this PersonPersonInformation.  
        :type: str
        """

        self._phone = phone

    @property
    def gender(self):
        """Gets the gender of this PersonPersonInformation.  


        :return: The gender of this PersonPersonInformation.  
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this PersonPersonInformation.


        :param gender: The gender of this PersonPersonInformation.  
        :type: str
        """

        self._gender = gender

    @property
    def raw_json(self):
        """Gets the raw_json of this PersonPersonInformation.  


        :return: The raw_json of this PersonPersonInformation.  
        :rtype: str
        """
        return self._raw_json

    @raw_json.setter
    def raw_json(self, raw_json):
        """Sets the raw_json of this PersonPersonInformation.


        :param raw_json: The raw_json of this PersonPersonInformation.  
        :type: str
        """

        self._raw_json = raw_json

    @property
    def request_id(self):
        """Gets the request_id of this PersonPersonInformation.  


        :return: The request_id of this PersonPersonInformation.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PersonPersonInformation.


        :param request_id: The request_id of this PersonPersonInformation.  
        :type: str
        """

        self._request_id = request_id

    @property
    def dead(self):
        """Gets the dead of this PersonPersonInformation.  


        :return: The dead of this PersonPersonInformation.  
        :rtype: datetime
        """
        return self._dead

    @dead.setter
    def dead(self, dead):
        """Sets the dead of this PersonPersonInformation.


        :param dead: The dead of this PersonPersonInformation.  
        :type: datetime
        """

        self._dead = dead

    @property
    def source(self):
        """Gets the source of this PersonPersonInformation.  


        :return: The source of this PersonPersonInformation.  
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PersonPersonInformation.


        :param source: The source of this PersonPersonInformation.  
        :type: str
        """

        self._source = source

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
        if not isinstance(other, PersonPersonInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
