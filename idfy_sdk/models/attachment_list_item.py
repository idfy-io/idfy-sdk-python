# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class AttachmentListItem(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'title': 'str',
        'description': 'str',
        'type': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'type': 'type',
        'file_name': 'fileName'
    }

    def __init__(self, id=None, title=None, description=None, type=None, file_name=None):  
        """AttachmentListItem"""  

        self._id = None
        self._title = None
        self._description = None
        self._type = None
        self._file_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if file_name is not None:
            self.file_name = file_name

    @property
    def id(self):
        """Gets the id of this AttachmentListItem.  

        The attachment's unique identifier.  

        :return: The id of this AttachmentListItem.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttachmentListItem.

        The attachment's unique identifier.  

        :param id: The id of this AttachmentListItem.  
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this AttachmentListItem.  

        The title of the attachment which will be presented to the user.  

        :return: The title of this AttachmentListItem.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AttachmentListItem.

        The title of the attachment which will be presented to the user.  

        :param title: The title of this AttachmentListItem.  
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this AttachmentListItem.  

        An optional description of the attachment.  

        :return: The description of this AttachmentListItem.  
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AttachmentListItem.

        An optional description of the attachment.  

        :param description: The description of this AttachmentListItem.  
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this AttachmentListItem.  

        The type of attachment.  

        :return: The type of this AttachmentListItem.  
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AttachmentListItem.

        The type of attachment.  

        :param type: The type of this AttachmentListItem.  
        :type: str
        """
        allowed_values = ["show_accept", "read_accept", "sign"]  
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def file_name(self):
        """Gets the file_name of this AttachmentListItem.  

        Filename with file extension. <span style=\"color:red;\">We only support PDF for attachments, set `convertToPdf` to `true` if you have a convertible file type.</span>  

        :return: The file_name of this AttachmentListItem.  
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this AttachmentListItem.

        Filename with file extension. <span style=\"color:red;\">We only support PDF for attachments, set `convertToPdf` to `true` if you have a convertible file type.</span>  

        :param file_name: The file_name of this AttachmentListItem.  
        :type: str
        """

        self._file_name = file_name

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
        if not isinstance(other, AttachmentListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
