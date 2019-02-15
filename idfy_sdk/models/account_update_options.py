# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.address import Address  
from idfy_sdk.models.contact import Contact  
from idfy_sdk.models.dealer_info import DealerInfo  
from idfy_sdk.models.settings import Settings  


class AccountUpdateOptions(object):

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
        'mva_number': 'str',
        'company_phone': 'str',
        'company_email': 'str',
        'company_url': 'str',
        'contact': 'Contact',
        'address': 'Address',
        'dealer': 'DealerInfo',
        'settings': 'Settings',
        'country': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'mva_number': 'MvaNumber',
        'company_phone': 'CompanyPhone',
        'company_email': 'CompanyEmail',
        'company_url': 'CompanyUrl',
        'contact': 'Contact',
        'address': 'Address',
        'dealer': 'Dealer',
        'settings': 'Settings',
        'country': 'Country'
    }

    def __init__(self, id=None, name=None, mva_number=None, company_phone=None, company_email=None, company_url=None, contact=None, address=None, dealer=None, settings=None, country=None):  
        """UpdateAccountRequest"""  

        self._id = None
        self._name = None
        self._mva_number = None
        self._company_phone = None
        self._company_email = None
        self._company_url = None
        self._contact = None
        self._address = None
        self._dealer = None
        self._settings = None
        self._country = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.mva_number = mva_number
        self.company_phone = company_phone
        self.company_email = company_email
        if company_url is not None:
            self.company_url = company_url
        if contact is not None:
            self.contact = contact
        if address is not None:
            self.address = address
        if dealer is not None:
            self.dealer = dealer
        if settings is not None:
            self.settings = settings
        if country is not None:
            self.country = country

    @property
    def id(self):
        """Gets the id of this UpdateAccountRequest.  

        Account Id  

        :return: The id of this UpdateAccountRequest.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateAccountRequest.

        Account Id  

        :param id: The id of this UpdateAccountRequest.  
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  

        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateAccountRequest.  

        Name of the account owner (company)  

        :return: The name of this UpdateAccountRequest.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAccountRequest.

        Name of the account owner (company)  

        :param name: The name of this UpdateAccountRequest.  
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  

        self._name = name

    @property
    def mva_number(self):
        """Gets the mva_number of this UpdateAccountRequest.  

        Mva / Organization number  

        :return: The mva_number of this UpdateAccountRequest.  
        :rtype: str
        """
        return self._mva_number

    @mva_number.setter
    def mva_number(self, mva_number):
        """Sets the mva_number of this UpdateAccountRequest.

        Mva / Organization number  

        :param mva_number: The mva_number of this UpdateAccountRequest.  
        :type: str
        """
        if mva_number is None:
            raise ValueError("Invalid value for `mva_number`, must not be `None`")  

        self._mva_number = mva_number

    @property
    def company_phone(self):
        """Gets the company_phone of this UpdateAccountRequest.  


        :return: The company_phone of this UpdateAccountRequest.  
        :rtype: str
        """
        return self._company_phone

    @company_phone.setter
    def company_phone(self, company_phone):
        """Sets the company_phone of this UpdateAccountRequest.


        :param company_phone: The company_phone of this UpdateAccountRequest.  
        :type: str
        """
        if company_phone is None:
            raise ValueError("Invalid value for `company_phone`, must not be `None`")  

        self._company_phone = company_phone

    @property
    def company_email(self):
        """Gets the company_email of this UpdateAccountRequest.  


        :return: The company_email of this UpdateAccountRequest.  
        :rtype: str
        """
        return self._company_email

    @company_email.setter
    def company_email(self, company_email):
        """Sets the company_email of this UpdateAccountRequest.


        :param company_email: The company_email of this UpdateAccountRequest.  
        :type: str
        """
        if company_email is None:
            raise ValueError("Invalid value for `company_email`, must not be `None`")  

        self._company_email = company_email

    @property
    def company_url(self):
        """Gets the company_url of this UpdateAccountRequest.  


        :return: The company_url of this UpdateAccountRequest.  
        :rtype: str
        """
        return self._company_url

    @company_url.setter
    def company_url(self, company_url):
        """Sets the company_url of this UpdateAccountRequest.


        :param company_url: The company_url of this UpdateAccountRequest.  
        :type: str
        """

        self._company_url = company_url

    @property
    def contact(self):
        """Gets the contact of this UpdateAccountRequest.  


        :return: The contact of this UpdateAccountRequest.  
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this UpdateAccountRequest.


        :param contact: The contact of this UpdateAccountRequest.  
        :type: Contact
        """

        self._contact = contact

    @property
    def address(self):
        """Gets the address of this UpdateAccountRequest.  


        :return: The address of this UpdateAccountRequest.  
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UpdateAccountRequest.


        :param address: The address of this UpdateAccountRequest.  
        :type: Address
        """

        self._address = address

    @property
    def dealer(self):
        """Gets the dealer of this UpdateAccountRequest.  


        :return: The dealer of this UpdateAccountRequest.  
        :rtype: DealerInfo
        """
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):
        """Sets the dealer of this UpdateAccountRequest.


        :param dealer: The dealer of this UpdateAccountRequest.  
        :type: DealerInfo
        """

        self._dealer = dealer

    @property
    def settings(self):
        """Gets the settings of this UpdateAccountRequest.  


        :return: The settings of this UpdateAccountRequest.  
        :rtype: Settings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this UpdateAccountRequest.


        :param settings: The settings of this UpdateAccountRequest.  
        :type: Settings
        """

        self._settings = settings

    @property
    def country(self):
        """Gets the country of this UpdateAccountRequest.  


        :return: The country of this UpdateAccountRequest.  
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UpdateAccountRequest.


        :param country: The country of this UpdateAccountRequest.  
        :type: str
        """

        self._country = country

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
        if not isinstance(other, AccountUpdateOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
