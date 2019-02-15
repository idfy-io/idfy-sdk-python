# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class TimeToLive(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'deadline': 'datetime',
        'delete_after_hours': 'int'
    }

    attribute_map = {
        'deadline': 'deadline',
        'delete_after_hours': 'deleteAfterHours'
    }

    def __init__(self, deadline=None, delete_after_hours=None):  
        """TimeToLive"""  

        self._deadline = None
        self._delete_after_hours = None
        self.discriminator = None

        if deadline is not None:
            self.deadline = deadline
        if delete_after_hours is not None:
            self.delete_after_hours = delete_after_hours

    @property
    def deadline(self):
        """Gets the deadline of this TimeToLive.  

        Time at which the document will expire (ISO 8601). The document can not be signed after this time. Default/maximum 45 days.  

        :return: The deadline of this TimeToLive.  
        :rtype: datetime
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this TimeToLive.

        Time at which the document will expire (ISO 8601). The document can not be signed after this time. Default/maximum 45 days.  

        :param deadline: The deadline of this TimeToLive.  
        :type: datetime
        """

        self._deadline = deadline

    @property
    def delete_after_hours(self):
        """Gets the delete_after_hours of this TimeToLive.  

        How many hours we will keep the document after it is signed or expired (deadline). Default/ maximum 7 days (168 hours). After this timespan the document and files will be permanently deleted on our side.  

        :return: The delete_after_hours of this TimeToLive.  
        :rtype: int
        """
        return self._delete_after_hours

    @delete_after_hours.setter
    def delete_after_hours(self, delete_after_hours):
        """Sets the delete_after_hours of this TimeToLive.

        How many hours we will keep the document after it is signed or expired (deadline). Default/ maximum 7 days (168 hours). After this timespan the document and files will be permanently deleted on our side.  

        :param delete_after_hours: The delete_after_hours of this TimeToLive.  
        :type: int
        """

        self._delete_after_hours = delete_after_hours

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
        if not isinstance(other, TimeToLive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
