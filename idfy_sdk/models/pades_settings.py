# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PadesSettings(object):

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
        'pades_template_id': 'str'
    }

    attribute_map = {
        'primary_language': 'primaryLanguage',
        'secondary_language': 'secondaryLanguage',
        'pades_template_id': 'padesTemplateId'
    }

    def __init__(self, primary_language=None, secondary_language=None, pades_template_id=None):  
        """PadesSettings"""  

        self._primary_language = None
        self._secondary_language = None
        self._pades_template_id = None
        self.discriminator = None

        if primary_language is not None:
            self.primary_language = primary_language
        if secondary_language is not None:
            self.secondary_language = secondary_language
        if pades_template_id is not None:
            self.pades_template_id = pades_template_id

    @property
    def primary_language(self):
        """Gets the primary_language of this PadesSettings.  

        The primary language of the PAdES explanatory page. Defaults to english.  

        :return: The primary_language of this PadesSettings.  
        :rtype: str
        """
        return self._primary_language

    @primary_language.setter
    def primary_language(self, primary_language):
        """Sets the primary_language of this PadesSettings.

        The primary language of the PAdES explanatory page. Defaults to english.  

        :param primary_language: The primary_language of this PadesSettings.  
        :type: str
        """
        allowed_values = ["EN", "NO", "DA", "SV", "FI"]  
        if primary_language not in allowed_values:
            raise ValueError(
                "Invalid value for `primary_language` ({0}), must be one of {1}"  
                .format(primary_language, allowed_values)
            )

        self._primary_language = primary_language

    @property
    def secondary_language(self):
        """Gets the secondary_language of this PadesSettings.  

        The secondary language of the PAdES explanatory page.  

        :return: The secondary_language of this PadesSettings.  
        :rtype: str
        """
        return self._secondary_language

    @secondary_language.setter
    def secondary_language(self, secondary_language):
        """Sets the secondary_language of this PadesSettings.

        The secondary language of the PAdES explanatory page.  

        :param secondary_language: The secondary_language of this PadesSettings.  
        :type: str
        """
        allowed_values = ["EN", "NO", "DA", "SV", "FI"]  
        if secondary_language not in allowed_values:
            raise ValueError(
                "Invalid value for `secondary_language` ({0}), must be one of {1}"  
                .format(secondary_language, allowed_values)
            )

        self._secondary_language = secondary_language

    @property
    def pades_template_id(self):
        """Gets the pades_template_id of this PadesSettings.  

        The unique ID of PAdES template to use. Can be used if you have previously created your own custom template.  

        :return: The pades_template_id of this PadesSettings.  
        :rtype: str
        """
        return self._pades_template_id

    @pades_template_id.setter
    def pades_template_id(self, pades_template_id):
        """Sets the pades_template_id of this PadesSettings.

        The unique ID of PAdES template to use. Can be used if you have previously created your own custom template.  

        :param pades_template_id: The pades_template_id of this PadesSettings.  
        :type: str
        """

        self._pades_template_id = pades_template_id

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
        if not isinstance(other, PadesSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
