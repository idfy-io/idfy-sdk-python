# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.extended_document_signature import ExtendedDocumentSignature  
from idfy_sdk.models.document_status_summary import DocumentStatusSummary  


class DocumentSummary(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'document_id': 'str',
        'account_id': 'str',
        'title': 'str',
        'description': 'str',
        'last_updated': 'datetime',
        'deadline': 'datetime',
        'signed_date': 'datetime',
        'status': 'DocumentStatusSummary', # Here!
        'external_id': 'str',
        'document_signatures': 'list[ExtendedDocumentSignature]',
        'required_signatures': 'int',
        'current_signatures': 'int',
        'tags': 'list[str]',
        'attachments': 'list[str]',
        'signers': 'list[str]',
        'created': 'datetime'
    }

    attribute_map = {
        'document_id': 'documentId',
        'account_id': 'accountId',
        'title': 'title',
        'description': 'description',
        'last_updated': 'lastUpdated',
        'deadline': 'deadline',
        'signed_date': 'signedDate',
        'status': 'status',
        'external_id': 'externalId',
        'document_signatures': 'documentSignatures',
        'required_signatures': 'requiredSignatures',
        'current_signatures': 'currentSignatures',
        'tags': 'tags',
        'attachments': 'attachments',
        'signers': 'signers',
        'created': 'created'
    }

    def __init__(self, document_id=None, account_id=None, title=None, description=None, last_updated=None, deadline=None, signed_date=None, status=None, external_id=None, document_signatures=None, required_signatures=None, current_signatures=None, tags=None, attachments=None, signers=None, created=None):  
        """DocumentSummary"""  

        self._document_id = None
        self._account_id = None
        self._title = None
        self._description = None
        self._last_updated = None
        self._deadline = None
        self._signed_date = None
        self._status = None
        self._external_id = None
        self._document_signatures = None
        self._required_signatures = None
        self._current_signatures = None
        self._tags = None
        self._attachments = None
        self._signers = None
        self._created = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if account_id is not None:
            self.account_id = account_id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if last_updated is not None:
            self.last_updated = last_updated
        if deadline is not None:
            self.deadline = deadline
        if signed_date is not None:
            self.signed_date = signed_date
        if status is not None:
            self.status = status
        if external_id is not None:
            self.external_id = external_id
        if document_signatures is not None:
            self.document_signatures = document_signatures
        if required_signatures is not None:
            self.required_signatures = required_signatures
        if current_signatures is not None:
            self.current_signatures = current_signatures
        if tags is not None:
            self.tags = tags
        if attachments is not None:
            self.attachments = attachments
        if signers is not None:
            self.signers = signers
        if created is not None:
            self.created = created

    @property
    def document_id(self):
        """Gets the document_id of this DocumentSummary.  

        Document id  

        :return: The document_id of this DocumentSummary.  
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this DocumentSummary.

        Document id  

        :param document_id: The document_id of this DocumentSummary.  
        :type: str
        """

        self._document_id = document_id

    @property
    def account_id(self):
        """Gets the account_id of this DocumentSummary.  

        Account id  

        :return: The account_id of this DocumentSummary.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DocumentSummary.

        Account id  

        :param account_id: The account_id of this DocumentSummary.  
        :type: str
        """

        self._account_id = account_id

    @property
    def title(self):
        """Gets the title of this DocumentSummary.  

        Document title  

        :return: The title of this DocumentSummary.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DocumentSummary.

        Document title  

        :param title: The title of this DocumentSummary.  
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this DocumentSummary.  

        Document description  

        :return: The description of this DocumentSummary.  
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocumentSummary.

        Document description  

        :param description: The description of this DocumentSummary.  
        :type: str
        """

        self._description = description

    @property
    def last_updated(self):
        """Gets the last_updated of this DocumentSummary.  

        When was the document last updated (ISO8601)  

        :return: The last_updated of this DocumentSummary.  
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this DocumentSummary.

        When was the document last updated (ISO8601)  

        :param last_updated: The last_updated of this DocumentSummary.  
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def deadline(self):
        """Gets the deadline of this DocumentSummary.  

        The sign deadline for the document (ISO8601)  

        :return: The deadline of this DocumentSummary.  
        :rtype: datetime
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this DocumentSummary.

        The sign deadline for the document (ISO8601)  

        :param deadline: The deadline of this DocumentSummary.  
        :type: datetime
        """

        self._deadline = deadline

    @property
    def signed_date(self):
        """Gets the signed_date of this DocumentSummary.  

        When was all the signatures processed (ISO8601)  

        :return: The signed_date of this DocumentSummary.  
        :rtype: datetime
        """
        return self._signed_date

    @signed_date.setter
    def signed_date(self, signed_date):
        """Sets the signed_date of this DocumentSummary.

        When was all the signatures processed (ISO8601)  

        :param signed_date: The signed_date of this DocumentSummary.  
        :type: datetime
        """

        self._signed_date = signed_date

    @property
    def status(self):
        """Gets the status of this DocumentSummary.  

        Document status  

        :return: The status of this DocumentSummary.  
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DocumentSummary.

        Document status  

        :param status: The status of this DocumentSummary.  
        :type: Status
        """

        self._status = status

    @property
    def external_id(self):
        """Gets the external_id of this DocumentSummary.  

        External document Id (your Id)  

        :return: The external_id of this DocumentSummary.  
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this DocumentSummary.

        External document Id (your Id)  

        :param external_id: The external_id of this DocumentSummary.  
        :type: str
        """

        self._external_id = external_id

    @property
    def document_signatures(self):
        """Gets the document_signatures of this DocumentSummary.  

        All the signatures received on this document  

        :return: The document_signatures of this DocumentSummary.  
        :rtype: list[ExtendedDocumentSignature]
        """
        return self._document_signatures

    @document_signatures.setter
    def document_signatures(self, document_signatures):
        """Sets the document_signatures of this DocumentSummary.

        All the signatures received on this document  

        :param document_signatures: The document_signatures of this DocumentSummary.  
        :type: list[ExtendedDocumentSignature]
        """

        self._document_signatures = document_signatures

    @property
    def required_signatures(self):
        """Gets the required_signatures of this DocumentSummary.  

        The number of required signatures on the document  

        :return: The required_signatures of this DocumentSummary.  
        :rtype: int
        """
        return self._required_signatures

    @required_signatures.setter
    def required_signatures(self, required_signatures):
        """Sets the required_signatures of this DocumentSummary.

        The number of required signatures on the document  

        :param required_signatures: The required_signatures of this DocumentSummary.  
        :type: int
        """

        self._required_signatures = required_signatures

    @property
    def current_signatures(self):
        """Gets the current_signatures of this DocumentSummary.  

        How many signatures is completed right now  

        :return: The current_signatures of this DocumentSummary.  
        :rtype: int
        """
        return self._current_signatures

    @current_signatures.setter
    def current_signatures(self, current_signatures):
        """Sets the current_signatures of this DocumentSummary.

        How many signatures is completed right now  

        :param current_signatures: The current_signatures of this DocumentSummary.  
        :type: int
        """

        self._current_signatures = current_signatures

    @property
    def tags(self):
        """Gets the tags of this DocumentSummary.  

        Document tags  

        :return: The tags of this DocumentSummary.  
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DocumentSummary.

        Document tags  

        :param tags: The tags of this DocumentSummary.  
        :type: list[str]
        """

        self._tags = tags

    @property
    def attachments(self):
        """Gets the attachments of this DocumentSummary.  

        A list of attachment Id's  

        :return: The attachments of this DocumentSummary.  
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this DocumentSummary.

        A list of attachment Id's  

        :param attachments: The attachments of this DocumentSummary.  
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def signers(self):
        """Gets the signers of this DocumentSummary.  

        A list of all the signers on the document  

        :return: The signers of this DocumentSummary.  
        :rtype: list[str]
        """
        return self._signers

    @signers.setter
    def signers(self, signers):
        """Sets the signers of this DocumentSummary.

        A list of all the signers on the document  

        :param signers: The signers of this DocumentSummary.  
        :type: list[str]
        """

        self._signers = signers

    @property
    def created(self):
        """Gets the created of this DocumentSummary.  

        When the document was created (ISO 8601)  

        :return: The created of this DocumentSummary.  
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DocumentSummary.

        When the document was created (ISO 8601)  

        :param created: The created of this DocumentSummary.  
        :type: datetime
        """

        self._created = created

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
        if not isinstance(other, DocumentSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
