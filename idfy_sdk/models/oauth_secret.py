# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class OauthSecret(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'value': 'str',
        'expiration': 'datetime',
        'type': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'value': 'Value',
        'expiration': 'Expiration',
        'type': 'Type'
    }

    def __init__(self, description=None, value=None, expiration=None, type=None):  
        """OauthSecret"""  

        self._description = None
        self._value = None
        self._expiration = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if value is not None:
            self.value = value
        if expiration is not None:
            self.expiration = expiration
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this OauthSecret.  


        :return: The description of this OauthSecret.  
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OauthSecret.


        :param description: The description of this OauthSecret.  
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """Gets the value of this OauthSecret.  


        :return: The value of this OauthSecret.  
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OauthSecret.


        :param value: The value of this OauthSecret.  
        :type: str
        """

        self._value = value

    @property
    def expiration(self):
        """Gets the expiration of this OauthSecret.  


        :return: The expiration of this OauthSecret.  
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this OauthSecret.


        :param expiration: The expiration of this OauthSecret.  
        :type: datetime
        """

        self._expiration = expiration

    @property
    def type(self):
        """Gets the type of this OauthSecret.  


        :return: The type of this OauthSecret.  
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OauthSecret.


        :param type: The type of this OauthSecret.  
        :type: str
        """

        self._type = type

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
        if not isinstance(other, OauthSecret):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
