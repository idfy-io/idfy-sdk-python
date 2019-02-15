# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.email import Email  
from idfy_sdk.models.sms import SMS  


class CanceledReceipt(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email': 'list[Email]',
        'sms': 'list[SMS]'
    }

    attribute_map = {
        'email': 'email',
        'sms': 'sms'
    }

    def __init__(self, email=None, sms=None):  
        """CanceledReceipt"""  

        self._email = None
        self._sms = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if sms is not None:
            self.sms = sms

    @property
    def email(self):
        """Gets the email of this CanceledReceipt.  

        A list of custom email texts to use for the notification. Default texts will be used if not specified.  

        :return: The email of this CanceledReceipt.  
        :rtype: list[Email]
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CanceledReceipt.

        A list of custom email texts to use for the notification. Default texts will be used if not specified.  

        :param email: The email of this CanceledReceipt.  
        :type: list[Email]
        """

        self._email = email

    @property
    def sms(self):
        """Gets the sms of this CanceledReceipt.  

        A list of custom SMS texts to use for the notification. Default texts will be used if not specified.  

        :return: The sms of this CanceledReceipt.  
        :rtype: list[SMS]
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this CanceledReceipt.

        A list of custom SMS texts to use for the notification. Default texts will be used if not specified.  

        :param sms: The sms of this CanceledReceipt.  
        :type: list[SMS]
        """

        self._sms = sms

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
        if not isinstance(other, CanceledReceipt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
