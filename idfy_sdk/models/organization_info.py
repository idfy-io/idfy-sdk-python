# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class OrganizationInfo(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'org_no': 'str',
        'company_name': 'str',
        'country_code': 'str'
    }

    attribute_map = {
        'org_no': 'orgNo',
        'company_name': 'companyName',
        'country_code': 'countryCode'
    }

    def __init__(self, org_no=None, company_name=None, country_code=None):  
        """OrganizationInfo"""  

        self._org_no = None
        self._company_name = None
        self._country_code = None
        self.discriminator = None

        if org_no is not None:
            self.org_no = org_no
        if company_name is not None:
            self.company_name = company_name
        if country_code is not None:
            self.country_code = country_code

    @property
    def org_no(self):
        """Gets the org_no of this OrganizationInfo.  


        :return: The org_no of this OrganizationInfo.  
        :rtype: str
        """
        return self._org_no

    @org_no.setter
    def org_no(self, org_no):
        """Sets the org_no of this OrganizationInfo.


        :param org_no: The org_no of this OrganizationInfo.  
        :type: str
        """

        self._org_no = org_no

    @property
    def company_name(self):
        """Gets the company_name of this OrganizationInfo.  


        :return: The company_name of this OrganizationInfo.  
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this OrganizationInfo.


        :param company_name: The company_name of this OrganizationInfo.  
        :type: str
        """

        self._company_name = company_name

    @property
    def country_code(self):
        """Gets the country_code of this OrganizationInfo.  


        :return: The country_code of this OrganizationInfo.  
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this OrganizationInfo.


        :param country_code: The country_code of this OrganizationInfo.  
        :type: str
        """

        self._country_code = country_code

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
        if not isinstance(other, OrganizationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
