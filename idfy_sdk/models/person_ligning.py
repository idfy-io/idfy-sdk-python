# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonLigning(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'skatte_ar_field': 'int',
        'formue_field': 'int',
        'endring_formue_field': 'float',
        'inntekt_field': 'int',
        'endring_inntekt_field': 'float',
        'skatt_field': 'int',
        'skatte_klasse_field': 'str',
        'skatte_klasse_utl_field': 'str',
        'kommunenr_field': 'str',
        'kommune_navn_field': 'str',
        'brutto_inntekt_field': 'int',
        'gjeldsgrad1_field': 'float',
        'gjeldsgrad2_field': 'float'
    }

    attribute_map = {
        'skatte_ar_field': 'skatteArField',
        'formue_field': 'formueField',
        'endring_formue_field': 'endringFormueField',
        'inntekt_field': 'inntektField',
        'endring_inntekt_field': 'endringInntektField',
        'skatt_field': 'skattField',
        'skatte_klasse_field': 'skatteKlasseField',
        'skatte_klasse_utl_field': 'skatteKlasseUtlField',
        'kommunenr_field': 'kommunenrField',
        'kommune_navn_field': 'kommuneNavnField',
        'brutto_inntekt_field': 'bruttoInntektField',
        'gjeldsgrad1_field': 'gjeldsgrad1Field',
        'gjeldsgrad2_field': 'gjeldsgrad2Field'
    }

    def __init__(self, skatte_ar_field=None, formue_field=None, endring_formue_field=None, inntekt_field=None, endring_inntekt_field=None, skatt_field=None, skatte_klasse_field=None, skatte_klasse_utl_field=None, kommunenr_field=None, kommune_navn_field=None, brutto_inntekt_field=None, gjeldsgrad1_field=None, gjeldsgrad2_field=None):  
        """PersonLigning"""  

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
        self._brutto_inntekt_field = None
        self._gjeldsgrad1_field = None
        self._gjeldsgrad2_field = None
        self.discriminator = None

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
        if brutto_inntekt_field is not None:
            self.brutto_inntekt_field = brutto_inntekt_field
        if gjeldsgrad1_field is not None:
            self.gjeldsgrad1_field = gjeldsgrad1_field
        if gjeldsgrad2_field is not None:
            self.gjeldsgrad2_field = gjeldsgrad2_field

    @property
    def skatte_ar_field(self):
        """Gets the skatte_ar_field of this PersonLigning.  


        :return: The skatte_ar_field of this PersonLigning.  
        :rtype: int
        """
        return self._skatte_ar_field

    @skatte_ar_field.setter
    def skatte_ar_field(self, skatte_ar_field):
        """Sets the skatte_ar_field of this PersonLigning.


        :param skatte_ar_field: The skatte_ar_field of this PersonLigning.  
        :type: int
        """

        self._skatte_ar_field = skatte_ar_field

    @property
    def formue_field(self):
        """Gets the formue_field of this PersonLigning.  


        :return: The formue_field of this PersonLigning.  
        :rtype: int
        """
        return self._formue_field

    @formue_field.setter
    def formue_field(self, formue_field):
        """Sets the formue_field of this PersonLigning.


        :param formue_field: The formue_field of this PersonLigning.  
        :type: int
        """

        self._formue_field = formue_field

    @property
    def endring_formue_field(self):
        """Gets the endring_formue_field of this PersonLigning.  


        :return: The endring_formue_field of this PersonLigning.  
        :rtype: float
        """
        return self._endring_formue_field

    @endring_formue_field.setter
    def endring_formue_field(self, endring_formue_field):
        """Sets the endring_formue_field of this PersonLigning.


        :param endring_formue_field: The endring_formue_field of this PersonLigning.  
        :type: float
        """

        self._endring_formue_field = endring_formue_field

    @property
    def inntekt_field(self):
        """Gets the inntekt_field of this PersonLigning.  


        :return: The inntekt_field of this PersonLigning.  
        :rtype: int
        """
        return self._inntekt_field

    @inntekt_field.setter
    def inntekt_field(self, inntekt_field):
        """Sets the inntekt_field of this PersonLigning.


        :param inntekt_field: The inntekt_field of this PersonLigning.  
        :type: int
        """

        self._inntekt_field = inntekt_field

    @property
    def endring_inntekt_field(self):
        """Gets the endring_inntekt_field of this PersonLigning.  


        :return: The endring_inntekt_field of this PersonLigning.  
        :rtype: float
        """
        return self._endring_inntekt_field

    @endring_inntekt_field.setter
    def endring_inntekt_field(self, endring_inntekt_field):
        """Sets the endring_inntekt_field of this PersonLigning.


        :param endring_inntekt_field: The endring_inntekt_field of this PersonLigning.  
        :type: float
        """

        self._endring_inntekt_field = endring_inntekt_field

    @property
    def skatt_field(self):
        """Gets the skatt_field of this PersonLigning.  


        :return: The skatt_field of this PersonLigning.  
        :rtype: int
        """
        return self._skatt_field

    @skatt_field.setter
    def skatt_field(self, skatt_field):
        """Sets the skatt_field of this PersonLigning.


        :param skatt_field: The skatt_field of this PersonLigning.  
        :type: int
        """

        self._skatt_field = skatt_field

    @property
    def skatte_klasse_field(self):
        """Gets the skatte_klasse_field of this PersonLigning.  


        :return: The skatte_klasse_field of this PersonLigning.  
        :rtype: str
        """
        return self._skatte_klasse_field

    @skatte_klasse_field.setter
    def skatte_klasse_field(self, skatte_klasse_field):
        """Sets the skatte_klasse_field of this PersonLigning.


        :param skatte_klasse_field: The skatte_klasse_field of this PersonLigning.  
        :type: str
        """

        self._skatte_klasse_field = skatte_klasse_field

    @property
    def skatte_klasse_utl_field(self):
        """Gets the skatte_klasse_utl_field of this PersonLigning.  


        :return: The skatte_klasse_utl_field of this PersonLigning.  
        :rtype: str
        """
        return self._skatte_klasse_utl_field

    @skatte_klasse_utl_field.setter
    def skatte_klasse_utl_field(self, skatte_klasse_utl_field):
        """Sets the skatte_klasse_utl_field of this PersonLigning.


        :param skatte_klasse_utl_field: The skatte_klasse_utl_field of this PersonLigning.  
        :type: str
        """

        self._skatte_klasse_utl_field = skatte_klasse_utl_field

    @property
    def kommunenr_field(self):
        """Gets the kommunenr_field of this PersonLigning.  


        :return: The kommunenr_field of this PersonLigning.  
        :rtype: str
        """
        return self._kommunenr_field

    @kommunenr_field.setter
    def kommunenr_field(self, kommunenr_field):
        """Sets the kommunenr_field of this PersonLigning.


        :param kommunenr_field: The kommunenr_field of this PersonLigning.  
        :type: str
        """

        self._kommunenr_field = kommunenr_field

    @property
    def kommune_navn_field(self):
        """Gets the kommune_navn_field of this PersonLigning.  


        :return: The kommune_navn_field of this PersonLigning.  
        :rtype: str
        """
        return self._kommune_navn_field

    @kommune_navn_field.setter
    def kommune_navn_field(self, kommune_navn_field):
        """Sets the kommune_navn_field of this PersonLigning.


        :param kommune_navn_field: The kommune_navn_field of this PersonLigning.  
        :type: str
        """

        self._kommune_navn_field = kommune_navn_field

    @property
    def brutto_inntekt_field(self):
        """Gets the brutto_inntekt_field of this PersonLigning.  


        :return: The brutto_inntekt_field of this PersonLigning.  
        :rtype: int
        """
        return self._brutto_inntekt_field

    @brutto_inntekt_field.setter
    def brutto_inntekt_field(self, brutto_inntekt_field):
        """Sets the brutto_inntekt_field of this PersonLigning.


        :param brutto_inntekt_field: The brutto_inntekt_field of this PersonLigning.  
        :type: int
        """

        self._brutto_inntekt_field = brutto_inntekt_field

    @property
    def gjeldsgrad1_field(self):
        """Gets the gjeldsgrad1_field of this PersonLigning.  


        :return: The gjeldsgrad1_field of this PersonLigning.  
        :rtype: float
        """
        return self._gjeldsgrad1_field

    @gjeldsgrad1_field.setter
    def gjeldsgrad1_field(self, gjeldsgrad1_field):
        """Sets the gjeldsgrad1_field of this PersonLigning.


        :param gjeldsgrad1_field: The gjeldsgrad1_field of this PersonLigning.  
        :type: float
        """

        self._gjeldsgrad1_field = gjeldsgrad1_field

    @property
    def gjeldsgrad2_field(self):
        """Gets the gjeldsgrad2_field of this PersonLigning.  


        :return: The gjeldsgrad2_field of this PersonLigning.  
        :rtype: float
        """
        return self._gjeldsgrad2_field

    @gjeldsgrad2_field.setter
    def gjeldsgrad2_field(self, gjeldsgrad2_field):
        """Sets the gjeldsgrad2_field of this PersonLigning.


        :param gjeldsgrad2_field: The gjeldsgrad2_field of this PersonLigning.  
        :type: float
        """

        self._gjeldsgrad2_field = gjeldsgrad2_field

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
        if not isinstance(other, PersonLigning):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
