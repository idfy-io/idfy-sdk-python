# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Identifikasjon(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'orgnr_field': 'int',
        'dunsnr_field': 'int'
    }

    attribute_map = {
        'orgnr_field': 'orgnrField',
        'dunsnr_field': 'dunsnrField'
    }

    def __init__(self, orgnr_field=None, dunsnr_field=None):  
        """Identifikasjon"""  

        self._orgnr_field = None
        self._dunsnr_field = None
        self.discriminator = None

        if orgnr_field is not None:
            self.orgnr_field = orgnr_field
        if dunsnr_field is not None:
            self.dunsnr_field = dunsnr_field

    @property
    def orgnr_field(self):
        """Gets the orgnr_field of this Identifikasjon.  


        :return: The orgnr_field of this Identifikasjon.  
        :rtype: int
        """
        return self._orgnr_field

    @orgnr_field.setter
    def orgnr_field(self, orgnr_field):
        """Sets the orgnr_field of this Identifikasjon.


        :param orgnr_field: The orgnr_field of this Identifikasjon.  
        :type: int
        """

        self._orgnr_field = orgnr_field

    @property
    def dunsnr_field(self):
        """Gets the dunsnr_field of this Identifikasjon.  


        :return: The dunsnr_field of this Identifikasjon.  
        :rtype: int
        """
        return self._dunsnr_field

    @dunsnr_field.setter
    def dunsnr_field(self, dunsnr_field):
        """Sets the dunsnr_field of this Identifikasjon.


        :param dunsnr_field: The dunsnr_field of this Identifikasjon.  
        :type: int
        """

        self._dunsnr_field = dunsnr_field

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
        if not isinstance(other, Identifikasjon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
