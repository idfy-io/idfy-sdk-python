# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class ReturnUrls(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error': 'str',
        'abort': 'str',
        'success': 'str'
    }

    attribute_map = {
        'error': 'Error',
        'abort': 'Abort',
        'success': 'Success'
    }

    def __init__(self, error=None, abort=None, success=None):  
        """ReturnUrls"""  

        self._error = None
        self._abort = None
        self._success = None
        self.discriminator = None

        self.error = error
        self.abort = abort
        self.success = success

    @property
    def error(self):
        """Gets the error of this ReturnUrls.  

        The url to be redirected to if the identification process fails. This url supports the following placeholders: [0] statuscode, [1] requestId, [2] ExternalReference (your unique id).  

        :return: The error of this ReturnUrls.  
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ReturnUrls.

        The url to be redirected to if the identification process fails. This url supports the following placeholders: [0] statuscode, [1] requestId, [2] ExternalReference (your unique id).  

        :param error: The error of this ReturnUrls.  
        :type: str
        """
        if error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  

        self._error = error

    @property
    def abort(self):
        """Gets the abort of this ReturnUrls.  

        The url to be redirected to if the user aborts the identification process. This url supports the following placeholders: [1] requestId, [2] ExternalReference (your unique id).  

        :return: The abort of this ReturnUrls.  
        :rtype: str
        """
        return self._abort

    @abort.setter
    def abort(self, abort):
        """Sets the abort of this ReturnUrls.

        The url to be redirected to if the user aborts the identification process. This url supports the following placeholders: [1] requestId, [2] ExternalReference (your unique id).  

        :param abort: The abort of this ReturnUrls.  
        :type: str
        """
        if abort is None:
            raise ValueError("Invalid value for `abort`, must not be `None`")  

        self._abort = abort

    @property
    def success(self):
        """Gets the success of this ReturnUrls.  

        The return urls to be redirected to after the identification process is a success. This url supports the following placeholders: [1] requestId, [2] ExternalReference (your unique id).  

        :return: The success of this ReturnUrls.  
        :rtype: str
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ReturnUrls.

        The return urls to be redirected to after the identification process is a success. This url supports the following placeholders: [1] requestId, [2] ExternalReference (your unique id).  

        :param success: The success of this ReturnUrls.  
        :type: str
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")  

        self._success = success

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
        if not isinstance(other, ReturnUrls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
