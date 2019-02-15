# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class OwnersAndBoardMembers(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'persons': 'list[PersonAmlResponse]',
        'companies': 'list[CompanyAmlResponse]'
    }

    attribute_map = {
        'persons': 'persons',
        'companies': 'companies'
    }

    def __init__(self, persons=None, companies=None):  
        """OwnersAndBoardMembers"""  

        self._persons = None
        self._companies = None
        self.discriminator = None

        if persons is not None:
            self.persons = persons
        if companies is not None:
            self.companies = companies

    @property
    def persons(self):
        """Gets the persons of this OwnersAndBoardMembers.  

        List of person results, same structure as documented in chapter 5.4 B2C Response, exluding “bisnodeReference”  

        :return: The persons of this OwnersAndBoardMembers.  
        :rtype: list[PersonAmlResponse]
        """
        return self._persons

    @persons.setter
    def persons(self, persons):
        """Sets the persons of this OwnersAndBoardMembers.

        List of person results, same structure as documented in chapter 5.4 B2C Response, exluding “bisnodeReference”  

        :param persons: The persons of this OwnersAndBoardMembers.  
        :type: list[PersonAmlResponse]
        """

        self._persons = persons

    @property
    def companies(self):
        """Gets the companies of this OwnersAndBoardMembers.  

        List of company results, same structure as current table, excluding “bisnodeReference” and “ownersAndBoardMembers”  

        :return: The companies of this OwnersAndBoardMembers.  
        :rtype: list[CompanyAmlResponse]
        """
        return self._companies

    @companies.setter
    def companies(self, companies):
        """Sets the companies of this OwnersAndBoardMembers.

        List of company results, same structure as current table, excluding “bisnodeReference” and “ownersAndBoardMembers”  

        :param companies: The companies of this OwnersAndBoardMembers.  
        :type: list[CompanyAmlResponse]
        """

        self._companies = companies

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
        if not isinstance(other, OwnersAndBoardMembers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

from idfy_sdk.models.company_aml_response import CompanyAmlResponse  
from idfy_sdk.models.person_aml_response import PersonAmlResponse  
