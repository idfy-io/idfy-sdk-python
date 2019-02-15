# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class KonsernLink(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'orgnr_overste_mor_field': 'int',
        'orgnr_naermeste_mor_field': 'int',
        'lopenr_field': 'int',
        'niva_deltagende_field': 'int',
        'landkode_deltagende_field': 'str',
        'orgnr_deltagende_field': 'int',
        'navn_deltagende_field': 'str',
        'eierandel_deltagende_field': 'float'
    }

    attribute_map = {
        'orgnr_overste_mor_field': 'orgnrOversteMorField',
        'orgnr_naermeste_mor_field': 'orgnrNaermesteMorField',
        'lopenr_field': 'lopenrField',
        'niva_deltagende_field': 'nivaDeltagendeField',
        'landkode_deltagende_field': 'landkodeDeltagendeField',
        'orgnr_deltagende_field': 'orgnrDeltagendeField',
        'navn_deltagende_field': 'navnDeltagendeField',
        'eierandel_deltagende_field': 'eierandelDeltagendeField'
    }

    def __init__(self, orgnr_overste_mor_field=None, orgnr_naermeste_mor_field=None, lopenr_field=None, niva_deltagende_field=None, landkode_deltagende_field=None, orgnr_deltagende_field=None, navn_deltagende_field=None, eierandel_deltagende_field=None):  
        """KonsernLink"""  

        self._orgnr_overste_mor_field = None
        self._orgnr_naermeste_mor_field = None
        self._lopenr_field = None
        self._niva_deltagende_field = None
        self._landkode_deltagende_field = None
        self._orgnr_deltagende_field = None
        self._navn_deltagende_field = None
        self._eierandel_deltagende_field = None
        self.discriminator = None

        if orgnr_overste_mor_field is not None:
            self.orgnr_overste_mor_field = orgnr_overste_mor_field
        if orgnr_naermeste_mor_field is not None:
            self.orgnr_naermeste_mor_field = orgnr_naermeste_mor_field
        if lopenr_field is not None:
            self.lopenr_field = lopenr_field
        if niva_deltagende_field is not None:
            self.niva_deltagende_field = niva_deltagende_field
        if landkode_deltagende_field is not None:
            self.landkode_deltagende_field = landkode_deltagende_field
        if orgnr_deltagende_field is not None:
            self.orgnr_deltagende_field = orgnr_deltagende_field
        if navn_deltagende_field is not None:
            self.navn_deltagende_field = navn_deltagende_field
        if eierandel_deltagende_field is not None:
            self.eierandel_deltagende_field = eierandel_deltagende_field

    @property
    def orgnr_overste_mor_field(self):
        """Gets the orgnr_overste_mor_field of this KonsernLink.  


        :return: The orgnr_overste_mor_field of this KonsernLink.  
        :rtype: int
        """
        return self._orgnr_overste_mor_field

    @orgnr_overste_mor_field.setter
    def orgnr_overste_mor_field(self, orgnr_overste_mor_field):
        """Sets the orgnr_overste_mor_field of this KonsernLink.


        :param orgnr_overste_mor_field: The orgnr_overste_mor_field of this KonsernLink.  
        :type: int
        """

        self._orgnr_overste_mor_field = orgnr_overste_mor_field

    @property
    def orgnr_naermeste_mor_field(self):
        """Gets the orgnr_naermeste_mor_field of this KonsernLink.  


        :return: The orgnr_naermeste_mor_field of this KonsernLink.  
        :rtype: int
        """
        return self._orgnr_naermeste_mor_field

    @orgnr_naermeste_mor_field.setter
    def orgnr_naermeste_mor_field(self, orgnr_naermeste_mor_field):
        """Sets the orgnr_naermeste_mor_field of this KonsernLink.


        :param orgnr_naermeste_mor_field: The orgnr_naermeste_mor_field of this KonsernLink.  
        :type: int
        """

        self._orgnr_naermeste_mor_field = orgnr_naermeste_mor_field

    @property
    def lopenr_field(self):
        """Gets the lopenr_field of this KonsernLink.  


        :return: The lopenr_field of this KonsernLink.  
        :rtype: int
        """
        return self._lopenr_field

    @lopenr_field.setter
    def lopenr_field(self, lopenr_field):
        """Sets the lopenr_field of this KonsernLink.


        :param lopenr_field: The lopenr_field of this KonsernLink.  
        :type: int
        """

        self._lopenr_field = lopenr_field

    @property
    def niva_deltagende_field(self):
        """Gets the niva_deltagende_field of this KonsernLink.  


        :return: The niva_deltagende_field of this KonsernLink.  
        :rtype: int
        """
        return self._niva_deltagende_field

    @niva_deltagende_field.setter
    def niva_deltagende_field(self, niva_deltagende_field):
        """Sets the niva_deltagende_field of this KonsernLink.


        :param niva_deltagende_field: The niva_deltagende_field of this KonsernLink.  
        :type: int
        """

        self._niva_deltagende_field = niva_deltagende_field

    @property
    def landkode_deltagende_field(self):
        """Gets the landkode_deltagende_field of this KonsernLink.  


        :return: The landkode_deltagende_field of this KonsernLink.  
        :rtype: str
        """
        return self._landkode_deltagende_field

    @landkode_deltagende_field.setter
    def landkode_deltagende_field(self, landkode_deltagende_field):
        """Sets the landkode_deltagende_field of this KonsernLink.


        :param landkode_deltagende_field: The landkode_deltagende_field of this KonsernLink.  
        :type: str
        """

        self._landkode_deltagende_field = landkode_deltagende_field

    @property
    def orgnr_deltagende_field(self):
        """Gets the orgnr_deltagende_field of this KonsernLink.  


        :return: The orgnr_deltagende_field of this KonsernLink.  
        :rtype: int
        """
        return self._orgnr_deltagende_field

    @orgnr_deltagende_field.setter
    def orgnr_deltagende_field(self, orgnr_deltagende_field):
        """Sets the orgnr_deltagende_field of this KonsernLink.


        :param orgnr_deltagende_field: The orgnr_deltagende_field of this KonsernLink.  
        :type: int
        """

        self._orgnr_deltagende_field = orgnr_deltagende_field

    @property
    def navn_deltagende_field(self):
        """Gets the navn_deltagende_field of this KonsernLink.  


        :return: The navn_deltagende_field of this KonsernLink.  
        :rtype: str
        """
        return self._navn_deltagende_field

    @navn_deltagende_field.setter
    def navn_deltagende_field(self, navn_deltagende_field):
        """Sets the navn_deltagende_field of this KonsernLink.


        :param navn_deltagende_field: The navn_deltagende_field of this KonsernLink.  
        :type: str
        """

        self._navn_deltagende_field = navn_deltagende_field

    @property
    def eierandel_deltagende_field(self):
        """Gets the eierandel_deltagende_field of this KonsernLink.  


        :return: The eierandel_deltagende_field of this KonsernLink.  
        :rtype: float
        """
        return self._eierandel_deltagende_field

    @eierandel_deltagende_field.setter
    def eierandel_deltagende_field(self, eierandel_deltagende_field):
        """Sets the eierandel_deltagende_field of this KonsernLink.


        :param eierandel_deltagende_field: The eierandel_deltagende_field of this KonsernLink.  
        :type: float
        """

        self._eierandel_deltagende_field = eierandel_deltagende_field

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
        if not isinstance(other, KonsernLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
