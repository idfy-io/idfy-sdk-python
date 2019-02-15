# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class MockEventRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'event_type': 'str'
    }

    attribute_map = {
        'event_type': 'eventType'
    }

    def __init__(self, event_type=None):  
        """MockEventRequest"""  

        self._event_type = None
        self.discriminator = None

        self.event_type = event_type

    @property
    def event_type(self):
        """Gets the event_type of this MockEventRequest.  

        Event type to mock  

        :return: The event_type of this MockEventRequest.  
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this MockEventRequest.

        Event type to mock  

        :param event_type: The event_type of this MockEventRequest.  
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  

        self._event_type = event_type

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
        if not isinstance(other, MockEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
