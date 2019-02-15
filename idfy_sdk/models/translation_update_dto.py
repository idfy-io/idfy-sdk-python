# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class TranslationUpdateDTO(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'value': 'str'
    }

    attribute_map = {
        'value': 'value'
    }

    def __init__(self, value=None):  
        """TranslationUpdateDTO"""  

        self._value = None
        self.discriminator = None

        self.value = value

    @property
    def value(self):
        """Gets the value of this TranslationUpdateDTO.  


        :return: The value of this TranslationUpdateDTO.  
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TranslationUpdateDTO.


        :param value: The value of this TranslationUpdateDTO.  
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  
        if value is not None and len(value) > 2500:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `2500`")  
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  

        self._value = value

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
        if not isinstance(other, TranslationUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
