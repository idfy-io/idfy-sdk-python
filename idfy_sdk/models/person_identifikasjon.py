# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonIdentifikasjon(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'internref_field': 'int'
    }

    attribute_map = {
        'internref_field': 'internrefField'
    }

    def __init__(self, internref_field=None):  
        """PersonIdentifikasjon"""  

        self._internref_field = None
        self.discriminator = None

        if internref_field is not None:
            self.internref_field = internref_field

    @property
    def internref_field(self):
        """Gets the internref_field of this PersonIdentifikasjon.  


        :return: The internref_field of this PersonIdentifikasjon.  
        :rtype: int
        """
        return self._internref_field

    @internref_field.setter
    def internref_field(self, internref_field):
        """Sets the internref_field of this PersonIdentifikasjon.


        :param internref_field: The internref_field of this PersonIdentifikasjon.  
        :type: int
        """

        self._internref_field = internref_field

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
        if not isinstance(other, PersonIdentifikasjon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
