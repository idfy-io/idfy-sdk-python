# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.signer_overrides import SignerOverrides  


class ManualReminder(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'notification_setting': 'str',
        'signers': 'dict(str, SignerOverrides)'
    }

    attribute_map = {
        'notification_setting': 'notificationSetting',
        'signers': 'signers'
    }

    def __init__(self, notification_setting=None, signers=None):  
        """ManualReminder"""  

        self._notification_setting = None
        self._signers = None
        self.discriminator = None

        self.notification_setting = notification_setting
        if signers is not None:
            self.signers = signers

    @property
    def notification_setting(self):
        """Gets the notification_setting of this ManualReminder.  

        Set what kind of reminders to send  

        :return: The notification_setting of this ManualReminder.  
        :rtype: str
        """
        return self._notification_setting

    @notification_setting.setter
    def notification_setting(self, notification_setting):
        """Sets the notification_setting of this ManualReminder.

        Set what kind of reminders to send  

        :param notification_setting: The notification_setting of this ManualReminder.  
        :type: str
        """
        if notification_setting is None:
            raise ValueError("Invalid value for `notification_setting`, must not be `None`")  
        allowed_values = ["off", "sendSms", "sendEmail", "sendBoth"]  
        if notification_setting not in allowed_values:
            raise ValueError(
                "Invalid value for `notification_setting` ({0}), must be one of {1}"  
                .format(notification_setting, allowed_values)
            )

        self._notification_setting = notification_setting

    @property
    def signers(self):
        """Gets the signers of this ManualReminder.  

        Optional: Define the signers that should receive this reminder (if not signed). Dictionary with signer id as key, you can ovveride the signer email/phone as value  

        :return: The signers of this ManualReminder.  
        :rtype: dict(str, SignerOverrides)
        """
        return self._signers

    @signers.setter
    def signers(self, signers):
        """Sets the signers of this ManualReminder.

        Optional: Define the signers that should receive this reminder (if not signed). Dictionary with signer id as key, you can ovveride the signer email/phone as value  

        :param signers: The signers of this ManualReminder.  
        :type: dict(str, SignerOverrides)
        """

        self._signers = signers

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
        if not isinstance(other, ManualReminder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
