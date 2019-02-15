# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.dialogs import Dialogs  
from idfy_sdk.models.styling import Styling  


class UI(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'language': 'str',
        'dialogs': 'Dialogs',
        'styling': 'Styling'
    }

    attribute_map = {
        'language': 'language',
        'dialogs': 'dialogs',
        'styling': 'styling'
    }

    def __init__(self, language=None, dialogs=None, styling=None):  
        """UI"""  

        self._language = None
        self._dialogs = None
        self._styling = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if dialogs is not None:
            self.dialogs = dialogs
        if styling is not None:
            self.styling = styling

    @property
    def language(self):
        """Gets the language of this UI.  

        The signer's preferred language. This language will be used when signing the document and in email/SMS notifications.  ///  

        :return: The language of this UI.  
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UI.

        The signer's preferred language. This language will be used when signing the document and in email/SMS notifications.  ///  

        :param language: The language of this UI.  
        :type: str
        """
        allowed_values = ["EN", "NO", "DA", "SV", "FI"]  
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def dialogs(self):
        """Gets the dialogs of this UI.  


        :return: The dialogs of this UI.  
        :rtype: Dialogs
        """
        return self._dialogs

    @dialogs.setter
    def dialogs(self, dialogs):
        """Sets the dialogs of this UI.


        :param dialogs: The dialogs of this UI.  
        :type: Dialogs
        """

        self._dialogs = dialogs

    @property
    def styling(self):
        """Gets the styling of this UI.  


        :return: The styling of this UI.  
        :rtype: Styling
        """
        return self._styling

    @styling.setter
    def styling(self, styling):
        """Sets the styling of this UI.


        :param styling: The styling of this UI.  
        :type: Styling
        """

        self._styling = styling

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
        if not isinstance(other, UI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
