# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class SignatureError(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error_message': 'str',
        'error_code': 'str',
        'eid_error_message': 'str',
        'eid_error_code': 'str'
    }

    attribute_map = {
        'error_message': 'errorMessage',
        'error_code': 'errorCode',
        'eid_error_message': 'eidErrorMessage',
        'eid_error_code': 'eidErrorCode'
    }

    def __init__(self, error_message=None, error_code=None, eid_error_message=None, eid_error_code=None):  
        """SignatureError"""  

        self._error_message = None
        self._error_code = None
        self._eid_error_message = None
        self._eid_error_code = None
        self.discriminator = None

        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code
        if eid_error_message is not None:
            self.eid_error_message = eid_error_message
        if eid_error_code is not None:
            self.eid_error_code = eid_error_code

    @property
    def error_message(self):
        """Gets the error_message of this SignatureError.  

        Idfy error message  

        :return: The error_message of this SignatureError.  
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this SignatureError.

        Idfy error message  

        :param error_message: The error_message of this SignatureError.  
        :type: str
        """

        self._error_message = error_message

    @property
    def error_code(self):
        """Gets the error_code of this SignatureError.  

        Idfy error code  

        :return: The error_code of this SignatureError.  
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this SignatureError.

        Idfy error code  

        :param error_code: The error_code of this SignatureError.  
        :type: str
        """

        self._error_code = error_code

    @property
    def eid_error_message(self):
        """Gets the eid_error_message of this SignatureError.  

        Eid provider error message  

        :return: The eid_error_message of this SignatureError.  
        :rtype: str
        """
        return self._eid_error_message

    @eid_error_message.setter
    def eid_error_message(self, eid_error_message):
        """Sets the eid_error_message of this SignatureError.

        Eid provider error message  

        :param eid_error_message: The eid_error_message of this SignatureError.  
        :type: str
        """

        self._eid_error_message = eid_error_message

    @property
    def eid_error_code(self):
        """Gets the eid_error_code of this SignatureError.  

        Eid provider error code  

        :return: The eid_error_code of this SignatureError.  
        :rtype: str
        """
        return self._eid_error_code

    @eid_error_code.setter
    def eid_error_code(self, eid_error_code):
        """Sets the eid_error_code of this SignatureError.

        Eid provider error code  

        :param eid_error_code: The eid_error_code of this SignatureError.  
        :type: str
        """

        self._eid_error_code = eid_error_code

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
        if not isinstance(other, SignatureError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
