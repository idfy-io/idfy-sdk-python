# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class OkonomiSammendragForetak(object):

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
        'totalinntekt_field': 'int',
        'resultat_for_skatt_field': 'int',
        'ars_resultat_field': 'int',
        'sum_eiendeler_field': 'int',
        'overskuddsprosent_field': 'float',
        'totalrentabilitet_field': 'float',
        'egenkapitalandel_field': 'float',
        'likviditetsgrad1_field': 'float',
        'likviditetsgrad2_field': 'float',
        'overskuddsprosent_bransje_field': 'float',
        'totalrentabilitet_bransje_field': 'float',
        'egenkapitalandel_bransje_field': 'float',
        'likviditetsgrad1_bransje_field': 'float',
        'likviditetsgrad2_bransje_field': 'float'
    }

    attribute_map = {
        'regnskaps_av_ar_field': 'regnskapsAvArField',
        'regnskaps_av_mnd_field': 'regnskapsAvMndField',
        'totalinntekt_field': 'totalinntektField',
        'resultat_for_skatt_field': 'resultatForSkattField',
        'ars_resultat_field': 'arsResultatField',
        'sum_eiendeler_field': 'sumEiendelerField',
        'overskuddsprosent_field': 'overskuddsprosentField',
        'totalrentabilitet_field': 'totalrentabilitetField',
        'egenkapitalandel_field': 'egenkapitalandelField',
        'likviditetsgrad1_field': 'likviditetsgrad1Field',
        'likviditetsgrad2_field': 'likviditetsgrad2Field',
        'overskuddsprosent_bransje_field': 'overskuddsprosentBransjeField',
        'totalrentabilitet_bransje_field': 'totalrentabilitetBransjeField',
        'egenkapitalandel_bransje_field': 'egenkapitalandelBransjeField',
        'likviditetsgrad1_bransje_field': 'likviditetsgrad1BransjeField',
        'likviditetsgrad2_bransje_field': 'likviditetsgrad2BransjeField'
    }

    def __init__(self, regnskaps_av_ar_field=None, regnskaps_av_mnd_field=None, totalinntekt_field=None, resultat_for_skatt_field=None, ars_resultat_field=None, sum_eiendeler_field=None, overskuddsprosent_field=None, totalrentabilitet_field=None, egenkapitalandel_field=None, likviditetsgrad1_field=None, likviditetsgrad2_field=None, overskuddsprosent_bransje_field=None, totalrentabilitet_bransje_field=None, egenkapitalandel_bransje_field=None, likviditetsgrad1_bransje_field=None, likviditetsgrad2_bransje_field=None):  
        """OkonomiSammendragForetak"""  

        self._regnskaps_av_ar_field = None
        self._regnskaps_av_mnd_field = None
        self._totalinntekt_field = None
        self._resultat_for_skatt_field = None
        self._ars_resultat_field = None
        self._sum_eiendeler_field = None
        self._overskuddsprosent_field = None
        self._totalrentabilitet_field = None
        self._egenkapitalandel_field = None
        self._likviditetsgrad1_field = None
        self._likviditetsgrad2_field = None
        self._overskuddsprosent_bransje_field = None
        self._totalrentabilitet_bransje_field = None
        self._egenkapitalandel_bransje_field = None
        self._likviditetsgrad1_bransje_field = None
        self._likviditetsgrad2_bransje_field = None
        self.discriminator = None

        if regnskaps_av_ar_field is not None:
            self.regnskaps_av_ar_field = regnskaps_av_ar_field
        if regnskaps_av_mnd_field is not None:
            self.regnskaps_av_mnd_field = regnskaps_av_mnd_field
        if totalinntekt_field is not None:
            self.totalinntekt_field = totalinntekt_field
        if resultat_for_skatt_field is not None:
            self.resultat_for_skatt_field = resultat_for_skatt_field
        if ars_resultat_field is not None:
            self.ars_resultat_field = ars_resultat_field
        if sum_eiendeler_field is not None:
            self.sum_eiendeler_field = sum_eiendeler_field
        if overskuddsprosent_field is not None:
            self.overskuddsprosent_field = overskuddsprosent_field
        if totalrentabilitet_field is not None:
            self.totalrentabilitet_field = totalrentabilitet_field
        if egenkapitalandel_field is not None:
            self.egenkapitalandel_field = egenkapitalandel_field
        if likviditetsgrad1_field is not None:
            self.likviditetsgrad1_field = likviditetsgrad1_field
        if likviditetsgrad2_field is not None:
            self.likviditetsgrad2_field = likviditetsgrad2_field
        if overskuddsprosent_bransje_field is not None:
            self.overskuddsprosent_bransje_field = overskuddsprosent_bransje_field
        if totalrentabilitet_bransje_field is not None:
            self.totalrentabilitet_bransje_field = totalrentabilitet_bransje_field
        if egenkapitalandel_bransje_field is not None:
            self.egenkapitalandel_bransje_field = egenkapitalandel_bransje_field
        if likviditetsgrad1_bransje_field is not None:
            self.likviditetsgrad1_bransje_field = likviditetsgrad1_bransje_field
        if likviditetsgrad2_bransje_field is not None:
            self.likviditetsgrad2_bransje_field = likviditetsgrad2_bransje_field

    @property
    def regnskaps_av_ar_field(self):
        """Gets the regnskaps_av_ar_field of this OkonomiSammendragForetak.  


        :return: The regnskaps_av_ar_field of this OkonomiSammendragForetak.  
        :rtype: int
        """
        return self._regnskaps_av_ar_field

    @regnskaps_av_ar_field.setter
    def regnskaps_av_ar_field(self, regnskaps_av_ar_field):
        """Sets the regnskaps_av_ar_field of this OkonomiSammendragForetak.


        :param regnskaps_av_ar_field: The regnskaps_av_ar_field of this OkonomiSammendragForetak.  
        :type: int
        """

        self._regnskaps_av_ar_field = regnskaps_av_ar_field

    @property
    def regnskaps_av_mnd_field(self):
        """Gets the regnskaps_av_mnd_field of this OkonomiSammendragForetak.  


        :return: The regnskaps_av_mnd_field of this OkonomiSammendragForetak.  
        :rtype: int
        """
        return self._regnskaps_av_mnd_field

    @regnskaps_av_mnd_field.setter
    def regnskaps_av_mnd_field(self, regnskaps_av_mnd_field):
        """Sets the regnskaps_av_mnd_field of this OkonomiSammendragForetak.


        :param regnskaps_av_mnd_field: The regnskaps_av_mnd_field of this OkonomiSammendragForetak.  
        :type: int
        """

        self._regnskaps_av_mnd_field = regnskaps_av_mnd_field

    @property
    def totalinntekt_field(self):
        """Gets the totalinntekt_field of this OkonomiSammendragForetak.  


        :return: The totalinntekt_field of this OkonomiSammendragForetak.  
        :rtype: int
        """
        return self._totalinntekt_field

    @totalinntekt_field.setter
    def totalinntekt_field(self, totalinntekt_field):
        """Sets the totalinntekt_field of this OkonomiSammendragForetak.


        :param totalinntekt_field: The totalinntekt_field of this OkonomiSammendragForetak.  
        :type: int
        """

        self._totalinntekt_field = totalinntekt_field

    @property
    def resultat_for_skatt_field(self):
        """Gets the resultat_for_skatt_field of this OkonomiSammendragForetak.  


        :return: The resultat_for_skatt_field of this OkonomiSammendragForetak.  
        :rtype: int
        """
        return self._resultat_for_skatt_field

    @resultat_for_skatt_field.setter
    def resultat_for_skatt_field(self, resultat_for_skatt_field):
        """Sets the resultat_for_skatt_field of this OkonomiSammendragForetak.


        :param resultat_for_skatt_field: The resultat_for_skatt_field of this OkonomiSammendragForetak.  
        :type: int
        """

        self._resultat_for_skatt_field = resultat_for_skatt_field

    @property
    def ars_resultat_field(self):
        """Gets the ars_resultat_field of this OkonomiSammendragForetak.  


        :return: The ars_resultat_field of this OkonomiSammendragForetak.  
        :rtype: int
        """
        return self._ars_resultat_field

    @ars_resultat_field.setter
    def ars_resultat_field(self, ars_resultat_field):
        """Sets the ars_resultat_field of this OkonomiSammendragForetak.


        :param ars_resultat_field: The ars_resultat_field of this OkonomiSammendragForetak.  
        :type: int
        """

        self._ars_resultat_field = ars_resultat_field

    @property
    def sum_eiendeler_field(self):
        """Gets the sum_eiendeler_field of this OkonomiSammendragForetak.  


        :return: The sum_eiendeler_field of this OkonomiSammendragForetak.  
        :rtype: int
        """
        return self._sum_eiendeler_field

    @sum_eiendeler_field.setter
    def sum_eiendeler_field(self, sum_eiendeler_field):
        """Sets the sum_eiendeler_field of this OkonomiSammendragForetak.


        :param sum_eiendeler_field: The sum_eiendeler_field of this OkonomiSammendragForetak.  
        :type: int
        """

        self._sum_eiendeler_field = sum_eiendeler_field

    @property
    def overskuddsprosent_field(self):
        """Gets the overskuddsprosent_field of this OkonomiSammendragForetak.  


        :return: The overskuddsprosent_field of this OkonomiSammendragForetak.  
        :rtype: float
        """
        return self._overskuddsprosent_field

    @overskuddsprosent_field.setter
    def overskuddsprosent_field(self, overskuddsprosent_field):
        """Sets the overskuddsprosent_field of this OkonomiSammendragForetak.


        :param overskuddsprosent_field: The overskuddsprosent_field of this OkonomiSammendragForetak.  
        :type: float
        """

        self._overskuddsprosent_field = overskuddsprosent_field

    @property
    def totalrentabilitet_field(self):
        """Gets the totalrentabilitet_field of this OkonomiSammendragForetak.  


        :return: The totalrentabilitet_field of this OkonomiSammendragForetak.  
        :rtype: float
        """
        return self._totalrentabilitet_field

    @totalrentabilitet_field.setter
    def totalrentabilitet_field(self, totalrentabilitet_field):
        """Sets the totalrentabilitet_field of this OkonomiSammendragForetak.


        :param totalrentabilitet_field: The totalrentabilitet_field of this OkonomiSammendragForetak.  
        :type: float
        """

        self._totalrentabilitet_field = totalrentabilitet_field

    @property
    def egenkapitalandel_field(self):
        """Gets the egenkapitalandel_field of this OkonomiSammendragForetak.  


        :return: The egenkapitalandel_field of this OkonomiSammendragForetak.  
        :rtype: float
        """
        return self._egenkapitalandel_field

    @egenkapitalandel_field.setter
    def egenkapitalandel_field(self, egenkapitalandel_field):
        """Sets the egenkapitalandel_field of this OkonomiSammendragForetak.


        :param egenkapitalandel_field: The egenkapitalandel_field of this OkonomiSammendragForetak.  
        :type: float
        """

        self._egenkapitalandel_field = egenkapitalandel_field

    @property
    def likviditetsgrad1_field(self):
        """Gets the likviditetsgrad1_field of this OkonomiSammendragForetak.  


        :return: The likviditetsgrad1_field of this OkonomiSammendragForetak.  
        :rtype: float
        """
        return self._likviditetsgrad1_field

    @likviditetsgrad1_field.setter
    def likviditetsgrad1_field(self, likviditetsgrad1_field):
        """Sets the likviditetsgrad1_field of this OkonomiSammendragForetak.


        :param likviditetsgrad1_field: The likviditetsgrad1_field of this OkonomiSammendragForetak.  
        :type: float
        """

        self._likviditetsgrad1_field = likviditetsgrad1_field

    @property
    def likviditetsgrad2_field(self):
        """Gets the likviditetsgrad2_field of this OkonomiSammendragForetak.  


        :return: The likviditetsgrad2_field of this OkonomiSammendragForetak.  
        :rtype: float
        """
        return self._likviditetsgrad2_field

    @likviditetsgrad2_field.setter
    def likviditetsgrad2_field(self, likviditetsgrad2_field):
        """Sets the likviditetsgrad2_field of this OkonomiSammendragForetak.


        :param likviditetsgrad2_field: The likviditetsgrad2_field of this OkonomiSammendragForetak.  
        :type: float
        """

        self._likviditetsgrad2_field = likviditetsgrad2_field

    @property
    def overskuddsprosent_bransje_field(self):
        """Gets the overskuddsprosent_bransje_field of this OkonomiSammendragForetak.  


        :return: The overskuddsprosent_bransje_field of this OkonomiSammendragForetak.  
        :rtype: float
        """
        return self._overskuddsprosent_bransje_field

    @overskuddsprosent_bransje_field.setter
    def overskuddsprosent_bransje_field(self, overskuddsprosent_bransje_field):
        """Sets the overskuddsprosent_bransje_field of this OkonomiSammendragForetak.


        :param overskuddsprosent_bransje_field: The overskuddsprosent_bransje_field of this OkonomiSammendragForetak.  
        :type: float
        """

        self._overskuddsprosent_bransje_field = overskuddsprosent_bransje_field

    @property
    def totalrentabilitet_bransje_field(self):
        """Gets the totalrentabilitet_bransje_field of this OkonomiSammendragForetak.  


        :return: The totalrentabilitet_bransje_field of this OkonomiSammendragForetak.  
        :rtype: float
        """
        return self._totalrentabilitet_bransje_field

    @totalrentabilitet_bransje_field.setter
    def totalrentabilitet_bransje_field(self, totalrentabilitet_bransje_field):
        """Sets the totalrentabilitet_bransje_field of this OkonomiSammendragForetak.


        :param totalrentabilitet_bransje_field: The totalrentabilitet_bransje_field of this OkonomiSammendragForetak.  
        :type: float
        """

        self._totalrentabilitet_bransje_field = totalrentabilitet_bransje_field

    @property
    def egenkapitalandel_bransje_field(self):
        """Gets the egenkapitalandel_bransje_field of this OkonomiSammendragForetak.  


        :return: The egenkapitalandel_bransje_field of this OkonomiSammendragForetak.  
        :rtype: float
        """
        return self._egenkapitalandel_bransje_field

    @egenkapitalandel_bransje_field.setter
    def egenkapitalandel_bransje_field(self, egenkapitalandel_bransje_field):
        """Sets the egenkapitalandel_bransje_field of this OkonomiSammendragForetak.


        :param egenkapitalandel_bransje_field: The egenkapitalandel_bransje_field of this OkonomiSammendragForetak.  
        :type: float
        """

        self._egenkapitalandel_bransje_field = egenkapitalandel_bransje_field

    @property
    def likviditetsgrad1_bransje_field(self):
        """Gets the likviditetsgrad1_bransje_field of this OkonomiSammendragForetak.  


        :return: The likviditetsgrad1_bransje_field of this OkonomiSammendragForetak.  
        :rtype: float
        """
        return self._likviditetsgrad1_bransje_field

    @likviditetsgrad1_bransje_field.setter
    def likviditetsgrad1_bransje_field(self, likviditetsgrad1_bransje_field):
        """Sets the likviditetsgrad1_bransje_field of this OkonomiSammendragForetak.


        :param likviditetsgrad1_bransje_field: The likviditetsgrad1_bransje_field of this OkonomiSammendragForetak.  
        :type: float
        """

        self._likviditetsgrad1_bransje_field = likviditetsgrad1_bransje_field

    @property
    def likviditetsgrad2_bransje_field(self):
        """Gets the likviditetsgrad2_bransje_field of this OkonomiSammendragForetak.  


        :return: The likviditetsgrad2_bransje_field of this OkonomiSammendragForetak.  
        :rtype: float
        """
        return self._likviditetsgrad2_bransje_field

    @likviditetsgrad2_bransje_field.setter
    def likviditetsgrad2_bransje_field(self, likviditetsgrad2_bransje_field):
        """Sets the likviditetsgrad2_bransje_field of this OkonomiSammendragForetak.


        :param likviditetsgrad2_bransje_field: The likviditetsgrad2_bransje_field of this OkonomiSammendragForetak.  
        :type: float
        """

        self._likviditetsgrad2_bransje_field = likviditetsgrad2_bransje_field

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
        if not isinstance(other, OkonomiSammendragForetak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
