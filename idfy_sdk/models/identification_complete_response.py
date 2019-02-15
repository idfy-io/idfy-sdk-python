# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class IdentificationCompleteResponse(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'done': 'bool'
    }

    attribute_map = {
        'done': 'Done'
    }

    def __init__(self, done=None):  
        """IdentificationCompleteResponse"""  

        self._done = None
        self.discriminator = None

        if done is not None:
            self.done = done

    @property
    def done(self):
        """Gets the done of this IdentificationCompleteResponse.  

        Is the idenfication process done?  

        :return: The done of this IdentificationCompleteResponse.  
        :rtype: bool
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this IdentificationCompleteResponse.

        Is the idenfication process done?  

        :param done: The done of this IdentificationCompleteResponse.  
        :type: bool
        """

        self._done = done

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
        if not isinstance(other, IdentificationCompleteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
