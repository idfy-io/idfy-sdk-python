# coding: utf-8

"""
    Idfy.Signature

    Sign contracts, declarations, forms and other documents using digital signatures.   ## Last update   Last build date for this endpoint: 18.03.2019

"""


import pprint
import re
from typing import List, Dict
from datetime import datetime as datetime


from idfy_sdk.services.signature.models.error import Error

class GenerateRedirectJwtRequest(object):
    """NOTE: This class is generated by Eivind.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': str,
        'document_id': str,
        'signer_id': str,
        'session_id': str,
        'status': str,
        'error': Error
    }

    attribute_map = {
        'account_id': 'accountId',
        'document_id': 'documentId',
        'signer_id': 'signerId',
        'session_id': 'sessionId',
        'status': 'status',
        'error': 'error'
    }

    def __init__(self, account_id=None, document_id=None, signer_id=None, session_id=None, status=None, error=None):

        self._account_id = None
        self._document_id = None
        self._signer_id = None
        self._session_id = None
        self._status = None
        self._error = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if document_id is not None:
            self.document_id = document_id
        if signer_id is not None:
            self.signer_id = signer_id
        if session_id is not None:
            self.session_id = session_id
        if status is not None:
            self.status = status
        if error is not None:
            self.error = error

    @property
    def account_id(self):
        """Gets the account_id of this GenerateRedirectJwtRequest.


        :return: The account_id of this GenerateRedirectJwtRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this GenerateRedirectJwtRequest.


        :param account_id: The account_id of this GenerateRedirectJwtRequest.
        :type: str
        """

        self._account_id = account_id

    @property
    def document_id(self):
        """Gets the document_id of this GenerateRedirectJwtRequest.


        :return: The document_id of this GenerateRedirectJwtRequest.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this GenerateRedirectJwtRequest.


        :param document_id: The document_id of this GenerateRedirectJwtRequest.
        :type: str
        """

        self._document_id = document_id

    @property
    def signer_id(self):
        """Gets the signer_id of this GenerateRedirectJwtRequest.


        :return: The signer_id of this GenerateRedirectJwtRequest.
        :rtype: str
        """
        return self._signer_id

    @signer_id.setter
    def signer_id(self, signer_id):
        """Sets the signer_id of this GenerateRedirectJwtRequest.


        :param signer_id: The signer_id of this GenerateRedirectJwtRequest.
        :type: str
        """

        self._signer_id = signer_id

    @property
    def session_id(self):
        """Gets the session_id of this GenerateRedirectJwtRequest.


        :return: The session_id of this GenerateRedirectJwtRequest.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this GenerateRedirectJwtRequest.


        :param session_id: The session_id of this GenerateRedirectJwtRequest.
        :type: str
        """

        self._session_id = session_id

    @property
    def status(self):
        """Gets the status of this GenerateRedirectJwtRequest.


        :return: The status of this GenerateRedirectJwtRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GenerateRedirectJwtRequest.


        :param status: The status of this GenerateRedirectJwtRequest.
        :type: str
        """

        self._status = status

    @property
    def error(self):
        """Gets the error of this GenerateRedirectJwtRequest.


        :return: The error of this GenerateRedirectJwtRequest.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this GenerateRedirectJwtRequest.


        :param error: The error of this GenerateRedirectJwtRequest.
        :type: Error
        """

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
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
        if not isinstance(other, GenerateRedirectJwtRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
