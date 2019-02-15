# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.canceled_receipt import CanceledReceipt  
from idfy_sdk.models.expired_receipt import ExpiredReceipt  
from idfy_sdk.models.final_receipt import FinalReceipt  
from idfy_sdk.models.reminder import Reminder  
from idfy_sdk.models.sign_request import SignRequest  
from idfy_sdk.models.signature_receipt import SignatureReceipt  


class Notification(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sign_request': 'SignRequest',
        'reminder': 'Reminder',
        'signature_receipt': 'SignatureReceipt',
        'final_receipt': 'FinalReceipt',
        'canceled_receipt': 'CanceledReceipt',
        'expired_receipt': 'ExpiredReceipt'
    }

    attribute_map = {
        'sign_request': 'signRequest',
        'reminder': 'reminder',
        'signature_receipt': 'signatureReceipt',
        'final_receipt': 'finalReceipt',
        'canceled_receipt': 'canceledReceipt',
        'expired_receipt': 'expiredReceipt'
    }

    def __init__(self, sign_request=None, reminder=None, signature_receipt=None, final_receipt=None, canceled_receipt=None, expired_receipt=None):  
        """Notification"""  

        self._sign_request = None
        self._reminder = None
        self._signature_receipt = None
        self._final_receipt = None
        self._canceled_receipt = None
        self._expired_receipt = None
        self.discriminator = None

        if sign_request is not None:
            self.sign_request = sign_request
        if reminder is not None:
            self.reminder = reminder
        if signature_receipt is not None:
            self.signature_receipt = signature_receipt
        if final_receipt is not None:
            self.final_receipt = final_receipt
        if canceled_receipt is not None:
            self.canceled_receipt = canceled_receipt
        if expired_receipt is not None:
            self.expired_receipt = expired_receipt

    @property
    def sign_request(self):
        """Gets the sign_request of this Notification.  


        :return: The sign_request of this Notification.  
        :rtype: SignRequest
        """
        return self._sign_request

    @sign_request.setter
    def sign_request(self, sign_request):
        """Sets the sign_request of this Notification.


        :param sign_request: The sign_request of this Notification.  
        :type: SignRequest
        """

        self._sign_request = sign_request

    @property
    def reminder(self):
        """Gets the reminder of this Notification.  


        :return: The reminder of this Notification.  
        :rtype: Reminder
        """
        return self._reminder

    @reminder.setter
    def reminder(self, reminder):
        """Sets the reminder of this Notification.


        :param reminder: The reminder of this Notification.  
        :type: Reminder
        """

        self._reminder = reminder

    @property
    def signature_receipt(self):
        """Gets the signature_receipt of this Notification.  


        :return: The signature_receipt of this Notification.  
        :rtype: SignatureReceipt
        """
        return self._signature_receipt

    @signature_receipt.setter
    def signature_receipt(self, signature_receipt):
        """Sets the signature_receipt of this Notification.


        :param signature_receipt: The signature_receipt of this Notification.  
        :type: SignatureReceipt
        """

        self._signature_receipt = signature_receipt

    @property
    def final_receipt(self):
        """Gets the final_receipt of this Notification.  


        :return: The final_receipt of this Notification.  
        :rtype: FinalReceipt
        """
        return self._final_receipt

    @final_receipt.setter
    def final_receipt(self, final_receipt):
        """Sets the final_receipt of this Notification.


        :param final_receipt: The final_receipt of this Notification.  
        :type: FinalReceipt
        """

        self._final_receipt = final_receipt

    @property
    def canceled_receipt(self):
        """Gets the canceled_receipt of this Notification.  


        :return: The canceled_receipt of this Notification.  
        :rtype: CanceledReceipt
        """
        return self._canceled_receipt

    @canceled_receipt.setter
    def canceled_receipt(self, canceled_receipt):
        """Sets the canceled_receipt of this Notification.


        :param canceled_receipt: The canceled_receipt of this Notification.  
        :type: CanceledReceipt
        """

        self._canceled_receipt = canceled_receipt

    @property
    def expired_receipt(self):
        """Gets the expired_receipt of this Notification.  


        :return: The expired_receipt of this Notification.  
        :rtype: ExpiredReceipt
        """
        return self._expired_receipt

    @expired_receipt.setter
    def expired_receipt(self, expired_receipt):
        """Sets the expired_receipt of this Notification.


        :param expired_receipt: The expired_receipt of this Notification.  
        :type: ExpiredReceipt
        """

        self._expired_receipt = expired_receipt

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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
