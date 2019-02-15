# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.ansatte_data import AnsatteData  
from idfy_sdk.models.bransje_data import BransjeData  


class Grunnfakta(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'selsk_form_kode_field': 'str',
        'selsk_form_tekst_field': 'str',
        'etablert_ar_field': 'int',
        'etablert_ar_field_specified': 'bool',
        'stiftet_dato_field': 'datetime',
        'aksjekapital_field': 'int',
        'aksjekapital_status_field': 'str',
        'registrert_sted_field': 'str',
        'registrert_dato_field': 'datetime',
        'revisor_orgnr_field': 'int',
        'revisor_navn_field': 'str',
        'bank_regnr_field': 'int',
        'bank_navn_field': 'str',
        'bransje_data_field': 'list[BransjeData]',
        'ansatte_data_field': 'list[AnsatteData]'
    }

    attribute_map = {
        'selsk_form_kode_field': 'selskFormKodeField',
        'selsk_form_tekst_field': 'selskFormTekstField',
        'etablert_ar_field': 'etablertArField',
        'etablert_ar_field_specified': 'etablertArFieldSpecified',
        'stiftet_dato_field': 'stiftetDatoField',
        'aksjekapital_field': 'aksjekapitalField',
        'aksjekapital_status_field': 'aksjekapitalStatusField',
        'registrert_sted_field': 'registrertStedField',
        'registrert_dato_field': 'registrertDatoField',
        'revisor_orgnr_field': 'revisorOrgnrField',
        'revisor_navn_field': 'revisorNavnField',
        'bank_regnr_field': 'bankRegnrField',
        'bank_navn_field': 'bankNavnField',
        'bransje_data_field': 'bransjeDataField',
        'ansatte_data_field': 'ansatteDataField'
    }

    def __init__(self, selsk_form_kode_field=None, selsk_form_tekst_field=None, etablert_ar_field=None, etablert_ar_field_specified=None, stiftet_dato_field=None, aksjekapital_field=None, aksjekapital_status_field=None, registrert_sted_field=None, registrert_dato_field=None, revisor_orgnr_field=None, revisor_navn_field=None, bank_regnr_field=None, bank_navn_field=None, bransje_data_field=None, ansatte_data_field=None):  
        """Grunnfakta"""  

        self._selsk_form_kode_field = None
        self._selsk_form_tekst_field = None
        self._etablert_ar_field = None
        self._etablert_ar_field_specified = None
        self._stiftet_dato_field = None
        self._aksjekapital_field = None
        self._aksjekapital_status_field = None
        self._registrert_sted_field = None
        self._registrert_dato_field = None
        self._revisor_orgnr_field = None
        self._revisor_navn_field = None
        self._bank_regnr_field = None
        self._bank_navn_field = None
        self._bransje_data_field = None
        self._ansatte_data_field = None
        self.discriminator = None

        if selsk_form_kode_field is not None:
            self.selsk_form_kode_field = selsk_form_kode_field
        if selsk_form_tekst_field is not None:
            self.selsk_form_tekst_field = selsk_form_tekst_field
        if etablert_ar_field is not None:
            self.etablert_ar_field = etablert_ar_field
        if etablert_ar_field_specified is not None:
            self.etablert_ar_field_specified = etablert_ar_field_specified
        if stiftet_dato_field is not None:
            self.stiftet_dato_field = stiftet_dato_field
        if aksjekapital_field is not None:
            self.aksjekapital_field = aksjekapital_field
        if aksjekapital_status_field is not None:
            self.aksjekapital_status_field = aksjekapital_status_field
        if registrert_sted_field is not None:
            self.registrert_sted_field = registrert_sted_field
        if registrert_dato_field is not None:
            self.registrert_dato_field = registrert_dato_field
        if revisor_orgnr_field is not None:
            self.revisor_orgnr_field = revisor_orgnr_field
        if revisor_navn_field is not None:
            self.revisor_navn_field = revisor_navn_field
        if bank_regnr_field is not None:
            self.bank_regnr_field = bank_regnr_field
        if bank_navn_field is not None:
            self.bank_navn_field = bank_navn_field
        if bransje_data_field is not None:
            self.bransje_data_field = bransje_data_field
        if ansatte_data_field is not None:
            self.ansatte_data_field = ansatte_data_field

    @property
    def selsk_form_kode_field(self):
        """Gets the selsk_form_kode_field of this Grunnfakta.  


        :return: The selsk_form_kode_field of this Grunnfakta.  
        :rtype: str
        """
        return self._selsk_form_kode_field

    @selsk_form_kode_field.setter
    def selsk_form_kode_field(self, selsk_form_kode_field):
        """Sets the selsk_form_kode_field of this Grunnfakta.


        :param selsk_form_kode_field: The selsk_form_kode_field of this Grunnfakta.  
        :type: str
        """

        self._selsk_form_kode_field = selsk_form_kode_field

    @property
    def selsk_form_tekst_field(self):
        """Gets the selsk_form_tekst_field of this Grunnfakta.  


        :return: The selsk_form_tekst_field of this Grunnfakta.  
        :rtype: str
        """
        return self._selsk_form_tekst_field

    @selsk_form_tekst_field.setter
    def selsk_form_tekst_field(self, selsk_form_tekst_field):
        """Sets the selsk_form_tekst_field of this Grunnfakta.


        :param selsk_form_tekst_field: The selsk_form_tekst_field of this Grunnfakta.  
        :type: str
        """

        self._selsk_form_tekst_field = selsk_form_tekst_field

    @property
    def etablert_ar_field(self):
        """Gets the etablert_ar_field of this Grunnfakta.  


        :return: The etablert_ar_field of this Grunnfakta.  
        :rtype: int
        """
        return self._etablert_ar_field

    @etablert_ar_field.setter
    def etablert_ar_field(self, etablert_ar_field):
        """Sets the etablert_ar_field of this Grunnfakta.


        :param etablert_ar_field: The etablert_ar_field of this Grunnfakta.  
        :type: int
        """

        self._etablert_ar_field = etablert_ar_field

    @property
    def etablert_ar_field_specified(self):
        """Gets the etablert_ar_field_specified of this Grunnfakta.  


        :return: The etablert_ar_field_specified of this Grunnfakta.  
        :rtype: bool
        """
        return self._etablert_ar_field_specified

    @etablert_ar_field_specified.setter
    def etablert_ar_field_specified(self, etablert_ar_field_specified):
        """Sets the etablert_ar_field_specified of this Grunnfakta.


        :param etablert_ar_field_specified: The etablert_ar_field_specified of this Grunnfakta.  
        :type: bool
        """

        self._etablert_ar_field_specified = etablert_ar_field_specified

    @property
    def stiftet_dato_field(self):
        """Gets the stiftet_dato_field of this Grunnfakta.  


        :return: The stiftet_dato_field of this Grunnfakta.  
        :rtype: datetime
        """
        return self._stiftet_dato_field

    @stiftet_dato_field.setter
    def stiftet_dato_field(self, stiftet_dato_field):
        """Sets the stiftet_dato_field of this Grunnfakta.


        :param stiftet_dato_field: The stiftet_dato_field of this Grunnfakta.  
        :type: datetime
        """

        self._stiftet_dato_field = stiftet_dato_field

    @property
    def aksjekapital_field(self):
        """Gets the aksjekapital_field of this Grunnfakta.  


        :return: The aksjekapital_field of this Grunnfakta.  
        :rtype: int
        """
        return self._aksjekapital_field

    @aksjekapital_field.setter
    def aksjekapital_field(self, aksjekapital_field):
        """Sets the aksjekapital_field of this Grunnfakta.


        :param aksjekapital_field: The aksjekapital_field of this Grunnfakta.  
        :type: int
        """

        self._aksjekapital_field = aksjekapital_field

    @property
    def aksjekapital_status_field(self):
        """Gets the aksjekapital_status_field of this Grunnfakta.  


        :return: The aksjekapital_status_field of this Grunnfakta.  
        :rtype: str
        """
        return self._aksjekapital_status_field

    @aksjekapital_status_field.setter
    def aksjekapital_status_field(self, aksjekapital_status_field):
        """Sets the aksjekapital_status_field of this Grunnfakta.


        :param aksjekapital_status_field: The aksjekapital_status_field of this Grunnfakta.  
        :type: str
        """

        self._aksjekapital_status_field = aksjekapital_status_field

    @property
    def registrert_sted_field(self):
        """Gets the registrert_sted_field of this Grunnfakta.  


        :return: The registrert_sted_field of this Grunnfakta.  
        :rtype: str
        """
        return self._registrert_sted_field

    @registrert_sted_field.setter
    def registrert_sted_field(self, registrert_sted_field):
        """Sets the registrert_sted_field of this Grunnfakta.


        :param registrert_sted_field: The registrert_sted_field of this Grunnfakta.  
        :type: str
        """

        self._registrert_sted_field = registrert_sted_field

    @property
    def registrert_dato_field(self):
        """Gets the registrert_dato_field of this Grunnfakta.  


        :return: The registrert_dato_field of this Grunnfakta.  
        :rtype: datetime
        """
        return self._registrert_dato_field

    @registrert_dato_field.setter
    def registrert_dato_field(self, registrert_dato_field):
        """Sets the registrert_dato_field of this Grunnfakta.


        :param registrert_dato_field: The registrert_dato_field of this Grunnfakta.  
        :type: datetime
        """

        self._registrert_dato_field = registrert_dato_field

    @property
    def revisor_orgnr_field(self):
        """Gets the revisor_orgnr_field of this Grunnfakta.  


        :return: The revisor_orgnr_field of this Grunnfakta.  
        :rtype: int
        """
        return self._revisor_orgnr_field

    @revisor_orgnr_field.setter
    def revisor_orgnr_field(self, revisor_orgnr_field):
        """Sets the revisor_orgnr_field of this Grunnfakta.


        :param revisor_orgnr_field: The revisor_orgnr_field of this Grunnfakta.  
        :type: int
        """

        self._revisor_orgnr_field = revisor_orgnr_field

    @property
    def revisor_navn_field(self):
        """Gets the revisor_navn_field of this Grunnfakta.  


        :return: The revisor_navn_field of this Grunnfakta.  
        :rtype: str
        """
        return self._revisor_navn_field

    @revisor_navn_field.setter
    def revisor_navn_field(self, revisor_navn_field):
        """Sets the revisor_navn_field of this Grunnfakta.


        :param revisor_navn_field: The revisor_navn_field of this Grunnfakta.  
        :type: str
        """

        self._revisor_navn_field = revisor_navn_field

    @property
    def bank_regnr_field(self):
        """Gets the bank_regnr_field of this Grunnfakta.  


        :return: The bank_regnr_field of this Grunnfakta.  
        :rtype: int
        """
        return self._bank_regnr_field

    @bank_regnr_field.setter
    def bank_regnr_field(self, bank_regnr_field):
        """Sets the bank_regnr_field of this Grunnfakta.


        :param bank_regnr_field: The bank_regnr_field of this Grunnfakta.  
        :type: int
        """

        self._bank_regnr_field = bank_regnr_field

    @property
    def bank_navn_field(self):
        """Gets the bank_navn_field of this Grunnfakta.  


        :return: The bank_navn_field of this Grunnfakta.  
        :rtype: str
        """
        return self._bank_navn_field

    @bank_navn_field.setter
    def bank_navn_field(self, bank_navn_field):
        """Sets the bank_navn_field of this Grunnfakta.


        :param bank_navn_field: The bank_navn_field of this Grunnfakta.  
        :type: str
        """

        self._bank_navn_field = bank_navn_field

    @property
    def bransje_data_field(self):
        """Gets the bransje_data_field of this Grunnfakta.  


        :return: The bransje_data_field of this Grunnfakta.  
        :rtype: list[BransjeData]
        """
        return self._bransje_data_field

    @bransje_data_field.setter
    def bransje_data_field(self, bransje_data_field):
        """Sets the bransje_data_field of this Grunnfakta.


        :param bransje_data_field: The bransje_data_field of this Grunnfakta.  
        :type: list[BransjeData]
        """

        self._bransje_data_field = bransje_data_field

    @property
    def ansatte_data_field(self):
        """Gets the ansatte_data_field of this Grunnfakta.  


        :return: The ansatte_data_field of this Grunnfakta.  
        :rtype: list[AnsatteData]
        """
        return self._ansatte_data_field

    @ansatte_data_field.setter
    def ansatte_data_field(self, ansatte_data_field):
        """Sets the ansatte_data_field of this Grunnfakta.


        :param ansatte_data_field: The ansatte_data_field of this Grunnfakta.  
        :type: list[AnsatteData]
        """

        self._ansatte_data_field = ansatte_data_field

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
        if not isinstance(other, Grunnfakta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
