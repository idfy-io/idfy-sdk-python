# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.seal import Seal  
from idfy_sdk.models.validated_signers import ValidatedSigners  
from idfy_sdk.models.validation_error import ValidationError  


class ValidateSDOResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'valid': 'bool',
        'seal': 'Seal',
        'signers': 'list[ValidatedSigners]',
        'summary': 'str',
        'validation_error': 'ValidationError',
        'audit_id': 'str'
    }

    attribute_map = {
        'request_id': 'requestId',
        'valid': 'valid',
        'seal': 'seal',
        'signers': 'signers',
        'summary': 'summary',
        'validation_error': 'validationError',
        'audit_id': 'auditId'
    }

    def __init__(self, request_id=None, valid=None, seal=None, signers=None, summary=None, validation_error=None, audit_id=None):  
        """ValidateSDOResponse"""  

        self._request_id = None
        self._valid = None
        self._seal = None
        self._signers = None
        self._summary = None
        self._validation_error = None
        self._audit_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if valid is not None:
            self.valid = valid
        if seal is not None:
            self.seal = seal
        if signers is not None:
            self.signers = signers
        if summary is not None:
            self.summary = summary
        if validation_error is not None:
            self.validation_error = validation_error
        if audit_id is not None:
            self.audit_id = audit_id

    @property
    def request_id(self):
        """Gets the request_id of this ValidateSDOResponse.  


        :return: The request_id of this ValidateSDOResponse.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ValidateSDOResponse.


        :param request_id: The request_id of this ValidateSDOResponse.  
        :type: str
        """

        self._request_id = request_id

    @property
    def valid(self):
        """Gets the valid of this ValidateSDOResponse.  

        Is the SDO valid  

        :return: The valid of this ValidateSDOResponse.  
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this ValidateSDOResponse.

        Is the SDO valid  

        :param valid: The valid of this ValidateSDOResponse.  
        :type: bool
        """

        self._valid = valid

    @property
    def seal(self):
        """Gets the seal of this ValidateSDOResponse.  

        Is the Seal of the SDO valid  

        :return: The seal of this ValidateSDOResponse.  
        :rtype: Seal
        """
        return self._seal

    @seal.setter
    def seal(self, seal):
        """Sets the seal of this ValidateSDOResponse.

        Is the Seal of the SDO valid  

        :param seal: The seal of this ValidateSDOResponse.  
        :type: Seal
        """

        self._seal = seal

    @property
    def signers(self):
        """Gets the signers of this ValidateSDOResponse.  


        :return: The signers of this ValidateSDOResponse.  
        :rtype: list[ValidatedSigners]
        """
        return self._signers

    @signers.setter
    def signers(self, signers):
        """Sets the signers of this ValidateSDOResponse.


        :param signers: The signers of this ValidateSDOResponse.  
        :type: list[ValidatedSigners]
        """

        self._signers = signers

    @property
    def summary(self):
        """Gets the summary of this ValidateSDOResponse.  


        :return: The summary of this ValidateSDOResponse.  
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ValidateSDOResponse.


        :param summary: The summary of this ValidateSDOResponse.  
        :type: str
        """

        self._summary = summary

    @property
    def validation_error(self):
        """Gets the validation_error of this ValidateSDOResponse.  


        :return: The validation_error of this ValidateSDOResponse.  
        :rtype: ValidationError
        """
        return self._validation_error

    @validation_error.setter
    def validation_error(self, validation_error):
        """Sets the validation_error of this ValidateSDOResponse.


        :param validation_error: The validation_error of this ValidateSDOResponse.  
        :type: ValidationError
        """

        self._validation_error = validation_error

    @property
    def audit_id(self):
        """Gets the audit_id of this ValidateSDOResponse.  

        The AuditId vil only be set for users with an account on the API.  

        :return: The audit_id of this ValidateSDOResponse.  
        :rtype: str
        """
        return self._audit_id

    @audit_id.setter
    def audit_id(self, audit_id):
        """Sets the audit_id of this ValidateSDOResponse.

        The AuditId vil only be set for users with an account on the API.  

        :param audit_id: The audit_id of this ValidateSDOResponse.  
        :type: str
        """

        self._audit_id = audit_id

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
        if not isinstance(other, ValidateSDOResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
