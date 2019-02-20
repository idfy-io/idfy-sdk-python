# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  




class DialogAfter(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'title': 'str',
        'message': 'str'
    }

    attribute_map = {
        'title': 'title',
        'message': 'message'
    }

    def __init__(self, title=None, message=None):  
        """DialogAfter"""  

        self._title = None
        self._message = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if message is not None:
            self.message = message

    @property
    def title(self):
        """Gets the title of this DialogAfter.  

        The title of the dialog.  

        :return: The title of this DialogAfter.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DialogAfter.

        The title of the dialog.  

        :param title: The title of this DialogAfter.  
        :type: str
        """

        self._title = title

    @property
    def message(self):
        """Gets the message of this DialogAfter.  

        The message body of the dialog.  

        :return: The message of this DialogAfter.  
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DialogAfter.

        The message body of the dialog.  

        :param message: The message of this DialogAfter.  
        :type: str
        """

        self._message = message

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
        if not isinstance(other, DialogAfter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
