# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class WebhookCreateConfig(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        'secret': 'str',
        'delivery_logging': 'str'
    }

    attribute_map = {
        'url': 'url',
        'secret': 'secret',
        'delivery_logging': 'deliveryLogging'
    }

    def __init__(self, url=None, secret=None, delivery_logging=None):  
        """WebhookCreateConfig"""  

        self._url = None
        self._secret = None
        self._delivery_logging = None
        self.discriminator = None

        self.url = url
        if secret is not None:
            self.secret = secret
        if delivery_logging is not None:
            self.delivery_logging = delivery_logging

    @property
    def url(self):
        """Gets the url of this WebhookCreateConfig.  

        The URL to which the payloads will be delivered.  

        :return: The url of this WebhookCreateConfig.  
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookCreateConfig.

        The URL to which the payloads will be delivered.  

        :param url: The url of this WebhookCreateConfig.  
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  

        self._url = url

    @property
    def secret(self):
        """Gets the secret of this WebhookCreateConfig.  

        Optional secret used to compute a HMAC hex digest of the payload,   which is passed with the HTTP request as an ``X-Idfy-Signature`` header.  

        :return: The secret of this WebhookCreateConfig.  
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this WebhookCreateConfig.

        Optional secret used to compute a HMAC hex digest of the payload,   which is passed with the HTTP request as an ``X-Idfy-Signature`` header.  

        :param secret: The secret of this WebhookCreateConfig.  
        :type: str
        """

        self._secret = secret

    @property
    def delivery_logging(self):
        """Gets the delivery_logging of this WebhookCreateConfig.  

        Determines whether to log webhook delivery attempts. Defaults to `never`.  

        :return: The delivery_logging of this WebhookCreateConfig.  
        :rtype: str
        """
        return self._delivery_logging

    @delivery_logging.setter
    def delivery_logging(self, delivery_logging):
        """Sets the delivery_logging of this WebhookCreateConfig.

        Determines whether to log webhook delivery attempts. Defaults to `never`.  

        :param delivery_logging: The delivery_logging of this WebhookCreateConfig.  
        :type: str
        """
        allowed_values = ["never", "failed", "always"]  
        if delivery_logging not in allowed_values:
            raise ValueError(
                "Invalid value for `delivery_logging` ({0}), must be one of {1}"  
                .format(delivery_logging, allowed_values)
            )

        self._delivery_logging = delivery_logging

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
        if not isinstance(other, WebhookCreateConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
