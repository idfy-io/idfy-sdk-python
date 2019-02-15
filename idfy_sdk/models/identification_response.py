# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.environment_info import EnvironmentInfo  
from idfy_sdk.models.error import Error  


class IdentificationResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'date_of_birth': 'str',
        'status': 'str',
        'social_security_number': 'str',
        'identity_provider_unique_id': 'str',
        'identity_provider': 'str',
        'error': 'Error',
        'environment_info': 'EnvironmentInfo',
        'meta_data': 'dict(str, str)',
        'request_id': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'first_name': 'FirstName',
        'middle_name': 'MiddleName',
        'last_name': 'LastName',
        'date_of_birth': 'DateOfBirth',
        'status': 'Status',
        'social_security_number': 'SocialSecurityNumber',
        'identity_provider_unique_id': 'IdentityProviderUniqueId',
        'identity_provider': 'IdentityProvider',
        'error': 'Error',
        'environment_info': 'EnvironmentInfo',
        'meta_data': 'MetaData',
        'request_id': 'RequestId'
    }

    def __init__(self, name=None, first_name=None, middle_name=None, last_name=None, date_of_birth=None, status=None, social_security_number=None, identity_provider_unique_id=None, identity_provider=None, error=None, environment_info=None, meta_data=None, request_id=None):  
        """IdentificationResponse"""  

        self._name = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._date_of_birth = None
        self._status = None
        self._social_security_number = None
        self._identity_provider_unique_id = None
        self._identity_provider = None
        self._error = None
        self._environment_info = None
        self._meta_data = None
        self._request_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if status is not None:
            self.status = status
        if social_security_number is not None:
            self.social_security_number = social_security_number
        if identity_provider_unique_id is not None:
            self.identity_provider_unique_id = identity_provider_unique_id
        if identity_provider is not None:
            self.identity_provider = identity_provider
        if error is not None:
            self.error = error
        if environment_info is not None:
            self.environment_info = environment_info
        if meta_data is not None:
            self.meta_data = meta_data
        if request_id is not None:
            self.request_id = request_id

    @property
    def name(self):
        """Gets the name of this IdentificationResponse.  

        The fullname of the user as reported back from the IdentityProvider  

        :return: The name of this IdentificationResponse.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentificationResponse.

        The fullname of the user as reported back from the IdentityProvider  

        :param name: The name of this IdentificationResponse.  
        :type: str
        """

        self._name = name

    @property
    def first_name(self):
        """Gets the first_name of this IdentificationResponse.  

        The first name of the user  

        :return: The first_name of this IdentificationResponse.  
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this IdentificationResponse.

        The first name of the user  

        :param first_name: The first_name of this IdentificationResponse.  
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this IdentificationResponse.  

        The middle name of the user (not always available)  

        :return: The middle_name of this IdentificationResponse.  
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this IdentificationResponse.

        The middle name of the user (not always available)  

        :param middle_name: The middle_name of this IdentificationResponse.  
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this IdentificationResponse.  

        The last name of the user  

        :return: The last_name of this IdentificationResponse.  
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this IdentificationResponse.

        The last name of the user  

        :param last_name: The last_name of this IdentificationResponse.  
        :type: str
        """

        self._last_name = last_name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this IdentificationResponse.  

        The users date of birth (not always available)  

        :return: The date_of_birth of this IdentificationResponse.  
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this IdentificationResponse.

        The users date of birth (not always available)  

        :param date_of_birth: The date_of_birth of this IdentificationResponse.  
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def status(self):
        """Gets the status of this IdentificationResponse.  

        The status of the identification process. If not success the identification process is not completed.  

        :return: The status of this IdentificationResponse.  
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IdentificationResponse.

        The status of the identification process. If not success the identification process is not completed.  

        :param status: The status of this IdentificationResponse.  
        :type: str
        """
        allowed_values = ["UNKNOWN", "SUCCESS", "ERROR", "USERABORTED", "INVALIDATED", "TIMEOUT", "CREATED", "USERINITIATED"]  
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def social_security_number(self):
        """Gets the social_security_number of this IdentificationResponse.  

        The social security number for the user (if allowed and if the GetSocialSecurityNumber is set to true in the request)  

        :return: The social_security_number of this IdentificationResponse.  
        :rtype: str
        """
        return self._social_security_number

    @social_security_number.setter
    def social_security_number(self, social_security_number):
        """Sets the social_security_number of this IdentificationResponse.

        The social security number for the user (if allowed and if the GetSocialSecurityNumber is set to true in the request)  

        :param social_security_number: The social_security_number of this IdentificationResponse.  
        :type: str
        """

        self._social_security_number = social_security_number

    @property
    def identity_provider_unique_id(self):
        """Gets the identity_provider_unique_id of this IdentificationResponse.  

        The uniqueID from the e-ID, this ID is unique for the user and is the same every time the user logs on. This is not a sensitiv ID and you could store this to identify the user in you database.  Remark: The Swedish BankID do not have an unique ID.  

        :return: The identity_provider_unique_id of this IdentificationResponse.  
        :rtype: str
        """
        return self._identity_provider_unique_id

    @identity_provider_unique_id.setter
    def identity_provider_unique_id(self, identity_provider_unique_id):
        """Sets the identity_provider_unique_id of this IdentificationResponse.

        The uniqueID from the e-ID, this ID is unique for the user and is the same every time the user logs on. This is not a sensitiv ID and you could store this to identify the user in you database.  Remark: The Swedish BankID do not have an unique ID.  

        :param identity_provider_unique_id: The identity_provider_unique_id of this IdentificationResponse.  
        :type: str
        """

        self._identity_provider_unique_id = identity_provider_unique_id

    @property
    def identity_provider(self):
        """Gets the identity_provider of this IdentificationResponse.  

        The identityprovider type (Norwegian BanKID, SwedishBankID, Nemid, etc)  

        :return: The identity_provider of this IdentificationResponse.  
        :rtype: str
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        """Sets the identity_provider of this IdentificationResponse.

        The identityprovider type (Norwegian BanKID, SwedishBankID, Nemid, etc)  

        :param identity_provider: The identity_provider of this IdentificationResponse.  
        :type: str
        """
        allowed_values = ["UNKNOWN", "NO_BANKID_MOBILE", "NO_BANKID_WEB", "SWE_BANKID", "SWE_BANKID_MOBILE", "NO_BUYPASS", "DA_NEMID", "FI_TUPAS"]  
        if identity_provider not in allowed_values:
            raise ValueError(
                "Invalid value for `identity_provider` ({0}), must be one of {1}"  
                .format(identity_provider, allowed_values)
            )

        self._identity_provider = identity_provider

    @property
    def error(self):
        """Gets the error of this IdentificationResponse.  

        Information about error if the identification process failed. (Only set if an error occured, if not is null)  

        :return: The error of this IdentificationResponse.  
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this IdentificationResponse.

        Information about error if the identification process failed. (Only set if an error occured, if not is null)  

        :param error: The error of this IdentificationResponse.  
        :type: Error
        """

        self._error = error

    @property
    def environment_info(self):
        """Gets the environment_info of this IdentificationResponse.  

        Information about the users environment as seen by IdentiSign, can be used to compare with own data.  

        :return: The environment_info of this IdentificationResponse.  
        :rtype: EnvironmentInfo
        """
        return self._environment_info

    @environment_info.setter
    def environment_info(self, environment_info):
        """Sets the environment_info of this IdentificationResponse.

        Information about the users environment as seen by IdentiSign, can be used to compare with own data.  

        :param environment_info: The environment_info of this IdentificationResponse.  
        :type: EnvironmentInfo
        """

        self._environment_info = environment_info

    @property
    def meta_data(self):
        """Gets the meta_data of this IdentificationResponse.  

        A dicitonary with extra information from each identityprovider, and extra services. See developer documentation for more information  

        :return: The meta_data of this IdentificationResponse.  
        :rtype: dict(str, str)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this IdentificationResponse.

        A dicitonary with extra information from each identityprovider, and extra services. See developer documentation for more information  

        :param meta_data: The meta_data of this IdentificationResponse.  
        :type: dict(str, str)
        """

        self._meta_data = meta_data

    @property
    def request_id(self):
        """Gets the request_id of this IdentificationResponse.  

        The RequestId  

        :return: The request_id of this IdentificationResponse.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this IdentificationResponse.

        The RequestId  

        :param request_id: The request_id of this IdentificationResponse.  
        :type: str
        """

        self._request_id = request_id

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
        if not isinstance(other, IdentificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
