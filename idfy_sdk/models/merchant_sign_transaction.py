# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class MerchantSignTransaction(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'account_id': 'str',
        'audit_log_reference': 'str',
        'external_reference': 'str',
        'oauth_client_id': 'str',
        'ip_address': 'str',
        'xslt': 'str',
        'data_to_sign': 'str',
        'result': 'str',
        'certificate': 'str',
        'time_stamp': 'datetime',
        'signed_document_id': 'str',
        'pades_created': 'bool',
        'pades_retrieved': 'bool',
        'pades_deleted': 'bool',
        'department_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'accountId',
        'audit_log_reference': 'auditLogReference',
        'external_reference': 'externalReference',
        'oauth_client_id': 'oauthClientId',
        'ip_address': 'ipAddress',
        'xslt': 'xslt',
        'data_to_sign': 'dataToSign',
        'result': 'result',
        'certificate': 'certificate',
        'time_stamp': 'timeStamp',
        'signed_document_id': 'signedDocumentId',
        'pades_created': 'padesCreated',
        'pades_retrieved': 'padesRetrieved',
        'pades_deleted': 'padesDeleted',
        'department_id': 'departmentId'
    }

    def __init__(self, id=None, account_id=None, audit_log_reference=None, external_reference=None, oauth_client_id=None, ip_address=None, xslt=None, data_to_sign=None, result=None, certificate=None, time_stamp=None, signed_document_id=None, pades_created=None, pades_retrieved=None, pades_deleted=None, department_id=None):  
        """MerchantSignTransaction"""  

        self._id = None
        self._account_id = None
        self._audit_log_reference = None
        self._external_reference = None
        self._oauth_client_id = None
        self._ip_address = None
        self._xslt = None
        self._data_to_sign = None
        self._result = None
        self._certificate = None
        self._time_stamp = None
        self._signed_document_id = None
        self._pades_created = None
        self._pades_retrieved = None
        self._pades_deleted = None
        self._department_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if audit_log_reference is not None:
            self.audit_log_reference = audit_log_reference
        if external_reference is not None:
            self.external_reference = external_reference
        if oauth_client_id is not None:
            self.oauth_client_id = oauth_client_id
        if ip_address is not None:
            self.ip_address = ip_address
        if xslt is not None:
            self.xslt = xslt
        if data_to_sign is not None:
            self.data_to_sign = data_to_sign
        if result is not None:
            self.result = result
        if certificate is not None:
            self.certificate = certificate
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if signed_document_id is not None:
            self.signed_document_id = signed_document_id
        if pades_created is not None:
            self.pades_created = pades_created
        if pades_retrieved is not None:
            self.pades_retrieved = pades_retrieved
        if pades_deleted is not None:
            self.pades_deleted = pades_deleted
        if department_id is not None:
            self.department_id = department_id
    
    @property  
    def department_id(self):
        return self._department_id
    
    @department_id.setter
    def department_id(self, department_id):
        self._department_id = department_id

    @property
    def id(self):
        """Gets the id of this MerchantSignTransaction.  

        Transaction Id  

        :return: The id of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MerchantSignTransaction.

        Transaction Id  

        :param id: The id of this MerchantSignTransaction.  
        :type: str
        """

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this MerchantSignTransaction.  

        Your account Id  

        :return: The account_id of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this MerchantSignTransaction.

        Your account Id  

        :param account_id: The account_id of this MerchantSignTransaction.  
        :type: str
        """

        self._account_id = account_id

    @property
    def audit_log_reference(self):
        """Gets the audit_log_reference of this MerchantSignTransaction.  

        Audit log Id  

        :return: The audit_log_reference of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._audit_log_reference

    @audit_log_reference.setter
    def audit_log_reference(self, audit_log_reference):
        """Sets the audit_log_reference of this MerchantSignTransaction.

        Audit log Id  

        :param audit_log_reference: The audit_log_reference of this MerchantSignTransaction.  
        :type: str
        """

        self._audit_log_reference = audit_log_reference

    @property
    def external_reference(self):
        """Gets the external_reference of this MerchantSignTransaction.  

        External Reference  

        :return: The external_reference of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this MerchantSignTransaction.

        External Reference  

        :param external_reference: The external_reference of this MerchantSignTransaction.  
        :type: str
        """

        self._external_reference = external_reference

    @property
    def oauth_client_id(self):
        """Gets the oauth_client_id of this MerchantSignTransaction.  

        The oauth client used in this transaction  

        :return: The oauth_client_id of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._oauth_client_id

    @oauth_client_id.setter
    def oauth_client_id(self, oauth_client_id):
        """Sets the oauth_client_id of this MerchantSignTransaction.

        The oauth client used in this transaction  

        :param oauth_client_id: The oauth_client_id of this MerchantSignTransaction.  
        :type: str
        """

        self._oauth_client_id = oauth_client_id

    @property
    def ip_address(self):
        """Gets the ip_address of this MerchantSignTransaction.  

        Ip address  

        :return: The ip_address of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this MerchantSignTransaction.

        Ip address  

        :param ip_address: The ip_address of this MerchantSignTransaction.  
        :type: str
        """

        self._ip_address = ip_address

    @property
    def xslt(self):
        """Gets the xslt of this MerchantSignTransaction.  

        Xslt sha256 hash  

        :return: The xslt of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._xslt

    @xslt.setter
    def xslt(self, xslt):
        """Sets the xslt of this MerchantSignTransaction.

        Xslt sha256 hash  

        :param xslt: The xslt of this MerchantSignTransaction.  
        :type: str
        """

        self._xslt = xslt

    @property
    def data_to_sign(self):
        """Gets the data_to_sign of this MerchantSignTransaction.  

        Data to sign sha256 hash  

        :return: The data_to_sign of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._data_to_sign

    @data_to_sign.setter
    def data_to_sign(self, data_to_sign):
        """Sets the data_to_sign of this MerchantSignTransaction.

        Data to sign sha256 hash  

        :param data_to_sign: The data_to_sign of this MerchantSignTransaction.  
        :type: str
        """

        self._data_to_sign = data_to_sign

    @property
    def result(self):
        """Gets the result of this MerchantSignTransaction.  

        Signed data sha256 hash  

        :return: The result of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this MerchantSignTransaction.

        Signed data sha256 hash  

        :param result: The result of this MerchantSignTransaction.  
        :type: str
        """

        self._result = result

    @property
    def certificate(self):
        """Gets the certificate of this MerchantSignTransaction.  

        Certificate  

        :return: The certificate of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this MerchantSignTransaction.

        Certificate  

        :param certificate: The certificate of this MerchantSignTransaction.  
        :type: str
        """

        self._certificate = certificate

    @property
    def time_stamp(self):
        """Gets the time_stamp of this MerchantSignTransaction.  

        Log save time  

        :return: The time_stamp of this MerchantSignTransaction.  
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this MerchantSignTransaction.

        Log save time  

        :param time_stamp: The time_stamp of this MerchantSignTransaction.  
        :type: datetime
        """

        self._time_stamp = time_stamp

    @property
    def signed_document_id(self):
        """Gets the signed_document_id of this MerchantSignTransaction.  

        For pades retrieval  

        :return: The signed_document_id of this MerchantSignTransaction.  
        :rtype: str
        """
        return self._signed_document_id

    @signed_document_id.setter
    def signed_document_id(self, signed_document_id):
        """Sets the signed_document_id of this MerchantSignTransaction.

        For pades retrieval  

        :param signed_document_id: The signed_document_id of this MerchantSignTransaction.  
        :type: str
        """

        self._signed_document_id = signed_document_id

    @property
    def pades_created(self):
        """Gets the pades_created of this MerchantSignTransaction.  


        :return: The pades_created of this MerchantSignTransaction.  
        :rtype: bool
        """
        return self._pades_created

    @pades_created.setter
    def pades_created(self, pades_created):
        """Sets the pades_created of this MerchantSignTransaction.


        :param pades_created: The pades_created of this MerchantSignTransaction.  
        :type: bool
        """

        self._pades_created = pades_created

    @property
    def pades_retrieved(self):
        """Gets the pades_retrieved of this MerchantSignTransaction.  


        :return: The pades_retrieved of this MerchantSignTransaction.  
        :rtype: bool
        """
        return self._pades_retrieved

    @pades_retrieved.setter
    def pades_retrieved(self, pades_retrieved):
        """Sets the pades_retrieved of this MerchantSignTransaction.


        :param pades_retrieved: The pades_retrieved of this MerchantSignTransaction.  
        :type: bool
        """

        self._pades_retrieved = pades_retrieved

    @property
    def pades_deleted(self):
        """Gets the pades_deleted of this MerchantSignTransaction.  


        :return: The pades_deleted of this MerchantSignTransaction.  
        :rtype: bool
        """
        return self._pades_deleted

    @pades_deleted.setter
    def pades_deleted(self, pades_deleted):
        """Sets the pades_deleted of this MerchantSignTransaction.


        :param pades_deleted: The pades_deleted of this MerchantSignTransaction.  
        :type: bool
        """

        self._pades_deleted = pades_deleted

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
        if not isinstance(other, MerchantSignTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
