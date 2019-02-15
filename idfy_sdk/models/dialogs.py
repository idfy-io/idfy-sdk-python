# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.dialog_after import DialogAfter  
from idfy_sdk.models.dialog_before import DialogBefore  


class Dialogs(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'before': 'DialogBefore',
        'after': 'DialogAfter'
    }

    attribute_map = {
        'before': 'before',
        'after': 'after'
    }

    def __init__(self, before=None, after=None):  
        """Dialogs"""  

        self._before = None
        self._after = None
        self.discriminator = None

        if before is not None:
            self.before = before
        if after is not None:
            self.after = after

    @property
    def before(self):
        """Gets the before of this Dialogs.  


        :return: The before of this Dialogs.  
        :rtype: DialogBefore
        """
        return self._before

    @before.setter
    def before(self, before):
        """Sets the before of this Dialogs.


        :param before: The before of this Dialogs.  
        :type: DialogBefore
        """

        self._before = before

    @property
    def after(self):
        """Gets the after of this Dialogs.  


        :return: The after of this Dialogs.  
        :rtype: DialogAfter
        """
        return self._after

    @after.setter
    def after(self, after):
        """Sets the after of this Dialogs.


        :param after: The after of this Dialogs.  
        :type: DialogAfter
        """

        self._after = after

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
        if not isinstance(other, Dialogs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
