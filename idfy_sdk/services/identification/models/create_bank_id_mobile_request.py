# coding: utf-8

"""
    Idfy Identification

    This endpoint enables authentication/identification through multiple identity providers such as Norwegian BankID, Swedish BankID and NemID. ## Last update   Last build date for this endpoint: 02.04.2019

"""


import pprint
import re
from typing import List, Dict
from datetime import datetime as datetime


class CreateBankIDMobileRequest(object):
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
        'mobile_number': str,
        'date_of_birth': str,
        'get_social_security_number': bool,
        'external_reference': str,
        'addonservices': Dict[str, str]
    }

    attribute_map = {
        'mobile_number': 'MobileNumber',
        'date_of_birth': 'DateOfBirth',
        'get_social_security_number': 'GetSocialSecurityNumber',
        'external_reference': 'ExternalReference',
        'addonservices': 'Addonservices'
    }

    def __init__(self, mobile_number=None, date_of_birth=None, get_social_security_number=None, external_reference=None, addonservices=None):

        self._mobile_number = None
        self._date_of_birth = None
        self._get_social_security_number = None
        self._external_reference = None
        self._addonservices = None
        self.discriminator = None

        if mobile_number is not None:
            self.mobile_number = mobile_number
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if get_social_security_number is not None:
            self.get_social_security_number = get_social_security_number
        if external_reference is not None:
            self.external_reference = external_reference
        if addonservices is not None:
            self.addonservices = addonservices

    @property
    def mobile_number(self):
        """Gets the mobile_number of this CreateBankIDMobileRequest.

        Mobile number for the user that is to be identified

        :return: The mobile_number of this CreateBankIDMobileRequest.
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """Sets the mobile_number of this CreateBankIDMobileRequest.

        Mobile number for the user that is to be identified

        :param mobile_number: The mobile_number of this CreateBankIDMobileRequest.
        :type: str
        """

        self._mobile_number = mobile_number

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this CreateBankIDMobileRequest.

        Date of birth for the user that is to be identified

        :return: The date_of_birth of this CreateBankIDMobileRequest.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this CreateBankIDMobileRequest.

        Date of birth for the user that is to be identified

        :param date_of_birth: The date_of_birth of this CreateBankIDMobileRequest.
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def get_social_security_number(self):
        """Gets the get_social_security_number of this CreateBankIDMobileRequest.

        Should the socialsecuritynumber be fetched from the identityprovider? Beware that there is an extra cost of doing this every time and one need permission to do it.

        :return: The get_social_security_number of this CreateBankIDMobileRequest.
        :rtype: bool
        """
        return self._get_social_security_number

    @get_social_security_number.setter
    def get_social_security_number(self, get_social_security_number):
        """Sets the get_social_security_number of this CreateBankIDMobileRequest.

        Should the socialsecuritynumber be fetched from the identityprovider? Beware that there is an extra cost of doing this every time and one need permission to do it.

        :param get_social_security_number: The get_social_security_number of this CreateBankIDMobileRequest.
        :type: bool
        """

        self._get_social_security_number = get_social_security_number

    @property
    def external_reference(self):
        """Gets the external_reference of this CreateBankIDMobileRequest.

        The merchants reference to the identification process

        :return: The external_reference of this CreateBankIDMobileRequest.
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this CreateBankIDMobileRequest.

        The merchants reference to the identification process

        :param external_reference: The external_reference of this CreateBankIDMobileRequest.
        :type: str
        """

        self._external_reference = external_reference

    @property
    def addonservices(self):
        """Gets the addonservices of this CreateBankIDMobileRequest.

        List of addon data that can be orderd. The result will be in MetaData list of the reponse

        :return: The addonservices of this CreateBankIDMobileRequest.
        :rtype: Dict[str, str]
        """
        return self._addonservices

    @addonservices.setter
    def addonservices(self, addonservices):
        """Sets the addonservices of this CreateBankIDMobileRequest.

        List of addon data that can be orderd. The result will be in MetaData list of the reponse

        :param addonservices: The addonservices of this CreateBankIDMobileRequest.
        :type: Dict[str, str]
        """

        self._addonservices = addonservices

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
        if not isinstance(other, CreateBankIDMobileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other