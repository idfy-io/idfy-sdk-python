# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class ContactDetails(object):

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
        'email': 'str',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'phone': 'phone',
        'email': 'email',
        'url': 'url'
    }

    def __init__(self, name=None, phone=None, email=None, url=None):  
        """ContactDetails"""  

        self._name = None
        self._phone = None
        self._email = None
        self._url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        self.email = email
        if url is not None:
            self.url = url

    @property
    def name(self):
        """Gets the name of this ContactDetails.  

        The name of the company.  

        :return: The name of this ContactDetails.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContactDetails.

        The name of the company.  

        :param name: The name of this ContactDetails.  
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this ContactDetails.  

        The phone number of the company.  

        :return: The phone of this ContactDetails.  
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ContactDetails.

        The phone number of the company.  

        :param phone: The phone of this ContactDetails.  
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this ContactDetails.  

        The email address of the company.  

        :return: The email of this ContactDetails.  
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactDetails.

        The email address of the company.  

        :param email: The email of this ContactDetails.  
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  

        self._email = email

    @property
    def url(self):
        """Gets the url of this ContactDetails.  

        The URL to the company's website.  

        :return: The url of this ContactDetails.  
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ContactDetails.

        The URL to the company's website.  

        :param url: The url of this ContactDetails.  
        :type: str
        """

        self._url = url

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
        if not isinstance(other, ContactDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
