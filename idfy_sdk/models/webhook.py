# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.webhook_config import WebhookConfig  
from idfy_sdk.models.webhook_response import WebhookResponse  


class Webhook(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'active': 'bool',
        'events': 'list[str]',
        'config': 'WebhookConfig',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'last_response': 'WebhookResponse',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'active': 'active',
        'events': 'events',
        'config': 'config',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'last_response': 'lastResponse',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, active=None, events=None, config=None, created_at=None, updated_at=None, last_response=None, tags=None):  
        """WebhookDto"""  

        self._id = None
        self._name = None
        self._active = None
        self._events = None
        self._config = None
        self._created_at = None
        self._updated_at = None
        self._last_response = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if active is not None:
            self.active = active
        if events is not None:
            self.events = events
        if config is not None:
            self.config = config
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if last_response is not None:
            self.last_response = last_response
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this WebhookDto.  

        The webhooks unique identifier.  

        :return: The id of this WebhookDto.  
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookDto.

        The webhooks unique identifier.  

        :param id: The id of this WebhookDto.  
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this WebhookDto.  

        Display name of the webhook.  

        :return: The name of this WebhookDto.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookDto.

        Display name of the webhook.  

        :param name: The name of this WebhookDto.  
        :type: str
        """

        self._name = name

    @property
    def active(self):
        """Gets the active of this WebhookDto.  

        Determines if the webhook is active.  

        :return: The active of this WebhookDto.  
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this WebhookDto.

        Determines if the webhook is active.  

        :param active: The active of this WebhookDto.  
        :type: bool
        """

        self._active = active

    @property
    def events(self):
        """Gets the events of this WebhookDto.  

        A list of events that the webhook triggers for.  

        :return: The events of this WebhookDto.  
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this WebhookDto.

        A list of events that the webhook triggers for.  

        :param events: The events of this WebhookDto.  
        :type: list[str]
        """

        self._events = events

    @property
    def config(self):
        """Gets the config of this WebhookDto.  


        :return: The config of this WebhookDto.  
        :rtype: WebhookConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this WebhookDto.


        :param config: The config of this WebhookDto.  
        :type: WebhookConfig
        """

        self._config = config

    @property
    def created_at(self):
        """Gets the created_at of this WebhookDto.  

        Time at which the webhook was created.  

        :return: The created_at of this WebhookDto.  
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebhookDto.

        Time at which the webhook was created.  

        :param created_at: The created_at of this WebhookDto.  
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this WebhookDto.  

        Time at which the webhook was last updated.  

        :return: The updated_at of this WebhookDto.  
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this WebhookDto.

        Time at which the webhook was last updated.  

        :param updated_at: The updated_at of this WebhookDto.  
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def last_response(self):
        """Gets the last_response of this WebhookDto.  


        :return: The last_response of this WebhookDto.  
        :rtype: WebhookResponse
        """
        return self._last_response

    @last_response.setter
    def last_response(self, last_response):
        """Sets the last_response of this WebhookDto.


        :param last_response: The last_response of this WebhookDto.  
        :type: WebhookResponse
        """

        self._last_response = last_response

    @property
    def tags(self):
        """Gets the tags of this WebhookDto.  

        A list of event tags that the webhook triggers for.  

        :return: The tags of this WebhookDto.  
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WebhookDto.

        A list of event tags that the webhook triggers for.  

        :param tags: The tags of this WebhookDto.  
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
