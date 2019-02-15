# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.person_arsaks_data import PersonArsaksData  


class PersonScoring(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'beslutning_field': 'str',
        'arsaks_data_field': 'list[PersonArsaksData]',
        'score_field': 'int',
        'grense_avslag_field': 'int',
        'grense_godkjent_field': 'int'
    }

    attribute_map = {
        'beslutning_field': 'beslutningField',
        'arsaks_data_field': 'arsaksDataField',
        'score_field': 'scoreField',
        'grense_avslag_field': 'grenseAvslagField',
        'grense_godkjent_field': 'grenseGodkjentField'
    }

    def __init__(self, beslutning_field=None, arsaks_data_field=None, score_field=None, grense_avslag_field=None, grense_godkjent_field=None):  
        """PersonScoring"""  

        self._beslutning_field = None
        self._arsaks_data_field = None
        self._score_field = None
        self._grense_avslag_field = None
        self._grense_godkjent_field = None
        self.discriminator = None

        if beslutning_field is not None:
            self.beslutning_field = beslutning_field
        if arsaks_data_field is not None:
            self.arsaks_data_field = arsaks_data_field
        if score_field is not None:
            self.score_field = score_field
        if grense_avslag_field is not None:
            self.grense_avslag_field = grense_avslag_field
        if grense_godkjent_field is not None:
            self.grense_godkjent_field = grense_godkjent_field

    @property
    def beslutning_field(self):
        """Gets the beslutning_field of this PersonScoring.  


        :return: The beslutning_field of this PersonScoring.  
        :rtype: str
        """
        return self._beslutning_field

    @beslutning_field.setter
    def beslutning_field(self, beslutning_field):
        """Sets the beslutning_field of this PersonScoring.


        :param beslutning_field: The beslutning_field of this PersonScoring.  
        :type: str
        """

        self._beslutning_field = beslutning_field

    @property
    def arsaks_data_field(self):
        """Gets the arsaks_data_field of this PersonScoring.  


        :return: The arsaks_data_field of this PersonScoring.  
        :rtype: list[PersonArsaksData]
        """
        return self._arsaks_data_field

    @arsaks_data_field.setter
    def arsaks_data_field(self, arsaks_data_field):
        """Sets the arsaks_data_field of this PersonScoring.


        :param arsaks_data_field: The arsaks_data_field of this PersonScoring.  
        :type: list[PersonArsaksData]
        """

        self._arsaks_data_field = arsaks_data_field

    @property
    def score_field(self):
        """Gets the score_field of this PersonScoring.  


        :return: The score_field of this PersonScoring.  
        :rtype: int
        """
        return self._score_field

    @score_field.setter
    def score_field(self, score_field):
        """Sets the score_field of this PersonScoring.


        :param score_field: The score_field of this PersonScoring.  
        :type: int
        """

        self._score_field = score_field

    @property
    def grense_avslag_field(self):
        """Gets the grense_avslag_field of this PersonScoring.  


        :return: The grense_avslag_field of this PersonScoring.  
        :rtype: int
        """
        return self._grense_avslag_field

    @grense_avslag_field.setter
    def grense_avslag_field(self, grense_avslag_field):
        """Sets the grense_avslag_field of this PersonScoring.


        :param grense_avslag_field: The grense_avslag_field of this PersonScoring.  
        :type: int
        """

        self._grense_avslag_field = grense_avslag_field

    @property
    def grense_godkjent_field(self):
        """Gets the grense_godkjent_field of this PersonScoring.  


        :return: The grense_godkjent_field of this PersonScoring.  
        :rtype: int
        """
        return self._grense_godkjent_field

    @grense_godkjent_field.setter
    def grense_godkjent_field(self, grense_godkjent_field):
        """Sets the grense_godkjent_field of this PersonScoring.


        :param grense_godkjent_field: The grense_godkjent_field of this PersonScoring.  
        :type: int
        """

        self._grense_godkjent_field = grense_godkjent_field

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
        if not isinstance(other, PersonScoring):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
