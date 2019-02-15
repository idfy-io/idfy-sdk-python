# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Juridisk(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'prokura_field': 'str',
        'signatur_field': 'str',
        'eier_struktur_field': 'str'
    }

    attribute_map = {
        'prokura_field': 'prokuraField',
        'signatur_field': 'signaturField',
        'eier_struktur_field': 'eierStrukturField'
    }

    def __init__(self, prokura_field=None, signatur_field=None, eier_struktur_field=None):  
        """Juridisk"""  

        self._prokura_field = None
        self._signatur_field = None
        self._eier_struktur_field = None
        self.discriminator = None

        if prokura_field is not None:
            self.prokura_field = prokura_field
        if signatur_field is not None:
            self.signatur_field = signatur_field
        if eier_struktur_field is not None:
            self.eier_struktur_field = eier_struktur_field

    @property
    def prokura_field(self):
        """Gets the prokura_field of this Juridisk.  


        :return: The prokura_field of this Juridisk.  
        :rtype: str
        """
        return self._prokura_field

    @prokura_field.setter
    def prokura_field(self, prokura_field):
        """Sets the prokura_field of this Juridisk.


        :param prokura_field: The prokura_field of this Juridisk.  
        :type: str
        """

        self._prokura_field = prokura_field

    @property
    def signatur_field(self):
        """Gets the signatur_field of this Juridisk.  


        :return: The signatur_field of this Juridisk.  
        :rtype: str
        """
        return self._signatur_field

    @signatur_field.setter
    def signatur_field(self, signatur_field):
        """Sets the signatur_field of this Juridisk.


        :param signatur_field: The signatur_field of this Juridisk.  
        :type: str
        """

        self._signatur_field = signatur_field

    @property
    def eier_struktur_field(self):
        """Gets the eier_struktur_field of this Juridisk.  


        :return: The eier_struktur_field of this Juridisk.  
        :rtype: str
        """
        return self._eier_struktur_field

    @eier_struktur_field.setter
    def eier_struktur_field(self, eier_struktur_field):
        """Sets the eier_struktur_field of this Juridisk.


        :param eier_struktur_field: The eier_struktur_field of this Juridisk.  
        :type: str
        """

        self._eier_struktur_field = eier_struktur_field

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
        if not isinstance(other, Juridisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
