# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class LeiNormalization(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cleaned': 'str',
        'normalized': 'str'
    }

    attribute_map = {
        'cleaned': 'Cleaned',
        'normalized': 'Normalized'
    }

    def __init__(self, cleaned=None, normalized=None):  
        """LeiNormalization"""  

        self._cleaned = None
        self._normalized = None
        self.discriminator = None

        if cleaned is not None:
            self.cleaned = cleaned
        if normalized is not None:
            self.normalized = normalized

    @property
    def cleaned(self):
        """Gets the cleaned of this LeiNormalization.  


        :return: The cleaned of this LeiNormalization.  
        :rtype: str
        """
        return self._cleaned

    @cleaned.setter
    def cleaned(self, cleaned):
        """Sets the cleaned of this LeiNormalization.


        :param cleaned: The cleaned of this LeiNormalization.  
        :type: str
        """

        self._cleaned = cleaned

    @property
    def normalized(self):
        """Gets the normalized of this LeiNormalization.  


        :return: The normalized of this LeiNormalization.  
        :rtype: str
        """
        return self._normalized

    @normalized.setter
    def normalized(self, normalized):
        """Sets the normalized of this LeiNormalization.


        :param normalized: The normalized of this LeiNormalization.  
        :type: str
        """

        self._normalized = normalized

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
        if not isinstance(other, LeiNormalization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
