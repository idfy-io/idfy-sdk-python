# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class TranslationDTO(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'subject_id': 'int',
        'key': 'str',
        'language': 'str',
        'value': 'str',
        'default_value': 'str'
    }

    attribute_map = {
        'subject_id': 'subjectId',
        'key': 'key',
        'language': 'language',
        'value': 'value',
        'default_value': 'defaultValue'
    }

    def __init__(self, subject_id=None, key=None, language=None, value=None, default_value=None):  
        """TranslationDTO"""  

        self._subject_id = None
        self._key = None
        self._language = None
        self._value = None
        self._default_value = None
        self.discriminator = None

        if subject_id is not None:
            self.subject_id = subject_id
        if key is not None:
            self.key = key
        if language is not None:
            self.language = language
        if value is not None:
            self.value = value
        if default_value is not None:
            self.default_value = default_value

    @property
    def subject_id(self):
        """Gets the subject_id of this TranslationDTO.  


        :return: The subject_id of this TranslationDTO.  
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this TranslationDTO.


        :param subject_id: The subject_id of this TranslationDTO.  
        :type: int
        """

        self._subject_id = subject_id

    @property
    def key(self):
        """Gets the key of this TranslationDTO.  


        :return: The key of this TranslationDTO.  
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TranslationDTO.


        :param key: The key of this TranslationDTO.  
        :type: str
        """

        self._key = key

    @property
    def language(self):
        """Gets the language of this TranslationDTO.  


        :return: The language of this TranslationDTO.  
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TranslationDTO.


        :param language: The language of this TranslationDTO.  
        :type: str
        """

        self._language = language

    @property
    def value(self):
        """Gets the value of this TranslationDTO.  


        :return: The value of this TranslationDTO.  
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TranslationDTO.


        :param value: The value of this TranslationDTO.  
        :type: str
        """

        self._value = value

    @property
    def default_value(self):
        """Gets the default_value of this TranslationDTO.  


        :return: The default_value of this TranslationDTO.  
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this TranslationDTO.


        :param default_value: The default_value of this TranslationDTO.  
        :type: str
        """

        self._default_value = default_value

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
        if not isinstance(other, TranslationDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
