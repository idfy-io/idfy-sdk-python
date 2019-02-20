# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  




class ArsaksData(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'arsaks_kode_field': 'str',
        'arsaks_tekst_field': 'str'
    }

    attribute_map = {
        'arsaks_kode_field': 'arsaksKodeField',
        'arsaks_tekst_field': 'arsaksTekstField'
    }

    def __init__(self, arsaks_kode_field=None, arsaks_tekst_field=None):  
        """ArsaksData"""  

        self._arsaks_kode_field = None
        self._arsaks_tekst_field = None
        self.discriminator = None

        if arsaks_kode_field is not None:
            self.arsaks_kode_field = arsaks_kode_field
        if arsaks_tekst_field is not None:
            self.arsaks_tekst_field = arsaks_tekst_field

    @property
    def arsaks_kode_field(self):
        """Gets the arsaks_kode_field of this ArsaksData.  


        :return: The arsaks_kode_field of this ArsaksData.  
        :rtype: str
        """
        return self._arsaks_kode_field

    @arsaks_kode_field.setter
    def arsaks_kode_field(self, arsaks_kode_field):
        """Sets the arsaks_kode_field of this ArsaksData.


        :param arsaks_kode_field: The arsaks_kode_field of this ArsaksData.  
        :type: str
        """

        self._arsaks_kode_field = arsaks_kode_field

    @property
    def arsaks_tekst_field(self):
        """Gets the arsaks_tekst_field of this ArsaksData.  


        :return: The arsaks_tekst_field of this ArsaksData.  
        :rtype: str
        """
        return self._arsaks_tekst_field

    @arsaks_tekst_field.setter
    def arsaks_tekst_field(self, arsaks_tekst_field):
        """Sets the arsaks_tekst_field of this ArsaksData.


        :param arsaks_tekst_field: The arsaks_tekst_field of this ArsaksData.  
        :type: str
        """

        self._arsaks_tekst_field = arsaks_tekst_field

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
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
        if not isinstance(other, ArsaksData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
