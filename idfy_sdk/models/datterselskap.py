# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Datterselskap(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'orgnr_field': 'int',
        'kode_type_field': 'str',
        'kode_tekst_field': 'str',
        'navn_field': 'str',
        'postnr_field': 'int',
        'poststed_field': 'str',
        'eierandel_field': 'float'
    }

    attribute_map = {
        'orgnr_field': 'orgnrField',
        'kode_type_field': 'kodeTypeField',
        'kode_tekst_field': 'kodeTekstField',
        'navn_field': 'navnField',
        'postnr_field': 'postnrField',
        'poststed_field': 'poststedField',
        'eierandel_field': 'eierandelField'
    }

    def __init__(self, orgnr_field=None, kode_type_field=None, kode_tekst_field=None, navn_field=None, postnr_field=None, poststed_field=None, eierandel_field=None):  
        """Datterselskap"""  

        self._orgnr_field = None
        self._kode_type_field = None
        self._kode_tekst_field = None
        self._navn_field = None
        self._postnr_field = None
        self._poststed_field = None
        self._eierandel_field = None
        self.discriminator = None

        if orgnr_field is not None:
            self.orgnr_field = orgnr_field
        if kode_type_field is not None:
            self.kode_type_field = kode_type_field
        if kode_tekst_field is not None:
            self.kode_tekst_field = kode_tekst_field
        if navn_field is not None:
            self.navn_field = navn_field
        if postnr_field is not None:
            self.postnr_field = postnr_field
        if poststed_field is not None:
            self.poststed_field = poststed_field
        if eierandel_field is not None:
            self.eierandel_field = eierandel_field

    @property
    def orgnr_field(self):
        """Gets the orgnr_field of this Datterselskap.  


        :return: The orgnr_field of this Datterselskap.  
        :rtype: int
        """
        return self._orgnr_field

    @orgnr_field.setter
    def orgnr_field(self, orgnr_field):
        """Sets the orgnr_field of this Datterselskap.


        :param orgnr_field: The orgnr_field of this Datterselskap.  
        :type: int
        """

        self._orgnr_field = orgnr_field

    @property
    def kode_type_field(self):
        """Gets the kode_type_field of this Datterselskap.  


        :return: The kode_type_field of this Datterselskap.  
        :rtype: str
        """
        return self._kode_type_field

    @kode_type_field.setter
    def kode_type_field(self, kode_type_field):
        """Sets the kode_type_field of this Datterselskap.


        :param kode_type_field: The kode_type_field of this Datterselskap.  
        :type: str
        """

        self._kode_type_field = kode_type_field

    @property
    def kode_tekst_field(self):
        """Gets the kode_tekst_field of this Datterselskap.  


        :return: The kode_tekst_field of this Datterselskap.  
        :rtype: str
        """
        return self._kode_tekst_field

    @kode_tekst_field.setter
    def kode_tekst_field(self, kode_tekst_field):
        """Sets the kode_tekst_field of this Datterselskap.


        :param kode_tekst_field: The kode_tekst_field of this Datterselskap.  
        :type: str
        """

        self._kode_tekst_field = kode_tekst_field

    @property
    def navn_field(self):
        """Gets the navn_field of this Datterselskap.  


        :return: The navn_field of this Datterselskap.  
        :rtype: str
        """
        return self._navn_field

    @navn_field.setter
    def navn_field(self, navn_field):
        """Sets the navn_field of this Datterselskap.


        :param navn_field: The navn_field of this Datterselskap.  
        :type: str
        """

        self._navn_field = navn_field

    @property
    def postnr_field(self):
        """Gets the postnr_field of this Datterselskap.  


        :return: The postnr_field of this Datterselskap.  
        :rtype: int
        """
        return self._postnr_field

    @postnr_field.setter
    def postnr_field(self, postnr_field):
        """Sets the postnr_field of this Datterselskap.


        :param postnr_field: The postnr_field of this Datterselskap.  
        :type: int
        """

        self._postnr_field = postnr_field

    @property
    def poststed_field(self):
        """Gets the poststed_field of this Datterselskap.  


        :return: The poststed_field of this Datterselskap.  
        :rtype: str
        """
        return self._poststed_field

    @poststed_field.setter
    def poststed_field(self, poststed_field):
        """Sets the poststed_field of this Datterselskap.


        :param poststed_field: The poststed_field of this Datterselskap.  
        :type: str
        """

        self._poststed_field = poststed_field

    @property
    def eierandel_field(self):
        """Gets the eierandel_field of this Datterselskap.  


        :return: The eierandel_field of this Datterselskap.  
        :rtype: float
        """
        return self._eierandel_field

    @eierandel_field.setter
    def eierandel_field(self, eierandel_field):
        """Sets the eierandel_field of this Datterselskap.


        :param eierandel_field: The eierandel_field of this Datterselskap.  
        :type: float
        """

        self._eierandel_field = eierandel_field

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
        if not isinstance(other, Datterselskap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
