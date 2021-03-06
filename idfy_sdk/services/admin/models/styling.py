# coding: utf-8

"""
    Idfy.Admin

    In this API you can manage your account details, logo, styling or manage your openid / oauth api clients. If you are a dealer you can also manage the accounts registered to this dealer.   ## Last update   Last build date for this API: 14.01.2018  

"""


import pprint
import re
from typing import List, Dict
from datetime import datetime as datetime


class Styling(object):
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
        'base64_encoded_css_data': str,
        'file_name': str
    }

    attribute_map = {
        'account_id': 'AccountId',
        'base64_encoded_css_data': 'Base64EncodedCssData',
        'file_name': 'FileName'
    }

    def __init__(self, account_id=None, base64_encoded_css_data=None, file_name=None):

        self._account_id = None
        self._base64_encoded_css_data = None
        self._file_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if base64_encoded_css_data is not None:
            self.base64_encoded_css_data = base64_encoded_css_data
        if file_name is not None:
            self.file_name = file_name

    @property
    def account_id(self):
        """Gets the account_id of this Styling.


        :return: The account_id of this Styling.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Styling.


        :param account_id: The account_id of this Styling.
        :type: str
        """

        self._account_id = account_id

    @property
    def base64_encoded_css_data(self):
        """Gets the base64_encoded_css_data of this Styling.


        :return: The base64_encoded_css_data of this Styling.
        :rtype: str
        """
        return self._base64_encoded_css_data

    @base64_encoded_css_data.setter
    def base64_encoded_css_data(self, base64_encoded_css_data):
        """Sets the base64_encoded_css_data of this Styling.


        :param base64_encoded_css_data: The base64_encoded_css_data of this Styling.
        :type: str
        """

        self._base64_encoded_css_data = base64_encoded_css_data

    @property
    def file_name(self):
        """Gets the file_name of this Styling.


        :return: The file_name of this Styling.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this Styling.


        :param file_name: The file_name of this Styling.
        :type: str
        """

        self._file_name = file_name

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
        if not isinstance(other, Styling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
