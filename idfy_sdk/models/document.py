# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.advanced import Advanced  
from idfy_sdk.models.contact_details import ContactDetails  
from idfy_sdk.models.data_to_sign import DataToSign  
from idfy_sdk.models.link import Link  
from idfy_sdk.models.notification import Notification  
from idfy_sdk.models.signer import Signer  
from idfy_sdk.models.document_status_summary import DocumentStatusSummary  


class Document(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'document_id': 'str',
        'signers': 'list[Signer]',
        'status': 'DocumentStatusSummary',
        'links': 'list[Link]',
        'title': 'str',
        'description': 'str',
        'external_id': 'str',
        'data_to_sign': 'DataToSign',
        'contact_details': 'ContactDetails',
        'notification': 'Notification',
        'advanced': 'Advanced'
    }

    attribute_map = {
        'document_id': 'documentId',
        'signers': 'signers',
        'status': 'status',
        'links': 'links',
        'title': 'title',
        'description': 'description',
        'external_id': 'externalId',
        'data_to_sign': 'dataToSign',
        'contact_details': 'contactDetails',
        'notification': 'notification',
        'advanced': 'advanced'
    }

    def __init__(self, document_id=None, signers=None, status=None, links=None, title=None, description=None, external_id=None, data_to_sign=None, contact_details=None, notification=None, advanced=None):  
        """CreateDocumentResponse"""  

        self._document_id = None
        self._signers = None
        self._status = None
        self._links = None
        self._title = None
        self._description = None
        self._external_id = None
        self._data_to_sign = None
        self._contact_details = None
        self._notification = None
        self._advanced = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if signers is not None:
            self.signers = signers
        if status is not None:
            self.status = status
        if links is not None:
            self.links = links
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if external_id is not None:
            self.external_id = external_id
        if data_to_sign is not None:
            self.data_to_sign = data_to_sign
        if contact_details is not None:
            self.contact_details = contact_details
        if notification is not None:
            self.notification = notification
        if advanced is not None:
            self.advanced = advanced

    @property
    def document_id(self):
        """Gets the document_id of this CreateDocumentResponse.  

        The document's unique identifier.  

        :return: The document_id of this CreateDocumentResponse.  
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this CreateDocumentResponse.

        The document's unique identifier.  

        :param document_id: The document_id of this CreateDocumentResponse.  
        :type: str
        """

        self._document_id = document_id

    @property
    def signers(self):
        """Gets the signers of this CreateDocumentResponse.  

        List of signers for the document.  

        :return: The signers of this CreateDocumentResponse.  
        :rtype: list[SignerResponse]
        """
        return self._signers

    @signers.setter
    def signers(self, signers):
        """Sets the signers of this CreateDocumentResponse.

        List of signers for the document.  

        :param signers: The signers of this CreateDocumentResponse.  
        :type: list[SignerResponse]
        """

        self._signers = signers

    @property
    def status(self):
        """Gets the status of this CreateDocumentResponse.  


        :return: The status of this CreateDocumentResponse.  
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateDocumentResponse.


        :param status: The status of this CreateDocumentResponse.  
        :type: Status
        """

        self._status = status

    @property
    def links(self):
        """Gets the links of this CreateDocumentResponse.  

        HATEOAS extra info links retrieved for the document.  

        :return: The links of this CreateDocumentResponse.  
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CreateDocumentResponse.

        HATEOAS extra info links retrieved for the document.  

        :param links: The links of this CreateDocumentResponse.  
        :type: list[Link]
        """

        self._links = links

    @property
    def title(self):
        """Gets the title of this CreateDocumentResponse.  

        The title of the document which will be presented to the user.  

        :return: The title of this CreateDocumentResponse.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateDocumentResponse.

        The title of the document which will be presented to the user.  

        :param title: The title of this CreateDocumentResponse.  
        :type: str
        """
        #if title is None:
        #    raise ValueError("Invalid value for `title`, must not be `None`")  
        #if title is not None and len(title) > 300:
        #    raise ValueError("Invalid value for `title`, length must be less than or equal to `300`")  
        #if title is not None and len(title) < 0:
        #    raise ValueError("Invalid value for `title`, length must be greater than or equal to `0`")  

        self._title = title

    @property
    def description(self):
        """Gets the description of this CreateDocumentResponse.  

        The description of the document.  

        :return: The description of this CreateDocumentResponse.  
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDocumentResponse.

        The description of the document.  

        :param description: The description of this CreateDocumentResponse.  
        :type: str
        """

        self._description = description

    @property
    def external_id(self):
        """Gets the external_id of this CreateDocumentResponse.  

        Your reference to this document.  

        :return: The external_id of this CreateDocumentResponse.  
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CreateDocumentResponse.

        Your reference to this document.  

        :param external_id: The external_id of this CreateDocumentResponse.  
        :type: str
        """
        #if external_id is None:
        #    raise ValueError("Invalid value for `external_id`, must not be `None`")  
        #if external_id is not None and len(external_id) > 255:
        #    raise ValueError("Invalid value for `external_id`, length must be less than or equal to `255`")  
        #if external_id is not None and len(external_id) < 4:
        #    raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `4`")  

        self._external_id = external_id

    @property
    def data_to_sign(self):
        """Gets the data_to_sign of this CreateDocumentResponse.  


        :return: The data_to_sign of this CreateDocumentResponse.  
        :rtype: DataToSign
        """
        return self._data_to_sign

    @data_to_sign.setter
    def data_to_sign(self, data_to_sign):
        """Sets the data_to_sign of this CreateDocumentResponse.


        :param data_to_sign: The data_to_sign of this CreateDocumentResponse.  
        :type: DataToSign
        """
        #if data_to_sign is None:
        #    raise ValueError("Invalid value for `data_to_sign`, must not be `None`")  

        self._data_to_sign = data_to_sign

    @property
    def contact_details(self):
        """Gets the contact_details of this CreateDocumentResponse.  


        :return: The contact_details of this CreateDocumentResponse.  
        :rtype: ContactDetails
        """
        return self._contact_details

    @contact_details.setter
    def contact_details(self, contact_details):
        """Sets the contact_details of this CreateDocumentResponse.


        :param contact_details: The contact_details of this CreateDocumentResponse.  
        :type: ContactDetails
        """
        #if contact_details is None:
        #    raise ValueError("Invalid value for `contact_details`, must not be `None`")  

        self._contact_details = contact_details

    @property
    def notification(self):
        """Gets the notification of this CreateDocumentResponse.  


        :return: The notification of this CreateDocumentResponse.  
        :rtype: Notification
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """Sets the notification of this CreateDocumentResponse.


        :param notification: The notification of this CreateDocumentResponse.  
        :type: Notification
        """

        self._notification = notification

    @property
    def advanced(self):
        """Gets the advanced of this CreateDocumentResponse.  


        :return: The advanced of this CreateDocumentResponse.  
        :rtype: Advanced
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this CreateDocumentResponse.


        :param advanced: The advanced of this CreateDocumentResponse.  
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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
