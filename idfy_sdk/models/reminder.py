# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.email import Email  
from idfy_sdk.models.sms import SMS  


class Reminder(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'chron_schedule': 'str',
        'max_reminders': 'int',
        'email': 'list[Email]',
        'sms': 'list[SMS]'
    }

    attribute_map = {
        'chron_schedule': 'chronSchedule',
        'max_reminders': 'maxReminders',
        'email': 'email',
        'sms': 'sms'
    }

    def __init__(self, chron_schedule=None, max_reminders=None, email=None, sms=None):  
        """Reminder"""  

        self._chron_schedule = None
        self._max_reminders = None
        self._email = None
        self._sms = None
        self.discriminator = None

        self.chron_schedule = chron_schedule
        if max_reminders is not None:
            self.max_reminders = max_reminders
        if email is not None:
            self.email = email
        if sms is not None:
            self.sms = sms

    @property
    def chron_schedule(self):
        """Gets the chron_schedule of this Reminder.  

        Defines a chron expression that control the interval of the reminders (Use UTC time). We use Quartz cron expressions, read more about it here: http://www.quartz-scheduler.org/documentation/quartz-2.x/tutorials/crontrigger.html.  

        :return: The chron_schedule of this Reminder.  
        :rtype: str
        """
        return self._chron_schedule

    @chron_schedule.setter
    def chron_schedule(self, chron_schedule):
        """Sets the chron_schedule of this Reminder.

        Defines a chron expression that control the interval of the reminders (Use UTC time). We use Quartz cron expressions, read more about it here: http://www.quartz-scheduler.org/documentation/quartz-2.x/tutorials/crontrigger.html.  

        :param chron_schedule: The chron_schedule of this Reminder.  
        :type: str
        """
        if chron_schedule is None:
            raise ValueError("Invalid value for `chron_schedule`, must not be `None`")  

        self._chron_schedule = chron_schedule

    @property
    def max_reminders(self):
        """Gets the max_reminders of this Reminder.  

        The maximum number of reminders to be sent for each signer.  

        :return: The max_reminders of this Reminder.  
        :rtype: int
        """
        return self._max_reminders

    @max_reminders.setter
    def max_reminders(self, max_reminders):
        """Sets the max_reminders of this Reminder.

        The maximum number of reminders to be sent for each signer.  

        :param max_reminders: The max_reminders of this Reminder.  
        :type: int
        """

        self._max_reminders = max_reminders

    @property
    def email(self):
        """Gets the email of this Reminder.  

        A list of custom email texts to use for the notification. Default texts will be used if not specified.  

        :return: The email of this Reminder.  
        :rtype: list[Email]
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Reminder.

        A list of custom email texts to use for the notification. Default texts will be used if not specified.  

        :param email: The email of this Reminder.  
        :type: list[Email]
        """

        self._email = email

    @property
    def sms(self):
        """Gets the sms of this Reminder.  

        A list of custom SMS texts to use for the notification. Default texts will be used if not specified.  

        :return: The sms of this Reminder.  
        :rtype: list[SMS]
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this Reminder.

        A list of custom SMS texts to use for the notification. Default texts will be used if not specified.  

        :param sms: The sms of this Reminder.  
        :type: list[SMS]
        """

        self._sms = sms

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
        if not isinstance(other, Reminder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
