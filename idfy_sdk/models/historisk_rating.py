# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class HistoriskRating(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'endr_ar_field': 'int',
        'endr_mnd_field': 'int',
        'rating_field': 'str',
        'limit_field': 'int',
        'aktuell_hendelse_field': 'str',
        'regn_ar_field': 'int'
    }

    attribute_map = {
        'endr_ar_field': 'endrArField',
        'endr_mnd_field': 'endrMndField',
        'rating_field': 'ratingField',
        'limit_field': 'limitField',
        'aktuell_hendelse_field': 'aktuellHendelseField',
        'regn_ar_field': 'regnArField'
    }

    def __init__(self, endr_ar_field=None, endr_mnd_field=None, rating_field=None, limit_field=None, aktuell_hendelse_field=None, regn_ar_field=None):  
        """HistoriskRating"""  

        self._endr_ar_field = None
        self._endr_mnd_field = None
        self._rating_field = None
        self._limit_field = None
        self._aktuell_hendelse_field = None
        self._regn_ar_field = None
        self.discriminator = None

        if endr_ar_field is not None:
            self.endr_ar_field = endr_ar_field
        if endr_mnd_field is not None:
            self.endr_mnd_field = endr_mnd_field
        if rating_field is not None:
            self.rating_field = rating_field
        if limit_field is not None:
            self.limit_field = limit_field
        if aktuell_hendelse_field is not None:
            self.aktuell_hendelse_field = aktuell_hendelse_field
        if regn_ar_field is not None:
            self.regn_ar_field = regn_ar_field

    @property
    def endr_ar_field(self):
        """Gets the endr_ar_field of this HistoriskRating.  


        :return: The endr_ar_field of this HistoriskRating.  
        :rtype: int
        """
        return self._endr_ar_field

    @endr_ar_field.setter
    def endr_ar_field(self, endr_ar_field):
        """Sets the endr_ar_field of this HistoriskRating.


        :param endr_ar_field: The endr_ar_field of this HistoriskRating.  
        :type: int
        """

        self._endr_ar_field = endr_ar_field

    @property
    def endr_mnd_field(self):
        """Gets the endr_mnd_field of this HistoriskRating.  


        :return: The endr_mnd_field of this HistoriskRating.  
        :rtype: int
        """
        return self._endr_mnd_field

    @endr_mnd_field.setter
    def endr_mnd_field(self, endr_mnd_field):
        """Sets the endr_mnd_field of this HistoriskRating.


        :param endr_mnd_field: The endr_mnd_field of this HistoriskRating.  
        :type: int
        """

        self._endr_mnd_field = endr_mnd_field

    @property
    def rating_field(self):
        """Gets the rating_field of this HistoriskRating.  


        :return: The rating_field of this HistoriskRating.  
        :rtype: str
        """
        return self._rating_field

    @rating_field.setter
    def rating_field(self, rating_field):
        """Sets the rating_field of this HistoriskRating.


        :param rating_field: The rating_field of this HistoriskRating.  
        :type: str
        """

        self._rating_field = rating_field

    @property
    def limit_field(self):
        """Gets the limit_field of this HistoriskRating.  


        :return: The limit_field of this HistoriskRating.  
        :rtype: int
        """
        return self._limit_field

    @limit_field.setter
    def limit_field(self, limit_field):
        """Sets the limit_field of this HistoriskRating.


        :param limit_field: The limit_field of this HistoriskRating.  
        :type: int
        """

        self._limit_field = limit_field

    @property
    def aktuell_hendelse_field(self):
        """Gets the aktuell_hendelse_field of this HistoriskRating.  


        :return: The aktuell_hendelse_field of this HistoriskRating.  
        :rtype: str
        """
        return self._aktuell_hendelse_field

    @aktuell_hendelse_field.setter
    def aktuell_hendelse_field(self, aktuell_hendelse_field):
        """Sets the aktuell_hendelse_field of this HistoriskRating.


        :param aktuell_hendelse_field: The aktuell_hendelse_field of this HistoriskRating.  
        :type: str
        """

        self._aktuell_hendelse_field = aktuell_hendelse_field

    @property
    def regn_ar_field(self):
        """Gets the regn_ar_field of this HistoriskRating.  


        :return: The regn_ar_field of this HistoriskRating.  
        :rtype: int
        """
        return self._regn_ar_field

    @regn_ar_field.setter
    def regn_ar_field(self, regn_ar_field):
        """Sets the regn_ar_field of this HistoriskRating.


        :param regn_ar_field: The regn_ar_field of this HistoriskRating.  
        :type: int
        """

        self._regn_ar_field = regn_ar_field

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
        if not isinstance(other, HistoriskRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
