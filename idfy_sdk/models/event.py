# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Event(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'type': 'str',
        'payload': 'object',
        'timestamp': 'datetime',
        'account_id': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'payload': 'payload',
        'timestamp': 'timestamp',
        'account_id': 'accountId',
        'tags': 'tags'
    }

    def __init__(self, id=None, type=None, payload=None, timestamp=None, account_id=None, tags=None):  
        """EventDto"""  

        self._id = None
        self._type = None
        self._payload = None
        self._timestamp = None
        self._account_id = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if payload is not None:
            self.payload = payload
        if timestamp is not None:
            self.timestamp = timestamp
        if account_id is not None:
            self.account_id = account_id
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this EventDto.  


        :return: The id of this EventDto.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventDto.


        :param id: The id of this EventDto.  
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this EventDto.  


        :return: The type of this EventDto.  
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventDto.


        :param type: The type of this EventDto.  
        :type: str
        """

        self._type = type

    @property
    def payload(self):
        """Gets the payload of this EventDto.  


        :return: The payload of this EventDto.  
        :rtype: object
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this EventDto.


        :param payload: The payload of this EventDto.  
        :type: object
        """

        self._payload = payload

    @property
    def timestamp(self):
        """Gets the timestamp of this EventDto.  


        :return: The timestamp of this EventDto.  
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this EventDto.


        :param timestamp: The timestamp of this EventDto.  
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def account_id(self):
        """Gets the account_id of this EventDto.  


        :return: The account_id of this EventDto.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this EventDto.


        :param account_id: The account_id of this EventDto.  
        :type: str
        """

        self._account_id = account_id

    @property
    def tags(self):
        """Gets the tags of this EventDto.  


        :return: The tags of this EventDto.  
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EventDto.


        :param tags: The tags of this EventDto.  
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
