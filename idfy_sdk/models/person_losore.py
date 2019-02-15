# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonLosore(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ajour_dato_field': 'datetime',
        'spes_tekst1_field': 'str',
        'spes_tekst2_field': 'str',
        'spes_tekst3_field': 'str'
    }

    attribute_map = {
        'ajour_dato_field': 'ajourDatoField',
        'spes_tekst1_field': 'spesTekst1Field',
        'spes_tekst2_field': 'spesTekst2Field',
        'spes_tekst3_field': 'spesTekst3Field'
    }

    def __init__(self, ajour_dato_field=None, spes_tekst1_field=None, spes_tekst2_field=None, spes_tekst3_field=None):  
        """PersonLosore"""  

        self._ajour_dato_field = None
        self._spes_tekst1_field = None
        self._spes_tekst2_field = None
        self._spes_tekst3_field = None
        self.discriminator = None

        if ajour_dato_field is not None:
            self.ajour_dato_field = ajour_dato_field
        if spes_tekst1_field is not None:
            self.spes_tekst1_field = spes_tekst1_field
        if spes_tekst2_field is not None:
            self.spes_tekst2_field = spes_tekst2_field
        if spes_tekst3_field is not None:
            self.spes_tekst3_field = spes_tekst3_field

    @property
    def ajour_dato_field(self):
        """Gets the ajour_dato_field of this PersonLosore.  


        :return: The ajour_dato_field of this PersonLosore.  
        :rtype: datetime
        """
        return self._ajour_dato_field

    @ajour_dato_field.setter
    def ajour_dato_field(self, ajour_dato_field):
        """Sets the ajour_dato_field of this PersonLosore.


        :param ajour_dato_field: The ajour_dato_field of this PersonLosore.  
        :type: datetime
        """

        self._ajour_dato_field = ajour_dato_field

    @property
    def spes_tekst1_field(self):
        """Gets the spes_tekst1_field of this PersonLosore.  


        :return: The spes_tekst1_field of this PersonLosore.  
        :rtype: str
        """
        return self._spes_tekst1_field

    @spes_tekst1_field.setter
    def spes_tekst1_field(self, spes_tekst1_field):
        """Sets the spes_tekst1_field of this PersonLosore.


        :param spes_tekst1_field: The spes_tekst1_field of this PersonLosore.  
        :type: str
        """

        self._spes_tekst1_field = spes_tekst1_field

    @property
    def spes_tekst2_field(self):
        """Gets the spes_tekst2_field of this PersonLosore.  


        :return: The spes_tekst2_field of this PersonLosore.  
        :rtype: str
        """
        return self._spes_tekst2_field

    @spes_tekst2_field.setter
    def spes_tekst2_field(self, spes_tekst2_field):
        """Sets the spes_tekst2_field of this PersonLosore.


        :param spes_tekst2_field: The spes_tekst2_field of this PersonLosore.  
        :type: str
        """

        self._spes_tekst2_field = spes_tekst2_field

    @property
    def spes_tekst3_field(self):
        """Gets the spes_tekst3_field of this PersonLosore.  


        :return: The spes_tekst3_field of this PersonLosore.  
        :rtype: str
        """
        return self._spes_tekst3_field

    @spes_tekst3_field.setter
    def spes_tekst3_field(self, spes_tekst3_field):
        """Sets the spes_tekst3_field of this PersonLosore.


        :param spes_tekst3_field: The spes_tekst3_field of this PersonLosore.  
        :type: str
        """

        self._spes_tekst3_field = spes_tekst3_field

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
        if not isinstance(other, PersonLosore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
