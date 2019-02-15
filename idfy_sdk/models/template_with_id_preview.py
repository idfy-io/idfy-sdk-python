# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class TemplateWithIdPreview(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'primary_language': 'str',
        'secondary_language': 'str',
        'xml_signature': 'str'
    }

    attribute_map = {
        'primary_language': 'PrimaryLanguage',
        'secondary_language': 'SecondaryLanguage',
        'xml_signature': 'XmlSignature'
    }

    def __init__(self, primary_language=None, secondary_language=None, xml_signature=None):  
        """TemplateWithIdPreview"""  

        self._primary_language = None
        self._secondary_language = None
        self._xml_signature = None
        self.discriminator = None

        self.primary_language = primary_language
        if secondary_language is not None:
            self.secondary_language = secondary_language
        if xml_signature is not None:
            self.xml_signature = xml_signature

    @property
    def primary_language(self):
        """Gets the primary_language of this TemplateWithIdPreview.  

        Primary language to use in the preview (required)  

        :return: The primary_language of this TemplateWithIdPreview.  
        :rtype: str
        """
        return self._primary_language

    @primary_language.setter
    def primary_language(self, primary_language):
        """Sets the primary_language of this TemplateWithIdPreview.

        Primary language to use in the preview (required)  

        :param primary_language: The primary_language of this TemplateWithIdPreview.  
        :type: str
        """
        if primary_language is None:
            raise ValueError("Invalid value for `primary_language`, must not be `None`")  
        allowed_values = ["en", "no", "sv", "da", "fi"]  
        if primary_language not in allowed_values:
            raise ValueError(
                "Invalid value for `primary_language` ({0}), must be one of {1}"  
                .format(primary_language, allowed_values)
            )

        self._primary_language = primary_language

    @property
    def secondary_language(self):
        """Gets the secondary_language of this TemplateWithIdPreview.  

        Secondary language to use in the prewview (optional)  

        :return: The secondary_language of this TemplateWithIdPreview.  
        :rtype: str
        """
        return self._secondary_language

    @secondary_language.setter
    def secondary_language(self, secondary_language):
        """Sets the secondary_language of this TemplateWithIdPreview.

        Secondary language to use in the prewview (optional)  

        :param secondary_language: The secondary_language of this TemplateWithIdPreview.  
        :type: str
        """
        allowed_values = ["en", "no", "sv", "da", "fi"]  
        if secondary_language not in allowed_values:
            raise ValueError(
                "Invalid value for `secondary_language` ({0}), must be one of {1}"  
                .format(secondary_language, allowed_values)
            )

        self._secondary_language = secondary_language

    @property
    def xml_signature(self):
        """Gets the xml_signature of this TemplateWithIdPreview.  

        Xml package signature in base64 encoding  

        :return: The xml_signature of this TemplateWithIdPreview.  
        :rtype: str
        """
        return self._xml_signature

    @xml_signature.setter
    def xml_signature(self, xml_signature):
        """Sets the xml_signature of this TemplateWithIdPreview.

        Xml package signature in base64 encoding  

        :param xml_signature: The xml_signature of this TemplateWithIdPreview.  
        :type: str
        """

        self._xml_signature = xml_signature

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
        if not isinstance(other, TemplateWithIdPreview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
