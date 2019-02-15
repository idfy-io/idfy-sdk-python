# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.notifications_setup import NotificationsSetup  


class Notifications(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'setup': 'NotificationsSetup',
        'merge_fields': 'dict(str, str)'
    }

    attribute_map = {
        'setup': 'setup',
        'merge_fields': 'mergeFields'
    }

    def __init__(self, setup=None, merge_fields=None):  
        """Notifications"""  

        self._setup = None
        self._merge_fields = None
        self.discriminator = None

        if setup is not None:
            self.setup = setup
        if merge_fields is not None:
            self.merge_fields = merge_fields

    @property
    def setup(self):
        """Gets the setup of this Notifications.  


        :return: The setup of this Notifications.  
        :rtype: NotificationsSetup
        """
        return self._setup

    @setup.setter
    def setup(self, setup):
        """Sets the setup of this Notifications.


        :param setup: The setup of this Notifications.  
        :type: NotificationsSetup
        """

        self._setup = setup

    @property
    def merge_fields(self):
        """Gets the merge_fields of this Notifications.  

        If you create your own notifications texts (See the root object -&gt; Notification), you can create your own merge fields with your own keys.   You can then specify the text you want to insert in these fields per signer in this dictionary. Set the dictionary key to the same value as the merge field value in your notification text, and the value to the text you want us to merge in.  

        :return: The merge_fields of this Notifications.  
        :rtype: dict(str, str)
        """
        return self._merge_fields

    @merge_fields.setter
    def merge_fields(self, merge_fields):
        """Sets the merge_fields of this Notifications.

        If you create your own notifications texts (See the root object -&gt; Notification), you can create your own merge fields with your own keys.   You can then specify the text you want to insert in these fields per signer in this dictionary. Set the dictionary key to the same value as the merge field value in your notification text, and the value to the text you want us to merge in.  

        :param merge_fields: The merge_fields of this Notifications.  
        :type: dict(str, str)
        """

        self._merge_fields = merge_fields

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
        if not isinstance(other, Notifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
