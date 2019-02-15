# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class LeiRegistrationAuthority(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'registration_authority_id': 'str',
        'registration_authority_entity_id': 'str'
    }

    attribute_map = {
        'registration_authority_id': 'RegistrationAuthorityId',
        'registration_authority_entity_id': 'RegistrationAuthorityEntityId'
    }

    def __init__(self, registration_authority_id=None, registration_authority_entity_id=None):  
        """LeiRegistrationAuthority"""  

        self._registration_authority_id = None
        self._registration_authority_entity_id = None
        self.discriminator = None

        if registration_authority_id is not None:
            self.registration_authority_id = registration_authority_id
        if registration_authority_entity_id is not None:
            self.registration_authority_entity_id = registration_authority_entity_id

    @property
    def registration_authority_id(self):
        """Gets the registration_authority_id of this LeiRegistrationAuthority.  


        :return: The registration_authority_id of this LeiRegistrationAuthority.  
        :rtype: str
        """
        return self._registration_authority_id

    @registration_authority_id.setter
    def registration_authority_id(self, registration_authority_id):
        """Sets the registration_authority_id of this LeiRegistrationAuthority.


        :param registration_authority_id: The registration_authority_id of this LeiRegistrationAuthority.  
        :type: str
        """

        self._registration_authority_id = registration_authority_id

    @property
    def registration_authority_entity_id(self):
        """Gets the registration_authority_entity_id of this LeiRegistrationAuthority.  


        :return: The registration_authority_entity_id of this LeiRegistrationAuthority.  
        :rtype: str
        """
        return self._registration_authority_entity_id

    @registration_authority_entity_id.setter
    def registration_authority_entity_id(self, registration_authority_entity_id):
        """Sets the registration_authority_entity_id of this LeiRegistrationAuthority.


        :param registration_authority_entity_id: The registration_authority_entity_id of this LeiRegistrationAuthority.  
        :type: str
        """

        self._registration_authority_entity_id = registration_authority_entity_id

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
        if not isinstance(other, LeiRegistrationAuthority):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
