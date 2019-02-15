# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class NokkeltallForetak(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'regnskaps_av_ar_field': 'int',
        'regnskaps_av_mnd_field': 'int',
        'overskuddsprosent_field': 'float',
        'rentedekningsgrad_field': 'float',
        'totalrentabilitet_field': 'float',
        'e_k_rentabilitet_field': 'float',
        'lang_lagerfinans_field': 'float',
        'gjennomsnitt_lager_field': 'float',
        'egenkapital_andel_field': 'float',
        'tapsbuffer_field': 'float',
        'fremmedkapital_kostnad_field': 'float',
        'likviditetsgrad1_field': 'float',
        'likviditetsgrad2_field': 'float',
        'likvider_prosent_salg_field': 'float'
    }

    attribute_map = {
        'regnskaps_av_ar_field': 'regnskapsAvArField',
        'regnskaps_av_mnd_field': 'regnskapsAvMndField',
        'overskuddsprosent_field': 'overskuddsprosentField',
        'rentedekningsgrad_field': 'rentedekningsgradField',
        'totalrentabilitet_field': 'totalrentabilitetField',
        'e_k_rentabilitet_field': 'eKRentabilitetField',
        'lang_lagerfinans_field': 'langLagerfinansField',
        'gjennomsnitt_lager_field': 'gjennomsnittLagerField',
        'egenkapital_andel_field': 'egenkapitalAndelField',
        'tapsbuffer_field': 'tapsbufferField',
        'fremmedkapital_kostnad_field': 'fremmedkapitalKostnadField',
        'likviditetsgrad1_field': 'likviditetsgrad1Field',
        'likviditetsgrad2_field': 'likviditetsgrad2Field',
        'likvider_prosent_salg_field': 'likviderProsentSalgField'
    }

    def __init__(self, regnskaps_av_ar_field=None, regnskaps_av_mnd_field=None, overskuddsprosent_field=None, rentedekningsgrad_field=None, totalrentabilitet_field=None, e_k_rentabilitet_field=None, lang_lagerfinans_field=None, gjennomsnitt_lager_field=None, egenkapital_andel_field=None, tapsbuffer_field=None, fremmedkapital_kostnad_field=None, likviditetsgrad1_field=None, likviditetsgrad2_field=None, likvider_prosent_salg_field=None):  
        """NokkeltallForetak"""  

        self._regnskaps_av_ar_field = None
        self._regnskaps_av_mnd_field = None
        self._overskuddsprosent_field = None
        self._rentedekningsgrad_field = None
        self._totalrentabilitet_field = None
        self._e_k_rentabilitet_field = None
        self._lang_lagerfinans_field = None
        self._gjennomsnitt_lager_field = None
        self._egenkapital_andel_field = None
        self._tapsbuffer_field = None
        self._fremmedkapital_kostnad_field = None
        self._likviditetsgrad1_field = None
        self._likviditetsgrad2_field = None
        self._likvider_prosent_salg_field = None
        self.discriminator = None

        if regnskaps_av_ar_field is not None:
            self.regnskaps_av_ar_field = regnskaps_av_ar_field
        if regnskaps_av_mnd_field is not None:
            self.regnskaps_av_mnd_field = regnskaps_av_mnd_field
        if overskuddsprosent_field is not None:
            self.overskuddsprosent_field = overskuddsprosent_field
        if rentedekningsgrad_field is not None:
            self.rentedekningsgrad_field = rentedekningsgrad_field
        if totalrentabilitet_field is not None:
            self.totalrentabilitet_field = totalrentabilitet_field
        if e_k_rentabilitet_field is not None:
            self.e_k_rentabilitet_field = e_k_rentabilitet_field
        if lang_lagerfinans_field is not None:
            self.lang_lagerfinans_field = lang_lagerfinans_field
        if gjennomsnitt_lager_field is not None:
            self.gjennomsnitt_lager_field = gjennomsnitt_lager_field
        if egenkapital_andel_field is not None:
            self.egenkapital_andel_field = egenkapital_andel_field
        if tapsbuffer_field is not None:
            self.tapsbuffer_field = tapsbuffer_field
        if fremmedkapital_kostnad_field is not None:
            self.fremmedkapital_kostnad_field = fremmedkapital_kostnad_field
        if likviditetsgrad1_field is not None:
            self.likviditetsgrad1_field = likviditetsgrad1_field
        if likviditetsgrad2_field is not None:
            self.likviditetsgrad2_field = likviditetsgrad2_field
        if likvider_prosent_salg_field is not None:
            self.likvider_prosent_salg_field = likvider_prosent_salg_field

    @property
    def regnskaps_av_ar_field(self):
        """Gets the regnskaps_av_ar_field of this NokkeltallForetak.  


        :return: The regnskaps_av_ar_field of this NokkeltallForetak.  
        :rtype: int
        """
        return self._regnskaps_av_ar_field

    @regnskaps_av_ar_field.setter
    def regnskaps_av_ar_field(self, regnskaps_av_ar_field):
        """Sets the regnskaps_av_ar_field of this NokkeltallForetak.


        :param regnskaps_av_ar_field: The regnskaps_av_ar_field of this NokkeltallForetak.  
        :type: int
        """

        self._regnskaps_av_ar_field = regnskaps_av_ar_field

    @property
    def regnskaps_av_mnd_field(self):
        """Gets the regnskaps_av_mnd_field of this NokkeltallForetak.  


        :return: The regnskaps_av_mnd_field of this NokkeltallForetak.  
        :rtype: int
        """
        return self._regnskaps_av_mnd_field

    @regnskaps_av_mnd_field.setter
    def regnskaps_av_mnd_field(self, regnskaps_av_mnd_field):
        """Sets the regnskaps_av_mnd_field of this NokkeltallForetak.


        :param regnskaps_av_mnd_field: The regnskaps_av_mnd_field of this NokkeltallForetak.  
        :type: int
        """

        self._regnskaps_av_mnd_field = regnskaps_av_mnd_field

    @property
    def overskuddsprosent_field(self):
        """Gets the overskuddsprosent_field of this NokkeltallForetak.  


        :return: The overskuddsprosent_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._overskuddsprosent_field

    @overskuddsprosent_field.setter
    def overskuddsprosent_field(self, overskuddsprosent_field):
        """Sets the overskuddsprosent_field of this NokkeltallForetak.


        :param overskuddsprosent_field: The overskuddsprosent_field of this NokkeltallForetak.  
        :type: float
        """

        self._overskuddsprosent_field = overskuddsprosent_field

    @property
    def rentedekningsgrad_field(self):
        """Gets the rentedekningsgrad_field of this NokkeltallForetak.  


        :return: The rentedekningsgrad_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._rentedekningsgrad_field

    @rentedekningsgrad_field.setter
    def rentedekningsgrad_field(self, rentedekningsgrad_field):
        """Sets the rentedekningsgrad_field of this NokkeltallForetak.


        :param rentedekningsgrad_field: The rentedekningsgrad_field of this NokkeltallForetak.  
        :type: float
        """

        self._rentedekningsgrad_field = rentedekningsgrad_field

    @property
    def totalrentabilitet_field(self):
        """Gets the totalrentabilitet_field of this NokkeltallForetak.  


        :return: The totalrentabilitet_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._totalrentabilitet_field

    @totalrentabilitet_field.setter
    def totalrentabilitet_field(self, totalrentabilitet_field):
        """Sets the totalrentabilitet_field of this NokkeltallForetak.


        :param totalrentabilitet_field: The totalrentabilitet_field of this NokkeltallForetak.  
        :type: float
        """

        self._totalrentabilitet_field = totalrentabilitet_field

    @property
    def e_k_rentabilitet_field(self):
        """Gets the e_k_rentabilitet_field of this NokkeltallForetak.  


        :return: The e_k_rentabilitet_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._e_k_rentabilitet_field

    @e_k_rentabilitet_field.setter
    def e_k_rentabilitet_field(self, e_k_rentabilitet_field):
        """Sets the e_k_rentabilitet_field of this NokkeltallForetak.


        :param e_k_rentabilitet_field: The e_k_rentabilitet_field of this NokkeltallForetak.  
        :type: float
        """

        self._e_k_rentabilitet_field = e_k_rentabilitet_field

    @property
    def lang_lagerfinans_field(self):
        """Gets the lang_lagerfinans_field of this NokkeltallForetak.  


        :return: The lang_lagerfinans_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._lang_lagerfinans_field

    @lang_lagerfinans_field.setter
    def lang_lagerfinans_field(self, lang_lagerfinans_field):
        """Sets the lang_lagerfinans_field of this NokkeltallForetak.


        :param lang_lagerfinans_field: The lang_lagerfinans_field of this NokkeltallForetak.  
        :type: float
        """

        self._lang_lagerfinans_field = lang_lagerfinans_field

    @property
    def gjennomsnitt_lager_field(self):
        """Gets the gjennomsnitt_lager_field of this NokkeltallForetak.  


        :return: The gjennomsnitt_lager_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._gjennomsnitt_lager_field

    @gjennomsnitt_lager_field.setter
    def gjennomsnitt_lager_field(self, gjennomsnitt_lager_field):
        """Sets the gjennomsnitt_lager_field of this NokkeltallForetak.


        :param gjennomsnitt_lager_field: The gjennomsnitt_lager_field of this NokkeltallForetak.  
        :type: float
        """

        self._gjennomsnitt_lager_field = gjennomsnitt_lager_field

    @property
    def egenkapital_andel_field(self):
        """Gets the egenkapital_andel_field of this NokkeltallForetak.  


        :return: The egenkapital_andel_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._egenkapital_andel_field

    @egenkapital_andel_field.setter
    def egenkapital_andel_field(self, egenkapital_andel_field):
        """Sets the egenkapital_andel_field of this NokkeltallForetak.


        :param egenkapital_andel_field: The egenkapital_andel_field of this NokkeltallForetak.  
        :type: float
        """

        self._egenkapital_andel_field = egenkapital_andel_field

    @property
    def tapsbuffer_field(self):
        """Gets the tapsbuffer_field of this NokkeltallForetak.  


        :return: The tapsbuffer_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._tapsbuffer_field

    @tapsbuffer_field.setter
    def tapsbuffer_field(self, tapsbuffer_field):
        """Sets the tapsbuffer_field of this NokkeltallForetak.


        :param tapsbuffer_field: The tapsbuffer_field of this NokkeltallForetak.  
        :type: float
        """

        self._tapsbuffer_field = tapsbuffer_field

    @property
    def fremmedkapital_kostnad_field(self):
        """Gets the fremmedkapital_kostnad_field of this NokkeltallForetak.  


        :return: The fremmedkapital_kostnad_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._fremmedkapital_kostnad_field

    @fremmedkapital_kostnad_field.setter
    def fremmedkapital_kostnad_field(self, fremmedkapital_kostnad_field):
        """Sets the fremmedkapital_kostnad_field of this NokkeltallForetak.


        :param fremmedkapital_kostnad_field: The fremmedkapital_kostnad_field of this NokkeltallForetak.  
        :type: float
        """

        self._fremmedkapital_kostnad_field = fremmedkapital_kostnad_field

    @property
    def likviditetsgrad1_field(self):
        """Gets the likviditetsgrad1_field of this NokkeltallForetak.  


        :return: The likviditetsgrad1_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._likviditetsgrad1_field

    @likviditetsgrad1_field.setter
    def likviditetsgrad1_field(self, likviditetsgrad1_field):
        """Sets the likviditetsgrad1_field of this NokkeltallForetak.


        :param likviditetsgrad1_field: The likviditetsgrad1_field of this NokkeltallForetak.  
        :type: float
        """

        self._likviditetsgrad1_field = likviditetsgrad1_field

    @property
    def likviditetsgrad2_field(self):
        """Gets the likviditetsgrad2_field of this NokkeltallForetak.  


        :return: The likviditetsgrad2_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._likviditetsgrad2_field

    @likviditetsgrad2_field.setter
    def likviditetsgrad2_field(self, likviditetsgrad2_field):
        """Sets the likviditetsgrad2_field of this NokkeltallForetak.


        :param likviditetsgrad2_field: The likviditetsgrad2_field of this NokkeltallForetak.  
        :type: float
        """

        self._likviditetsgrad2_field = likviditetsgrad2_field

    @property
    def likvider_prosent_salg_field(self):
        """Gets the likvider_prosent_salg_field of this NokkeltallForetak.  


        :return: The likvider_prosent_salg_field of this NokkeltallForetak.  
        :rtype: float
        """
        return self._likvider_prosent_salg_field

    @likvider_prosent_salg_field.setter
    def likvider_prosent_salg_field(self, likvider_prosent_salg_field):
        """Sets the likvider_prosent_salg_field of this NokkeltallForetak.


        :param likvider_prosent_salg_field: The likvider_prosent_salg_field of this NokkeltallForetak.  
        :type: float
        """

        self._likvider_prosent_salg_field = likvider_prosent_salg_field

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
        if not isinstance(other, NokkeltallForetak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
