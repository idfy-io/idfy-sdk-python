# coding: utf-8

"""
    Idfy.Signature

    Sign contracts, declarations, forms and other documents using digital signatures.   ## Last update   Last build date for this endpoint: 18.03.2019

"""


import pprint
import re
from typing import List, Dict
from datetime import datetime as datetime


class AttachmentItem(object):
    """NOTE: This class is generated by Eivind.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'title': str,
        'checksum': str
    }

    attribute_map = {
        'title': 'title',
        'checksum': 'checksum'
    }

    def __init__(self, title=None, checksum=None):

        self._title = None
        self._checksum = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if checksum is not None:
            self.checksum = checksum

    @property
    def title(self):
        """Gets the title of this AttachmentItem.


        :return: The title of this AttachmentItem.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AttachmentItem.


        :param title: The title of this AttachmentItem.
        :type: str
        """

        self._title = title

    @property
    def checksum(self):
        """Gets the checksum of this AttachmentItem.


        :return: The checksum of this AttachmentItem.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this AttachmentItem.


        :param checksum: The checksum of this AttachmentItem.
        :type: str
        """

        self._checksum = checksum

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
        if not isinstance(other, AttachmentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
