# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class MerchantError(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error_code': 'int',
        'error_description': 'str'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_description': 'errorDescription'
    }

    def __init__(self, error_code=None, error_description=None):  
        """MerchantError"""  

        self._error_code = None
        self._error_description = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_description is not None:
            self.error_description = error_description

    @property
    def error_code(self):
        """Gets the error_code of this MerchantError.  


        :return: The error_code of this MerchantError.  
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this MerchantError.


        :param error_code: The error_code of this MerchantError.  
        :type: int
        """

        self._error_code = error_code

    @property
    def error_description(self):
        """Gets the error_description of this MerchantError.  


        :return: The error_description of this MerchantError.  
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this MerchantError.


        :param error_description: The error_description of this MerchantError.  
        :type: str
        """

        self._error_description = error_description

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
        if not isinstance(other, MerchantError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
