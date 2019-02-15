# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.advanced import Advanced  
from idfy_sdk.models.contact_details import ContactDetails  
from idfy_sdk.models.notification import Notification  


class UpdateDocumentRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'title': 'str',
        'description': 'str',
        'notification': 'Notification',
        'contact_details': 'ContactDetails',
        'advanced': 'Advanced'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'notification': 'notification',
        'contact_details': 'contactDetails',
        'advanced': 'advanced'
    }

    def __init__(self, title=None, description=None, notification=None, contact_details=None, advanced=None):  
        """UpdateDocumentRequest"""  

        self._title = None
        self._description = None
        self._notification = None
        self._contact_details = None
        self._advanced = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if notification is not None:
            self.notification = notification
        if contact_details is not None:
            self.contact_details = contact_details
        if advanced is not None:
            self.advanced = advanced

    @property
    def title(self):
        """Gets the title of this UpdateDocumentRequest.  


        :return: The title of this UpdateDocumentRequest.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdateDocumentRequest.


        :param title: The title of this UpdateDocumentRequest.  
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this UpdateDocumentRequest.  


        :return: The description of this UpdateDocumentRequest.  
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDocumentRequest.


        :param description: The description of this UpdateDocumentRequest.  
        :type: str
        """

        self._description = description

    @property
    def notification(self):
        """Gets the notification of this UpdateDocumentRequest.  


        :return: The notification of this UpdateDocumentRequest.  
        :rtype: Notification
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this UpdateDocumentRequest.


        :param notification: The notification of this UpdateDocumentRequest.  
        :type: Notification
        """

        self._notification = notification

    @property
    def contact_details(self):
        """Gets the contact_details of this UpdateDocumentRequest.  


        :return: The contact_details of this UpdateDocumentRequest.  
        :rtype: ContactDetails
        """
        return self._contact_details

    @contact_details.setter
    def contact_details(self, contact_details):
        """Sets the contact_details of this UpdateDocumentRequest.


        :param contact_details: The contact_details of this UpdateDocumentRequest.  
        :type: ContactDetails
        """

        self._contact_details = contact_details

    @property
    def advanced(self):
        """Gets the advanced of this UpdateDocumentRequest.  


        :return: The advanced of this UpdateDocumentRequest.  
        :rtype: Advanced
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this UpdateDocumentRequest.


        :param advanced: The advanced of this UpdateDocumentRequest.  
        :type: Advanced
        """

        self._advanced = advanced

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
        if not isinstance(other, UpdateDocumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
