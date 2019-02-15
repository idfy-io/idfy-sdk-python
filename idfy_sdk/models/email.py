# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Email(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'language': 'str',
        'subject': 'str',
        'text': 'str',
        'sender_name': 'str'
    }

    attribute_map = {
        'language': 'language',
        'subject': 'subject',
        'text': 'text',
        'sender_name': 'senderName'
    }

    def __init__(self, language=None, subject=None, text=None, sender_name=None):  
        """Email"""  

        self._language = None
        self._subject = None
        self._text = None
        self._sender_name = None
        self.discriminator = None

        self.language = language
        if subject is not None:
            self.subject = subject
        if text is not None:
            self.text = text
        if sender_name is not None:
            self.sender_name = sender_name

    @property
    def language(self):
        """Gets the language of this Email.  

        The language of the email notification.  

        :return: The language of this Email.  
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Email.

        The language of the email notification.  

        :param language: The language of this Email.  
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
    def subject(self):
        """Gets the subject of this Email.  

        The email subject.  

        :return: The subject of this Email.  
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Email.

        The email subject.  

        :param subject: The subject of this Email.  
        :type: str
        """

        self._subject = subject

    @property
    def text(self):
        """Gets the text of this Email.  

        The email notification body. Plain text and markdown is supported.  

        :return: The text of this Email.  
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Email.

        The email notification body. Plain text and markdown is supported.  

        :param text: The text of this Email.  
        :type: str
        """

        self._text = text

    @property
    def sender_name(self):
        """Gets the sender_name of this Email.  

        The name to use as email sender.  

        :return: The sender_name of this Email.  
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """Sets the sender_name of this Email.

        The name to use as email sender.  

        :param sender_name: The sender_name of this Email.  
        :type: str
        """

        self._sender_name = sender_name

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
        if not isinstance(other, Email):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
