# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonEiendomListe(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'kommunenr_field': 'str',
        'kommune_navn_field': 'str',
        'gardnr_field': 'int',
        'bruksnr_field': 'int',
        'festenr_field': 'int',
        'seksjonsnr_field': 'int',
        'type_field': 'str',
        'andel_field': 'str'
    }

    attribute_map = {
        'kommunenr_field': 'kommunenrField',
        'kommune_navn_field': 'kommuneNavnField',
        'gardnr_field': 'gardnrField',
        'bruksnr_field': 'bruksnrField',
        'festenr_field': 'festenrField',
        'seksjonsnr_field': 'seksjonsnrField',
        'type_field': 'typeField',
        'andel_field': 'andelField'
    }

    def __init__(self, kommunenr_field=None, kommune_navn_field=None, gardnr_field=None, bruksnr_field=None, festenr_field=None, seksjonsnr_field=None, type_field=None, andel_field=None):  
        """PersonEiendomListe"""  

        self._kommunenr_field = None
        self._kommune_navn_field = None
        self._gardnr_field = None
        self._bruksnr_field = None
        self._festenr_field = None
        self._seksjonsnr_field = None
        self._type_field = None
        self._andel_field = None
        self.discriminator = None

        if kommunenr_field is not None:
            self.kommunenr_field = kommunenr_field
        if kommune_navn_field is not None:
            self.kommune_navn_field = kommune_navn_field
        if gardnr_field is not None:
            self.gardnr_field = gardnr_field
        if bruksnr_field is not None:
            self.bruksnr_field = bruksnr_field
        if festenr_field is not None:
            self.festenr_field = festenr_field
        if seksjonsnr_field is not None:
            self.seksjonsnr_field = seksjonsnr_field
        if type_field is not None:
            self.type_field = type_field
        if andel_field is not None:
            self.andel_field = andel_field

    @property
    def kommunenr_field(self):
        """Gets the kommunenr_field of this PersonEiendomListe.  


        :return: The kommunenr_field of this PersonEiendomListe.  
        :rtype: str
        """
        return self._kommunenr_field

    @kommunenr_field.setter
    def kommunenr_field(self, kommunenr_field):
        """Sets the kommunenr_field of this PersonEiendomListe.


        :param kommunenr_field: The kommunenr_field of this PersonEiendomListe.  
        :type: str
        """

        self._kommunenr_field = kommunenr_field

    @property
    def kommune_navn_field(self):
        """Gets the kommune_navn_field of this PersonEiendomListe.  


        :return: The kommune_navn_field of this PersonEiendomListe.  
        :rtype: str
        """
        return self._kommune_navn_field

    @kommune_navn_field.setter
    def kommune_navn_field(self, kommune_navn_field):
        """Sets the kommune_navn_field of this PersonEiendomListe.


        :param kommune_navn_field: The kommune_navn_field of this PersonEiendomListe.  
        :type: str
        """

        self._kommune_navn_field = kommune_navn_field

    @property
    def gardnr_field(self):
        """Gets the gardnr_field of this PersonEiendomListe.  


        :return: The gardnr_field of this PersonEiendomListe.  
        :rtype: int
        """
        return self._gardnr_field

    @gardnr_field.setter
    def gardnr_field(self, gardnr_field):
        """Sets the gardnr_field of this PersonEiendomListe.


        :param gardnr_field: The gardnr_field of this PersonEiendomListe.  
        :type: int
        """

        self._gardnr_field = gardnr_field

    @property
    def bruksnr_field(self):
        """Gets the bruksnr_field of this PersonEiendomListe.  


        :return: The bruksnr_field of this PersonEiendomListe.  
        :rtype: int
        """
        return self._bruksnr_field

    @bruksnr_field.setter
    def bruksnr_field(self, bruksnr_field):
        """Sets the bruksnr_field of this PersonEiendomListe.


        :param bruksnr_field: The bruksnr_field of this PersonEiendomListe.  
        :type: int
        """

        self._bruksnr_field = bruksnr_field

    @property
    def festenr_field(self):
        """Gets the festenr_field of this PersonEiendomListe.  


        :return: The festenr_field of this PersonEiendomListe.  
        :rtype: int
        """
        return self._festenr_field

    @festenr_field.setter
    def festenr_field(self, festenr_field):
        """Sets the festenr_field of this PersonEiendomListe.


        :param festenr_field: The festenr_field of this PersonEiendomListe.  
        :type: int
        """

        self._festenr_field = festenr_field

    @property
    def seksjonsnr_field(self):
        """Gets the seksjonsnr_field of this PersonEiendomListe.  


        :return: The seksjonsnr_field of this PersonEiendomListe.  
        :rtype: int
        """
        return self._seksjonsnr_field

    @seksjonsnr_field.setter
    def seksjonsnr_field(self, seksjonsnr_field):
        """Sets the seksjonsnr_field of this PersonEiendomListe.


        :param seksjonsnr_field: The seksjonsnr_field of this PersonEiendomListe.  
        :type: int
        """

        self._seksjonsnr_field = seksjonsnr_field

    @property
    def type_field(self):
        """Gets the type_field of this PersonEiendomListe.  


        :return: The type_field of this PersonEiendomListe.  
        :rtype: str
        """
        return self._type_field

    @type_field.setter
    def type_field(self, type_field):
        """Sets the type_field of this PersonEiendomListe.


        :param type_field: The type_field of this PersonEiendomListe.  
        :type: str
        """

        self._type_field = type_field

    @property
    def andel_field(self):
        """Gets the andel_field of this PersonEiendomListe.  


        :return: The andel_field of this PersonEiendomListe.  
        :rtype: str
        """
        return self._andel_field

    @andel_field.setter
    def andel_field(self, andel_field):
        """Sets the andel_field of this PersonEiendomListe.


        :param andel_field: The andel_field of this PersonEiendomListe.  
        :type: str
        """

        self._andel_field = andel_field

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
        if not isinstance(other, PersonEiendomListe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
