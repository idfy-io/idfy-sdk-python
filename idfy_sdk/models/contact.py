# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Contact(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'phone': 'str',
        'mobile': 'str',
        'email': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'phone': 'Phone',
        'mobile': 'Mobile',
        'email': 'Email'
    }

    def __init__(self, name=None, phone=None, mobile=None, email=None):  
        """Contact"""  

        self._name = None
        self._phone = None
        self._mobile = None
        self._email = None
        self.discriminator = None

        self.name = name
        if phone is not None:
            self.phone = phone
        self.mobile = mobile
        self.email = email

    @property
    def name(self):
        """Gets the name of this Contact.  


        :return: The name of this Contact.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Contact.


        :param name: The name of this Contact.  
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this Contact.  


        :return: The phone of this Contact.  
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Contact.


        :param phone: The phone of this Contact.  
        :type: str
        """

        self._phone = phone

    @property
    def mobile(self):
        """Gets the mobile of this Contact.  


        :return: The mobile of this Contact.  
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this Contact.


        :param mobile: The mobile of this Contact.  
        :type: str
        """
        if mobile is None:
            raise ValueError("Invalid value for `mobile`, must not be `None`")  

        self._mobile = mobile

    @property
    def email(self):
        """Gets the email of this Contact.  


        :return: The email of this Contact.  
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Contact.


        :param email: The email of this Contact.  
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  

        self._email = email

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
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
