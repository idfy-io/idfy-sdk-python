# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.person_verv_data import PersonVervData  


class PersonFullmaktPerson(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'internreferanse_field': 'int',
        'fodt_dato_field': 'datetime',
        'fodt_dato_field_specified': 'bool',
        'navn_field': 'str',
        'adresse_field': 'str',
        'postnr_field': 'int',
        'poststed_field': 'str',
        'fullmakt_type_kode_field': 'str',
        'fullmakt_type_tekst_field': 'str',
        'fullmakt_kode_field': 'str',
        'fullmakt_tekst_field': 'str',
        'prioritet_field': 'int',
        'prioritet_field_specified': 'bool',
        'antall_field': 'int',
        'antall_field_specified': 'bool',
        'obligatorisk_field': 'bool',
        'obligatorisk_field_specified': 'bool',
        'verv_field': 'list[PersonVervData]'
    }

    attribute_map = {
        'internreferanse_field': 'internreferanseField',
        'fodt_dato_field': 'fodtDatoField',
        'fodt_dato_field_specified': 'fodtDatoFieldSpecified',
        'navn_field': 'navnField',
        'adresse_field': 'adresseField',
        'postnr_field': 'postnrField',
        'poststed_field': 'poststedField',
        'fullmakt_type_kode_field': 'fullmaktTypeKodeField',
        'fullmakt_type_tekst_field': 'fullmaktTypeTekstField',
        'fullmakt_kode_field': 'fullmaktKodeField',
        'fullmakt_tekst_field': 'fullmaktTekstField',
        'prioritet_field': 'prioritetField',
        'prioritet_field_specified': 'prioritetFieldSpecified',
        'antall_field': 'antallField',
        'antall_field_specified': 'antallFieldSpecified',
        'obligatorisk_field': 'obligatoriskField',
        'obligatorisk_field_specified': 'obligatoriskFieldSpecified',
        'verv_field': 'vervField'
    }

    def __init__(self, internreferanse_field=None, fodt_dato_field=None, fodt_dato_field_specified=None, navn_field=None, adresse_field=None, postnr_field=None, poststed_field=None, fullmakt_type_kode_field=None, fullmakt_type_tekst_field=None, fullmakt_kode_field=None, fullmakt_tekst_field=None, prioritet_field=None, prioritet_field_specified=None, antall_field=None, antall_field_specified=None, obligatorisk_field=None, obligatorisk_field_specified=None, verv_field=None):  
        """PersonFullmaktPerson"""  

        self._internreferanse_field = None
        self._fodt_dato_field = None
        self._fodt_dato_field_specified = None
        self._navn_field = None
        self._adresse_field = None
        self._postnr_field = None
        self._poststed_field = None
        self._fullmakt_type_kode_field = None
        self._fullmakt_type_tekst_field = None
        self._fullmakt_kode_field = None
        self._fullmakt_tekst_field = None
        self._prioritet_field = None
        self._prioritet_field_specified = None
        self._antall_field = None
        self._antall_field_specified = None
        self._obligatorisk_field = None
        self._obligatorisk_field_specified = None
        self._verv_field = None
        self.discriminator = None

        if internreferanse_field is not None:
            self.internreferanse_field = internreferanse_field
        if fodt_dato_field is not None:
            self.fodt_dato_field = fodt_dato_field
        if fodt_dato_field_specified is not None:
            self.fodt_dato_field_specified = fodt_dato_field_specified
        if navn_field is not None:
            self.navn_field = navn_field
        if adresse_field is not None:
            self.adresse_field = adresse_field
        if postnr_field is not None:
            self.postnr_field = postnr_field
        if poststed_field is not None:
            self.poststed_field = poststed_field
        if fullmakt_type_kode_field is not None:
            self.fullmakt_type_kode_field = fullmakt_type_kode_field
        if fullmakt_type_tekst_field is not None:
            self.fullmakt_type_tekst_field = fullmakt_type_tekst_field
        if fullmakt_kode_field is not None:
            self.fullmakt_kode_field = fullmakt_kode_field
        if fullmakt_tekst_field is not None:
            self.fullmakt_tekst_field = fullmakt_tekst_field
        if prioritet_field is not None:
            self.prioritet_field = prioritet_field
        if prioritet_field_specified is not None:
            self.prioritet_field_specified = prioritet_field_specified
        if antall_field is not None:
            self.antall_field = antall_field
        if antall_field_specified is not None:
            self.antall_field_specified = antall_field_specified
        if obligatorisk_field is not None:
            self.obligatorisk_field = obligatorisk_field
        if obligatorisk_field_specified is not None:
            self.obligatorisk_field_specified = obligatorisk_field_specified
        if verv_field is not None:
            self.verv_field = verv_field

    @property
    def internreferanse_field(self):
        """Gets the internreferanse_field of this PersonFullmaktPerson.  


        :return: The internreferanse_field of this PersonFullmaktPerson.  
        :rtype: int
        """
        return self._internreferanse_field

    @internreferanse_field.setter
    def internreferanse_field(self, internreferanse_field):
        """Sets the internreferanse_field of this PersonFullmaktPerson.


        :param internreferanse_field: The internreferanse_field of this PersonFullmaktPerson.  
        :type: int
        """

        self._internreferanse_field = internreferanse_field

    @property
    def fodt_dato_field(self):
        """Gets the fodt_dato_field of this PersonFullmaktPerson.  


        :return: The fodt_dato_field of this PersonFullmaktPerson.  
        :rtype: datetime
        """
        return self._fodt_dato_field

    @fodt_dato_field.setter
    def fodt_dato_field(self, fodt_dato_field):
        """Sets the fodt_dato_field of this PersonFullmaktPerson.


        :param fodt_dato_field: The fodt_dato_field of this PersonFullmaktPerson.  
        :type: datetime
        """

        self._fodt_dato_field = fodt_dato_field

    @property
    def fodt_dato_field_specified(self):
        """Gets the fodt_dato_field_specified of this PersonFullmaktPerson.  


        :return: The fodt_dato_field_specified of this PersonFullmaktPerson.  
        :rtype: bool
        """
        return self._fodt_dato_field_specified

    @fodt_dato_field_specified.setter
    def fodt_dato_field_specified(self, fodt_dato_field_specified):
        """Sets the fodt_dato_field_specified of this PersonFullmaktPerson.


        :param fodt_dato_field_specified: The fodt_dato_field_specified of this PersonFullmaktPerson.  
        :type: bool
        """

        self._fodt_dato_field_specified = fodt_dato_field_specified

    @property
    def navn_field(self):
        """Gets the navn_field of this PersonFullmaktPerson.  


        :return: The navn_field of this PersonFullmaktPerson.  
        :rtype: str
        """
        return self._navn_field

    @navn_field.setter
    def navn_field(self, navn_field):
        """Sets the navn_field of this PersonFullmaktPerson.


        :param navn_field: The navn_field of this PersonFullmaktPerson.  
        :type: str
        """

        self._navn_field = navn_field

    @property
    def adresse_field(self):
        """Gets the adresse_field of this PersonFullmaktPerson.  


        :return: The adresse_field of this PersonFullmaktPerson.  
        :rtype: str
        """
        return self._adresse_field

    @adresse_field.setter
    def adresse_field(self, adresse_field):
        """Sets the adresse_field of this PersonFullmaktPerson.


        :param adresse_field: The adresse_field of this PersonFullmaktPerson.  
        :type: str
        """

        self._adresse_field = adresse_field

    @property
    def postnr_field(self):
        """Gets the postnr_field of this PersonFullmaktPerson.  


        :return: The postnr_field of this PersonFullmaktPerson.  
        :rtype: int
        """
        return self._postnr_field

    @postnr_field.setter
    def postnr_field(self, postnr_field):
        """Sets the postnr_field of this PersonFullmaktPerson.


        :param postnr_field: The postnr_field of this PersonFullmaktPerson.  
        :type: int
        """

        self._postnr_field = postnr_field

    @property
    def poststed_field(self):
        """Gets the poststed_field of this PersonFullmaktPerson.  


        :return: The poststed_field of this PersonFullmaktPerson.  
        :rtype: str
        """
        return self._poststed_field

    @poststed_field.setter
    def poststed_field(self, poststed_field):
        """Sets the poststed_field of this PersonFullmaktPerson.


        :param poststed_field: The poststed_field of this PersonFullmaktPerson.  
        :type: str
        """

        self._poststed_field = poststed_field

    @property
    def fullmakt_type_kode_field(self):
        """Gets the fullmakt_type_kode_field of this PersonFullmaktPerson.  


        :return: The fullmakt_type_kode_field of this PersonFullmaktPerson.  
        :rtype: str
        """
        return self._fullmakt_type_kode_field

    @fullmakt_type_kode_field.setter
    def fullmakt_type_kode_field(self, fullmakt_type_kode_field):
        """Sets the fullmakt_type_kode_field of this PersonFullmaktPerson.


        :param fullmakt_type_kode_field: The fullmakt_type_kode_field of this PersonFullmaktPerson.  
        :type: str
        """

        self._fullmakt_type_kode_field = fullmakt_type_kode_field

    @property
    def fullmakt_type_tekst_field(self):
        """Gets the fullmakt_type_tekst_field of this PersonFullmaktPerson.  


        :return: The fullmakt_type_tekst_field of this PersonFullmaktPerson.  
        :rtype: str
        """
        return self._fullmakt_type_tekst_field

    @fullmakt_type_tekst_field.setter
    def fullmakt_type_tekst_field(self, fullmakt_type_tekst_field):
        """Sets the fullmakt_type_tekst_field of this PersonFullmaktPerson.


        :param fullmakt_type_tekst_field: The fullmakt_type_tekst_field of this PersonFullmaktPerson.  
        :type: str
        """

        self._fullmakt_type_tekst_field = fullmakt_type_tekst_field

    @property
    def fullmakt_kode_field(self):
        """Gets the fullmakt_kode_field of this PersonFullmaktPerson.  


        :return: The fullmakt_kode_field of this PersonFullmaktPerson.  
        :rtype: str
        """
        return self._fullmakt_kode_field

    @fullmakt_kode_field.setter
    def fullmakt_kode_field(self, fullmakt_kode_field):
        """Sets the fullmakt_kode_field of this PersonFullmaktPerson.


        :param fullmakt_kode_field: The fullmakt_kode_field of this PersonFullmaktPerson.  
        :type: str
        """

        self._fullmakt_kode_field = fullmakt_kode_field

    @property
    def fullmakt_tekst_field(self):
        """Gets the fullmakt_tekst_field of this PersonFullmaktPerson.  


        :return: The fullmakt_tekst_field of this PersonFullmaktPerson.  
        :rtype: str
        """
        return self._fullmakt_tekst_field

    @fullmakt_tekst_field.setter
    def fullmakt_tekst_field(self, fullmakt_tekst_field):
        """Sets the fullmakt_tekst_field of this PersonFullmaktPerson.


        :param fullmakt_tekst_field: The fullmakt_tekst_field of this PersonFullmaktPerson.  
        :type: str
        """

        self._fullmakt_tekst_field = fullmakt_tekst_field

    @property
    def prioritet_field(self):
        """Gets the prioritet_field of this PersonFullmaktPerson.  


        :return: The prioritet_field of this PersonFullmaktPerson.  
        :rtype: int
        """
        return self._prioritet_field

    @prioritet_field.setter
    def prioritet_field(self, prioritet_field):
        """Sets the prioritet_field of this PersonFullmaktPerson.


        :param prioritet_field: The prioritet_field of this PersonFullmaktPerson.  
        :type: int
        """

        self._prioritet_field = prioritet_field

    @property
    def prioritet_field_specified(self):
        """Gets the prioritet_field_specified of this PersonFullmaktPerson.  


        :return: The prioritet_field_specified of this PersonFullmaktPerson.  
        :rtype: bool
        """
        return self._prioritet_field_specified

    @prioritet_field_specified.setter
    def prioritet_field_specified(self, prioritet_field_specified):
        """Sets the prioritet_field_specified of this PersonFullmaktPerson.


        :param prioritet_field_specified: The prioritet_field_specified of this PersonFullmaktPerson.  
        :type: bool
        """

        self._prioritet_field_specified = prioritet_field_specified

    @property
    def antall_field(self):
        """Gets the antall_field of this PersonFullmaktPerson.  


        :return: The antall_field of this PersonFullmaktPerson.  
        :rtype: int
        """
        return self._antall_field

    @antall_field.setter
    def antall_field(self, antall_field):
        """Sets the antall_field of this PersonFullmaktPerson.


        :param antall_field: The antall_field of this PersonFullmaktPerson.  
        :type: int
        """

        self._antall_field = antall_field

    @property
    def antall_field_specified(self):
        """Gets the antall_field_specified of this PersonFullmaktPerson.  


        :return: The antall_field_specified of this PersonFullmaktPerson.  
        :rtype: bool
        """
        return self._antall_field_specified

    @antall_field_specified.setter
    def antall_field_specified(self, antall_field_specified):
        """Sets the antall_field_specified of this PersonFullmaktPerson.


        :param antall_field_specified: The antall_field_specified of this PersonFullmaktPerson.  
        :type: bool
        """

        self._antall_field_specified = antall_field_specified

    @property
    def obligatorisk_field(self):
        """Gets the obligatorisk_field of this PersonFullmaktPerson.  


        :return: The obligatorisk_field of this PersonFullmaktPerson.  
        :rtype: bool
        """
        return self._obligatorisk_field

    @obligatorisk_field.setter
    def obligatorisk_field(self, obligatorisk_field):
        """Sets the obligatorisk_field of this PersonFullmaktPerson.


        :param obligatorisk_field: The obligatorisk_field of this PersonFullmaktPerson.  
        :type: bool
        """

        self._obligatorisk_field = obligatorisk_field

    @property
    def obligatorisk_field_specified(self):
        """Gets the obligatorisk_field_specified of this PersonFullmaktPerson.  


        :return: The obligatorisk_field_specified of this PersonFullmaktPerson.  
        :rtype: bool
        """
        return self._obligatorisk_field_specified

    @obligatorisk_field_specified.setter
    def obligatorisk_field_specified(self, obligatorisk_field_specified):
        """Sets the obligatorisk_field_specified of this PersonFullmaktPerson.


        :param obligatorisk_field_specified: The obligatorisk_field_specified of this PersonFullmaktPerson.  
        :type: bool
        """

        self._obligatorisk_field_specified = obligatorisk_field_specified

    @property
    def verv_field(self):
        """Gets the verv_field of this PersonFullmaktPerson.  


        :return: The verv_field of this PersonFullmaktPerson.  
        :rtype: list[PersonVervData]
        """
        return self._verv_field

    @verv_field.setter
    def verv_field(self, verv_field):
        """Sets the verv_field of this PersonFullmaktPerson.


        :param verv_field: The verv_field of this PersonFullmaktPerson.  
        :type: list[PersonVervData]
        """

        self._verv_field = verv_field

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
        if not isinstance(other, PersonFullmaktPerson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
