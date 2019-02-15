# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.onboarding import Onboarding  


class Dealer(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'customer_number': 'int',
        'mva_number': 'str',
        'company_phone': 'str',
        'company_email': 'str',
        'company_url': 'str',
        'onboarding': 'Onboarding'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'customer_number': 'CustomerNumber',
        'mva_number': 'MvaNumber',
        'company_phone': 'CompanyPhone',
        'company_email': 'CompanyEmail',
        'company_url': 'CompanyUrl',
        'onboarding': 'Onboarding'
    }

    def __init__(self, id=None, name=None, customer_number=None, mva_number=None, company_phone=None, company_email=None, company_url=None, onboarding=None):  
        """Dealer"""  

        self._id = None
        self._name = None
        self._customer_number = None
        self._mva_number = None
        self._company_phone = None
        self._company_email = None
        self._company_url = None
        self._onboarding = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.customer_number = customer_number
        if mva_number is not None:
            self.mva_number = mva_number
        if company_phone is not None:
            self.company_phone = company_phone
        if company_email is not None:
            self.company_email = company_email
        if company_url is not None:
            self.company_url = company_url
        if onboarding is not None:
            self.onboarding = onboarding

    @property
    def id(self):
        """Gets the id of this Dealer.  


        :return: The id of this Dealer.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Dealer.


        :param id: The id of this Dealer.  
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  

        self._id = id

    @property
    def name(self):
        """Gets the name of this Dealer.  


        :return: The name of this Dealer.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dealer.


        :param name: The name of this Dealer.  
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  

        self._name = name

    @property
    def customer_number(self):
        """Gets the customer_number of this Dealer.  


        :return: The customer_number of this Dealer.  
        :rtype: int
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this Dealer.


        :param customer_number: The customer_number of this Dealer.  
        :type: int
        """
        if customer_number is None:
            raise ValueError("Invalid value for `customer_number`, must not be `None`")  

        self._customer_number = customer_number

    @property
    def mva_number(self):
        """Gets the mva_number of this Dealer.  


        :return: The mva_number of this Dealer.  
        :rtype: str
        """
        return self._mva_number

    @mva_number.setter
    def mva_number(self, mva_number):
        """Sets the mva_number of this Dealer.


        :param mva_number: The mva_number of this Dealer.  
        :type: str
        """

        self._mva_number = mva_number

    @property
    def company_phone(self):
        """Gets the company_phone of this Dealer.  


        :return: The company_phone of this Dealer.  
        :rtype: str
        """
        return self._company_phone

    @company_phone.setter
    def company_phone(self, company_phone):
        """Sets the company_phone of this Dealer.


        :param company_phone: The company_phone of this Dealer.  
        :type: str
        """

        self._company_phone = company_phone

    @property
    def company_email(self):
        """Gets the company_email of this Dealer.  


        :return: The company_email of this Dealer.  
        :rtype: str
        """
        return self._company_email

    @company_email.setter
    def company_email(self, company_email):
        """Sets the company_email of this Dealer.


        :param company_email: The company_email of this Dealer.  
        :type: str
        """

        self._company_email = company_email

    @property
    def company_url(self):
        """Gets the company_url of this Dealer.  


        :return: The company_url of this Dealer.  
        :rtype: str
        """
        return self._company_url

    @company_url.setter
    def company_url(self, company_url):
        """Sets the company_url of this Dealer.


        :param company_url: The company_url of this Dealer.  
        :type: str
        """

        self._company_url = company_url

    @property
    def onboarding(self):
        """Gets the onboarding of this Dealer.  


        :return: The onboarding of this Dealer.  
        :rtype: Onboarding
        """
        return self._onboarding

    @onboarding.setter
    def onboarding(self, onboarding):
        """Sets the onboarding of this Dealer.


        :param onboarding: The onboarding of this Dealer.  
        :type: Onboarding
        """

        self._onboarding = onboarding

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
        if not isinstance(other, Dealer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
