# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Link(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'href': 'str',
        'rel': 'str',
        'content_type': 'str',
        'error': 'str',
        'resource_status': 'str'
    }

    attribute_map = {
        'href': 'href',
        'rel': 'rel',
        'content_type': 'contentType',
        'error': 'error',
        'resource_status': 'resourceStatus'
    }

    def __init__(self, href=None, rel=None, content_type=None, error=None, resource_status=None):  
        """Link"""  

        self._href = None
        self._rel = None
        self._content_type = None
        self._error = None
        self._resource_status = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if rel is not None:
            self.rel = rel
        if content_type is not None:
            self.content_type = content_type
        if error is not None:
            self.error = error
        if resource_status is not None:
            self.resource_status = resource_status

    @property
    def href(self):
        """Gets the href of this Link.  


        :return: The href of this Link.  
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Link.


        :param href: The href of this Link.  
        :type: str
        """

        self._href = href

    @property
    def rel(self):
        """Gets the rel of this Link.  


        :return: The rel of this Link.  
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this Link.


        :param rel: The rel of this Link.  
        :type: str
        """

        self._rel = rel

    @property
    def content_type(self):
        """Gets the content_type of this Link.  


        :return: The content_type of this Link.  
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Link.


        :param content_type: The content_type of this Link.  
        :type: str
        """

        self._content_type = content_type

    @property
    def error(self):
        """Gets the error of this Link.  


        :return: The error of this Link.  
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Link.


        :param error: The error of this Link.  
        :type: str
        """

        self._error = error

    @property
    def resource_status(self):
        """Gets the resource_status of this Link.  


        :return: The resource_status of this Link.  
        :rtype: str
        """
        return self._resource_status

    @resource_status.setter
    def resource_status(self, resource_status):
        """Sets the resource_status of this Link.


        :param resource_status: The resource_status of this Link.  
        :type: str
        """
        allowed_values = ["Unknown", "NotReady", "Success", "signatureError", "NotFound", "BadInput", "ServiceUnavailable", "Unauthorized", "TimeOut"]  
        if resource_status not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_status` ({0}), must be one of {1}"  
                .format(resource_status, allowed_values)
            )

        self._resource_status = resource_status

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
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
