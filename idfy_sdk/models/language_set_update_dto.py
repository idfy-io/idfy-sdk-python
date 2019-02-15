# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class LanguageSetUpdateDTO(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'is_active': 'isActive'
    }

    def __init__(self, name=None, is_active=None):  
        """LanguageSetUpdateDTO"""  

        self._name = None
        self._is_active = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if is_active is not None:
            self.is_active = is_active

    @property
    def name(self):
        """Gets the name of this LanguageSetUpdateDTO.  


        :return: The name of this LanguageSetUpdateDTO.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LanguageSetUpdateDTO.


        :param name: The name of this LanguageSetUpdateDTO.  
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  

        self._name = name

    @property
    def is_active(self):
        """Gets the is_active of this LanguageSetUpdateDTO.  


        :return: The is_active of this LanguageSetUpdateDTO.  
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this LanguageSetUpdateDTO.


        :param is_active: The is_active of this LanguageSetUpdateDTO.  
        :type: bool
        """

        self._is_active = is_active

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
        if not isinstance(other, LanguageSetUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other