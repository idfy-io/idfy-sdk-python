# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PdfTemplateListItem(object):

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
        'last_edited': 'datetime'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'last_edited': 'LastEdited'
    }

    def __init__(self, id=None, name=None, last_edited=None):  
        """PdfTemplateListItem"""  

        self._id = None
        self._name = None
        self._last_edited = None
        self.discriminator = None

        self.id = id
        self.name = name
        if last_edited is not None:
            self.last_edited = last_edited

    @property
    def id(self):
        """Gets the id of this PdfTemplateListItem.  


        :return: The id of this PdfTemplateListItem.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PdfTemplateListItem.


        :param id: The id of this PdfTemplateListItem.  
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  

        self._id = id

    @property
    def name(self):
        """Gets the name of this PdfTemplateListItem.  

        The name of the Pdf template  

        :return: The name of this PdfTemplateListItem.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PdfTemplateListItem.

        The name of the Pdf template  

        :param name: The name of this PdfTemplateListItem.  
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  

        self._name = name

    @property
    def last_edited(self):
        """Gets the last_edited of this PdfTemplateListItem.  

        Timestamp when the template is last edited  

        :return: The last_edited of this PdfTemplateListItem.  
        :rtype: datetime
        """
        return self._last_edited

    @last_edited.setter
    def last_edited(self, last_edited):
        """Sets the last_edited of this PdfTemplateListItem.

        Timestamp when the template is last edited  

        :param last_edited: The last_edited of this PdfTemplateListItem.  
        :type: datetime
        """

        self._last_edited = last_edited

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
        if not isinstance(other, PdfTemplateListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
