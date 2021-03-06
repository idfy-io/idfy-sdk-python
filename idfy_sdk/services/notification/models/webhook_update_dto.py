# coding: utf-8

"""
    Idfy Notification API

    This endpoint lets you manage events that are raised when something happens in your account

"""


import pprint
import re
from typing import List, Dict
from datetime import datetime as datetime


from idfy_sdk.services.notification.models.webhook_config import WebhookConfig

class WebhookUpdateDto(object):
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
        'name': str,
        'active': bool,
        'events': List[str],
        'config': WebhookConfig,
        'tags': List[str]
    }

    attribute_map = {
        'name': 'name',
        'active': 'active',
        'events': 'events',
        'config': 'config',
        'tags': 'tags'
    }

    def __init__(self, name=None, active=None, events=None, config=None, tags=None):

        self._name = None
        self._active = None
        self._events = None
        self._config = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if active is not None:
            self.active = active
        if events is not None:
            self.events = events
        if config is not None:
            self.config = config
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this WebhookUpdateDto.

        Display name of the webhook.

        :return: The name of this WebhookUpdateDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookUpdateDto.

        Display name of the webhook.

        :param name: The name of this WebhookUpdateDto.
        :type: str
        """

        self._name = name

    @property
    def active(self):
        """Gets the active of this WebhookUpdateDto.

        Determines whether the webhook is active or not.

        :return: The active of this WebhookUpdateDto.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this WebhookUpdateDto.

        Determines whether the webhook is active or not.

        :param active: The active of this WebhookUpdateDto.
        :type: bool
        """

        self._active = active

    @property
    def events(self):
        """Gets the events of this WebhookUpdateDto.

        A list of events that the webhook triggers for.

        :return: The events of this WebhookUpdateDto.
        :rtype: List[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this WebhookUpdateDto.

        A list of events that the webhook triggers for.

        :param events: The events of this WebhookUpdateDto.
        :type: List[str]
        """

        self._events = events

    @property
    def config(self):
        """Gets the config of this WebhookUpdateDto.


        :return: The config of this WebhookUpdateDto.
        :rtype: WebhookConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this WebhookUpdateDto.


        :param config: The config of this WebhookUpdateDto.
        :type: WebhookConfig
        """

        self._config = config

    @property
    def tags(self):
        """Gets the tags of this WebhookUpdateDto.

        An optional list of event tags that the webhook triggers for.

        :return: The tags of this WebhookUpdateDto.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this WebhookUpdateDto.

        An optional list of event tags that the webhook triggers for.

        :param tags: The tags of this WebhookUpdateDto.
        :type: List[str]
        """

        self._tags = tags

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
        if not isinstance(other, WebhookUpdateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
