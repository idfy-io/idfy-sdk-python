# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.lei_record import LeiRecord  


class SearchResult(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'next_url': 'str',
        'start': 'int',
        'num_found': 'int',
        'rows': 'int',
        'results': 'list[LeiRecord]'
    }

    attribute_map = {
        'next_url': 'next_url',
        'start': 'Start',
        'num_found': 'NumFound',
        'rows': 'Rows',
        'results': 'Results'
    }

    def __init__(self, next_url=None, start=None, num_found=None, rows=None, results=None):  
        """SearchResult"""  

        self._next_url = None
        self._start = None
        self._num_found = None
        self._rows = None
        self._results = None
        self.discriminator = None

        if next_url is not None:
            self.next_url = next_url
        if start is not None:
            self.start = start
        if num_found is not None:
            self.num_found = num_found
        if rows is not None:
            self.rows = rows
        if results is not None:
            self.results = results

    @property
    def next_url(self):
        """Gets the next_url of this SearchResult.  


        :return: The next_url of this SearchResult.  
        :rtype: str
        """
        return self._next_url

    @next_url.setter
    def next_url(self, next_url):
        """Sets the next_url of this SearchResult.


        :param next_url: The next_url of this SearchResult.  
        :type: str
        """

        self._next_url = next_url

    @property
    def start(self):
        """Gets the start of this SearchResult.  


        :return: The start of this SearchResult.  
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SearchResult.


        :param start: The start of this SearchResult.  
        :type: int
        """

        self._start = start

    @property
    def num_found(self):
        """Gets the num_found of this SearchResult.  


        :return: The num_found of this SearchResult.  
        :rtype: int
        """
        return self._num_found

    @num_found.setter
    def num_found(self, num_found):
        """Sets the num_found of this SearchResult.


        :param num_found: The num_found of this SearchResult.  
        :type: int
        """

        self._num_found = num_found

    @property
    def rows(self):
        """Gets the rows of this SearchResult.  


        :return: The rows of this SearchResult.  
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this SearchResult.


        :param rows: The rows of this SearchResult.  
        :type: int
        """

        self._rows = rows

    @property
    def results(self):
        """Gets the results of this SearchResult.  


        :return: The results of this SearchResult.  
        :rtype: list[LeiRecord]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this SearchResult.


        :param results: The results of this SearchResult.  
        :type: list[LeiRecord]
        """

        self._results = results

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
        if not isinstance(other, SearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
