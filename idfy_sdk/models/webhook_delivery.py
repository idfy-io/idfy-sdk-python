# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class WebhookDelivery(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'webhook_id': 'int',
        'event_id': 'str',
        'timestamp': 'datetime',
        'url': 'str',
        'elapsed_ms': 'int',
        'request_headers': 'object',
        'request_body': 'object',
        'response_headers': 'object',
        'response_body': 'object',
        'response_status_code': 'int',
        'response_message': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'webhook_id': 'webhookId',
        'event_id': 'eventId',
        'timestamp': 'timestamp',
        'url': 'url',
        'elapsed_ms': 'elapsedMs',
        'request_headers': 'requestHeaders',
        'request_body': 'requestBody',
        'response_headers': 'responseHeaders',
        'response_body': 'responseBody',
        'response_status_code': 'responseStatusCode',
        'response_message': 'responseMessage',
        'error_message': 'errorMessage'
    }

    def __init__(self, id=None, webhook_id=None, event_id=None, timestamp=None, url=None, elapsed_ms=None, request_headers=None, request_body=None, response_headers=None, response_body=None, response_status_code=None, response_message=None, error_message=None):  
        """WebhookDeliveryDto"""  

        self._id = None
        self._webhook_id = None
        self._event_id = None
        self._timestamp = None
        self._url = None
        self._elapsed_ms = None
        self._request_headers = None
        self._request_body = None
        self._response_headers = None
        self._response_body = None
        self._response_status_code = None
        self._response_message = None
        self._error_message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if webhook_id is not None:
            self.webhook_id = webhook_id
        if event_id is not None:
            self.event_id = event_id
        if timestamp is not None:
            self.timestamp = timestamp
        if url is not None:
            self.url = url
        if elapsed_ms is not None:
            self.elapsed_ms = elapsed_ms
        if request_headers is not None:
            self.request_headers = request_headers
        if request_body is not None:
            self.request_body = request_body
        if response_headers is not None:
            self.response_headers = response_headers
        if response_body is not None:
            self.response_body = response_body
        if response_status_code is not None:
            self.response_status_code = response_status_code
        if response_message is not None:
            self.response_message = response_message
        if error_message is not None:
            self.error_message = error_message

    @property
    def id(self):
        """Gets the id of this WebhookDeliveryDto.  

        The webhooks unique identifier.  

        :return: The id of this WebhookDeliveryDto.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookDeliveryDto.

        The webhooks unique identifier.  

        :param id: The id of this WebhookDeliveryDto.  
        :type: str
        """

        self._id = id

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookDeliveryDto.  


        :return: The webhook_id of this WebhookDeliveryDto.  
        :rtype: int
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookDeliveryDto.


        :param webhook_id: The webhook_id of this WebhookDeliveryDto.  
        :type: int
        """

        self._webhook_id = webhook_id

    @property
    def event_id(self):
        """Gets the event_id of this WebhookDeliveryDto.  


        :return: The event_id of this WebhookDeliveryDto.  
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this WebhookDeliveryDto.


        :param event_id: The event_id of this WebhookDeliveryDto.  
        :type: str
        """

        self._event_id = event_id

    @property
    def timestamp(self):
        """Gets the timestamp of this WebhookDeliveryDto.  


        :return: The timestamp of this WebhookDeliveryDto.  
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WebhookDeliveryDto.


        :param timestamp: The timestamp of this WebhookDeliveryDto.  
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def url(self):
        """Gets the url of this WebhookDeliveryDto.  


        :return: The url of this WebhookDeliveryDto.  
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookDeliveryDto.


        :param url: The url of this WebhookDeliveryDto.  
        :type: str
        """

        self._url = url

    @property
    def elapsed_ms(self):
        """Gets the elapsed_ms of this WebhookDeliveryDto.  


        :return: The elapsed_ms of this WebhookDeliveryDto.  
        :rtype: int
        """
        return self._elapsed_ms

    @elapsed_ms.setter
    def elapsed_ms(self, elapsed_ms):
        """Sets the elapsed_ms of this WebhookDeliveryDto.


        :param elapsed_ms: The elapsed_ms of this WebhookDeliveryDto.  
        :type: int
        """

        self._elapsed_ms = elapsed_ms

    @property
    def request_headers(self):
        """Gets the request_headers of this WebhookDeliveryDto.  


        :return: The request_headers of this WebhookDeliveryDto.  
        :rtype: object
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """Sets the request_headers of this WebhookDeliveryDto.


        :param request_headers: The request_headers of this WebhookDeliveryDto.  
        :type: object
        """

        self._request_headers = request_headers

    @property
    def request_body(self):
        """Gets the request_body of this WebhookDeliveryDto.  


        :return: The request_body of this WebhookDeliveryDto.  
        :rtype: object
        """
        return self._request_body

    @request_body.setter
    def request_body(self, request_body):
        """Sets the request_body of this WebhookDeliveryDto.


        :param request_body: The request_body of this WebhookDeliveryDto.  
        :type: object
        """

        self._request_body = request_body

    @property
    def response_headers(self):
        """Gets the response_headers of this WebhookDeliveryDto.  


        :return: The response_headers of this WebhookDeliveryDto.  
        :rtype: object
        """
        return self._response_headers

    @response_headers.setter
    def response_headers(self, response_headers):
        """Sets the response_headers of this WebhookDeliveryDto.


        :param response_headers: The response_headers of this WebhookDeliveryDto.  
        :type: object
        """

        self._response_headers = response_headers

    @property
    def response_body(self):
        """Gets the response_body of this WebhookDeliveryDto.  


        :return: The response_body of this WebhookDeliveryDto.  
        :rtype: object
        """
        return self._response_body

    @response_body.setter
    def response_body(self, response_body):
        """Sets the response_body of this WebhookDeliveryDto.


        :param response_body: The response_body of this WebhookDeliveryDto.  
        :type: object
        """

        self._response_body = response_body

    @property
    def response_status_code(self):
        """Gets the response_status_code of this WebhookDeliveryDto.  


        :return: The response_status_code of this WebhookDeliveryDto.  
        :rtype: int
        """
        return self._response_status_code

    @response_status_code.setter
    def response_status_code(self, response_status_code):
        """Sets the response_status_code of this WebhookDeliveryDto.


        :param response_status_code: The response_status_code of this WebhookDeliveryDto.  
        :type: int
        """

        self._response_status_code = response_status_code

    @property
    def response_message(self):
        """Gets the response_message of this WebhookDeliveryDto.  


        :return: The response_message of this WebhookDeliveryDto.  
        :rtype: str
        """
        return self._response_message

    @response_message.setter
    def response_message(self, response_message):
        """Sets the response_message of this WebhookDeliveryDto.


        :param response_message: The response_message of this WebhookDeliveryDto.  
        :type: str
        """

        self._response_message = response_message

    @property
    def error_message(self):
        """Gets the error_message of this WebhookDeliveryDto.  


        :return: The error_message of this WebhookDeliveryDto.  
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this WebhookDeliveryDto.


        :param error_message: The error_message of this WebhookDeliveryDto.  
        :type: str
        """

        self._error_message = error_message

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
        if not isinstance(other, WebhookDelivery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
