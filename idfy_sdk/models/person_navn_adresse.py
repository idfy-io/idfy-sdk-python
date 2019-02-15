# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonNavnAdresse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status_field': 'str',
        'status_dato_field': 'datetime',
        'fodselsdato_field': 'datetime',
        'navn_field': 'str',
        'adresse_field': 'str',
        'postnr_field': 'str',
        'poststed_field': 'str',
        'kommune_field': 'str',
        'fylke_field': 'str',
        'alder_field': 'int',
        'kjonn_field': 'str',
        'telefon_field': 'list[str]'
    }

    attribute_map = {
        'status_field': 'statusField',
        'status_dato_field': 'statusDatoField',
        'fodselsdato_field': 'fodselsdatoField',
        'navn_field': 'navnField',
        'adresse_field': 'adresseField',
        'postnr_field': 'postnrField',
        'poststed_field': 'poststedField',
        'kommune_field': 'kommuneField',
        'fylke_field': 'fylkeField',
        'alder_field': 'alderField',
        'kjonn_field': 'kjonnField',
        'telefon_field': 'telefonField'
    }

    def __init__(self, status_field=None, status_dato_field=None, fodselsdato_field=None, navn_field=None, adresse_field=None, postnr_field=None, poststed_field=None, kommune_field=None, fylke_field=None, alder_field=None, kjonn_field=None, telefon_field=None):  
        """PersonNavnAdresse"""  

        self._status_field = None
        self._status_dato_field = None
        self._fodselsdato_field = None
        self._navn_field = None
        self._adresse_field = None
        self._postnr_field = None
        self._poststed_field = None
        self._kommune_field = None
        self._fylke_field = None
        self._alder_field = None
        self._kjonn_field = None
        self._telefon_field = None
        self.discriminator = None

        if status_field is not None:
            self.status_field = status_field
        if status_dato_field is not None:
            self.status_dato_field = status_dato_field
        if fodselsdato_field is not None:
            self.fodselsdato_field = fodselsdato_field
        if navn_field is not None:
            self.navn_field = navn_field
        if adresse_field is not None:
            self.adresse_field = adresse_field
        if postnr_field is not None:
            self.postnr_field = postnr_field
        if poststed_field is not None:
            self.poststed_field = poststed_field
        if kommune_field is not None:
            self.kommune_field = kommune_field
        if fylke_field is not None:
            self.fylke_field = fylke_field
        if alder_field is not None:
            self.alder_field = alder_field
        if kjonn_field is not None:
            self.kjonn_field = kjonn_field
        if telefon_field is not None:
            self.telefon_field = telefon_field

    @property
    def status_field(self):
        """Gets the status_field of this PersonNavnAdresse.  


        :return: The status_field of this PersonNavnAdresse.  
        :rtype: str
        """
        return self._status_field

    @status_field.setter
    def status_field(self, status_field):
        """Sets the status_field of this PersonNavnAdresse.


        :param status_field: The status_field of this PersonNavnAdresse.  
        :type: str
        """

        self._status_field = status_field

    @property
    def status_dato_field(self):
        """Gets the status_dato_field of this PersonNavnAdresse.  


        :return: The status_dato_field of this PersonNavnAdresse.  
        :rtype: datetime
        """
        return self._status_dato_field

    @status_dato_field.setter
    def status_dato_field(self, status_dato_field):
        """Sets the status_dato_field of this PersonNavnAdresse.


        :param status_dato_field: The status_dato_field of this PersonNavnAdresse.  
        :type: datetime
        """

        self._status_dato_field = status_dato_field

    @property
    def fodselsdato_field(self):
        """Gets the fodselsdato_field of this PersonNavnAdresse.  


        :return: The fodselsdato_field of this PersonNavnAdresse.  
        :rtype: datetime
        """
        return self._fodselsdato_field

    @fodselsdato_field.setter
    def fodselsdato_field(self, fodselsdato_field):
        """Sets the fodselsdato_field of this PersonNavnAdresse.


        :param fodselsdato_field: The fodselsdato_field of this PersonNavnAdresse.  
        :type: datetime
        """

        self._fodselsdato_field = fodselsdato_field

    @property
    def navn_field(self):
        """Gets the navn_field of this PersonNavnAdresse.  


        :return: The navn_field of this PersonNavnAdresse.  
        :rtype: str
        """
        return self._navn_field

    @navn_field.setter
    def navn_field(self, navn_field):
        """Sets the navn_field of this PersonNavnAdresse.


        :param navn_field: The navn_field of this PersonNavnAdresse.  
        :type: str
        """

        self._navn_field = navn_field

    @property
    def adresse_field(self):
        """Gets the adresse_field of this PersonNavnAdresse.  


        :return: The adresse_field of this PersonNavnAdresse.  
        :rtype: str
        """
        return self._adresse_field

    @adresse_field.setter
    def adresse_field(self, adresse_field):
        """Sets the adresse_field of this PersonNavnAdresse.


        :param adresse_field: The adresse_field of this PersonNavnAdresse.  
        :type: str
        """

        self._adresse_field = adresse_field

    @property
    def postnr_field(self):
        """Gets the postnr_field of this PersonNavnAdresse.  


        :return: The postnr_field of this PersonNavnAdresse.  
        :rtype: str
        """
        return self._postnr_field

    @postnr_field.setter
    def postnr_field(self, postnr_field):
        """Sets the postnr_field of this PersonNavnAdresse.


        :param postnr_field: The postnr_field of this PersonNavnAdresse.  
        :type: str
        """

        self._postnr_field = postnr_field

    @property
    def poststed_field(self):
        """Gets the poststed_field of this PersonNavnAdresse.  


        :return: The poststed_field of this PersonNavnAdresse.  
        :rtype: str
        """
        return self._poststed_field

    @poststed_field.setter
    def poststed_field(self, poststed_field):
        """Sets the poststed_field of this PersonNavnAdresse.


        :param poststed_field: The poststed_field of this PersonNavnAdresse.  
        :type: str
        """

        self._poststed_field = poststed_field

    @property
    def kommune_field(self):
        """Gets the kommune_field of this PersonNavnAdresse.  


        :return: The kommune_field of this PersonNavnAdresse.  
        :rtype: str
        """
        return self._kommune_field

    @kommune_field.setter
    def kommune_field(self, kommune_field):
        """Sets the kommune_field of this PersonNavnAdresse.


        :param kommune_field: The kommune_field of this PersonNavnAdresse.  
        :type: str
        """

        self._kommune_field = kommune_field

    @property
    def fylke_field(self):
        """Gets the fylke_field of this PersonNavnAdresse.  


        :return: The fylke_field of this PersonNavnAdresse.  
        :rtype: str
        """
        return self._fylke_field

    @fylke_field.setter
    def fylke_field(self, fylke_field):
        """Sets the fylke_field of this PersonNavnAdresse.


        :param fylke_field: The fylke_field of this PersonNavnAdresse.  
        :type: str
        """

        self._fylke_field = fylke_field

    @property
    def alder_field(self):
        """Gets the alder_field of this PersonNavnAdresse.  


        :return: The alder_field of this PersonNavnAdresse.  
        :rtype: int
        """
        return self._alder_field

    @alder_field.setter
    def alder_field(self, alder_field):
        """Sets the alder_field of this PersonNavnAdresse.


        :param alder_field: The alder_field of this PersonNavnAdresse.  
        :type: int
        """

        self._alder_field = alder_field

    @property
    def kjonn_field(self):
        """Gets the kjonn_field of this PersonNavnAdresse.  


        :return: The kjonn_field of this PersonNavnAdresse.  
        :rtype: str
        """
        return self._kjonn_field

    @kjonn_field.setter
    def kjonn_field(self, kjonn_field):
        """Sets the kjonn_field of this PersonNavnAdresse.


        :param kjonn_field: The kjonn_field of this PersonNavnAdresse.  
        :type: str
        """

        self._kjonn_field = kjonn_field

    @property
    def telefon_field(self):
        """Gets the telefon_field of this PersonNavnAdresse.  


        :return: The telefon_field of this PersonNavnAdresse.  
        :rtype: list[str]
        """
        return self._telefon_field

    @telefon_field.setter
    def telefon_field(self, telefon_field):
        """Sets the telefon_field of this PersonNavnAdresse.


        :param telefon_field: The telefon_field of this PersonNavnAdresse.  
        :type: list[str]
        """

        self._telefon_field = telefon_field

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
        if not isinstance(other, PersonNavnAdresse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
