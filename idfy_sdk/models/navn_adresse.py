# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class NavnAdresse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'kode_type_field': 'str',
        'kode_tekst_field': 'str',
        'navn_field': 'str',
        'gate_adresse_field': 'str',
        'gate_postboks_field': 'int',
        'gate_postnr_field': 'int',
        'gate_poststed_field': 'str',
        'post_adresse_field': 'str',
        'post_postboks_field': 'int',
        'post_postnr_field': 'int',
        'post_poststed_field': 'str'
    }

    attribute_map = {
        'kode_type_field': 'kodeTypeField',
        'kode_tekst_field': 'kodeTekstField',
        'navn_field': 'navnField',
        'gate_adresse_field': 'gateAdresseField',
        'gate_postboks_field': 'gatePostboksField',
        'gate_postnr_field': 'gatePostnrField',
        'gate_poststed_field': 'gatePoststedField',
        'post_adresse_field': 'postAdresseField',
        'post_postboks_field': 'postPostboksField',
        'post_postnr_field': 'postPostnrField',
        'post_poststed_field': 'postPoststedField'
    }

    def __init__(self, kode_type_field=None, kode_tekst_field=None, navn_field=None, gate_adresse_field=None, gate_postboks_field=None, gate_postnr_field=None, gate_poststed_field=None, post_adresse_field=None, post_postboks_field=None, post_postnr_field=None, post_poststed_field=None):  
        """NavnAdresse"""  

        self._kode_type_field = None
        self._kode_tekst_field = None
        self._navn_field = None
        self._gate_adresse_field = None
        self._gate_postboks_field = None
        self._gate_postnr_field = None
        self._gate_poststed_field = None
        self._post_adresse_field = None
        self._post_postboks_field = None
        self._post_postnr_field = None
        self._post_poststed_field = None
        self.discriminator = None

        if kode_type_field is not None:
            self.kode_type_field = kode_type_field
        if kode_tekst_field is not None:
            self.kode_tekst_field = kode_tekst_field
        if navn_field is not None:
            self.navn_field = navn_field
        if gate_adresse_field is not None:
            self.gate_adresse_field = gate_adresse_field
        if gate_postboks_field is not None:
            self.gate_postboks_field = gate_postboks_field
        if gate_postnr_field is not None:
            self.gate_postnr_field = gate_postnr_field
        if gate_poststed_field is not None:
            self.gate_poststed_field = gate_poststed_field
        if post_adresse_field is not None:
            self.post_adresse_field = post_adresse_field
        if post_postboks_field is not None:
            self.post_postboks_field = post_postboks_field
        if post_postnr_field is not None:
            self.post_postnr_field = post_postnr_field
        if post_poststed_field is not None:
            self.post_poststed_field = post_poststed_field

    @property
    def kode_type_field(self):
        """Gets the kode_type_field of this NavnAdresse.  


        :return: The kode_type_field of this NavnAdresse.  
        :rtype: str
        """
        return self._kode_type_field

    @kode_type_field.setter
    def kode_type_field(self, kode_type_field):
        """Sets the kode_type_field of this NavnAdresse.


        :param kode_type_field: The kode_type_field of this NavnAdresse.  
        :type: str
        """

        self._kode_type_field = kode_type_field

    @property
    def kode_tekst_field(self):
        """Gets the kode_tekst_field of this NavnAdresse.  


        :return: The kode_tekst_field of this NavnAdresse.  
        :rtype: str
        """
        return self._kode_tekst_field

    @kode_tekst_field.setter
    def kode_tekst_field(self, kode_tekst_field):
        """Sets the kode_tekst_field of this NavnAdresse.


        :param kode_tekst_field: The kode_tekst_field of this NavnAdresse.  
        :type: str
        """

        self._kode_tekst_field = kode_tekst_field

    @property
    def navn_field(self):
        """Gets the navn_field of this NavnAdresse.  


        :return: The navn_field of this NavnAdresse.  
        :rtype: str
        """
        return self._navn_field

    @navn_field.setter
    def navn_field(self, navn_field):
        """Sets the navn_field of this NavnAdresse.


        :param navn_field: The navn_field of this NavnAdresse.  
        :type: str
        """

        self._navn_field = navn_field

    @property
    def gate_adresse_field(self):
        """Gets the gate_adresse_field of this NavnAdresse.  


        :return: The gate_adresse_field of this NavnAdresse.  
        :rtype: str
        """
        return self._gate_adresse_field

    @gate_adresse_field.setter
    def gate_adresse_field(self, gate_adresse_field):
        """Sets the gate_adresse_field of this NavnAdresse.


        :param gate_adresse_field: The gate_adresse_field of this NavnAdresse.  
        :type: str
        """

        self._gate_adresse_field = gate_adresse_field

    @property
    def gate_postboks_field(self):
        """Gets the gate_postboks_field of this NavnAdresse.  


        :return: The gate_postboks_field of this NavnAdresse.  
        :rtype: int
        """
        return self._gate_postboks_field

    @gate_postboks_field.setter
    def gate_postboks_field(self, gate_postboks_field):
        """Sets the gate_postboks_field of this NavnAdresse.


        :param gate_postboks_field: The gate_postboks_field of this NavnAdresse.  
        :type: int
        """

        self._gate_postboks_field = gate_postboks_field

    @property
    def gate_postnr_field(self):
        """Gets the gate_postnr_field of this NavnAdresse.  


        :return: The gate_postnr_field of this NavnAdresse.  
        :rtype: int
        """
        return self._gate_postnr_field

    @gate_postnr_field.setter
    def gate_postnr_field(self, gate_postnr_field):
        """Sets the gate_postnr_field of this NavnAdresse.


        :param gate_postnr_field: The gate_postnr_field of this NavnAdresse.  
        :type: int
        """

        self._gate_postnr_field = gate_postnr_field

    @property
    def gate_poststed_field(self):
        """Gets the gate_poststed_field of this NavnAdresse.  


        :return: The gate_poststed_field of this NavnAdresse.  
        :rtype: str
        """
        return self._gate_poststed_field

    @gate_poststed_field.setter
    def gate_poststed_field(self, gate_poststed_field):
        """Sets the gate_poststed_field of this NavnAdresse.


        :param gate_poststed_field: The gate_poststed_field of this NavnAdresse.  
        :type: str
        """

        self._gate_poststed_field = gate_poststed_field

    @property
    def post_adresse_field(self):
        """Gets the post_adresse_field of this NavnAdresse.  


        :return: The post_adresse_field of this NavnAdresse.  
        :rtype: str
        """
        return self._post_adresse_field

    @post_adresse_field.setter
    def post_adresse_field(self, post_adresse_field):
        """Sets the post_adresse_field of this NavnAdresse.


        :param post_adresse_field: The post_adresse_field of this NavnAdresse.  
        :type: str
        """

        self._post_adresse_field = post_adresse_field

    @property
    def post_postboks_field(self):
        """Gets the post_postboks_field of this NavnAdresse.  


        :return: The post_postboks_field of this NavnAdresse.  
        :rtype: int
        """
        return self._post_postboks_field

    @post_postboks_field.setter
    def post_postboks_field(self, post_postboks_field):
        """Sets the post_postboks_field of this NavnAdresse.


        :param post_postboks_field: The post_postboks_field of this NavnAdresse.  
        :type: int
        """

        self._post_postboks_field = post_postboks_field

    @property
    def post_postnr_field(self):
        """Gets the post_postnr_field of this NavnAdresse.  


        :return: The post_postnr_field of this NavnAdresse.  
        :rtype: int
        """
        return self._post_postnr_field

    @post_postnr_field.setter
    def post_postnr_field(self, post_postnr_field):
        """Sets the post_postnr_field of this NavnAdresse.


        :param post_postnr_field: The post_postnr_field of this NavnAdresse.  
        :type: int
        """

        self._post_postnr_field = post_postnr_field

    @property
    def post_poststed_field(self):
        """Gets the post_poststed_field of this NavnAdresse.  


        :return: The post_poststed_field of this NavnAdresse.  
        :rtype: str
        """
        return self._post_poststed_field

    @post_poststed_field.setter
    def post_poststed_field(self, post_poststed_field):
        """Sets the post_poststed_field of this NavnAdresse.


        :param post_poststed_field: The post_poststed_field of this NavnAdresse.  
        :type: str
        """

        self._post_poststed_field = post_poststed_field

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
        if not isinstance(other, NavnAdresse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
