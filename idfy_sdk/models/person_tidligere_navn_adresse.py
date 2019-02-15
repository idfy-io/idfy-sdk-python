# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonTidligereNavnAdresse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tidligere_navn_adresse1_field': 'str',
        'endrings_dato_field': 'datetime',
        'endrings_type_field': 'str',
        'tidligere_post_adresse_field': 'str'
    }

    attribute_map = {
        'tidligere_navn_adresse1_field': 'tidligereNavnAdresse1Field',
        'endrings_dato_field': 'endringsDatoField',
        'endrings_type_field': 'endringsTypeField',
        'tidligere_post_adresse_field': 'tidligerePostAdresseField'
    }

    def __init__(self, tidligere_navn_adresse1_field=None, endrings_dato_field=None, endrings_type_field=None, tidligere_post_adresse_field=None):  
        """PersonTidligereNavnAdresse"""  

        self._tidligere_navn_adresse1_field = None
        self._endrings_dato_field = None
        self._endrings_type_field = None
        self._tidligere_post_adresse_field = None
        self.discriminator = None

        if tidligere_navn_adresse1_field is not None:
            self.tidligere_navn_adresse1_field = tidligere_navn_adresse1_field
        if endrings_dato_field is not None:
            self.endrings_dato_field = endrings_dato_field
        if endrings_type_field is not None:
            self.endrings_type_field = endrings_type_field
        if tidligere_post_adresse_field is not None:
            self.tidligere_post_adresse_field = tidligere_post_adresse_field

    @property
    def tidligere_navn_adresse1_field(self):
        """Gets the tidligere_navn_adresse1_field of this PersonTidligereNavnAdresse.  


        :return: The tidligere_navn_adresse1_field of this PersonTidligereNavnAdresse.  
        :rtype: str
        """
        return self._tidligere_navn_adresse1_field

    @tidligere_navn_adresse1_field.setter
    def tidligere_navn_adresse1_field(self, tidligere_navn_adresse1_field):
        """Sets the tidligere_navn_adresse1_field of this PersonTidligereNavnAdresse.


        :param tidligere_navn_adresse1_field: The tidligere_navn_adresse1_field of this PersonTidligereNavnAdresse.  
        :type: str
        """

        self._tidligere_navn_adresse1_field = tidligere_navn_adresse1_field

    @property
    def endrings_dato_field(self):
        """Gets the endrings_dato_field of this PersonTidligereNavnAdresse.  


        :return: The endrings_dato_field of this PersonTidligereNavnAdresse.  
        :rtype: datetime
        """
        return self._endrings_dato_field

    @endrings_dato_field.setter
    def endrings_dato_field(self, endrings_dato_field):
        """Sets the endrings_dato_field of this PersonTidligereNavnAdresse.


        :param endrings_dato_field: The endrings_dato_field of this PersonTidligereNavnAdresse.  
        :type: datetime
        """

        self._endrings_dato_field = endrings_dato_field

    @property
    def endrings_type_field(self):
        """Gets the endrings_type_field of this PersonTidligereNavnAdresse.  


        :return: The endrings_type_field of this PersonTidligereNavnAdresse.  
        :rtype: str
        """
        return self._endrings_type_field

    @endrings_type_field.setter
    def endrings_type_field(self, endrings_type_field):
        """Sets the endrings_type_field of this PersonTidligereNavnAdresse.


        :param endrings_type_field: The endrings_type_field of this PersonTidligereNavnAdresse.  
        :type: str
        """

        self._endrings_type_field = endrings_type_field

    @property
    def tidligere_post_adresse_field(self):
        """Gets the tidligere_post_adresse_field of this PersonTidligereNavnAdresse.  


        :return: The tidligere_post_adresse_field of this PersonTidligereNavnAdresse.  
        :rtype: str
        """
        return self._tidligere_post_adresse_field

    @tidligere_post_adresse_field.setter
    def tidligere_post_adresse_field(self, tidligere_post_adresse_field):
        """Sets the tidligere_post_adresse_field of this PersonTidligereNavnAdresse.


        :param tidligere_post_adresse_field: The tidligere_post_adresse_field of this PersonTidligereNavnAdresse.  
        :type: str
        """

        self._tidligere_post_adresse_field = tidligere_post_adresse_field

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
        if not isinstance(other, PersonTidligereNavnAdresse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
