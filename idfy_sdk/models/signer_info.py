# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.mobile import Mobile  
from idfy_sdk.models.organization_info import OrganizationInfo  


class SignerInfo(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'social_security_number': 'str',
        'mobile': 'Mobile',
        'organization_info': 'OrganizationInfo'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'social_security_number': 'socialSecurityNumber',
        'mobile': 'mobile',
        'organization_info': 'organizationInfo'
    }

    def __init__(self, first_name=None, last_name=None, email=None, social_security_number=None, mobile=None, organization_info=None):  
        """SignerInfo"""  

        self._first_name = None
        self._last_name = None
        self._email = None
        self._social_security_number = None
        self._mobile = None
        self._organization_info = None
        self.discriminator = None

        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if social_security_number is not None:
            self.social_security_number = social_security_number
        if mobile is not None:
            self.mobile = mobile
        if organization_info is not None:
            self.organization_info = organization_info

    @property
    def first_name(self):
        """Gets the first_name of this SignerInfo.  

        The signer's first name.  

        :return: The first_name of this SignerInfo.  
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SignerInfo.

        The signer's first name.  

        :param first_name: The first_name of this SignerInfo.  
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this SignerInfo.  

        The signer's last name.  

        :return: The last_name of this SignerInfo.  
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SignerInfo.

        The signer's last name.  

        :param last_name: The last_name of this SignerInfo.  
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this SignerInfo.  

        The signer's email adress. Define this if you are using notifications.  

        :return: The email of this SignerInfo.  
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SignerInfo.

        The signer's email adress. Define this if you are using notifications.  

        :param email: The email of this SignerInfo.  
        :type: str
        """

        self._email = email

    @property
    def social_security_number(self):
        """Gets the social_security_number of this SignerInfo.  

        Prefilled social security number.  

        :return: The social_security_number of this SignerInfo.  
        :rtype: str
        """
        return self._social_security_number

    @social_security_number.setter
    def social_security_number(self, social_security_number):
        """Sets the social_security_number of this SignerInfo.

        Prefilled social security number.  

        :param social_security_number: The social_security_number of this SignerInfo.  
        :type: str
        """

        self._social_security_number = social_security_number

    @property
    def mobile(self):
        """Gets the mobile of this SignerInfo.  


        :return: The mobile of this SignerInfo.  
        :rtype: Mobile
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this SignerInfo.


        :param mobile: The mobile of this SignerInfo.  
        :type: Mobile
        """

        self._mobile = mobile

    @property
    def organization_info(self):
        """Gets the organization_info of this SignerInfo.  


        :return: The organization_info of this SignerInfo.  
        :rtype: OrganizationInfo
        """
        return self._organization_info

    @organization_info.setter
    def organization_info(self, organization_info):
        """Sets the organization_info of this SignerInfo.


        :param organization_info: The organization_info of this SignerInfo.  
        :type: OrganizationInfo
        """

        self._organization_info = organization_info

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
        if not isinstance(other, SignerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
