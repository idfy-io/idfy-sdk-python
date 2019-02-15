# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.sdo_signers import SDOSigners  
from idfy_sdk.models.seal import Seal  
from idfy_sdk.models.validation_error import ValidationError  


class ParseSDOResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'audit_id': 'str',
        'signers_valid': 'bool',
        'seal': 'Seal',
        'signers': 'list[SDOSigners]',
        'summary': 'str',
        'validation_error': 'ValidationError',
        'signed_data': 'str'
    }

    attribute_map = {
        'request_id': 'requestId',
        'audit_id': 'auditId',
        'signers_valid': 'signersValid',
        'seal': 'seal',
        'signers': 'signers',
        'summary': 'summary',
        'validation_error': 'validationError',
        'signed_data': 'signedData'
    }

    def __init__(self, request_id=None, audit_id=None, signers_valid=None, seal=None, signers=None, summary=None, validation_error=None, signed_data=None):  
        """ParseSDOResponse"""  

        self._request_id = None
        self._audit_id = None
        self._signers_valid = None
        self._seal = None
        self._signers = None
        self._summary = None
        self._validation_error = None
        self._signed_data = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if audit_id is not None:
            self.audit_id = audit_id
        if signers_valid is not None:
            self.signers_valid = signers_valid
        if seal is not None:
            self.seal = seal
        if signers is not None:
            self.signers = signers
        if summary is not None:
            self.summary = summary
        if validation_error is not None:
            self.validation_error = validation_error
        if signed_data is not None:
            self.signed_data = signed_data

    @property
    def request_id(self):
        """Gets the request_id of this ParseSDOResponse.  


        :return: The request_id of this ParseSDOResponse.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ParseSDOResponse.


        :param request_id: The request_id of this ParseSDOResponse.  
        :type: str
        """

        self._request_id = request_id

    @property
    def audit_id(self):
        """Gets the audit_id of this ParseSDOResponse.  

        Reference to audit log  

        :return: The audit_id of this ParseSDOResponse.  
        :rtype: str
        """
        return self._audit_id

    @audit_id.setter
    def audit_id(self, audit_id):
        """Sets the audit_id of this ParseSDOResponse.

        Reference to audit log  

        :param audit_id: The audit_id of this ParseSDOResponse.  
        :type: str
        """

        self._audit_id = audit_id

    @property
    def signers_valid(self):
        """Gets the signers_valid of this ParseSDOResponse.  

        Is the signatures valid  

        :return: The signers_valid of this ParseSDOResponse.  
        :rtype: bool
        """
        return self._signers_valid

    @signers_valid.setter
    def signers_valid(self, signers_valid):
        """Sets the signers_valid of this ParseSDOResponse.

        Is the signatures valid  

        :param signers_valid: The signers_valid of this ParseSDOResponse.  
        :type: bool
        """

        self._signers_valid = signers_valid

    @property
    def seal(self):
        """Gets the seal of this ParseSDOResponse.  

        Is the sealing of the SDO valid  

        :return: The seal of this ParseSDOResponse.  
        :rtype: Seal
        """
        return self._seal

    @seal.setter
    def seal(self, seal):
        """Sets the seal of this ParseSDOResponse.

        Is the sealing of the SDO valid  

        :param seal: The seal of this ParseSDOResponse.  
        :type: Seal
        """

        self._seal = seal

    @property
    def signers(self):
        """Gets the signers of this ParseSDOResponse.  

        Signers list  

        :return: The signers of this ParseSDOResponse.  
        :rtype: list[SDOSigners]
        """
        return self._signers

    @signers.setter
    def signers(self, signers):
        """Sets the signers of this ParseSDOResponse.

        Signers list  

        :param signers: The signers of this ParseSDOResponse.  
        :type: list[SDOSigners]
        """

        self._signers = signers

    @property
    def summary(self):
        """Gets the summary of this ParseSDOResponse.  

        Summary  

        :return: The summary of this ParseSDOResponse.  
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ParseSDOResponse.

        Summary  

        :param summary: The summary of this ParseSDOResponse.  
        :type: str
        """

        self._summary = summary

    @property
    def validation_error(self):
        """Gets the validation_error of this ParseSDOResponse.  

        Error messages  

        :return: The validation_error of this ParseSDOResponse.  
        :rtype: ValidationError
        """
        return self._validation_error

    @validation_error.setter
    def validation_error(self, validation_error):
        """Sets the validation_error of this ParseSDOResponse.

        Error messages  

        :param validation_error: The validation_error of this ParseSDOResponse.  
        :type: ValidationError
        """

        self._validation_error = validation_error

    @property
    def signed_data(self):
        """Gets the signed_data of this ParseSDOResponse.  

        Original data from document (base64 string)  

        :return: The signed_data of this ParseSDOResponse.  
        :rtype: str
        """
        return self._signed_data

    @signed_data.setter
    def signed_data(self, signed_data):
        """Sets the signed_data of this ParseSDOResponse.

        Original data from document (base64 string)  

        :param signed_data: The signed_data of this ParseSDOResponse.  
        :type: str
        """

        self._signed_data = signed_data

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
        if not isinstance(other, ParseSDOResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
