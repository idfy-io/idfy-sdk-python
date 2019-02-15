# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonBetaDetaljer(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'registrert_dato_field': 'datetime',
        'beta_gruppe_kode_field': 'str',
        'beta_gruppe_tekst_field': 'str',
        'beta_type_field': 'str',
        'beta_tekst_field': 'str',
        'beta_belop_field': 'int',
        'kilde_kode_field': 'str',
        'kilde_tekst_field': 'str',
        'kilde_referansenr_field': 'int',
        'status_anmerkning_field': 'str',
        'status_dato_field': 'datetime',
        'kreditor_field': 'str'
    }

    attribute_map = {
        'registrert_dato_field': 'registrertDatoField',
        'beta_gruppe_kode_field': 'betaGruppeKodeField',
        'beta_gruppe_tekst_field': 'betaGruppeTekstField',
        'beta_type_field': 'betaTypeField',
        'beta_tekst_field': 'betaTekstField',
        'beta_belop_field': 'betaBelopField',
        'kilde_kode_field': 'kildeKodeField',
        'kilde_tekst_field': 'kildeTekstField',
        'kilde_referansenr_field': 'kildeReferansenrField',
        'status_anmerkning_field': 'statusAnmerkningField',
        'status_dato_field': 'statusDatoField',
        'kreditor_field': 'kreditorField'
    }

    def __init__(self, registrert_dato_field=None, beta_gruppe_kode_field=None, beta_gruppe_tekst_field=None, beta_type_field=None, beta_tekst_field=None, beta_belop_field=None, kilde_kode_field=None, kilde_tekst_field=None, kilde_referansenr_field=None, status_anmerkning_field=None, status_dato_field=None, kreditor_field=None):  
        """PersonBetaDetaljer"""  

        self._registrert_dato_field = None
        self._beta_gruppe_kode_field = None
        self._beta_gruppe_tekst_field = None
        self._beta_type_field = None
        self._beta_tekst_field = None
        self._beta_belop_field = None
        self._kilde_kode_field = None
        self._kilde_tekst_field = None
        self._kilde_referansenr_field = None
        self._status_anmerkning_field = None
        self._status_dato_field = None
        self._kreditor_field = None
        self.discriminator = None

        if registrert_dato_field is not None:
            self.registrert_dato_field = registrert_dato_field
        if beta_gruppe_kode_field is not None:
            self.beta_gruppe_kode_field = beta_gruppe_kode_field
        if beta_gruppe_tekst_field is not None:
            self.beta_gruppe_tekst_field = beta_gruppe_tekst_field
        if beta_type_field is not None:
            self.beta_type_field = beta_type_field
        if beta_tekst_field is not None:
            self.beta_tekst_field = beta_tekst_field
        if beta_belop_field is not None:
            self.beta_belop_field = beta_belop_field
        if kilde_kode_field is not None:
            self.kilde_kode_field = kilde_kode_field
        if kilde_tekst_field is not None:
            self.kilde_tekst_field = kilde_tekst_field
        if kilde_referansenr_field is not None:
            self.kilde_referansenr_field = kilde_referansenr_field
        if status_anmerkning_field is not None:
            self.status_anmerkning_field = status_anmerkning_field
        if status_dato_field is not None:
            self.status_dato_field = status_dato_field
        if kreditor_field is not None:
            self.kreditor_field = kreditor_field

    @property
    def registrert_dato_field(self):
        """Gets the registrert_dato_field of this PersonBetaDetaljer.  


        :return: The registrert_dato_field of this PersonBetaDetaljer.  
        :rtype: datetime
        """
        return self._registrert_dato_field

    @registrert_dato_field.setter
    def registrert_dato_field(self, registrert_dato_field):
        """Sets the registrert_dato_field of this PersonBetaDetaljer.


        :param registrert_dato_field: The registrert_dato_field of this PersonBetaDetaljer.  
        :type: datetime
        """

        self._registrert_dato_field = registrert_dato_field

    @property
    def beta_gruppe_kode_field(self):
        """Gets the beta_gruppe_kode_field of this PersonBetaDetaljer.  


        :return: The beta_gruppe_kode_field of this PersonBetaDetaljer.  
        :rtype: str
        """
        return self._beta_gruppe_kode_field

    @beta_gruppe_kode_field.setter
    def beta_gruppe_kode_field(self, beta_gruppe_kode_field):
        """Sets the beta_gruppe_kode_field of this PersonBetaDetaljer.


        :param beta_gruppe_kode_field: The beta_gruppe_kode_field of this PersonBetaDetaljer.  
        :type: str
        """

        self._beta_gruppe_kode_field = beta_gruppe_kode_field

    @property
    def beta_gruppe_tekst_field(self):
        """Gets the beta_gruppe_tekst_field of this PersonBetaDetaljer.  


        :return: The beta_gruppe_tekst_field of this PersonBetaDetaljer.  
        :rtype: str
        """
        return self._beta_gruppe_tekst_field

    @beta_gruppe_tekst_field.setter
    def beta_gruppe_tekst_field(self, beta_gruppe_tekst_field):
        """Sets the beta_gruppe_tekst_field of this PersonBetaDetaljer.


        :param beta_gruppe_tekst_field: The beta_gruppe_tekst_field of this PersonBetaDetaljer.  
        :type: str
        """

        self._beta_gruppe_tekst_field = beta_gruppe_tekst_field

    @property
    def beta_type_field(self):
        """Gets the beta_type_field of this PersonBetaDetaljer.  


        :return: The beta_type_field of this PersonBetaDetaljer.  
        :rtype: str
        """
        return self._beta_type_field

    @beta_type_field.setter
    def beta_type_field(self, beta_type_field):
        """Sets the beta_type_field of this PersonBetaDetaljer.


        :param beta_type_field: The beta_type_field of this PersonBetaDetaljer.  
        :type: str
        """

        self._beta_type_field = beta_type_field

    @property
    def beta_tekst_field(self):
        """Gets the beta_tekst_field of this PersonBetaDetaljer.  


        :return: The beta_tekst_field of this PersonBetaDetaljer.  
        :rtype: str
        """
        return self._beta_tekst_field

    @beta_tekst_field.setter
    def beta_tekst_field(self, beta_tekst_field):
        """Sets the beta_tekst_field of this PersonBetaDetaljer.


        :param beta_tekst_field: The beta_tekst_field of this PersonBetaDetaljer.  
        :type: str
        """

        self._beta_tekst_field = beta_tekst_field

    @property
    def beta_belop_field(self):
        """Gets the beta_belop_field of this PersonBetaDetaljer.  


        :return: The beta_belop_field of this PersonBetaDetaljer.  
        :rtype: int
        """
        return self._beta_belop_field

    @beta_belop_field.setter
    def beta_belop_field(self, beta_belop_field):
        """Sets the beta_belop_field of this PersonBetaDetaljer.


        :param beta_belop_field: The beta_belop_field of this PersonBetaDetaljer.  
        :type: int
        """

        self._beta_belop_field = beta_belop_field

    @property
    def kilde_kode_field(self):
        """Gets the kilde_kode_field of this PersonBetaDetaljer.  


        :return: The kilde_kode_field of this PersonBetaDetaljer.  
        :rtype: str
        """
        return self._kilde_kode_field

    @kilde_kode_field.setter
    def kilde_kode_field(self, kilde_kode_field):
        """Sets the kilde_kode_field of this PersonBetaDetaljer.


        :param kilde_kode_field: The kilde_kode_field of this PersonBetaDetaljer.  
        :type: str
        """

        self._kilde_kode_field = kilde_kode_field

    @property
    def kilde_tekst_field(self):
        """Gets the kilde_tekst_field of this PersonBetaDetaljer.  


        :return: The kilde_tekst_field of this PersonBetaDetaljer.  
        :rtype: str
        """
        return self._kilde_tekst_field

    @kilde_tekst_field.setter
    def kilde_tekst_field(self, kilde_tekst_field):
        """Sets the kilde_tekst_field of this PersonBetaDetaljer.


        :param kilde_tekst_field: The kilde_tekst_field of this PersonBetaDetaljer.  
        :type: str
        """

        self._kilde_tekst_field = kilde_tekst_field

    @property
    def kilde_referansenr_field(self):
        """Gets the kilde_referansenr_field of this PersonBetaDetaljer.  


        :return: The kilde_referansenr_field of this PersonBetaDetaljer.  
        :rtype: int
        """
        return self._kilde_referansenr_field

    @kilde_referansenr_field.setter
    def kilde_referansenr_field(self, kilde_referansenr_field):
        """Sets the kilde_referansenr_field of this PersonBetaDetaljer.


        :param kilde_referansenr_field: The kilde_referansenr_field of this PersonBetaDetaljer.  
        :type: int
        """

        self._kilde_referansenr_field = kilde_referansenr_field

    @property
    def status_anmerkning_field(self):
        """Gets the status_anmerkning_field of this PersonBetaDetaljer.  


        :return: The status_anmerkning_field of this PersonBetaDetaljer.  
        :rtype: str
        """
        return self._status_anmerkning_field

    @status_anmerkning_field.setter
    def status_anmerkning_field(self, status_anmerkning_field):
        """Sets the status_anmerkning_field of this PersonBetaDetaljer.


        :param status_anmerkning_field: The status_anmerkning_field of this PersonBetaDetaljer.  
        :type: str
        """

        self._status_anmerkning_field = status_anmerkning_field

    @property
    def status_dato_field(self):
        """Gets the status_dato_field of this PersonBetaDetaljer.  


        :return: The status_dato_field of this PersonBetaDetaljer.  
        :rtype: datetime
        """
        return self._status_dato_field

    @status_dato_field.setter
    def status_dato_field(self, status_dato_field):
        """Sets the status_dato_field of this PersonBetaDetaljer.


        :param status_dato_field: The status_dato_field of this PersonBetaDetaljer.  
        :type: datetime
        """

        self._status_dato_field = status_dato_field

    @property
    def kreditor_field(self):
        """Gets the kreditor_field of this PersonBetaDetaljer.  


        :return: The kreditor_field of this PersonBetaDetaljer.  
        :rtype: str
        """
        return self._kreditor_field

    @kreditor_field.setter
    def kreditor_field(self, kreditor_field):
        """Sets the kreditor_field of this PersonBetaDetaljer.


        :param kreditor_field: The kreditor_field of this PersonBetaDetaljer.  
        :type: str
        """

        self._kreditor_field = kreditor_field

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
        if not isinstance(other, PersonBetaDetaljer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
