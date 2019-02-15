# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Role(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'description': 'str'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description'
    }

    def __init__(self, code=None, description=None):  
        """Role"""  

        self._code = None
        self._description = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if description is not None:
            self.description = description

    @property
    def code(self):
        """Gets the code of this Role.  


        :return: The code of this Role.  
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Role.


        :param code: The code of this Role.  
        :type: str
        """
        allowed_values = ["Unknown", "CHAIRMAN_OF_THE_BOARD", "DEPUTY_CHAIRMAN_OF_THE_BOARD", "BOARD_MEMBER", "EMPLOYEES_REPRESENTATIVE", "DEPUTY_BOARD_MEMBER", "OBSERVER", "REPRESENTATIVE_FOREIGN_ENTITY", "LIABLE_PARTNER", "CEO", "COMPANY_SECRETARY", "AUDITOR", "AUDIT_EXEMPTION", "CERTIFIED_ACCOUNTANT", "CONTACT"]  
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def description(self):
        """Gets the description of this Role.  


        :return: The description of this Role.  
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Role.


        :param description: The description of this Role.  
        :type: str
        """

        self._description = description

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
        if not isinstance(other, Role):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
