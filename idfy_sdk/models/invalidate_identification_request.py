# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class InvalidateIdentificationRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str'
    }

    attribute_map = {
        'request_id': 'RequestId'
    }

    def __init__(self, request_id=None):  
        """InvalidateIdentificationRequest"""  

        self._request_id = None
        self.discriminator = None

        self.request_id = request_id

    @property
    def request_id(self):
        """Gets the request_id of this InvalidateIdentificationRequest.  

        The requestid of the identification process  

        :return: The request_id of this InvalidateIdentificationRequest.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this InvalidateIdentificationRequest.

        The requestid of the identification process  

        :param request_id: The request_id of this InvalidateIdentificationRequest.  
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  

        self._request_id = request_id

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
        if not isinstance(other, InvalidateIdentificationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
