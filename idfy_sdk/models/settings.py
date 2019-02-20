# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  




class Settings(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sms_sender': 'str'
    }

    attribute_map = {
        'sms_sender': 'SMSSender'
    }

    def __init__(self, sms_sender=None):  
        """Settings"""  

        self._sms_sender = None
        self.discriminator = None

        if sms_sender is not None:
            self.sms_sender = sms_sender

    @property
    def sms_sender(self):
        """Gets the sms_sender of this Settings.  


        :return: The sms_sender of this Settings.  
        :rtype: str
        """
        return self._sms_sender

    @sms_sender.setter
    def sms_sender(self, sms_sender):
        """Sets the sms_sender of this Settings.


        :param sms_sender: The sms_sender of this Settings.  
        :type: str
        """

        self._sms_sender = sms_sender

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
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
        if not isinstance(other, Settings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
