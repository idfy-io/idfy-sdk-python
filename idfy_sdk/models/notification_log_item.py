# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class NotificationLogItem(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sent_time_stamp': 'str',
        'title': 'str',
        'text': 'str',
        'message_type': 'str',
        'status': 'str',
        'from_address': 'str',
        'receiver': 'str'
    }

    attribute_map = {
        'sent_time_stamp': 'sentTimeStamp',
        'title': 'title',
        'text': 'text',
        'message_type': 'messageType',
        'status': 'status',
        'from_address': 'fromAddress',
        'receiver': 'receiver'
    }

    def __init__(self, sent_time_stamp=None, title=None, text=None, message_type=None, status=None, from_address=None, receiver=None):  
        """NotificationLogItem"""  

        self._sent_time_stamp = None
        self._title = None
        self._text = None
        self._message_type = None
        self._status = None
        self._from_address = None
        self._receiver = None
        self.discriminator = None

        if sent_time_stamp is not None:
            self.sent_time_stamp = sent_time_stamp
        if title is not None:
            self.title = title
        if text is not None:
            self.text = text
        if message_type is not None:
            self.message_type = message_type
        if status is not None:
            self.status = status
        if from_address is not None:
            self.from_address = from_address
        if receiver is not None:
            self.receiver = receiver

    @property
    def sent_time_stamp(self):
        """Gets the sent_time_stamp of this NotificationLogItem.  


        :return: The sent_time_stamp of this NotificationLogItem.  
        :rtype: str
        """
        return self._sent_time_stamp

    @sent_time_stamp.setter
    def sent_time_stamp(self, sent_time_stamp):
        """Sets the sent_time_stamp of this NotificationLogItem.


        :param sent_time_stamp: The sent_time_stamp of this NotificationLogItem.  
        :type: str
        """

        self._sent_time_stamp = sent_time_stamp

    @property
    def title(self):
        """Gets the title of this NotificationLogItem.  


        :return: The title of this NotificationLogItem.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NotificationLogItem.


        :param title: The title of this NotificationLogItem.  
        :type: str
        """

        self._title = title

    @property
    def text(self):
        """Gets the text of this NotificationLogItem.  


        :return: The text of this NotificationLogItem.  
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this NotificationLogItem.


        :param text: The text of this NotificationLogItem.  
        :type: str
        """

        self._text = text

    @property
    def message_type(self):
        """Gets the message_type of this NotificationLogItem.  


        :return: The message_type of this NotificationLogItem.  
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this NotificationLogItem.


        :param message_type: The message_type of this NotificationLogItem.  
        :type: str
        """

        self._message_type = message_type

    @property
    def status(self):
        """Gets the status of this NotificationLogItem.  


        :return: The status of this NotificationLogItem.  
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NotificationLogItem.


        :param status: The status of this NotificationLogItem.  
        :type: str
        """

        self._status = status

    @property
    def from_address(self):
        """Gets the from_address of this NotificationLogItem.  


        :return: The from_address of this NotificationLogItem.  
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this NotificationLogItem.


        :param from_address: The from_address of this NotificationLogItem.  
        :type: str
        """

        self._from_address = from_address

    @property
    def receiver(self):
        """Gets the receiver of this NotificationLogItem.  


        :return: The receiver of this NotificationLogItem.  
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this NotificationLogItem.


        :param receiver: The receiver of this NotificationLogItem.  
        :type: str
        """

        self._receiver = receiver

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
        if not isinstance(other, NotificationLogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
