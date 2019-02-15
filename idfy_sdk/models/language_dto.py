# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class LanguageDTO(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'code': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'name': 'name'
    }

    def __init__(self, id=None, code=None, name=None):  
        """LanguageDTO"""  

        self._id = None
        self._code = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this LanguageDTO.  


        :return: The id of this LanguageDTO.  
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LanguageDTO.


        :param id: The id of this LanguageDTO.  
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this LanguageDTO.  


        :return: The code of this LanguageDTO.  
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LanguageDTO.


        :param code: The code of this LanguageDTO.  
        :type: str
        """

        self._code = code

    @property
    def name(self):
        """Gets the name of this LanguageDTO.  


        :return: The name of this LanguageDTO.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LanguageDTO.


        :param name: The name of this LanguageDTO.  
        :type: str
        """

        self._name = name

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
        if not isinstance(other, LanguageDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
