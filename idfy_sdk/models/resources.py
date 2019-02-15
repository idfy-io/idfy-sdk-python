# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Resources(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'logo_url': 'str',
        'css_url': 'str'
    }

    attribute_map = {
        'logo_url': 'LogoUrl',
        'css_url': 'CssUrl'
    }

    def __init__(self, logo_url=None, css_url=None):  
        """Resources"""  

        self._logo_url = None
        self._css_url = None
        self.discriminator = None

        if logo_url is not None:
            self.logo_url = logo_url
        if css_url is not None:
            self.css_url = css_url

    @property
    def logo_url(self):
        """Gets the logo_url of this Resources.  

        The logo uploaded to this account  

        :return: The logo_url of this Resources.  
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this Resources.

        The logo uploaded to this account  

        :param logo_url: The logo_url of this Resources.  
        :type: str
        """

        self._logo_url = logo_url

    @property
    def css_url(self):
        """Gets the css_url of this Resources.  

        Custom css uploaded to this account  

        :return: The css_url of this Resources.  
        :rtype: str
        """
        return self._css_url

    @css_url.setter
    def css_url(self, css_url):
        """Sets the css_url of this Resources.

        Custom css uploaded to this account  

        :param css_url: The css_url of this Resources.  
        :type: str
        """

        self._css_url = css_url

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
        if not isinstance(other, Resources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
