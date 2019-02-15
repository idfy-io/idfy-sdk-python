# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class BransjeData(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bransje_kode_field': 'int',
        'bransje_tekst_field': 'str'
    }

    attribute_map = {
        'bransje_kode_field': 'bransjeKodeField',
        'bransje_tekst_field': 'bransjeTekstField'
    }

    def __init__(self, bransje_kode_field=None, bransje_tekst_field=None):  
        """BransjeData"""  

        self._bransje_kode_field = None
        self._bransje_tekst_field = None
        self.discriminator = None

        if bransje_kode_field is not None:
            self.bransje_kode_field = bransje_kode_field
        if bransje_tekst_field is not None:
            self.bransje_tekst_field = bransje_tekst_field

    @property
    def bransje_kode_field(self):
        """Gets the bransje_kode_field of this BransjeData.  


        :return: The bransje_kode_field of this BransjeData.  
        :rtype: int
        """
        return self._bransje_kode_field

    @bransje_kode_field.setter
    def bransje_kode_field(self, bransje_kode_field):
        """Sets the bransje_kode_field of this BransjeData.


        :param bransje_kode_field: The bransje_kode_field of this BransjeData.  
        :type: int
        """

        self._bransje_kode_field = bransje_kode_field

    @property
    def bransje_tekst_field(self):
        """Gets the bransje_tekst_field of this BransjeData.  


        :return: The bransje_tekst_field of this BransjeData.  
        :rtype: str
        """
        return self._bransje_tekst_field

    @bransje_tekst_field.setter
    def bransje_tekst_field(self, bransje_tekst_field):
        """Sets the bransje_tekst_field of this BransjeData.


        :param bransje_tekst_field: The bransje_tekst_field of this BransjeData.  
        :type: str
        """

        self._bransje_tekst_field = bransje_tekst_field

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
        if not isinstance(other, BransjeData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
