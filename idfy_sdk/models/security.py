# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Security(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'one_time_use': 'bool',
        'ip_white_list': 'list[str]'
    }

    attribute_map = {
        'one_time_use': 'oneTimeUse',
        'ip_white_list': 'ipWhiteList'
    }

    def __init__(self, one_time_use=None, ip_white_list=None):  
        """Security"""  

        self._one_time_use = None
        self._ip_white_list = None
        self.discriminator = None

        if one_time_use is not None:
            self.one_time_use = one_time_use
        if ip_white_list is not None:
            self.ip_white_list = ip_white_list

    @property
    def one_time_use(self):
        """Gets the one_time_use of this Security.  

        (Coming soon) Determines if the link is one-time use.  

        :return: The one_time_use of this Security.  
        :rtype: bool
        """
        return self._one_time_use

    @one_time_use.setter
    def one_time_use(self, one_time_use):
        """Sets the one_time_use of this Security.

        (Coming soon) Determines if the link is one-time use.  

        :param one_time_use: The one_time_use of this Security.  
        :type: bool
        """

        self._one_time_use = one_time_use

    @property
    def ip_white_list(self):
        """Gets the ip_white_list of this Security.  

        (Coming soon) A list of IP addresses that are allowed to see / sign the document.  

        :return: The ip_white_list of this Security.  
        :rtype: list[str]
        """
        return self._ip_white_list

    @ip_white_list.setter
    def ip_white_list(self, ip_white_list):
        """Sets the ip_white_list of this Security.

        (Coming soon) A list of IP addresses that are allowed to see / sign the document.  

        :param ip_white_list: The ip_white_list of this Security.  
        :type: list[str]
        """

        self._ip_white_list = ip_white_list

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
        if not isinstance(other, Security):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
