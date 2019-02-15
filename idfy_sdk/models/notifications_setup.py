# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class NotificationsSetup(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request': 'str',
        'reminder': 'str',
        'signature_receipt': 'str',
        'final_receipt': 'str',
        'canceled': 'str',
        'expired': 'str'
    }

    attribute_map = {
        'request': 'request',
        'reminder': 'reminder',
        'signature_receipt': 'signatureReceipt',
        'final_receipt': 'finalReceipt',
        'canceled': 'canceled',
        'expired': 'expired'
    }

    def __init__(self, request=None, reminder=None, signature_receipt=None, final_receipt=None, canceled=None, expired=None):  
        """NotificationsSetup"""  

        self._request = None
        self._reminder = None
        self._signature_receipt = None
        self._final_receipt = None
        self._canceled = None
        self._expired = None
        self.discriminator = None

        if request is not None:
            self.request = request
        if reminder is not None:
            self.reminder = reminder
        if signature_receipt is not None:
            self.signature_receipt = signature_receipt
        if final_receipt is not None:
            self.final_receipt = final_receipt
        if canceled is not None:
            self.canceled = canceled
        if expired is not None:
            self.expired = expired

    @property
    def request(self):
        """Gets the request of this NotificationsSetup.  


        :return: The request of this NotificationsSetup.  
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this NotificationsSetup.


        :param request: The request of this NotificationsSetup.  
        :type: str
        """
        allowed_values = ["off", "sendSms", "sendEmail", "sendBoth"]  
        if request not in allowed_values:
            raise ValueError(
                "Invalid value for `request` ({0}), must be one of {1}"  
                .format(request, allowed_values)
            )

        self._request = request

    @property
    def reminder(self):
        """Gets the reminder of this NotificationsSetup.  


        :return: The reminder of this NotificationsSetup.  
        :rtype: str
        """
        return self._reminder

    @reminder.setter
    def reminder(self, reminder):
        """Sets the reminder of this NotificationsSetup.


        :param reminder: The reminder of this NotificationsSetup.  
        :type: str
        """
        allowed_values = ["off", "sendSms", "sendEmail", "sendBoth"]  
        if reminder not in allowed_values:
            raise ValueError(
                "Invalid value for `reminder` ({0}), must be one of {1}"  
                .format(reminder, allowed_values)
            )

        self._reminder = reminder

    @property
    def signature_receipt(self):
        """Gets the signature_receipt of this NotificationsSetup.  


        :return: The signature_receipt of this NotificationsSetup.  
        :rtype: str
        """
        return self._signature_receipt

    @signature_receipt.setter
    def signature_receipt(self, signature_receipt):
        """Sets the signature_receipt of this NotificationsSetup.


        :param signature_receipt: The signature_receipt of this NotificationsSetup.  
        :type: str
        """
        allowed_values = ["off", "sendSms", "sendEmail", "sendBoth"]  
        if signature_receipt not in allowed_values:
            raise ValueError(
                "Invalid value for `signature_receipt` ({0}), must be one of {1}"  
                .format(signature_receipt, allowed_values)
            )

        self._signature_receipt = signature_receipt

    @property
    def final_receipt(self):
        """Gets the final_receipt of this NotificationsSetup.  


        :return: The final_receipt of this NotificationsSetup.  
        :rtype: str
        """
        return self._final_receipt

    @final_receipt.setter
    def final_receipt(self, final_receipt):
        """Sets the final_receipt of this NotificationsSetup.


        :param final_receipt: The final_receipt of this NotificationsSetup.  
        :type: str
        """
        allowed_values = ["off", "sendSms", "sendEmail", "sendBoth"]  
        if final_receipt not in allowed_values:
            raise ValueError(
                "Invalid value for `final_receipt` ({0}), must be one of {1}"  
                .format(final_receipt, allowed_values)
            )

        self._final_receipt = final_receipt

    @property
    def canceled(self):
        """Gets the canceled of this NotificationsSetup.  


        :return: The canceled of this NotificationsSetup.  
        :rtype: str
        """
        return self._canceled

    @canceled.setter
    def canceled(self, canceled):
        """Sets the canceled of this NotificationsSetup.


        :param canceled: The canceled of this NotificationsSetup.  
        :type: str
        """
        allowed_values = ["off", "sendSms", "sendEmail", "sendBoth"]  
        if canceled not in allowed_values:
            raise ValueError(
                "Invalid value for `canceled` ({0}), must be one of {1}"  
                .format(canceled, allowed_values)
            )

        self._canceled = canceled

    @property
    def expired(self):
        """Gets the expired of this NotificationsSetup.  


        :return: The expired of this NotificationsSetup.  
        :rtype: str
        """
        return self._expired

    @expired.setter
    def expired(self, expired):
        """Sets the expired of this NotificationsSetup.


        :param expired: The expired of this NotificationsSetup.  
        :type: str
        """
        allowed_values = ["off", "sendSms", "sendEmail", "sendBoth"]  
        if expired not in allowed_values:
            raise ValueError(
                "Invalid value for `expired` ({0}), must be one of {1}"  
                .format(expired, allowed_values)
            )

        self._expired = expired

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
        if not isinstance(other, NotificationsSetup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
