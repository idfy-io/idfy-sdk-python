# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Rettighetshavere(object):

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
        'andel_field': 'float',
        'indirekte_eier_field': 'bool'
    }

    attribute_map = {
        'internreferanse_field': 'internreferanseField',
        'fodt_dato_field': 'fodtDatoField',
        'fodt_dato_field_specified': 'fodtDatoFieldSpecified',
        'navn_field': 'navnField',
        'adresse_field': 'adresseField',
        'postnr_field': 'postnrField',
        'poststed_field': 'poststedField',
        'andel_field': 'andelField',
        'indirekte_eier_field': 'indirekteEierField'
    }

    def __init__(self, internreferanse_field=None, fodt_dato_field=None, fodt_dato_field_specified=None, navn_field=None, adresse_field=None, postnr_field=None, poststed_field=None, andel_field=None, indirekte_eier_field=None):  
        """Rettighetshavere"""  

        self._internreferanse_field = None
        self._fodt_dato_field = None
        self._fodt_dato_field_specified = None
        self._navn_field = None
        self._adresse_field = None
        self._postnr_field = None
        self._poststed_field = None
        self._andel_field = None
        self._indirekte_eier_field = None
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
        if andel_field is not None:
            self.andel_field = andel_field
        if indirekte_eier_field is not None:
            self.indirekte_eier_field = indirekte_eier_field

    @property
    def internreferanse_field(self):
        """Gets the internreferanse_field of this Rettighetshavere.  


        :return: The internreferanse_field of this Rettighetshavere.  
        :rtype: int
        """
        return self._internreferanse_field

    @internreferanse_field.setter
    def internreferanse_field(self, internreferanse_field):
        """Sets the internreferanse_field of this Rettighetshavere.


        :param internreferanse_field: The internreferanse_field of this Rettighetshavere.  
        :type: int
        """

        self._internreferanse_field = internreferanse_field

    @property
    def fodt_dato_field(self):
        """Gets the fodt_dato_field of this Rettighetshavere.  


        :return: The fodt_dato_field of this Rettighetshavere.  
        :rtype: datetime
        """
        return self._fodt_dato_field

    @fodt_dato_field.setter
    def fodt_dato_field(self, fodt_dato_field):
        """Sets the fodt_dato_field of this Rettighetshavere.


        :param fodt_dato_field: The fodt_dato_field of this Rettighetshavere.  
        :type: datetime
        """

        self._fodt_dato_field = fodt_dato_field

    @property
    def fodt_dato_field_specified(self):
        """Gets the fodt_dato_field_specified of this Rettighetshavere.  


        :return: The fodt_dato_field_specified of this Rettighetshavere.  
        :rtype: bool
        """
        return self._fodt_dato_field_specified

    @fodt_dato_field_specified.setter
    def fodt_dato_field_specified(self, fodt_dato_field_specified):
        """Sets the fodt_dato_field_specified of this Rettighetshavere.


        :param fodt_dato_field_specified: The fodt_dato_field_specified of this Rettighetshavere.  
        :type: bool
        """

        self._fodt_dato_field_specified = fodt_dato_field_specified

    @property
    def navn_field(self):
        """Gets the navn_field of this Rettighetshavere.  


        :return: The navn_field of this Rettighetshavere.  
        :rtype: str
        """
        return self._navn_field

    @navn_field.setter
    def navn_field(self, navn_field):
        """Sets the navn_field of this Rettighetshavere.


        :param navn_field: The navn_field of this Rettighetshavere.  
        :type: str
        """

        self._navn_field = navn_field

    @property
    def adresse_field(self):
        """Gets the adresse_field of this Rettighetshavere.  


        :return: The adresse_field of this Rettighetshavere.  
        :rtype: str
        """
        return self._adresse_field

    @adresse_field.setter
    def adresse_field(self, adresse_field):
        """Sets the adresse_field of this Rettighetshavere.


        :param adresse_field: The adresse_field of this Rettighetshavere.  
        :type: str
        """

        self._adresse_field = adresse_field

    @property
    def postnr_field(self):
        """Gets the postnr_field of this Rettighetshavere.  


        :return: The postnr_field of this Rettighetshavere.  
        :rtype: int
        """
        return self._postnr_field

    @postnr_field.setter
    def postnr_field(self, postnr_field):
        """Sets the postnr_field of this Rettighetshavere.


        :param postnr_field: The postnr_field of this Rettighetshavere.  
        :type: int
        """

        self._postnr_field = postnr_field

    @property
    def poststed_field(self):
        """Gets the poststed_field of this Rettighetshavere.  


        :return: The poststed_field of this Rettighetshavere.  
        :rtype: str
        """
        return self._poststed_field

    @poststed_field.setter
    def poststed_field(self, poststed_field):
        """Sets the poststed_field of this Rettighetshavere.


        :param poststed_field: The poststed_field of this Rettighetshavere.  
        :type: str
        """

        self._poststed_field = poststed_field

    @property
    def andel_field(self):
        """Gets the andel_field of this Rettighetshavere.  


        :return: The andel_field of this Rettighetshavere.  
        :rtype: float
        """
        return self._andel_field

    @andel_field.setter
    def andel_field(self, andel_field):
        """Sets the andel_field of this Rettighetshavere.


        :param andel_field: The andel_field of this Rettighetshavere.  
        :type: float
        """

        self._andel_field = andel_field

    @property
    def indirekte_eier_field(self):
        """Gets the indirekte_eier_field of this Rettighetshavere.  


        :return: The indirekte_eier_field of this Rettighetshavere.  
        :rtype: bool
        """
        return self._indirekte_eier_field

    @indirekte_eier_field.setter
    def indirekte_eier_field(self, indirekte_eier_field):
        """Sets the indirekte_eier_field of this Rettighetshavere.


        :param indirekte_eier_field: The indirekte_eier_field of this Rettighetshavere.  
        :type: bool
        """

        self._indirekte_eier_field = indirekte_eier_field

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
        if not isinstance(other, Rettighetshavere):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
