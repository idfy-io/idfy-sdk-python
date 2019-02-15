# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class OkonomiEnk(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fodselsdato_eier_field': 'datetime',
        'skatte_ar_field': 'int',
        'formue_field': 'int',
        'endring_formue_field': 'float',
        'inntekt_field': 'int',
        'endring_inntekt_field': 'float',
        'skatt_field': 'int',
        'skatte_klasse_field': 'str',
        'skatte_klasse_utl_field': 'str',
        'kommunenr_field': 'int',
        'kommune_navn_field': 'str'
    }

    attribute_map = {
        'fodselsdato_eier_field': 'fodselsdatoEierField',
        'skatte_ar_field': 'skatteArField',
        'formue_field': 'formueField',
        'endring_formue_field': 'endringFormueField',
        'inntekt_field': 'inntektField',
        'endring_inntekt_field': 'endringInntektField',
        'skatt_field': 'skattField',
        'skatte_klasse_field': 'skatteKlasseField',
        'skatte_klasse_utl_field': 'skatteKlasseUtlField',
        'kommunenr_field': 'kommunenrField',
        'kommune_navn_field': 'kommuneNavnField'
    }

    def __init__(self, fodselsdato_eier_field=None, skatte_ar_field=None, formue_field=None, endring_formue_field=None, inntekt_field=None, endring_inntekt_field=None, skatt_field=None, skatte_klasse_field=None, skatte_klasse_utl_field=None, kommunenr_field=None, kommune_navn_field=None):  
        """OkonomiEnk"""  

        self._fodselsdato_eier_field = None
        self._skatte_ar_field = None
        self._formue_field = None
        self._endring_formue_field = None
        self._inntekt_field = None
        self._endring_inntekt_field = None
        self._skatt_field = None
        self._skatte_klasse_field = None
        self._skatte_klasse_utl_field = None
        self._kommunenr_field = None
        self._kommune_navn_field = None
        self.discriminator = None

        if fodselsdato_eier_field is not None:
            self.fodselsdato_eier_field = fodselsdato_eier_field
        if skatte_ar_field is not None:
            self.skatte_ar_field = skatte_ar_field
        if formue_field is not None:
            self.formue_field = formue_field
        if endring_formue_field is not None:
            self.endring_formue_field = endring_formue_field
        if inntekt_field is not None:
            self.inntekt_field = inntekt_field
        if endring_inntekt_field is not None:
            self.endring_inntekt_field = endring_inntekt_field
        if skatt_field is not None:
            self.skatt_field = skatt_field
        if skatte_klasse_field is not None:
            self.skatte_klasse_field = skatte_klasse_field
        if skatte_klasse_utl_field is not None:
            self.skatte_klasse_utl_field = skatte_klasse_utl_field
        if kommunenr_field is not None:
            self.kommunenr_field = kommunenr_field
        if kommune_navn_field is not None:
            self.kommune_navn_field = kommune_navn_field

    @property
    def fodselsdato_eier_field(self):
        """Gets the fodselsdato_eier_field of this OkonomiEnk.  


        :return: The fodselsdato_eier_field of this OkonomiEnk.  
        :rtype: datetime
        """
        return self._fodselsdato_eier_field

    @fodselsdato_eier_field.setter
    def fodselsdato_eier_field(self, fodselsdato_eier_field):
        """Sets the fodselsdato_eier_field of this OkonomiEnk.


        :param fodselsdato_eier_field: The fodselsdato_eier_field of this OkonomiEnk.  
        :type: datetime
        """

        self._fodselsdato_eier_field = fodselsdato_eier_field

    @property
    def skatte_ar_field(self):
        """Gets the skatte_ar_field of this OkonomiEnk.  


        :return: The skatte_ar_field of this OkonomiEnk.  
        :rtype: int
        """
        return self._skatte_ar_field

    @skatte_ar_field.setter
    def skatte_ar_field(self, skatte_ar_field):
        """Sets the skatte_ar_field of this OkonomiEnk.


        :param skatte_ar_field: The skatte_ar_field of this OkonomiEnk.  
        :type: int
        """

        self._skatte_ar_field = skatte_ar_field

    @property
    def formue_field(self):
        """Gets the formue_field of this OkonomiEnk.  


        :return: The formue_field of this OkonomiEnk.  
        :rtype: int
        """
        return self._formue_field

    @formue_field.setter
    def formue_field(self, formue_field):
        """Sets the formue_field of this OkonomiEnk.


        :param formue_field: The formue_field of this OkonomiEnk.  
        :type: int
        """

        self._formue_field = formue_field

    @property
    def endring_formue_field(self):
        """Gets the endring_formue_field of this OkonomiEnk.  


        :return: The endring_formue_field of this OkonomiEnk.  
        :rtype: float
        """
        return self._endring_formue_field

    @endring_formue_field.setter
    def endring_formue_field(self, endring_formue_field):
        """Sets the endring_formue_field of this OkonomiEnk.


        :param endring_formue_field: The endring_formue_field of this OkonomiEnk.  
        :type: float
        """

        self._endring_formue_field = endring_formue_field

    @property
    def inntekt_field(self):
        """Gets the inntekt_field of this OkonomiEnk.  


        :return: The inntekt_field of this OkonomiEnk.  
        :rtype: int
        """
        return self._inntekt_field

    @inntekt_field.setter
    def inntekt_field(self, inntekt_field):
        """Sets the inntekt_field of this OkonomiEnk.


        :param inntekt_field: The inntekt_field of this OkonomiEnk.  
        :type: int
        """

        self._inntekt_field = inntekt_field

    @property
    def endring_inntekt_field(self):
        """Gets the endring_inntekt_field of this OkonomiEnk.  


        :return: The endring_inntekt_field of this OkonomiEnk.  
        :rtype: float
        """
        return self._endring_inntekt_field

    @endring_inntekt_field.setter
    def endring_inntekt_field(self, endring_inntekt_field):
        """Sets the endring_inntekt_field of this OkonomiEnk.


        :param endring_inntekt_field: The endring_inntekt_field of this OkonomiEnk.  
        :type: float
        """

        self._endring_inntekt_field = endring_inntekt_field

    @property
    def skatt_field(self):
        """Gets the skatt_field of this OkonomiEnk.  


        :return: The skatt_field of this OkonomiEnk.  
        :rtype: int
        """
        return self._skatt_field

    @skatt_field.setter
    def skatt_field(self, skatt_field):
        """Sets the skatt_field of this OkonomiEnk.


        :param skatt_field: The skatt_field of this OkonomiEnk.  
        :type: int
        """

        self._skatt_field = skatt_field

    @property
    def skatte_klasse_field(self):
        """Gets the skatte_klasse_field of this OkonomiEnk.  


        :return: The skatte_klasse_field of this OkonomiEnk.  
        :rtype: str
        """
        return self._skatte_klasse_field

    @skatte_klasse_field.setter
    def skatte_klasse_field(self, skatte_klasse_field):
        """Sets the skatte_klasse_field of this OkonomiEnk.


        :param skatte_klasse_field: The skatte_klasse_field of this OkonomiEnk.  
        :type: str
        """

        self._skatte_klasse_field = skatte_klasse_field

    @property
    def skatte_klasse_utl_field(self):
        """Gets the skatte_klasse_utl_field of this OkonomiEnk.  


        :return: The skatte_klasse_utl_field of this OkonomiEnk.  
        :rtype: str
        """
        return self._skatte_klasse_utl_field

    @skatte_klasse_utl_field.setter
    def skatte_klasse_utl_field(self, skatte_klasse_utl_field):
        """Sets the skatte_klasse_utl_field of this OkonomiEnk.


        :param skatte_klasse_utl_field: The skatte_klasse_utl_field of this OkonomiEnk.  
        :type: str
        """

        self._skatte_klasse_utl_field = skatte_klasse_utl_field

    @property
    def kommunenr_field(self):
        """Gets the kommunenr_field of this OkonomiEnk.  


        :return: The kommunenr_field of this OkonomiEnk.  
        :rtype: int
        """
        return self._kommunenr_field

    @kommunenr_field.setter
    def kommunenr_field(self, kommunenr_field):
        """Sets the kommunenr_field of this OkonomiEnk.


        :param kommunenr_field: The kommunenr_field of this OkonomiEnk.  
        :type: int
        """

        self._kommunenr_field = kommunenr_field

    @property
    def kommune_navn_field(self):
        """Gets the kommune_navn_field of this OkonomiEnk.  


        :return: The kommune_navn_field of this OkonomiEnk.  
        :rtype: str
        """
        return self._kommune_navn_field

    @kommune_navn_field.setter
    def kommune_navn_field(self, kommune_navn_field):
        """Sets the kommune_navn_field of this OkonomiEnk.


        :param kommune_navn_field: The kommune_navn_field of this OkonomiEnk.  
        :type: str
        """

        self._kommune_navn_field = kommune_navn_field

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
        if not isinstance(other, OkonomiEnk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
