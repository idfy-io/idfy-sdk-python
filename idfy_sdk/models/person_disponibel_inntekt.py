# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonDisponibelInntekt(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'kode_field': 'int',
        'beskrivelse_field': 'str'
    }

    attribute_map = {
        'kode_field': 'kodeField',
        'beskrivelse_field': 'beskrivelseField'
    }

    def __init__(self, kode_field=None, beskrivelse_field=None):  
        """PersonDisponibelInntekt"""  

        self._kode_field = None
        self._beskrivelse_field = None
        self.discriminator = None

        if kode_field is not None:
            self.kode_field = kode_field
        if beskrivelse_field is not None:
            self.beskrivelse_field = beskrivelse_field

    @property
    def kode_field(self):
        """Gets the kode_field of this PersonDisponibelInntekt.  


        :return: The kode_field of this PersonDisponibelInntekt.  
        :rtype: int
        """
        return self._kode_field

    @kode_field.setter
    def kode_field(self, kode_field):
        """Sets the kode_field of this PersonDisponibelInntekt.


        :param kode_field: The kode_field of this PersonDisponibelInntekt.  
        :type: int
        """

        self._kode_field = kode_field

    @property
    def beskrivelse_field(self):
        """Gets the beskrivelse_field of this PersonDisponibelInntekt.  


        :return: The beskrivelse_field of this PersonDisponibelInntekt.  
        :rtype: str
        """
        return self._beskrivelse_field

    @beskrivelse_field.setter
    def beskrivelse_field(self, beskrivelse_field):
        """Sets the beskrivelse_field of this PersonDisponibelInntekt.


        :param beskrivelse_field: The beskrivelse_field of this PersonDisponibelInntekt.  
        :type: str
        """

        self._beskrivelse_field = beskrivelse_field

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
        if not isinstance(other, PersonDisponibelInntekt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
