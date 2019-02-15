# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Verv(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'intern_ref_field': 'int',
        'fodt_dato_field': 'datetime',
        'fodt_dato_field_specified': 'bool',
        'navn_field': 'str',
        'telefon_field': 'list[str]',
        'postnr_field': 'int',
        'poststed_field': 'str',
        'verv_kode_field': 'str',
        'verv_tekst_field': 'str'
    }

    attribute_map = {
        'intern_ref_field': 'internRefField',
        'fodt_dato_field': 'fodtDatoField',
        'fodt_dato_field_specified': 'fodtDatoFieldSpecified',
        'navn_field': 'navnField',
        'telefon_field': 'telefonField',
        'postnr_field': 'postnrField',
        'poststed_field': 'poststedField',
        'verv_kode_field': 'vervKodeField',
        'verv_tekst_field': 'vervTekstField'
    }

    def __init__(self, intern_ref_field=None, fodt_dato_field=None, fodt_dato_field_specified=None, navn_field=None, telefon_field=None, postnr_field=None, poststed_field=None, verv_kode_field=None, verv_tekst_field=None):  
        """Verv"""  

        self._intern_ref_field = None
        self._fodt_dato_field = None
        self._fodt_dato_field_specified = None
        self._navn_field = None
        self._telefon_field = None
        self._postnr_field = None
        self._poststed_field = None
        self._verv_kode_field = None
        self._verv_tekst_field = None
        self.discriminator = None

        if intern_ref_field is not None:
            self.intern_ref_field = intern_ref_field
        if fodt_dato_field is not None:
            self.fodt_dato_field = fodt_dato_field
        if fodt_dato_field_specified is not None:
            self.fodt_dato_field_specified = fodt_dato_field_specified
        if navn_field is not None:
            self.navn_field = navn_field
        if telefon_field is not None:
            self.telefon_field = telefon_field
        if postnr_field is not None:
            self.postnr_field = postnr_field
        if poststed_field is not None:
            self.poststed_field = poststed_field
        if verv_kode_field is not None:
            self.verv_kode_field = verv_kode_field
        if verv_tekst_field is not None:
            self.verv_tekst_field = verv_tekst_field

    @property
    def intern_ref_field(self):
        """Gets the intern_ref_field of this Verv.  


        :return: The intern_ref_field of this Verv.  
        :rtype: int
        """
        return self._intern_ref_field

    @intern_ref_field.setter
    def intern_ref_field(self, intern_ref_field):
        """Sets the intern_ref_field of this Verv.


        :param intern_ref_field: The intern_ref_field of this Verv.  
        :type: int
        """

        self._intern_ref_field = intern_ref_field

    @property
    def fodt_dato_field(self):
        """Gets the fodt_dato_field of this Verv.  


        :return: The fodt_dato_field of this Verv.  
        :rtype: datetime
        """
        return self._fodt_dato_field

    @fodt_dato_field.setter
    def fodt_dato_field(self, fodt_dato_field):
        """Sets the fodt_dato_field of this Verv.


        :param fodt_dato_field: The fodt_dato_field of this Verv.  
        :type: datetime
        """

        self._fodt_dato_field = fodt_dato_field

    @property
    def fodt_dato_field_specified(self):
        """Gets the fodt_dato_field_specified of this Verv.  


        :return: The fodt_dato_field_specified of this Verv.  
        :rtype: bool
        """
        return self._fodt_dato_field_specified

    @fodt_dato_field_specified.setter
    def fodt_dato_field_specified(self, fodt_dato_field_specified):
        """Sets the fodt_dato_field_specified of this Verv.


        :param fodt_dato_field_specified: The fodt_dato_field_specified of this Verv.  
        :type: bool
        """

        self._fodt_dato_field_specified = fodt_dato_field_specified

    @property
    def navn_field(self):
        """Gets the navn_field of this Verv.  


        :return: The navn_field of this Verv.  
        :rtype: str
        """
        return self._navn_field

    @navn_field.setter
    def navn_field(self, navn_field):
        """Sets the navn_field of this Verv.


        :param navn_field: The navn_field of this Verv.  
        :type: str
        """

        self._navn_field = navn_field

    @property
    def telefon_field(self):
        """Gets the telefon_field of this Verv.  


        :return: The telefon_field of this Verv.  
        :rtype: list[str]
        """
        return self._telefon_field

    @telefon_field.setter
    def telefon_field(self, telefon_field):
        """Sets the telefon_field of this Verv.


        :param telefon_field: The telefon_field of this Verv.  
        :type: list[str]
        """

        self._telefon_field = telefon_field

    @property
    def postnr_field(self):
        """Gets the postnr_field of this Verv.  


        :return: The postnr_field of this Verv.  
        :rtype: int
        """
        return self._postnr_field

    @postnr_field.setter
    def postnr_field(self, postnr_field):
        """Sets the postnr_field of this Verv.


        :param postnr_field: The postnr_field of this Verv.  
        :type: int
        """

        self._postnr_field = postnr_field

    @property
    def poststed_field(self):
        """Gets the poststed_field of this Verv.  


        :return: The poststed_field of this Verv.  
        :rtype: str
        """
        return self._poststed_field

    @poststed_field.setter
    def poststed_field(self, poststed_field):
        """Sets the poststed_field of this Verv.


        :param poststed_field: The poststed_field of this Verv.  
        :type: str
        """

        self._poststed_field = poststed_field

    @property
    def verv_kode_field(self):
        """Gets the verv_kode_field of this Verv.  


        :return: The verv_kode_field of this Verv.  
        :rtype: str
        """
        return self._verv_kode_field

    @verv_kode_field.setter
    def verv_kode_field(self, verv_kode_field):
        """Sets the verv_kode_field of this Verv.


        :param verv_kode_field: The verv_kode_field of this Verv.  
        :type: str
        """

        self._verv_kode_field = verv_kode_field

    @property
    def verv_tekst_field(self):
        """Gets the verv_tekst_field of this Verv.  


        :return: The verv_tekst_field of this Verv.  
        :rtype: str
        """
        return self._verv_tekst_field

    @verv_tekst_field.setter
    def verv_tekst_field(self, verv_tekst_field):
        """Sets the verv_tekst_field of this Verv.


        :param verv_tekst_field: The verv_tekst_field of this Verv.  
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
        if not isinstance(other, Verv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
