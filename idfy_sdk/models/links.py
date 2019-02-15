# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Links(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'next': 'str',
        'previous': 'str',
        'first': 'str'
    }

    attribute_map = {
        'next': 'next',
        'previous': 'previous',
        'first': 'first'
    }

    def __init__(self, next=None, previous=None, first=None):  
        """Links"""  

        self._next = None
        self._previous = None
        self._first = None
        self.discriminator = None

        if next is not None:
            self.next = next
        if previous is not None:
            self.previous = previous
        if first is not None:
            self.first = first

    @property
    def next(self):
        """Gets the next of this Links.  


        :return: The next of this Links.  
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Links.


        :param next: The next of this Links.  
        :type: str
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this Links.  


        :return: The previous of this Links.  
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this Links.


        :param previous: The previous of this Links.  
        :type: str
        """

        self._previous = previous

    @property
    def first(self):
        """Gets the first of this Links.  


        :return: The first of this Links.  
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this Links.


        :param first: The first of this Links.  
        :type: str
        """

        self._first = first

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
        if not isinstance(other, Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
