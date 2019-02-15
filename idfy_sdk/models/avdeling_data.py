# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class AvdelingData(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'antall_ansatte_field': 'int',
        'antall_ansatte_field_specified': 'bool',
        'telefon_field': 'int',
        'telefon_field_specified': 'bool',
        'telefax_field': 'int',
        'telefax_field_specified': 'bool',
        'stiftet_dato_field': 'datetime',
        'bransje_kode_field': 'str',
        'bransje_tekst_field': 'str',
        'daglig_leder_field': 'str',
        'hovedforetak_orgnr_field': 'int',
        'hovedforetak_orgnr_field_specified': 'bool',
        'hovedforetak_dunsnr_field': 'int',
        'hovedforetak_dunsnr_field_specified': 'bool',
        'hovedforetak_navn_field': 'str'
    }

    attribute_map = {
        'antall_ansatte_field': 'antallAnsatteField',
        'antall_ansatte_field_specified': 'antallAnsatteFieldSpecified',
        'telefon_field': 'telefonField',
        'telefon_field_specified': 'telefonFieldSpecified',
        'telefax_field': 'telefaxField',
        'telefax_field_specified': 'telefaxFieldSpecified',
        'stiftet_dato_field': 'stiftetDatoField',
        'bransje_kode_field': 'bransjeKodeField',
        'bransje_tekst_field': 'bransjeTekstField',
        'daglig_leder_field': 'dagligLederField',
        'hovedforetak_orgnr_field': 'hovedforetakOrgnrField',
        'hovedforetak_orgnr_field_specified': 'hovedforetakOrgnrFieldSpecified',
        'hovedforetak_dunsnr_field': 'hovedforetakDunsnrField',
        'hovedforetak_dunsnr_field_specified': 'hovedforetakDunsnrFieldSpecified',
        'hovedforetak_navn_field': 'hovedforetakNavnField'
    }

    def __init__(self, antall_ansatte_field=None, antall_ansatte_field_specified=None, telefon_field=None, telefon_field_specified=None, telefax_field=None, telefax_field_specified=None, stiftet_dato_field=None, bransje_kode_field=None, bransje_tekst_field=None, daglig_leder_field=None, hovedforetak_orgnr_field=None, hovedforetak_orgnr_field_specified=None, hovedforetak_dunsnr_field=None, hovedforetak_dunsnr_field_specified=None, hovedforetak_navn_field=None):  
        """AvdelingData"""  

        self._antall_ansatte_field = None
        self._antall_ansatte_field_specified = None
        self._telefon_field = None
        self._telefon_field_specified = None
        self._telefax_field = None
        self._telefax_field_specified = None
        self._stiftet_dato_field = None
        self._bransje_kode_field = None
        self._bransje_tekst_field = None
        self._daglig_leder_field = None
        self._hovedforetak_orgnr_field = None
        self._hovedforetak_orgnr_field_specified = None
        self._hovedforetak_dunsnr_field = None
        self._hovedforetak_dunsnr_field_specified = None
        self._hovedforetak_navn_field = None
        self.discriminator = None

        if antall_ansatte_field is not None:
            self.antall_ansatte_field = antall_ansatte_field
        if antall_ansatte_field_specified is not None:
            self.antall_ansatte_field_specified = antall_ansatte_field_specified
        if telefon_field is not None:
            self.telefon_field = telefon_field
        if telefon_field_specified is not None:
            self.telefon_field_specified = telefon_field_specified
        if telefax_field is not None:
            self.telefax_field = telefax_field
        if telefax_field_specified is not None:
            self.telefax_field_specified = telefax_field_specified
        if stiftet_dato_field is not None:
            self.stiftet_dato_field = stiftet_dato_field
        if bransje_kode_field is not None:
            self.bransje_kode_field = bransje_kode_field
        if bransje_tekst_field is not None:
            self.bransje_tekst_field = bransje_tekst_field
        if daglig_leder_field is not None:
            self.daglig_leder_field = daglig_leder_field
        if hovedforetak_orgnr_field is not None:
            self.hovedforetak_orgnr_field = hovedforetak_orgnr_field
        if hovedforetak_orgnr_field_specified is not None:
            self.hovedforetak_orgnr_field_specified = hovedforetak_orgnr_field_specified
        if hovedforetak_dunsnr_field is not None:
            self.hovedforetak_dunsnr_field = hovedforetak_dunsnr_field
        if hovedforetak_dunsnr_field_specified is not None:
            self.hovedforetak_dunsnr_field_specified = hovedforetak_dunsnr_field_specified
        if hovedforetak_navn_field is not None:
            self.hovedforetak_navn_field = hovedforetak_navn_field

    @property
    def antall_ansatte_field(self):
        """Gets the antall_ansatte_field of this AvdelingData.  


        :return: The antall_ansatte_field of this AvdelingData.  
        :rtype: int
        """
        return self._antall_ansatte_field

    @antall_ansatte_field.setter
    def antall_ansatte_field(self, antall_ansatte_field):
        """Sets the antall_ansatte_field of this AvdelingData.


        :param antall_ansatte_field: The antall_ansatte_field of this AvdelingData.  
        :type: int
        """

        self._antall_ansatte_field = antall_ansatte_field

    @property
    def antall_ansatte_field_specified(self):
        """Gets the antall_ansatte_field_specified of this AvdelingData.  


        :return: The antall_ansatte_field_specified of this AvdelingData.  
        :rtype: bool
        """
        return self._antall_ansatte_field_specified

    @antall_ansatte_field_specified.setter
    def antall_ansatte_field_specified(self, antall_ansatte_field_specified):
        """Sets the antall_ansatte_field_specified of this AvdelingData.


        :param antall_ansatte_field_specified: The antall_ansatte_field_specified of this AvdelingData.  
        :type: bool
        """

        self._antall_ansatte_field_specified = antall_ansatte_field_specified

    @property
    def telefon_field(self):
        """Gets the telefon_field of this AvdelingData.  


        :return: The telefon_field of this AvdelingData.  
        :rtype: int
        """
        return self._telefon_field

    @telefon_field.setter
    def telefon_field(self, telefon_field):
        """Sets the telefon_field of this AvdelingData.


        :param telefon_field: The telefon_field of this AvdelingData.  
        :type: int
        """

        self._telefon_field = telefon_field

    @property
    def telefon_field_specified(self):
        """Gets the telefon_field_specified of this AvdelingData.  


        :return: The telefon_field_specified of this AvdelingData.  
        :rtype: bool
        """
        return self._telefon_field_specified

    @telefon_field_specified.setter
    def telefon_field_specified(self, telefon_field_specified):
        """Sets the telefon_field_specified of this AvdelingData.


        :param telefon_field_specified: The telefon_field_specified of this AvdelingData.  
        :type: bool
        """

        self._telefon_field_specified = telefon_field_specified

    @property
    def telefax_field(self):
        """Gets the telefax_field of this AvdelingData.  


        :return: The telefax_field of this AvdelingData.  
        :rtype: int
        """
        return self._telefax_field

    @telefax_field.setter
    def telefax_field(self, telefax_field):
        """Sets the telefax_field of this AvdelingData.


        :param telefax_field: The telefax_field of this AvdelingData.  
        :type: int
        """

        self._telefax_field = telefax_field

    @property
    def telefax_field_specified(self):
        """Gets the telefax_field_specified of this AvdelingData.  


        :return: The telefax_field_specified of this AvdelingData.  
        :rtype: bool
        """
        return self._telefax_field_specified

    @telefax_field_specified.setter
    def telefax_field_specified(self, telefax_field_specified):
        """Sets the telefax_field_specified of this AvdelingData.


        :param telefax_field_specified: The telefax_field_specified of this AvdelingData.  
        :type: bool
        """

        self._telefax_field_specified = telefax_field_specified

    @property
    def stiftet_dato_field(self):
        """Gets the stiftet_dato_field of this AvdelingData.  


        :return: The stiftet_dato_field of this AvdelingData.  
        :rtype: datetime
        """
        return self._stiftet_dato_field

    @stiftet_dato_field.setter
    def stiftet_dato_field(self, stiftet_dato_field):
        """Sets the stiftet_dato_field of this AvdelingData.


        :param stiftet_dato_field: The stiftet_dato_field of this AvdelingData.  
        :type: datetime
        """

        self._stiftet_dato_field = stiftet_dato_field

    @property
    def bransje_kode_field(self):
        """Gets the bransje_kode_field of this AvdelingData.  


        :return: The bransje_kode_field of this AvdelingData.  
        :rtype: str
        """
        return self._bransje_kode_field

    @bransje_kode_field.setter
    def bransje_kode_field(self, bransje_kode_field):
        """Sets the bransje_kode_field of this AvdelingData.


        :param bransje_kode_field: The bransje_kode_field of this AvdelingData.  
        :type: str
        """

        self._bransje_kode_field = bransje_kode_field

    @property
    def bransje_tekst_field(self):
        """Gets the bransje_tekst_field of this AvdelingData.  


        :return: The bransje_tekst_field of this AvdelingData.  
        :rtype: str
        """
        return self._bransje_tekst_field

    @bransje_tekst_field.setter
    def bransje_tekst_field(self, bransje_tekst_field):
        """Sets the bransje_tekst_field of this AvdelingData.


        :param bransje_tekst_field: The bransje_tekst_field of this AvdelingData.  
        :type: str
        """

        self._bransje_tekst_field = bransje_tekst_field

    @property
    def daglig_leder_field(self):
        """Gets the daglig_leder_field of this AvdelingData.  


        :return: The daglig_leder_field of this AvdelingData.  
        :rtype: str
        """
        return self._daglig_leder_field

    @daglig_leder_field.setter
    def daglig_leder_field(self, daglig_leder_field):
        """Sets the daglig_leder_field of this AvdelingData.


        :param daglig_leder_field: The daglig_leder_field of this AvdelingData.  
        :type: str
        """

        self._daglig_leder_field = daglig_leder_field

    @property
    def hovedforetak_orgnr_field(self):
        """Gets the hovedforetak_orgnr_field of this AvdelingData.  


        :return: The hovedforetak_orgnr_field of this AvdelingData.  
        :rtype: int
        """
        return self._hovedforetak_orgnr_field

    @hovedforetak_orgnr_field.setter
    def hovedforetak_orgnr_field(self, hovedforetak_orgnr_field):
        """Sets the hovedforetak_orgnr_field of this AvdelingData.


        :param hovedforetak_orgnr_field: The hovedforetak_orgnr_field of this AvdelingData.  
        :type: int
        """

        self._hovedforetak_orgnr_field = hovedforetak_orgnr_field

    @property
    def hovedforetak_orgnr_field_specified(self):
        """Gets the hovedforetak_orgnr_field_specified of this AvdelingData.  


        :return: The hovedforetak_orgnr_field_specified of this AvdelingData.  
        :rtype: bool
        """
        return self._hovedforetak_orgnr_field_specified

    @hovedforetak_orgnr_field_specified.setter
    def hovedforetak_orgnr_field_specified(self, hovedforetak_orgnr_field_specified):
        """Sets the hovedforetak_orgnr_field_specified of this AvdelingData.


        :param hovedforetak_orgnr_field_specified: The hovedforetak_orgnr_field_specified of this AvdelingData.  
        :type: bool
        """

        self._hovedforetak_orgnr_field_specified = hovedforetak_orgnr_field_specified

    @property
    def hovedforetak_dunsnr_field(self):
        """Gets the hovedforetak_dunsnr_field of this AvdelingData.  


        :return: The hovedforetak_dunsnr_field of this AvdelingData.  
        :rtype: int
        """
        return self._hovedforetak_dunsnr_field

    @hovedforetak_dunsnr_field.setter
    def hovedforetak_dunsnr_field(self, hovedforetak_dunsnr_field):
        """Sets the hovedforetak_dunsnr_field of this AvdelingData.


        :param hovedforetak_dunsnr_field: The hovedforetak_dunsnr_field of this AvdelingData.  
        :type: int
        """

        self._hovedforetak_dunsnr_field = hovedforetak_dunsnr_field

    @property
    def hovedforetak_dunsnr_field_specified(self):
        """Gets the hovedforetak_dunsnr_field_specified of this AvdelingData.  


        :return: The hovedforetak_dunsnr_field_specified of this AvdelingData.  
        :rtype: bool
        """
        return self._hovedforetak_dunsnr_field_specified

    @hovedforetak_dunsnr_field_specified.setter
    def hovedforetak_dunsnr_field_specified(self, hovedforetak_dunsnr_field_specified):
        """Sets the hovedforetak_dunsnr_field_specified of this AvdelingData.


        :param hovedforetak_dunsnr_field_specified: The hovedforetak_dunsnr_field_specified of this AvdelingData.  
        :type: bool
        """

        self._hovedforetak_dunsnr_field_specified = hovedforetak_dunsnr_field_specified

    @property
    def hovedforetak_navn_field(self):
        """Gets the hovedforetak_navn_field of this AvdelingData.  


        :return: The hovedforetak_navn_field of this AvdelingData.  
        :rtype: str
        """
        return self._hovedforetak_navn_field

    @hovedforetak_navn_field.setter
    def hovedforetak_navn_field(self, hovedforetak_navn_field):
        """Sets the hovedforetak_navn_field of this AvdelingData.


        :param hovedforetak_navn_field: The hovedforetak_navn_field of this AvdelingData.  
        :type: str
        """

        self._hovedforetak_navn_field = hovedforetak_navn_field

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
        if not isinstance(other, AvdelingData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
