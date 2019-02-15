# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class EiendomNorge(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'svar_eiendom_norge_field': 'str'
    }

    attribute_map = {
        'svar_eiendom_norge_field': 'svarEiendomNorgeField'
    }

    def __init__(self, svar_eiendom_norge_field=None):  
        """EiendomNorge"""  

        self._svar_eiendom_norge_field = None
        self.discriminator = None

        if svar_eiendom_norge_field is not None:
            self.svar_eiendom_norge_field = svar_eiendom_norge_field

    @property
    def svar_eiendom_norge_field(self):
        """Gets the svar_eiendom_norge_field of this EiendomNorge.  


        :return: The svar_eiendom_norge_field of this EiendomNorge.  
        :rtype: str
        """
        return self._svar_eiendom_norge_field

    @svar_eiendom_norge_field.setter
    def svar_eiendom_norge_field(self, svar_eiendom_norge_field):
        """Sets the svar_eiendom_norge_field of this EiendomNorge.


        :param svar_eiendom_norge_field: The svar_eiendom_norge_field of this EiendomNorge.  
        :type: str
        """

        self._svar_eiendom_norge_field = svar_eiendom_norge_field

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
        if not isinstance(other, EiendomNorge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
