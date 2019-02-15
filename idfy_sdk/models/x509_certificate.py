# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class X509Certificate(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'raw_data': 'str'
    }

    attribute_map = {
        'raw_data': 'rawData'
    }

    def __init__(self, raw_data=None):  
        """X509Certificate"""  

        self._raw_data = None
        self.discriminator = None

        if raw_data is not None:
            self.raw_data = raw_data

    @property
    def raw_data(self):
        """Gets the raw_data of this X509Certificate.  


        :return: The raw_data of this X509Certificate.  
        :rtype: str
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this X509Certificate.


        :param raw_data: The raw_data of this X509Certificate.  
        :type: str
        """

        self._raw_data = raw_data

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
        if not isinstance(other, X509Certificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
