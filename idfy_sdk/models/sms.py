# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class SMS(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'language': 'str',
        'text': 'str',
        'sender': 'str'
    }

    attribute_map = {
        'language': 'language',
        'text': 'text',
        'sender': 'sender'
    }

    def __init__(self, language=None, text=None, sender=None):  
        """SMS"""  

        self._language = None
        self._text = None
        self._sender = None
        self.discriminator = None

        self.language = language
        if text is not None:
            self.text = text
        if sender is not None:
            self.sender = sender

    @property
    def language(self):
        """Gets the language of this SMS.  

        The language of the SMS notification.  

        :return: The language of this SMS.  
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SMS.

        The language of the SMS notification.  

        :param language: The language of this SMS.  
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  
        allowed_values = ["EN", "NO", "DA", "SV", "FI"]  
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def text(self):
        """Gets the text of this SMS.  

        The SMS notification text.  

        :return: The text of this SMS.  
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SMS.

        The SMS notification text.  

        :param text: The text of this SMS.  
        :type: str
        """

        self._text = text

    @property
    def sender(self):
        """Gets the sender of this SMS.  

        The name to use as SMS sender.  

        :return: The sender of this SMS.  
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this SMS.

        The name to use as SMS sender.  

        :param sender: The sender of this SMS.  
        :type: str
        """

        self._sender = sender

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
        if not isinstance(other, SMS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
