# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.identification_log_item import IdentificationLogItem  


class LogItemList(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'next_link': 'str',
        'total_links': 'int',
        'list': 'list[IdentificationLogItem]'
    }

    attribute_map = {
        'next_link': 'NextLink',
        'total_links': 'TotalLinks',
        'list': 'List'
    }

    def __init__(self, next_link=None, total_links=None, list=None):  
        """ListResultIdentificationLogItem"""  

        self._next_link = None
        self._total_links = None
        self._list = None
        self.discriminator = None

        if next_link is not None:
            self.next_link = next_link
        if total_links is not None:
            self.total_links = total_links
        if list is not None:
            self.list = list

    @property
    def next_link(self):
        """Gets the next_link of this ListResultIdentificationLogItem.  

        Link to the next results if not set there are less then the return limit of 1000  

        :return: The next_link of this ListResultIdentificationLogItem.  
        :rtype: str
        """
        return self._next_link

    @next_link.setter
    def next_link(self, next_link):
        """Sets the next_link of this ListResultIdentificationLogItem.

        Link to the next results if not set there are less then the return limit of 1000  

        :param next_link: The next_link of this ListResultIdentificationLogItem.  
        :type: str
        """

        self._next_link = next_link

    @property
    def total_links(self):
        """Gets the total_links of this ListResultIdentificationLogItem.  

        The total amount of links (pages) for the list  

        :return: The total_links of this ListResultIdentificationLogItem.  
        :rtype: int
        """
        return self._total_links

    @total_links.setter
    def total_links(self, total_links):
        """Sets the total_links of this ListResultIdentificationLogItem.

        The total amount of links (pages) for the list  

        :param total_links: The total_links of this ListResultIdentificationLogItem.  
        :type: int
        """

        self._total_links = total_links

    @property
    def list(self):
        """Gets the list of this ListResultIdentificationLogItem.  

        List of results  

        :return: The list of this ListResultIdentificationLogItem.  
        :rtype: list[IdentificationLogItem]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this ListResultIdentificationLogItem.

        List of results  

        :param list: The list of this ListResultIdentificationLogItem.  
        :type: list[IdentificationLogItem]
        """

        self._list = list

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
        if not isinstance(other, LogItemList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
