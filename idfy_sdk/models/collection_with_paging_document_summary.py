# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.document_summary import DocumentSummary  
from idfy_sdk.models.links import Links  


class CollectionWithPagingDocumentSummary(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'offset': 'int',
        'limit': 'int',
        'size': 'int',
        'links': 'Links',
        'data': 'list[DocumentSummary]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'size': 'size',
        'links': 'links',
        'data': 'data'
    }

    def __init__(self, offset=None, limit=None, size=None, links=None, data=None):  
        """CollectionWithPagingDocumentSummary"""  

        self._offset = None
        self._limit = None
        self._size = None
        self._links = None
        self._data = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if size is not None:
            self.size = size
        if links is not None:
            self.links = links
        if data is not None:
            self.data = data

    @property
    def offset(self):
        """Gets the offset of this CollectionWithPagingDocumentSummary.  

        The offset of the current page.  

        :return: The offset of this CollectionWithPagingDocumentSummary.  
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this CollectionWithPagingDocumentSummary.

        The offset of the current page.  

        :param offset: The offset of this CollectionWithPagingDocumentSummary.  
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this CollectionWithPagingDocumentSummary.  

        The limit of the current paging options.  

        :return: The limit of this CollectionWithPagingDocumentSummary.  
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this CollectionWithPagingDocumentSummary.

        The limit of the current paging options.  

        :param limit: The limit of this CollectionWithPagingDocumentSummary.  
        :type: int
        """

        self._limit = limit

    @property
    def size(self):
        """Gets the size of this CollectionWithPagingDocumentSummary.  

        The total size of the collection (irrespective of any paging options).  

        :return: The size of this CollectionWithPagingDocumentSummary.  
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CollectionWithPagingDocumentSummary.

        The total size of the collection (irrespective of any paging options).  

        :param size: The size of this CollectionWithPagingDocumentSummary.  
        :type: int
        """

        self._size = size

    @property
    def links(self):
        """Gets the links of this CollectionWithPagingDocumentSummary.  


        :return: The links of this CollectionWithPagingDocumentSummary.  
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CollectionWithPagingDocumentSummary.


        :param links: The links of this CollectionWithPagingDocumentSummary.  
        :type: Links
        """

        self._links = links

    @property
    def data(self):
        """Gets the data of this CollectionWithPagingDocumentSummary.  


        :return: The data of this CollectionWithPagingDocumentSummary.  
        :rtype: list[DocumentSummary]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CollectionWithPagingDocumentSummary.


        :param data: The data of this CollectionWithPagingDocumentSummary.  
        :type: list[DocumentSummary]
        """

        self._data = data

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
        if not isinstance(other, CollectionWithPagingDocumentSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
