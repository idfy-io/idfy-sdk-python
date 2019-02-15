# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class VervData(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'verv_kode_field': 'str',
        'verv_tekst_field': 'str'
    }

    attribute_map = {
        'verv_kode_field': 'vervKodeField',
        'verv_tekst_field': 'vervTekstField'
    }

    def __init__(self, verv_kode_field=None, verv_tekst_field=None):  
        """VervData"""  

        self._verv_kode_field = None
        self._verv_tekst_field = None
        self.discriminator = None

        if verv_kode_field is not None:
            self.verv_kode_field = verv_kode_field
        if verv_tekst_field is not None:
            self.verv_tekst_field = verv_tekst_field

    @property
    def verv_kode_field(self):
        """Gets the verv_kode_field of this VervData.  


        :return: The verv_kode_field of this VervData.  
        :rtype: str
        """
        return self._verv_kode_field

    @verv_kode_field.setter
    def verv_kode_field(self, verv_kode_field):
        """Sets the verv_kode_field of this VervData.


        :param verv_kode_field: The verv_kode_field of this VervData.  
        :type: str
        """

        self._verv_kode_field = verv_kode_field

    @property
    def verv_tekst_field(self):
        """Gets the verv_tekst_field of this VervData.  


        :return: The verv_tekst_field of this VervData.  
        :rtype: str
        """
        return self._verv_tekst_field

    @verv_tekst_field.setter
    def verv_tekst_field(self, verv_tekst_field):
        """Sets the verv_tekst_field of this VervData.


        :param verv_tekst_field: The verv_tekst_field of this VervData.  
        :type: str
        """

        self._verv_tekst_field = verv_tekst_field

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
        if not isinstance(other, VervData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
