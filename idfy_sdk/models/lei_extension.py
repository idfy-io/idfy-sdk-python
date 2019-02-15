# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.lei_normalizations import LeiNormalizations  


class LeiExtension(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'normalizations': 'LeiNormalizations'
    }

    attribute_map = {
        'normalizations': 'Normalizations'
    }

    def __init__(self, normalizations=None):  
        """LeiExtension"""  

        self._normalizations = None
        self.discriminator = None

        if normalizations is not None:
            self.normalizations = normalizations

    @property
    def normalizations(self):
        """Gets the normalizations of this LeiExtension.  


        :return: The normalizations of this LeiExtension.  
        :rtype: LeiNormalizations
        """
        return self._normalizations

    @normalizations.setter
    def normalizations(self, normalizations):
        """Sets the normalizations of this LeiExtension.


        :param normalizations: The normalizations of this LeiExtension.  
        :type: LeiNormalizations
        """

        self._normalizations = normalizations

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
        if not isinstance(other, LeiExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
