# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.merchant_error import MerchantError  


class SignResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'signed_data': 'str',
        'audit_log_reference': 'str',
        'signing_format': 'str',
        'error': 'MerchantError',
        'sign_certificate_base64_string': 'str',
        'transaction_id': 'str',
        'signed_document_id': 'str',
        'department_id': 'str',
        'data_encoding_format': 'str'
    }

    attribute_map = {
        'signed_data': 'signedData',
        'audit_log_reference': 'auditLogReference',
        'signing_format': 'signingFormat',
        'error': 'error',
        'sign_certificate_base64_string': 'signCertificateBase64String',
        'transaction_id': 'transactionId',
        'signed_document_id': 'signedDocumentId',
        'department_id': 'departmentId',
        'data_encoding_format': 'dataEncodingFormat'
    }

    def __init__(self, signed_data=None, audit_log_reference=None, signing_format=None, error=None, sign_certificate_base64_string=None, transaction_id=None, signed_document_id=None, department_id=None, data_encoding_format=None):  
        """SignResponse"""  

        self._signed_data = None
        self._audit_log_reference = None
        self._signing_format = None
        self._error = None
        self._sign_certificate_base64_string = None
        self._transaction_id = None
        self._signed_document_id = None
        self._department_id = None
        self._data_encoding_format = None
        self.discriminator = None

        if signed_data is not None:
            self.signed_data = signed_data
        if audit_log_reference is not None:
            self.audit_log_reference = audit_log_reference
        if signing_format is not None:
            self.signing_format = signing_format
        if error is not None:
            self.error = error
        if sign_certificate_base64_string is not None:
            self.sign_certificate_base64_string = sign_certificate_base64_string
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if signed_document_id is not None:
            self.signed_document_id = signed_document_id
        if department_id is not None:
            self.department_id = department_id
        if data_encoding_format is not None:
            self.data_encoding_format = data_encoding_format
    
    @property
    def department_id(self):
        return self._department_id
    
    @department_id.setter
    def department_id(self, department_id):
        self._department_id = department_id
    
    @property
    def data_encoding_format(self):
        return self._data_encoding_format
    
    @data_encoding_format.setter
    def data_encoding_format(self, data_encoding_format):
        self._data_encoding_format = data_encoding_format

    @property
    def signed_data(self):
        """Gets the signed_data of this SignResponse.  

        base 64 encoded signed data  

        :return: The signed_data of this SignResponse.  
        :rtype: str
        """
        return self._signed_data

    @signed_data.setter
    def signed_data(self, signed_data):
        """Sets the signed_data of this SignResponse.

        base 64 encoded signed data  

        :param signed_data: The signed_data of this SignResponse.  
        :type: str
        """

        self._signed_data = signed_data

    @property
    def audit_log_reference(self):
        """Gets the audit_log_reference of this SignResponse.  

        Reference Id to audit log  

        :return: The audit_log_reference of this SignResponse.  
        :rtype: str
        """
        return self._audit_log_reference

    @audit_log_reference.setter
    def audit_log_reference(self, audit_log_reference):
        """Sets the audit_log_reference of this SignResponse.

        Reference Id to audit log  

        :param audit_log_reference: The audit_log_reference of this SignResponse.  
        :type: str
        """

        self._audit_log_reference = audit_log_reference

    @property
    def signing_format(self):
        """Gets the signing_format of this SignResponse.  

        Signing format  

        :return: The signing_format of this SignResponse.  
        :rtype: str
        """
        return self._signing_format

    @signing_format.setter
    def signing_format(self, signing_format):
        """Sets the signing_format of this SignResponse.

        Signing format  

        :param signing_format: The signing_format of this SignResponse.  
        :type: str
        """
        allowed_values = ["use_provider_setting", "no_bankid_seid_sdo", "no_bankid_pades", "no_buypass_seid_sdo", "da_nemid_xmldsig", "sv_bankid_native_pkcs7"]  
        if signing_format not in allowed_values:
            raise ValueError(
                "Invalid value for `signing_format` ({0}), must be one of {1}"  
                .format(signing_format, allowed_values)
            )

        self._signing_format = signing_format

    @property
    def error(self):
        """Gets the error of this SignResponse.  

        Error message  

        :return: The error of this SignResponse.  
        :rtype: MerchantError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this SignResponse.

        Error message  

        :param error: The error of this SignResponse.  
        :type: MerchantError
        """

        self._error = error

    @property
    def sign_certificate_base64_string(self):
        """Gets the sign_certificate_base64_string of this SignResponse.  

        Signed with certificate  

        :return: The sign_certificate_base64_string of this SignResponse.  
        :rtype: str
        """
        return self._sign_certificate_base64_string

    @sign_certificate_base64_string.setter
    def sign_certificate_base64_string(self, sign_certificate_base64_string):
        """Sets the sign_certificate_base64_string of this SignResponse.

        Signed with certificate  

        :param sign_certificate_base64_string: The sign_certificate_base64_string of this SignResponse.  
        :type: str
        """

        self._sign_certificate_base64_string = sign_certificate_base64_string

    @property
    def transaction_id(self):
        """Gets the transaction_id of this SignResponse.  

        Id to look up the transaction at a later time  

        :return: The transaction_id of this SignResponse.  
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this SignResponse.

        Id to look up the transaction at a later time  

        :param transaction_id: The transaction_id of this SignResponse.  
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def signed_document_id(self):
        """Gets the signed_document_id of this SignResponse.  

        Id to retrieve signed file (pades)  

        :return: The signed_document_id of this SignResponse.  
        :rtype: str
        """
        return self._signed_document_id

    @signed_document_id.setter
    def signed_document_id(self, signed_document_id):
        """Sets the signed_document_id of this SignResponse.

        Id to retrieve signed file (pades)  

        :param signed_document_id: The signed_document_id of this SignResponse.  
        :type: str
        """

        self._signed_document_id = signed_document_id

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
        if not isinstance(other, SignResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
