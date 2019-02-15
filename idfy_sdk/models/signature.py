# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Signature(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'date_of_birth': 'str',
        'role': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'date_of_birth': 'DateOfBirth',
        'role': 'Role'
    }

    def __init__(self, name=None, date_of_birth=None, role=None):  
        """Signature"""  

        self._name = None
        self._date_of_birth = None
        self._role = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if role is not None:
            self.role = role

    @property
    def name(self):
        """Gets the name of this Signature.  


        :return: The name of this Signature.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Signature.


        :param name: The name of this Signature.  
        :type: str
        """

        self._name = name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this Signature.  


        :return: The date_of_birth of this Signature.  
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this Signature.


        :param date_of_birth: The date_of_birth of this Signature.  
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def role(self):
        """Gets the role of this Signature.  


        :return: The role of this Signature.  
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Signature.


        :param role: The role of this Signature.  
        :type: str
        """

        self._role = role

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
        if not isinstance(other, Signature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
