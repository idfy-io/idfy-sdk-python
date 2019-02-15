# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class IFrameSettings(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'domain': 'str',
        'web_messaging': 'bool',
        'height': 'int'
    }

    attribute_map = {
        'domain': 'Domain',
        'web_messaging': 'WebMessaging',
        'height': 'Height'
    }

    def __init__(self, domain=None, web_messaging=None, height=None):  
        """IFrameSettings"""  

        self._domain = None
        self._web_messaging = None
        self._height = None
        self.discriminator = None

        self.domain = domain
        if web_messaging is not None:
            self.web_messaging = web_messaging
        if height is not None:
            self.height = height

    @property
    def domain(self):
        """Gets the domain of this IFrameSettings.  

        The domain of the site hosting the iFrame, this is used for the CSP policy and must be correct.  

        :return: The domain of this IFrameSettings.  
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this IFrameSettings.

        The domain of the site hosting the iFrame, this is used for the CSP policy and must be correct.  

        :param domain: The domain of this IFrameSettings.  
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  

        self._domain = domain

    @property
    def web_messaging(self):
        """Gets the web_messaging of this IFrameSettings.  

        Should WebMessaging be used for redirect of the iFrame parent, modern browsers have some issues with childs redirecting parents without the same origin. To use this include this script: https://signerecommon.blob.core.windows.net/files/signereid_webmessaging.js  

        :return: The web_messaging of this IFrameSettings.  
        :rtype: bool
        """
        return self._web_messaging

    @web_messaging.setter
    def web_messaging(self, web_messaging):
        """Sets the web_messaging of this IFrameSettings.

        Should WebMessaging be used for redirect of the iFrame parent, modern browsers have some issues with childs redirecting parents without the same origin. To use this include this script: https://signerecommon.blob.core.windows.net/files/signereid_webmessaging.js  

        :param web_messaging: The web_messaging of this IFrameSettings.  
        :type: bool
        """

        self._web_messaging = web_messaging

    @property
    def height(self):
        """Gets the height of this IFrameSettings.  

        Height of the frame when used in iFrame.  

        :return: The height of this IFrameSettings.  
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this IFrameSettings.

        Height of the frame when used in iFrame.  

        :param height: The height of this IFrameSettings.  
        :type: int
        """

        self._height = height

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
        if not isinstance(other, IFrameSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
