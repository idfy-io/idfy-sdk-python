# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class CreateIdentificationResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'url': 'Url',
        'request_id': 'RequestId'
    }

    def __init__(self, url=None, request_id=None):  
        """CreateIdentificationResponse"""  

        self._url = None
        self._request_id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if request_id is not None:
            self.request_id = request_id

    @property
    def url(self):
        """Gets the url of this CreateIdentificationResponse.  

        The url to use as src for iframe or to redirect the user to  

        :return: The url of this CreateIdentificationResponse.  
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateIdentificationResponse.

        The url to use as src for iframe or to redirect the user to  

        :param url: The url of this CreateIdentificationResponse.  
        :type: str
        """

        self._url = url

    @property
    def request_id(self):
        """Gets the request_id of this CreateIdentificationResponse.  

        Requestid used to get the reponse form server afterwards  

        :return: The request_id of this CreateIdentificationResponse.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateIdentificationResponse.

        Requestid used to get the reponse form server afterwards  

        :param request_id: The request_id of this CreateIdentificationResponse.  
        :type: str
        """

        self._request_id = request_id

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
        if not isinstance(other, CreateIdentificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
