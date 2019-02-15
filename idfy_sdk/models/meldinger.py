# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Meldinger(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'meldings_kode_field': 'int',
        'meldings_tekst_field': 'str'
    }

    attribute_map = {
        'meldings_kode_field': 'meldingsKodeField',
        'meldings_tekst_field': 'meldingsTekstField'
    }

    def __init__(self, meldings_kode_field=None, meldings_tekst_field=None):  
        """Meldinger"""  

        self._meldings_kode_field = None
        self._meldings_tekst_field = None
        self.discriminator = None

        if meldings_kode_field is not None:
            self.meldings_kode_field = meldings_kode_field
        if meldings_tekst_field is not None:
            self.meldings_tekst_field = meldings_tekst_field

    @property
    def meldings_kode_field(self):
        """Gets the meldings_kode_field of this Meldinger.  


        :return: The meldings_kode_field of this Meldinger.  
        :rtype: int
        """
        return self._meldings_kode_field

    @meldings_kode_field.setter
    def meldings_kode_field(self, meldings_kode_field):
        """Sets the meldings_kode_field of this Meldinger.


        :param meldings_kode_field: The meldings_kode_field of this Meldinger.  
        :type: int
        """

        self._meldings_kode_field = meldings_kode_field

    @property
    def meldings_tekst_field(self):
        """Gets the meldings_tekst_field of this Meldinger.  


        :return: The meldings_tekst_field of this Meldinger.  
        :rtype: str
        """
        return self._meldings_tekst_field

    @meldings_tekst_field.setter
    def meldings_tekst_field(self, meldings_tekst_field):
        """Sets the meldings_tekst_field of this Meldinger.


        :param meldings_tekst_field: The meldings_tekst_field of this Meldinger.  
        :type: str
        """

        self._meldings_tekst_field = meldings_tekst_field

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
        if not isinstance(other, Meldinger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
