# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.extra_info_document_request import ExtraInfoDocumentRequest  
from idfy_sdk.models.security import Security  
from idfy_sdk.models.time_to_live import TimeToLive  


class Advanced(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tags': 'list[str]',
        'attachments': 'int',
        'required_signatures': 'int',
        'created_by_application': 'str',
        'get_social_security_number': 'bool',
        'extra_info': 'ExtraInfoDocumentRequest',
        'security': 'Security',
        'time_to_live': 'TimeToLive',
        'department_id': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'attachments': 'attachments',
        'required_signatures': 'requiredSignatures',
        'created_by_application': 'createdByApplication',
        'get_social_security_number': 'getSocialSecurityNumber',
        'extra_info': 'extraInfo',
        'security': 'security',
        'time_to_live': 'timeToLive',
        'department_id': 'departmentId'
    }

    def __init__(self, tags=None, attachments=None, required_signatures=None, created_by_application=None, get_social_security_number=None, extra_info=None, security=None, time_to_live=None, department_id=None):  
        """Advanced"""  

        self._tags = None
        self._attachments = None
        self._required_signatures = None
        self._created_by_application = None
        self._get_social_security_number = None
        self._extra_info = None
        self._security = None
        self._time_to_live = None
        self._department_id = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if attachments is not None:
            self.attachments = attachments
        if required_signatures is not None:
            self.required_signatures = required_signatures
        if created_by_application is not None:
            self.created_by_application = created_by_application
        if get_social_security_number is not None:
            self.get_social_security_number = get_social_security_number
        if extra_info is not None:
            self.extra_info = extra_info
        if security is not None:
            self.security = security
        if time_to_live is not None:
            self.time_to_live = time_to_live
        if department_id is not None:
            self.department_id = department_id

    @property
    def tags(self):
        """Gets the tags of this Advanced.  

        A list of tags to add to the document. These tags can be used to query for document data and will also be added to all events that are triggered for the document.  

        :return: The tags of this Advanced.  
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Advanced.

        A list of tags to add to the document. These tags can be used to query for document data and will also be added to all events that are triggered for the document.  

        :param tags: The tags of this Advanced.  
        :type: list[str]
        """

        self._tags = tags

    @property
    def attachments(self):
        """Gets the attachments of this Advanced.  

        The number of attachments this document will have. Attachments can be added [here](#operation/Attachment_Create) after the document is created.  <span style=\"color: red\">If you set this value to 3, you MUST upload 3 attachments before anyone can sign the document.</span>  

        :return: The attachments of this Advanced.  
        :rtype: int
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Advanced.

        The number of attachments this document will have. Attachments can be added [here](#operation/Attachment_Create) after the document is created.  <span style=\"color: red\">If you set this value to 3, you MUST upload 3 attachments before anyone can sign the document.</span>  

        :param attachments: The attachments of this Advanced.  
        :type: int
        """

        self._attachments = attachments

    @property
    def required_signatures(self):
        """Gets the required_signatures of this Advanced.  

        The number of signatures required before the document can be sealed and marked as completed.  

        :return: The required_signatures of this Advanced.  
        :rtype: int
        """
        return self._required_signatures

    @required_signatures.setter
    def required_signatures(self, required_signatures):
        """Sets the required_signatures of this Advanced.

        The number of signatures required before the document can be sealed and marked as completed.  

        :param required_signatures: The required_signatures of this Advanced.  
        :type: int
        """

        self._required_signatures = required_signatures

    @property
    def created_by_application(self):
        """Gets the created_by_application of this Advanced.  

        The name of the application that created the document. Used for Idfy statistics.  

        :return: The created_by_application of this Advanced.  
        :rtype: str
        """
        return self._created_by_application

    @created_by_application.setter
    def created_by_application(self, created_by_application):
        """Sets the created_by_application of this Advanced.

        The name of the application that created the document. Used for Idfy statistics.  

        :param created_by_application: The created_by_application of this Advanced.  
        :type: str
        """

        self._created_by_application = created_by_application

    @property
    def get_social_security_number(self):
        """Gets the get_social_security_number of this Advanced.  

        Determines if the social security number of the signers should be retrieved after a successful signature.  Requires a certificate with permission to retrieve SSN.  

        :return: The get_social_security_number of this Advanced.  
        :rtype: bool
        """
        return self._get_social_security_number

    @get_social_security_number.setter
    def get_social_security_number(self, get_social_security_number):
        """Sets the get_social_security_number of this Advanced.

        Determines if the social security number of the signers should be retrieved after a successful signature.  Requires a certificate with permission to retrieve SSN.  

        :param get_social_security_number: The get_social_security_number of this Advanced.  
        :type: bool
        """

        self._get_social_security_number = get_social_security_number

    @property
    def extra_info(self):
        """Gets the extra_info of this Advanced.  


        :return: The extra_info of this Advanced.  
        :rtype: ExtraInfoDocumentRequest
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this Advanced.


        :param extra_info: The extra_info of this Advanced.  
        :type: ExtraInfoDocumentRequest
        """

        self._extra_info = extra_info

    @property
    def security(self):
        """Gets the security of this Advanced.  


        :return: The security of this Advanced.  
        :rtype: Security
        """
        return self._security

    @security.setter
    def security(self, security):
        """Sets the security of this Advanced.


        :param security: The security of this Advanced.  
        :type: Security
        """

        self._security = security

    @property
    def time_to_live(self):
        """Gets the time_to_live of this Advanced.  


        :return: The time_to_live of this Advanced.  
        :rtype: TimeToLive
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        """Sets the time_to_live of this Advanced.


        :param time_to_live: The time_to_live of this Advanced.  
        :type: TimeToLive
        """

        self._time_to_live = time_to_live

    @property
    def department_id(self):
        """Gets the department_id of this Advanced.  

        The department ID to mark the invoice with.  

        :return: The department_id of this Advanced.  
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this Advanced.

        The department ID to mark the invoice with.  

        :param department_id: The department_id of this Advanced.  
        :type: str
        """
        if department_id is not None and len(department_id) > 100:
            raise ValueError("Invalid value for `department_id`, length must be less than or equal to `100`")  
        if department_id is not None and len(department_id) < 0:
            raise ValueError("Invalid value for `department_id`, length must be greater than or equal to `0`")  

        self._department_id = department_id

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
        if not isinstance(other, Advanced):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
