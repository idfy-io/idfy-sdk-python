# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class EventTypeInfo(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, description=None):  
        """EventTypeInfo"""  

        self._id = None
        self._name = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this EventTypeInfo.  

        Event type  

        :return: The id of this EventTypeInfo.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventTypeInfo.

        Event type  

        :param id: The id of this EventTypeInfo.  
        :type: str
        """
        allowed_values = ["document_before_deleted", "document_canceled", "document_created", "document_deleted", "document_expired", "document_email_opened", "document_form_partially_signed", "document_form_signed", "document_link_opened", "document_packaged", "document_partially_signed", "document_read", "document_signed"]  
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"  
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def name(self):
        """Gets the name of this EventTypeInfo.  

        Display name of the event  

        :return: The name of this EventTypeInfo.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventTypeInfo.

        Display name of the event  

        :param name: The name of this EventTypeInfo.  
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this EventTypeInfo.  

        Description of the event  

        :return: The description of this EventTypeInfo.  
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EventTypeInfo.

        Description of the event  

        :param description: The description of this EventTypeInfo.  
        :type: str
        """

        self._description = description

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
        if not isinstance(other, EventTypeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
