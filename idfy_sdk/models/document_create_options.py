# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.advanced import Advanced  
from idfy_sdk.models.contact_details import ContactDetails  
from idfy_sdk.models.data_to_sign import DataToSign  
from idfy_sdk.models.notification import Notification  
from idfy_sdk.models.signer_wrapper import SignerWrapper  


class DocumentCreateOptions(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'signers': 'list[SignerWrapper]',
        'title': 'str',
        'description': 'str',
        'external_id': 'str',
        'data_to_sign': 'DataToSign',
        'contact_details': 'ContactDetails',
        'notification': 'Notification',
        'advanced': 'Advanced'
    }

    attribute_map = {
        'signers': 'signers',
        'title': 'title',
        'description': 'description',
        'external_id': 'externalId',
        'data_to_sign': 'dataToSign',
        'contact_details': 'contactDetails',
        'notification': 'notification',
        'advanced': 'advanced'
    }

    def __init__(self, signers=None, title=None, description=None, external_id=None, data_to_sign=None, contact_details=None, notification=None, advanced=None):  
        """CreateDocumentRequestWrapper"""  

        self._signers = None
        self._title = None
        self._description = None
        self._external_id = None
        self._data_to_sign = None
        self._contact_details = None
        self._notification = None
        self._advanced = None
        self.discriminator = None

        self.signers = signers
        self.title = title
        if description is not None:
            self.description = description
        self.external_id = external_id
        self.data_to_sign = data_to_sign
        self.contact_details = contact_details
        if notification is not None:
            self.notification = notification
        if advanced is not None:
            self.advanced = advanced

    @property
    def signers(self):
        """Gets the signers of this CreateDocumentRequestWrapper.  


        :return: The signers of this CreateDocumentRequestWrapper.  
        :rtype: list[SignerWrapper]
        """
        return self._signers

    @signers.setter
    def signers(self, signers):
        """Sets the signers of this CreateDocumentRequestWrapper.


        :param signers: The signers of this CreateDocumentRequestWrapper.  
        :type: list[SignerWrapper]
        """
        if signers is None:
            raise ValueError("Invalid value for `signers`, must not be `None`")  

        self._signers = signers

    @property
    def title(self):
        """Gets the title of this CreateDocumentRequestWrapper.  

        The title of the document which will be presented to the user.  

        :return: The title of this CreateDocumentRequestWrapper.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateDocumentRequestWrapper.

        The title of the document which will be presented to the user.  

        :param title: The title of this CreateDocumentRequestWrapper.  
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  
        if title is not None and len(title) > 300:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `300`")  
        if title is not None and len(title) < 0:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `0`")  

        self._title = title

    @property
    def description(self):
        """Gets the description of this CreateDocumentRequestWrapper.  

        The description of the document.  

        :return: The description of this CreateDocumentRequestWrapper.  
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDocumentRequestWrapper.

        The description of the document.  

        :param description: The description of this CreateDocumentRequestWrapper.  
        :type: str
        """

        self._description = description

    @property
    def external_id(self):
        """Gets the external_id of this CreateDocumentRequestWrapper.  

        Your reference to this document.  

        :return: The external_id of this CreateDocumentRequestWrapper.  
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CreateDocumentRequestWrapper.

        Your reference to this document.  

        :param external_id: The external_id of this CreateDocumentRequestWrapper.  
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")  
        if external_id is not None and len(external_id) > 255:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `255`")  
        if external_id is not None and len(external_id) < 4:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `4`")  

        self._external_id = external_id

    @property
    def data_to_sign(self):
        """Gets the data_to_sign of this CreateDocumentRequestWrapper.  


        :return: The data_to_sign of this CreateDocumentRequestWrapper.  
        :rtype: DataToSign
        """
        return self._data_to_sign

    @data_to_sign.setter
    def data_to_sign(self, data_to_sign):
        """Sets the data_to_sign of this CreateDocumentRequestWrapper.


        :param data_to_sign: The data_to_sign of this CreateDocumentRequestWrapper.  
        :type: DataToSign
        """
        if data_to_sign is None:
            raise ValueError("Invalid value for `data_to_sign`, must not be `None`")  

        self._data_to_sign = data_to_sign

    @property
    def contact_details(self):
        """Gets the contact_details of this CreateDocumentRequestWrapper.  


        :return: The contact_details of this CreateDocumentRequestWrapper.  
        :rtype: ContactDetails
        """
        return self._contact_details

    @contact_details.setter
    def contact_details(self, contact_details):
        """Sets the contact_details of this CreateDocumentRequestWrapper.


        :param contact_details: The contact_details of this CreateDocumentRequestWrapper.  
        :type: ContactDetails
        """
        if contact_details is None:
            raise ValueError("Invalid value for `contact_details`, must not be `None`")  

        self._contact_details = contact_details

    @property
    def notification(self):
        """Gets the notification of this CreateDocumentRequestWrapper.  


        :return: The notification of this CreateDocumentRequestWrapper.  
        :rtype: Notification
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this CreateDocumentRequestWrapper.


        :param notification: The notification of this CreateDocumentRequestWrapper.  
        :type: Notification
        """

        self._notification = notification

    @property
    def advanced(self):
        """Gets the advanced of this CreateDocumentRequestWrapper.  


        :return: The advanced of this CreateDocumentRequestWrapper.  
        :rtype: Advanced
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this CreateDocumentRequestWrapper.


        :param advanced: The advanced of this CreateDocumentRequestWrapper.  
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
        if not isinstance(other, DocumentCreateOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
