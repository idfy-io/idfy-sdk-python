# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.lei_normalization import LeiNormalization  


class LeiNormalizations(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'legal_name': 'LeiNormalization'
    }

    attribute_map = {
        'legal_name': 'LegalName'
    }

    def __init__(self, legal_name=None):  
        """LeiNormalizations"""  

        self._legal_name = None
        self.discriminator = None

        if legal_name is not None:
            self.legal_name = legal_name

    @property
    def legal_name(self):
        """Gets the legal_name of this LeiNormalizations.  


        :return: The legal_name of this LeiNormalizations.  
        :rtype: LeiNormalization
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this LeiNormalizations.


        :param legal_name: The legal_name of this LeiNormalizations.  
        :type: LeiNormalization
        """

        self._legal_name = legal_name

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
        if not isinstance(other, LeiNormalizations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
