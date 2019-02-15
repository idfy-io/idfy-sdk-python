# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class DealerInfo(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'reference': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'reference': 'Reference'
    }

    def __init__(self, id=None, reference=None):  
        """DealerInfo"""  

        self._id = None
        self._reference = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if reference is not None:
            self.reference = reference

    @property
    def id(self):
        """Gets the id of this DealerInfo.  


        :return: The id of this DealerInfo.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DealerInfo.


        :param id: The id of this DealerInfo.  
        :type: str
        """

        self._id = id

    @property
    def reference(self):
        """Gets the reference of this DealerInfo.  


        :return: The reference of this DealerInfo.  
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this DealerInfo.


        :param reference: The reference of this DealerInfo.  
        :type: str
        """

        self._reference = reference

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
        if not isinstance(other, DealerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
