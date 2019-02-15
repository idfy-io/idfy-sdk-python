# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.lei_entity import LeiEntity  
from idfy_sdk.models.lei_extension import LeiExtension  
from idfy_sdk.models.lei_registration import LeiRegistration  


class LeiRecord(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'lei': 'str',
        'entity': 'LeiEntity',
        'registration': 'LeiRegistration',
        'extension': 'LeiExtension'
    }

    attribute_map = {
        'lei': 'Lei',
        'entity': 'Entity',
        'registration': 'Registration',
        'extension': 'Extension'
    }

    def __init__(self, lei=None, entity=None, registration=None, extension=None):  
        """LeiRecord"""  

        self._lei = None
        self._entity = None
        self._registration = None
        self._extension = None
        self.discriminator = None

        if lei is not None:
            self.lei = lei
        if entity is not None:
            self.entity = entity
        if registration is not None:
            self.registration = registration
        if extension is not None:
            self.extension = extension

    @property
    def lei(self):
        """Gets the lei of this LeiRecord.  


        :return: The lei of this LeiRecord.  
        :rtype: str
        """
        return self._lei

    @lei.setter
    def lei(self, lei):
        """Sets the lei of this LeiRecord.


        :param lei: The lei of this LeiRecord.  
        :type: str
        """

        self._lei = lei

    @property
    def entity(self):
        """Gets the entity of this LeiRecord.  


        :return: The entity of this LeiRecord.  
        :rtype: LeiEntity
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this LeiRecord.


        :param entity: The entity of this LeiRecord.  
        :type: LeiEntity
        """

        self._entity = entity

    @property
    def registration(self):
        """Gets the registration of this LeiRecord.  


        :return: The registration of this LeiRecord.  
        :rtype: LeiRegistration
        """
        return self._registration

    @registration.setter
    def registration(self, registration):
        """Sets the registration of this LeiRecord.


        :param registration: The registration of this LeiRecord.  
        :type: LeiRegistration
        """

        self._registration = registration

    @property
    def extension(self):
        """Gets the extension of this LeiRecord.  


        :return: The extension of this LeiRecord.  
        :rtype: LeiExtension
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this LeiRecord.


        :param extension: The extension of this LeiRecord.  
        :type: LeiExtension
        """

        self._extension = extension

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
        if not isinstance(other, LeiRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
