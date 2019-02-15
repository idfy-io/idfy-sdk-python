# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Onboarding(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'heading': 'str',
        'lead_paragraph': 'str',
        'logo_url': 'str',
        'return_url': 'str'
    }

    attribute_map = {
        'heading': 'Heading',
        'lead_paragraph': 'LeadParagraph',
        'logo_url': 'LogoUrl',
        'return_url': 'ReturnUrl'
    }

    def __init__(self, heading=None, lead_paragraph=None, logo_url=None, return_url=None):  
        """Onboarding"""  

        self._heading = None
        self._lead_paragraph = None
        self._logo_url = None
        self._return_url = None
        self.discriminator = None

        if heading is not None:
            self.heading = heading
        if lead_paragraph is not None:
            self.lead_paragraph = lead_paragraph
        if logo_url is not None:
            self.logo_url = logo_url
        if return_url is not None:
            self.return_url = return_url

    @property
    def heading(self):
        """Gets the heading of this Onboarding.  


        :return: The heading of this Onboarding.  
        :rtype: str
        """
        return self._heading

    @heading.setter
    def heading(self, heading):
        """Sets the heading of this Onboarding.


        :param heading: The heading of this Onboarding.  
        :type: str
        """

        self._heading = heading

    @property
    def lead_paragraph(self):
        """Gets the lead_paragraph of this Onboarding.  


        :return: The lead_paragraph of this Onboarding.  
        :rtype: str
        """
        return self._lead_paragraph

    @lead_paragraph.setter
    def lead_paragraph(self, lead_paragraph):
        """Sets the lead_paragraph of this Onboarding.


        :param lead_paragraph: The lead_paragraph of this Onboarding.  
        :type: str
        """

        self._lead_paragraph = lead_paragraph

    @property
    def logo_url(self):
        """Gets the logo_url of this Onboarding.  


        :return: The logo_url of this Onboarding.  
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this Onboarding.


        :param logo_url: The logo_url of this Onboarding.  
        :type: str
        """

        self._logo_url = logo_url

    @property
    def return_url(self):
        """Gets the return_url of this Onboarding.  


        :return: The return_url of this Onboarding.  
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """Sets the return_url of this Onboarding.


        :param return_url: The return_url of this Onboarding.  
        :type: str
        """

        self._return_url = return_url

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
        if not isinstance(other, Onboarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
