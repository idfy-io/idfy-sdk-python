# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.person_fullmakt_person import PersonFullmaktPerson  


class PersonFullmaktForetak(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dunsnr_field': 'int',
        'orgnr_field': 'int',
        'navn_field': 'str',
        'adresse_field': 'str',
        'postnr_field': 'int',
        'poststed_field': 'str',
        'status_kode_field': 'str',
        'status_tekst_field': 'str',
        'selskapsform_field': 'str',
        'prokura_kode_field': 'str',
        'prokura_tekst_field': 'str',
        'signatur_kode_field': 'str',
        'signatur_tekst_field': 'str',
        'fullmakt_person_field': 'list[PersonFullmaktPerson]'
    }

    attribute_map = {
        'dunsnr_field': 'dunsnrField',
        'orgnr_field': 'orgnrField',
        'navn_field': 'navnField',
        'adresse_field': 'adresseField',
        'postnr_field': 'postnrField',
        'poststed_field': 'poststedField',
        'status_kode_field': 'statusKodeField',
        'status_tekst_field': 'statusTekstField',
        'selskapsform_field': 'selskapsformField',
        'prokura_kode_field': 'prokuraKodeField',
        'prokura_tekst_field': 'prokuraTekstField',
        'signatur_kode_field': 'signaturKodeField',
        'signatur_tekst_field': 'signaturTekstField',
        'fullmakt_person_field': 'fullmaktPersonField'
    }

    def __init__(self, dunsnr_field=None, orgnr_field=None, navn_field=None, adresse_field=None, postnr_field=None, poststed_field=None, status_kode_field=None, status_tekst_field=None, selskapsform_field=None, prokura_kode_field=None, prokura_tekst_field=None, signatur_kode_field=None, signatur_tekst_field=None, fullmakt_person_field=None):  
        """PersonFullmaktForetak"""  

        self._dunsnr_field = None
        self._orgnr_field = None
        self._navn_field = None
        self._adresse_field = None
        self._postnr_field = None
        self._poststed_field = None
        self._status_kode_field = None
        self._status_tekst_field = None
        self._selskapsform_field = None
        self._prokura_kode_field = None
        self._prokura_tekst_field = None
        self._signatur_kode_field = None
        self._signatur_tekst_field = None
        self._fullmakt_person_field = None
        self.discriminator = None

        if dunsnr_field is not None:
            self.dunsnr_field = dunsnr_field
        if orgnr_field is not None:
            self.orgnr_field = orgnr_field
        if navn_field is not None:
            self.navn_field = navn_field
        if adresse_field is not None:
            self.adresse_field = adresse_field
        if postnr_field is not None:
            self.postnr_field = postnr_field
        if poststed_field is not None:
            self.poststed_field = poststed_field
        if status_kode_field is not None:
            self.status_kode_field = status_kode_field
        if status_tekst_field is not None:
            self.status_tekst_field = status_tekst_field
        if selskapsform_field is not None:
            self.selskapsform_field = selskapsform_field
        if prokura_kode_field is not None:
            self.prokura_kode_field = prokura_kode_field
        if prokura_tekst_field is not None:
            self.prokura_tekst_field = prokura_tekst_field
        if signatur_kode_field is not None:
            self.signatur_kode_field = signatur_kode_field
        if signatur_tekst_field is not None:
            self.signatur_tekst_field = signatur_tekst_field
        if fullmakt_person_field is not None:
            self.fullmakt_person_field = fullmakt_person_field

    @property
    def dunsnr_field(self):
        """Gets the dunsnr_field of this PersonFullmaktForetak.  


        :return: The dunsnr_field of this PersonFullmaktForetak.  
        :rtype: int
        """
        return self._dunsnr_field

    @dunsnr_field.setter
    def dunsnr_field(self, dunsnr_field):
        """Sets the dunsnr_field of this PersonFullmaktForetak.


        :param dunsnr_field: The dunsnr_field of this PersonFullmaktForetak.  
        :type: int
        """

        self._dunsnr_field = dunsnr_field

    @property
    def orgnr_field(self):
        """Gets the orgnr_field of this PersonFullmaktForetak.  


        :return: The orgnr_field of this PersonFullmaktForetak.  
        :rtype: int
        """
        return self._orgnr_field

    @orgnr_field.setter
    def orgnr_field(self, orgnr_field):
        """Sets the orgnr_field of this PersonFullmaktForetak.


        :param orgnr_field: The orgnr_field of this PersonFullmaktForetak.  
        :type: int
        """

        self._orgnr_field = orgnr_field

    @property
    def navn_field(self):
        """Gets the navn_field of this PersonFullmaktForetak.  


        :return: The navn_field of this PersonFullmaktForetak.  
        :rtype: str
        """
        return self._navn_field

    @navn_field.setter
    def navn_field(self, navn_field):
        """Sets the navn_field of this PersonFullmaktForetak.


        :param navn_field: The navn_field of this PersonFullmaktForetak.  
        :type: str
        """

        self._navn_field = navn_field

    @property
    def adresse_field(self):
        """Gets the adresse_field of this PersonFullmaktForetak.  


        :return: The adresse_field of this PersonFullmaktForetak.  
        :rtype: str
        """
        return self._adresse_field

    @adresse_field.setter
    def adresse_field(self, adresse_field):
        """Sets the adresse_field of this PersonFullmaktForetak.


        :param adresse_field: The adresse_field of this PersonFullmaktForetak.  
        :type: str
        """

        self._adresse_field = adresse_field

    @property
    def postnr_field(self):
        """Gets the postnr_field of this PersonFullmaktForetak.  


        :return: The postnr_field of this PersonFullmaktForetak.  
        :rtype: int
        """
        return self._postnr_field

    @postnr_field.setter
    def postnr_field(self, postnr_field):
        """Sets the postnr_field of this PersonFullmaktForetak.


        :param postnr_field: The postnr_field of this PersonFullmaktForetak.  
        :type: int
        """

        self._postnr_field = postnr_field

    @property
    def poststed_field(self):
        """Gets the poststed_field of this PersonFullmaktForetak.  


        :return: The poststed_field of this PersonFullmaktForetak.  
        :rtype: str
        """
        return self._poststed_field

    @poststed_field.setter
    def poststed_field(self, poststed_field):
        """Sets the poststed_field of this PersonFullmaktForetak.


        :param poststed_field: The poststed_field of this PersonFullmaktForetak.  
        :type: str
        """

        self._poststed_field = poststed_field

    @property
    def status_kode_field(self):
        """Gets the status_kode_field of this PersonFullmaktForetak.  


        :return: The status_kode_field of this PersonFullmaktForetak.  
        :rtype: str
        """
        return self._status_kode_field

    @status_kode_field.setter
    def status_kode_field(self, status_kode_field):
        """Sets the status_kode_field of this PersonFullmaktForetak.


        :param status_kode_field: The status_kode_field of this PersonFullmaktForetak.  
        :type: str
        """

        self._status_kode_field = status_kode_field

    @property
    def status_tekst_field(self):
        """Gets the status_tekst_field of this PersonFullmaktForetak.  


        :return: The status_tekst_field of this PersonFullmaktForetak.  
        :rtype: str
        """
        return self._status_tekst_field

    @status_tekst_field.setter
    def status_tekst_field(self, status_tekst_field):
        """Sets the status_tekst_field of this PersonFullmaktForetak.


        :param status_tekst_field: The status_tekst_field of this PersonFullmaktForetak.  
        :type: str
        """

        self._status_tekst_field = status_tekst_field

    @property
    def selskapsform_field(self):
        """Gets the selskapsform_field of this PersonFullmaktForetak.  


        :return: The selskapsform_field of this PersonFullmaktForetak.  
        :rtype: str
        """
        return self._selskapsform_field

    @selskapsform_field.setter
    def selskapsform_field(self, selskapsform_field):
        """Sets the selskapsform_field of this PersonFullmaktForetak.


        :param selskapsform_field: The selskapsform_field of this PersonFullmaktForetak.  
        :type: str
        """

        self._selskapsform_field = selskapsform_field

    @property
    def prokura_kode_field(self):
        """Gets the prokura_kode_field of this PersonFullmaktForetak.  


        :return: The prokura_kode_field of this PersonFullmaktForetak.  
        :rtype: str
        """
        return self._prokura_kode_field

    @prokura_kode_field.setter
    def prokura_kode_field(self, prokura_kode_field):
        """Sets the prokura_kode_field of this PersonFullmaktForetak.


        :param prokura_kode_field: The prokura_kode_field of this PersonFullmaktForetak.  
        :type: str
        """

        self._prokura_kode_field = prokura_kode_field

    @property
    def prokura_tekst_field(self):
        """Gets the prokura_tekst_field of this PersonFullmaktForetak.  


        :return: The prokura_tekst_field of this PersonFullmaktForetak.  
        :rtype: str
        """
        return self._prokura_tekst_field

    @prokura_tekst_field.setter
    def prokura_tekst_field(self, prokura_tekst_field):
        """Sets the prokura_tekst_field of this PersonFullmaktForetak.


        :param prokura_tekst_field: The prokura_tekst_field of this PersonFullmaktForetak.  
        :type: str
        """

        self._prokura_tekst_field = prokura_tekst_field

    @property
    def signatur_kode_field(self):
        """Gets the signatur_kode_field of this PersonFullmaktForetak.  


        :return: The signatur_kode_field of this PersonFullmaktForetak.  
        :rtype: str
        """
        return self._signatur_kode_field

    @signatur_kode_field.setter
    def signatur_kode_field(self, signatur_kode_field):
        """Sets the signatur_kode_field of this PersonFullmaktForetak.


        :param signatur_kode_field: The signatur_kode_field of this PersonFullmaktForetak.  
        :type: str
        """

        self._signatur_kode_field = signatur_kode_field

    @property
    def signatur_tekst_field(self):
        """Gets the signatur_tekst_field of this PersonFullmaktForetak.  


        :return: The signatur_tekst_field of this PersonFullmaktForetak.  
        :rtype: str
        """
        return self._signatur_tekst_field

    @signatur_tekst_field.setter
    def signatur_tekst_field(self, signatur_tekst_field):
        """Sets the signatur_tekst_field of this PersonFullmaktForetak.


        :param signatur_tekst_field: The signatur_tekst_field of this PersonFullmaktForetak.  
        :type: str
        """

        self._signatur_tekst_field = signatur_tekst_field

    @property
    def fullmakt_person_field(self):
        """Gets the fullmakt_person_field of this PersonFullmaktForetak.  


        :return: The fullmakt_person_field of this PersonFullmaktForetak.  
        :rtype: list[PersonFullmaktPerson]
        """
        return self._fullmakt_person_field

    @fullmakt_person_field.setter
    def fullmakt_person_field(self, fullmakt_person_field):
        """Sets the fullmakt_person_field of this PersonFullmaktForetak.


        :param fullmakt_person_field: The fullmakt_person_field of this PersonFullmaktForetak.  
        :type: list[PersonFullmaktPerson]
        """

        self._fullmakt_person_field = fullmakt_person_field

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
        if not isinstance(other, PersonFullmaktForetak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
