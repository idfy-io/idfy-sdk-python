# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class EnvironmentInfo(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_agent': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'user_agent': 'UserAgent',
        'ip_address': 'IPAddress'
    }

    def __init__(self, user_agent=None, ip_address=None):  
        """EnvironmentInfo"""  

        self._user_agent = None
        self._ip_address = None
        self.discriminator = None

        if user_agent is not None:
            self.user_agent = user_agent
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def user_agent(self):
        """Gets the user_agent of this EnvironmentInfo.  

        The users user-agent (browser/device)  

        :return: The user_agent of this EnvironmentInfo.  
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this EnvironmentInfo.

        The users user-agent (browser/device)  

        :param user_agent: The user_agent of this EnvironmentInfo.  
        :type: str
        """

        self._user_agent = user_agent

    @property
    def ip_address(self):
        """Gets the ip_address of this EnvironmentInfo.  

        The IP-address of the user  

        :return: The ip_address of this EnvironmentInfo.  
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this EnvironmentInfo.

        The IP-address of the user  

        :param ip_address: The ip_address of this EnvironmentInfo.  
        :type: str
        """

        self._ip_address = ip_address

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
        if not isinstance(other, EnvironmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
