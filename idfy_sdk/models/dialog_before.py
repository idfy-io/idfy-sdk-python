# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class DialogBefore(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'use_check_box': 'bool',
        'title': 'str',
        'message': 'str'
    }

    attribute_map = {
        'use_check_box': 'useCheckBox',
        'title': 'title',
        'message': 'message'
    }

    def __init__(self, use_check_box=None, title=None, message=None):  
        """DialogBefore"""  

        self._use_check_box = None
        self._title = None
        self._message = None
        self.discriminator = None

        if use_check_box is not None:
            self.use_check_box = use_check_box
        if title is not None:
            self.title = title
        if message is not None:
            self.message = message

    @property
    def use_check_box(self):
        """Gets the use_check_box of this DialogBefore.  

        Determines if a the user must confirm that the dialog message has been read before they can continue.  

        :return: The use_check_box of this DialogBefore.  
        :rtype: bool
        """
        return self._use_check_box

    @use_check_box.setter
    def use_check_box(self, use_check_box):
        """Sets the use_check_box of this DialogBefore.

        Determines if a the user must confirm that the dialog message has been read before they can continue.  

        :param use_check_box: The use_check_box of this DialogBefore.  
        :type: bool
        """

        self._use_check_box = use_check_box

    @property
    def title(self):
        """Gets the title of this DialogBefore.  

        The title of the dialog.  

        :return: The title of this DialogBefore.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DialogBefore.

        The title of the dialog.  

        :param title: The title of this DialogBefore.  
        :type: str
        """

        self._title = title

    @property
    def message(self):
        """Gets the message of this DialogBefore.  

        The message body of the dialog.  

        :return: The message of this DialogBefore.  
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DialogBefore.

        The message body of the dialog.  

        :param message: The message of this DialogBefore.  
        :type: str
        """

        self._message = message

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
        if not isinstance(other, DialogBefore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
