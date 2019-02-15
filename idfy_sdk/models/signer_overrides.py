# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.mobile import Mobile  


class SignerOverrides(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email_override': 'str',
        'mobile_override': 'Mobile'
    }

    attribute_map = {
        'email_override': 'emailOverride',
        'mobile_override': 'mobileOverride'
    }

    def __init__(self, email_override=None, mobile_override=None):  
        """SignerOverrides"""  

        self._email_override = None
        self._mobile_override = None
        self.discriminator = None

        if email_override is not None:
            self.email_override = email_override
        if mobile_override is not None:
            self.mobile_override = mobile_override

    @property
    def email_override(self):
        """Gets the email_override of this SignerOverrides.  

        Set a new email address on the signer (all fututre notifications to this specific signer will be sent to this email)  

        :return: The email_override of this SignerOverrides.  
        :rtype: str
        """
        return self._email_override

    @email_override.setter
    def email_override(self, email_override):
        """Sets the email_override of this SignerOverrides.

        Set a new email address on the signer (all fututre notifications to this specific signer will be sent to this email)  

        :param email_override: The email_override of this SignerOverrides.  
        :type: str
        """

        self._email_override = email_override

    @property
    def mobile_override(self):
        """Gets the mobile_override of this SignerOverrides.  


        :return: The mobile_override of this SignerOverrides.  
        :rtype: Mobile
        """
        return self._mobile_override

    @mobile_override.setter
    def mobile_override(self, mobile_override):
        """Sets the mobile_override of this SignerOverrides.


        :param mobile_override: The mobile_override of this SignerOverrides.  
        :type: Mobile
        """

        self._mobile_override = mobile_override

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
        if not isinstance(other, SignerOverrides):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
