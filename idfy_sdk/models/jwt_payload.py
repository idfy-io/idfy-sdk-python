# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.sign_success import SignSuccess  
from idfy_sdk.models.signature_error import SignatureError  


class JwtPayload(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'document_id': 'str',
        'external_id': 'str',
        'signer_id': 'str',
        'external_signer_id': 'str',
        'error': 'SignatureError',
        'sign_success': 'SignSuccess',
        'expires': 'datetime',
        'aborted': 'bool'
    }

    attribute_map = {
        'account_id': 'accountId',
        'document_id': 'documentId',
        'external_id': 'externalId',
        'signer_id': 'signerId',
        'external_signer_id': 'externalSignerId',
        'error': 'error',
        'sign_success': 'signSuccess',
        'expires': 'expires',
        'aborted': 'aborted'
    }

    def __init__(self, account_id=None, document_id=None, external_id=None, signer_id=None, external_signer_id=None, error=None, sign_success=None, expires=None, aborted=None):  
        """JwtPayload"""  

        self._account_id = None
        self._document_id = None
        self._external_id = None
        self._signer_id = None
        self._external_signer_id = None
        self._error = None
        self._sign_success = None
        self._expires = None
        self._aborted = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if document_id is not None:
            self.document_id = document_id
        if external_id is not None:
            self.external_id = external_id
        if signer_id is not None:
            self.signer_id = signer_id
        if external_signer_id is not None:
            self.external_signer_id = external_signer_id
        if error is not None:
            self.error = error
        if sign_success is not None:
            self.sign_success = sign_success
        if expires is not None:
            self.expires = expires
        if aborted is not None:
            self.aborted = aborted

    @property
    def account_id(self):
        """Gets the account_id of this JwtPayload.  

        Account Id  

        :return: The account_id of this JwtPayload.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this JwtPayload.

        Account Id  

        :param account_id: The account_id of this JwtPayload.  
        :type: str
        """

        self._account_id = account_id

    @property
    def document_id(self):
        """Gets the document_id of this JwtPayload.  

        Document Id  

        :return: The document_id of this JwtPayload.  
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this JwtPayload.

        Document Id  

        :param document_id: The document_id of this JwtPayload.  
        :type: str
        """

        self._document_id = document_id

    @property
    def external_id(self):
        """Gets the external_id of this JwtPayload.  

        External document Id  

        :return: The external_id of this JwtPayload.  
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this JwtPayload.

        External document Id  

        :param external_id: The external_id of this JwtPayload.  
        :type: str
        """

        self._external_id = external_id

    @property
    def signer_id(self):
        """Gets the signer_id of this JwtPayload.  

        Signer Id  

        :return: The signer_id of this JwtPayload.  
        :rtype: str
        """
        return self._signer_id

    @signer_id.setter
    def signer_id(self, signer_id):
        """Sets the signer_id of this JwtPayload.

        Signer Id  

        :param signer_id: The signer_id of this JwtPayload.  
        :type: str
        """

        self._signer_id = signer_id

    @property
    def external_signer_id(self):
        """Gets the external_signer_id of this JwtPayload.  

        External signer Id  

        :return: The external_signer_id of this JwtPayload.  
        :rtype: str
        """
        return self._external_signer_id

    @external_signer_id.setter
    def external_signer_id(self, external_signer_id):
        """Sets the external_signer_id of this JwtPayload.

        External signer Id  

        :param external_signer_id: The external_signer_id of this JwtPayload.  
        :type: str
        """

        self._external_signer_id = external_signer_id

    @property
    def error(self):
        """Gets the error of this JwtPayload.  

        Error object, will be included on error  

        :return: The error of this JwtPayload.  
        :rtype: SignatureError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this JwtPayload.

        Error object, will be included on error  

        :param error: The error of this JwtPayload.  
        :type: SignatureError
        """

        self._error = error

    @property
    def sign_success(self):
        """Gets the sign_success of this JwtPayload.  

        Success object, will be included on sign success  

        :return: The sign_success of this JwtPayload.  
        :rtype: SignSuccess
        """
        return self._sign_success

    @sign_success.setter
    def sign_success(self, sign_success):
        """Sets the sign_success of this JwtPayload.

        Success object, will be included on sign success  

        :param sign_success: The sign_success of this JwtPayload.  
        :type: SignSuccess
        """

        self._sign_success = sign_success

    @property
    def expires(self):
        """Gets the expires of this JwtPayload.  

        When the jwt expires (ISO 8601)  

        :return: The expires of this JwtPayload.  
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this JwtPayload.

        When the jwt expires (ISO 8601)  

        :param expires: The expires of this JwtPayload.  
        :type: datetime
        """

        self._expires = expires

    @property
    def aborted(self):
        """Gets the aborted of this JwtPayload.  

        Set to true if user aborted  

        :return: The aborted of this JwtPayload.  
        :rtype: bool
        """
        return self._aborted

    @aborted.setter
    def aborted(self, aborted):
        """Sets the aborted of this JwtPayload.

        Set to true if user aborted  

        :param aborted: The aborted of this JwtPayload.  
        :type: bool
        """

        self._aborted = aborted

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
        if not isinstance(other, JwtPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
