# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Rating(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'rating1_field': 'str',
        'rating_beskrivelse_field': 'str',
        'limit_field': 'int',
        'aktuell_hendelse_field': 'str',
        'delb_grunnfakta_field': 'str',
        'delb_eier_jurdisk_field': 'str',
        'delb_okonomi_field': 'str',
        'delb_betalingserfaring_field': 'str'
    }

    attribute_map = {
        'rating1_field': 'rating1Field',
        'rating_beskrivelse_field': 'ratingBeskrivelseField',
        'limit_field': 'limitField',
        'aktuell_hendelse_field': 'aktuellHendelseField',
        'delb_grunnfakta_field': 'delbGrunnfaktaField',
        'delb_eier_jurdisk_field': 'delbEierJurdiskField',
        'delb_okonomi_field': 'delbOkonomiField',
        'delb_betalingserfaring_field': 'delbBetalingserfaringField'
    }

    def __init__(self, rating1_field=None, rating_beskrivelse_field=None, limit_field=None, aktuell_hendelse_field=None, delb_grunnfakta_field=None, delb_eier_jurdisk_field=None, delb_okonomi_field=None, delb_betalingserfaring_field=None):  
        """Rating"""  

        self._rating1_field = None
        self._rating_beskrivelse_field = None
        self._limit_field = None
        self._aktuell_hendelse_field = None
        self._delb_grunnfakta_field = None
        self._delb_eier_jurdisk_field = None
        self._delb_okonomi_field = None
        self._delb_betalingserfaring_field = None
        self.discriminator = None

        if rating1_field is not None:
            self.rating1_field = rating1_field
        if rating_beskrivelse_field is not None:
            self.rating_beskrivelse_field = rating_beskrivelse_field
        if limit_field is not None:
            self.limit_field = limit_field
        if aktuell_hendelse_field is not None:
            self.aktuell_hendelse_field = aktuell_hendelse_field
        if delb_grunnfakta_field is not None:
            self.delb_grunnfakta_field = delb_grunnfakta_field
        if delb_eier_jurdisk_field is not None:
            self.delb_eier_jurdisk_field = delb_eier_jurdisk_field
        if delb_okonomi_field is not None:
            self.delb_okonomi_field = delb_okonomi_field
        if delb_betalingserfaring_field is not None:
            self.delb_betalingserfaring_field = delb_betalingserfaring_field

    @property
    def rating1_field(self):
        """Gets the rating1_field of this Rating.  


        :return: The rating1_field of this Rating.  
        :rtype: str
        """
        return self._rating1_field

    @rating1_field.setter
    def rating1_field(self, rating1_field):
        """Sets the rating1_field of this Rating.


        :param rating1_field: The rating1_field of this Rating.  
        :type: str
        """

        self._rating1_field = rating1_field

    @property
    def rating_beskrivelse_field(self):
        """Gets the rating_beskrivelse_field of this Rating.  


        :return: The rating_beskrivelse_field of this Rating.  
        :rtype: str
        """
        return self._rating_beskrivelse_field

    @rating_beskrivelse_field.setter
    def rating_beskrivelse_field(self, rating_beskrivelse_field):
        """Sets the rating_beskrivelse_field of this Rating.


        :param rating_beskrivelse_field: The rating_beskrivelse_field of this Rating.  
        :type: str
        """

        self._rating_beskrivelse_field = rating_beskrivelse_field

    @property
    def limit_field(self):
        """Gets the limit_field of this Rating.  


        :return: The limit_field of this Rating.  
        :rtype: int
        """
        return self._limit_field

    @limit_field.setter
    def limit_field(self, limit_field):
        """Sets the limit_field of this Rating.


        :param limit_field: The limit_field of this Rating.  
        :type: int
        """

        self._limit_field = limit_field

    @property
    def aktuell_hendelse_field(self):
        """Gets the aktuell_hendelse_field of this Rating.  


        :return: The aktuell_hendelse_field of this Rating.  
        :rtype: str
        """
        return self._aktuell_hendelse_field

    @aktuell_hendelse_field.setter
    def aktuell_hendelse_field(self, aktuell_hendelse_field):
        """Sets the aktuell_hendelse_field of this Rating.


        :param aktuell_hendelse_field: The aktuell_hendelse_field of this Rating.  
        :type: str
        """

        self._aktuell_hendelse_field = aktuell_hendelse_field

    @property
    def delb_grunnfakta_field(self):
        """Gets the delb_grunnfakta_field of this Rating.  


        :return: The delb_grunnfakta_field of this Rating.  
        :rtype: str
        """
        return self._delb_grunnfakta_field

    @delb_grunnfakta_field.setter
    def delb_grunnfakta_field(self, delb_grunnfakta_field):
        """Sets the delb_grunnfakta_field of this Rating.


        :param delb_grunnfakta_field: The delb_grunnfakta_field of this Rating.  
        :type: str
        """

        self._delb_grunnfakta_field = delb_grunnfakta_field

    @property
    def delb_eier_jurdisk_field(self):
        """Gets the delb_eier_jurdisk_field of this Rating.  


        :return: The delb_eier_jurdisk_field of this Rating.  
        :rtype: str
        """
        return self._delb_eier_jurdisk_field

    @delb_eier_jurdisk_field.setter
    def delb_eier_jurdisk_field(self, delb_eier_jurdisk_field):
        """Sets the delb_eier_jurdisk_field of this Rating.


        :param delb_eier_jurdisk_field: The delb_eier_jurdisk_field of this Rating.  
        :type: str
        """

        self._delb_eier_jurdisk_field = delb_eier_jurdisk_field

    @property
    def delb_okonomi_field(self):
        """Gets the delb_okonomi_field of this Rating.  


        :return: The delb_okonomi_field of this Rating.  
        :rtype: str
        """
        return self._delb_okonomi_field

    @delb_okonomi_field.setter
    def delb_okonomi_field(self, delb_okonomi_field):
        """Sets the delb_okonomi_field of this Rating.


        :param delb_okonomi_field: The delb_okonomi_field of this Rating.  
        :type: str
        """

        self._delb_okonomi_field = delb_okonomi_field

    @property
    def delb_betalingserfaring_field(self):
        """Gets the delb_betalingserfaring_field of this Rating.  


        :return: The delb_betalingserfaring_field of this Rating.  
        :rtype: str
        """
        return self._delb_betalingserfaring_field

    @delb_betalingserfaring_field.setter
    def delb_betalingserfaring_field(self, delb_betalingserfaring_field):
        """Sets the delb_betalingserfaring_field of this Rating.


        :param delb_betalingserfaring_field: The delb_betalingserfaring_field of this Rating.  
        :type: str
        """

        self._delb_betalingserfaring_field = delb_betalingserfaring_field

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
        if not isinstance(other, Rating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
