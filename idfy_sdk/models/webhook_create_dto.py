# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.webhook_create_config import WebhookCreateConfig  


class WebhookCreateDto(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'active': 'bool',
        'events': 'list[str]',
        'config': 'WebhookCreateConfig',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'active': 'active',
        'events': 'events',
        'config': 'config',
        'tags': 'tags'
    }

    def __init__(self, name=None, active=None, events=None, config=None, tags=None):  
        """WebhookCreateDto"""  

        self._name = None
        self._active = None
        self._events = None
        self._config = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.active = active
        self.events = events
        self.config = config
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this WebhookCreateDto.  

        Display name of the webhook.  

        :return: The name of this WebhookCreateDto.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookCreateDto.

        Display name of the webhook.  

        :param name: The name of this WebhookCreateDto.  
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  

        self._name = name

    @property
    def active(self):
        """Gets the active of this WebhookCreateDto.  

        Determines whether the webhook is active or not.  

        :return: The active of this WebhookCreateDto.  
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this WebhookCreateDto.

        Determines whether the webhook is active or not.  

        :param active: The active of this WebhookCreateDto.  
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  

        self._active = active

    @property
    def events(self):
        """Gets the events of this WebhookCreateDto.  

        A list of events that the webhook triggers for.  

        :return: The events of this WebhookCreateDto.  
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this WebhookCreateDto.

        A list of events that the webhook triggers for.  

        :param events: The events of this WebhookCreateDto.  
        :type: list[str]
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")  

        self._events = events

    @property
    def config(self):
        """Gets the config of this WebhookCreateDto.  


        :return: The config of this WebhookCreateDto.  
        :rtype: WebhookCreateConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this WebhookCreateDto.


        :param config: The config of this WebhookCreateDto.  
        :type: WebhookCreateConfig
        """
        if config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  

        self._config = config

    @property
    def tags(self):
        """Gets the tags of this WebhookCreateDto.  

        An optional list of event tags that the webhook triggers for.  

        :return: The tags of this WebhookCreateDto.  
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WebhookCreateDto.

        An optional list of event tags that the webhook triggers for.  

        :param tags: The tags of this WebhookCreateDto.  
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
        if not isinstance(other, WebhookCreateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
