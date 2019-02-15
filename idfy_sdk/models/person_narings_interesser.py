# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonNaringsInteresser(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'orgnr_field': 'int',
        'status_kode_field': 'str',
        'status_tekst_field': 'str',
        'status_dato_field': 'datetime',
        'navn_field': 'str',
        'selsk_form_field': 'str',
        'rolle_field': 'str',
        'eierandel_field': 'float',
        'verv_kode_field': 'str',
        'verv_tekst_field': 'str'
    }

    attribute_map = {
        'orgnr_field': 'orgnrField',
        'status_kode_field': 'statusKodeField',
        'status_tekst_field': 'statusTekstField',
        'status_dato_field': 'statusDatoField',
        'navn_field': 'navnField',
        'selsk_form_field': 'selskFormField',
        'rolle_field': 'rolleField',
        'eierandel_field': 'eierandelField',
        'verv_kode_field': 'vervKodeField',
        'verv_tekst_field': 'vervTekstField'
    }

    def __init__(self, orgnr_field=None, status_kode_field=None, status_tekst_field=None, status_dato_field=None, navn_field=None, selsk_form_field=None, rolle_field=None, eierandel_field=None, verv_kode_field=None, verv_tekst_field=None):  
        """PersonNaringsInteresser"""  

        self._orgnr_field = None
        self._status_kode_field = None
        self._status_tekst_field = None
        self._status_dato_field = None
        self._navn_field = None
        self._selsk_form_field = None
        self._rolle_field = None
        self._eierandel_field = None
        self._verv_kode_field = None
        self._verv_tekst_field = None
        self.discriminator = None

        if orgnr_field is not None:
            self.orgnr_field = orgnr_field
        if status_kode_field is not None:
            self.status_kode_field = status_kode_field
        if status_tekst_field is not None:
            self.status_tekst_field = status_tekst_field
        if status_dato_field is not None:
            self.status_dato_field = status_dato_field
        if navn_field is not None:
            self.navn_field = navn_field
        if selsk_form_field is not None:
            self.selsk_form_field = selsk_form_field
        if rolle_field is not None:
            self.rolle_field = rolle_field
        if eierandel_field is not None:
            self.eierandel_field = eierandel_field
        if verv_kode_field is not None:
            self.verv_kode_field = verv_kode_field
        if verv_tekst_field is not None:
            self.verv_tekst_field = verv_tekst_field

    @property
    def orgnr_field(self):
        """Gets the orgnr_field of this PersonNaringsInteresser.  


        :return: The orgnr_field of this PersonNaringsInteresser.  
        :rtype: int
        """
        return self._orgnr_field

    @orgnr_field.setter
    def orgnr_field(self, orgnr_field):
        """Sets the orgnr_field of this PersonNaringsInteresser.


        :param orgnr_field: The orgnr_field of this PersonNaringsInteresser.  
        :type: int
        """

        self._orgnr_field = orgnr_field

    @property
    def status_kode_field(self):
        """Gets the status_kode_field of this PersonNaringsInteresser.  


        :return: The status_kode_field of this PersonNaringsInteresser.  
        :rtype: str
        """
        return self._status_kode_field

    @status_kode_field.setter
    def status_kode_field(self, status_kode_field):
        """Sets the status_kode_field of this PersonNaringsInteresser.


        :param status_kode_field: The status_kode_field of this PersonNaringsInteresser.  
        :type: str
        """

        self._status_kode_field = status_kode_field

    @property
    def status_tekst_field(self):
        """Gets the status_tekst_field of this PersonNaringsInteresser.  


        :return: The status_tekst_field of this PersonNaringsInteresser.  
        :rtype: str
        """
        return self._status_tekst_field

    @status_tekst_field.setter
    def status_tekst_field(self, status_tekst_field):
        """Sets the status_tekst_field of this PersonNaringsInteresser.


        :param status_tekst_field: The status_tekst_field of this PersonNaringsInteresser.  
        :type: str
        """

        self._status_tekst_field = status_tekst_field

    @property
    def status_dato_field(self):
        """Gets the status_dato_field of this PersonNaringsInteresser.  


        :return: The status_dato_field of this PersonNaringsInteresser.  
        :rtype: datetime
        """
        return self._status_dato_field

    @status_dato_field.setter
    def status_dato_field(self, status_dato_field):
        """Sets the status_dato_field of this PersonNaringsInteresser.


        :param status_dato_field: The status_dato_field of this PersonNaringsInteresser.  
        :type: datetime
        """

        self._status_dato_field = status_dato_field

    @property
    def navn_field(self):
        """Gets the navn_field of this PersonNaringsInteresser.  


        :return: The navn_field of this PersonNaringsInteresser.  
        :rtype: str
        """
        return self._navn_field

    @navn_field.setter
    def navn_field(self, navn_field):
        """Sets the navn_field of this PersonNaringsInteresser.


        :param navn_field: The navn_field of this PersonNaringsInteresser.  
        :type: str
        """

        self._navn_field = navn_field

    @property
    def selsk_form_field(self):
        """Gets the selsk_form_field of this PersonNaringsInteresser.  


        :return: The selsk_form_field of this PersonNaringsInteresser.  
        :rtype: str
        """
        return self._selsk_form_field

    @selsk_form_field.setter
    def selsk_form_field(self, selsk_form_field):
        """Sets the selsk_form_field of this PersonNaringsInteresser.


        :param selsk_form_field: The selsk_form_field of this PersonNaringsInteresser.  
        :type: str
        """

        self._selsk_form_field = selsk_form_field

    @property
    def rolle_field(self):
        """Gets the rolle_field of this PersonNaringsInteresser.  


        :return: The rolle_field of this PersonNaringsInteresser.  
        :rtype: str
        """
        return self._rolle_field

    @rolle_field.setter
    def rolle_field(self, rolle_field):
        """Sets the rolle_field of this PersonNaringsInteresser.


        :param rolle_field: The rolle_field of this PersonNaringsInteresser.  
        :type: str
        """

        self._rolle_field = rolle_field

    @property
    def eierandel_field(self):
        """Gets the eierandel_field of this PersonNaringsInteresser.  


        :return: The eierandel_field of this PersonNaringsInteresser.  
        :rtype: float
        """
        return self._eierandel_field

    @eierandel_field.setter
    def eierandel_field(self, eierandel_field):
        """Sets the eierandel_field of this PersonNaringsInteresser.


        :param eierandel_field: The eierandel_field of this PersonNaringsInteresser.  
        :type: float
        """

        self._eierandel_field = eierandel_field

    @property
    def verv_kode_field(self):
        """Gets the verv_kode_field of this PersonNaringsInteresser.  


        :return: The verv_kode_field of this PersonNaringsInteresser.  
        :rtype: str
        """
        return self._verv_kode_field

    @verv_kode_field.setter
    def verv_kode_field(self, verv_kode_field):
        """Sets the verv_kode_field of this PersonNaringsInteresser.


        :param verv_kode_field: The verv_kode_field of this PersonNaringsInteresser.  
        :type: str
        """

        self._verv_kode_field = verv_kode_field

    @property
    def verv_tekst_field(self):
        """Gets the verv_tekst_field of this PersonNaringsInteresser.  


        :return: The verv_tekst_field of this PersonNaringsInteresser.  
        :rtype: str
        """
        return self._verv_tekst_field

    @verv_tekst_field.setter
    def verv_tekst_field(self, verv_tekst_field):
        """Sets the verv_tekst_field of this PersonNaringsInteresser.


        :param verv_tekst_field: The verv_tekst_field of this PersonNaringsInteresser.  
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
        if not isinstance(other, PersonNaringsInteresser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
