# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class LanguageSetDTO(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'is_active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'is_active': 'isActive'
    }

    def __init__(self, id=None, name=None, created_at=None, updated_at=None, is_active=None):  
        """LanguageSetDTO"""  

        self._id = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._is_active = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if is_active is not None:
            self.is_active = is_active

    @property
    def id(self):
        """Gets the id of this LanguageSetDTO.  


        :return: The id of this LanguageSetDTO.  
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LanguageSetDTO.


        :param id: The id of this LanguageSetDTO.  
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this LanguageSetDTO.  


        :return: The name of this LanguageSetDTO.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LanguageSetDTO.


        :param name: The name of this LanguageSetDTO.  
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this LanguageSetDTO.  


        :return: The created_at of this LanguageSetDTO.  
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LanguageSetDTO.


        :param created_at: The created_at of this LanguageSetDTO.  
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this LanguageSetDTO.  


        :return: The updated_at of this LanguageSetDTO.  
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LanguageSetDTO.


        :param updated_at: The updated_at of this LanguageSetDTO.  
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def is_active(self):
        """Gets the is_active of this LanguageSetDTO.  


        :return: The is_active of this LanguageSetDTO.  
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this LanguageSetDTO.


        :param is_active: The is_active of this LanguageSetDTO.  
        :type: bool
        """

        self._is_active = is_active

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
        if not isinstance(other, LanguageSetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
