# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.economy import Economy  
from idfy_sdk.models.hent_foretak_response import HentForetakResponse  


class CreditCheckCompanyResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'org_number': 'int',
        'org_name': 'str',
        'address': 'str',
        'postal_code': 'str',
        'city': 'str',
        'incorporation_date': 'datetime',
        'chair_man': 'str',
        'ceo': 'str',
        'economy': 'Economy',
        'bisnode_rating_code': 'str',
        'bisnode_rating_description': 'str',
        'credit_limit': 'float',
        'payment_defaults': 'str',
        'request_id': 'str',
        'report': 'str',
        'detailed_information': 'HentForetakResponse',
        'number_of_payment_defaults': 'int'
    }

    attribute_map = {
        'org_number': 'OrgNumber',
        'org_name': 'OrgName',
        'address': 'Address',
        'postal_code': 'PostalCode',
        'city': 'City',
        'incorporation_date': 'IncorporationDate',
        'chair_man': 'ChairMan',
        'ceo': 'CEO',
        'economy': 'Economy',
        'bisnode_rating_code': 'BisnodeRatingCode',
        'bisnode_rating_description': 'BisnodeRatingDescription',
        'credit_limit': 'CreditLimit',
        'payment_defaults': 'PaymentDefaults',
        'request_id': 'RequestId',
        'report': 'Report',
        'detailed_information': 'DetailedInformation',
        'number_of_payment_defaults': 'NumberOfPaymentDefaults'
    }

    def __init__(self, org_number=None, org_name=None, address=None, postal_code=None, city=None, incorporation_date=None, chair_man=None, ceo=None, economy=None, bisnode_rating_code=None, bisnode_rating_description=None, credit_limit=None, payment_defaults=None, request_id=None, report=None, detailed_information=None, number_of_payment_defaults=None):  
        """CreditCheckCompanyResponse"""  

        self._org_number = None
        self._org_name = None
        self._address = None
        self._postal_code = None
        self._city = None
        self._incorporation_date = None
        self._chair_man = None
        self._ceo = None
        self._economy = None
        self._bisnode_rating_code = None
        self._bisnode_rating_description = None
        self._credit_limit = None
        self._payment_defaults = None
        self._request_id = None
        self._report = None
        self._detailed_information = None
        self._number_of_payment_defaults = None
        self.discriminator = None

        if org_number is not None:
            self.org_number = org_number
        if org_name is not None:
            self.org_name = org_name
        if address is not None:
            self.address = address
        if postal_code is not None:
            self.postal_code = postal_code
        if city is not None:
            self.city = city
        if incorporation_date is not None:
            self.incorporation_date = incorporation_date
        if chair_man is not None:
            self.chair_man = chair_man
        if ceo is not None:
            self.ceo = ceo
        if economy is not None:
            self.economy = economy
        if bisnode_rating_code is not None:
            self.bisnode_rating_code = bisnode_rating_code
        if bisnode_rating_description is not None:
            self.bisnode_rating_description = bisnode_rating_description
        if credit_limit is not None:
            self.credit_limit = credit_limit
        if payment_defaults is not None:
            self.payment_defaults = payment_defaults
        if request_id is not None:
            self.request_id = request_id
        if report is not None:
            self.report = report
        if detailed_information is not None:
            self.detailed_information = detailed_information
        if number_of_payment_defaults is not None:
            self.number_of_payment_defaults = number_of_payment_defaults

    @property
    def org_number(self):
        """Gets the org_number of this CreditCheckCompanyResponse.  


        :return: The org_number of this CreditCheckCompanyResponse.  
        :rtype: int
        """
        return self._org_number

    @org_number.setter
    def org_number(self, org_number):
        """Sets the org_number of this CreditCheckCompanyResponse.


        :param org_number: The org_number of this CreditCheckCompanyResponse.  
        :type: int
        """

        self._org_number = org_number

    @property
    def org_name(self):
        """Gets the org_name of this CreditCheckCompanyResponse.  


        :return: The org_name of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this CreditCheckCompanyResponse.


        :param org_name: The org_name of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._org_name = org_name

    @property
    def address(self):
        """Gets the address of this CreditCheckCompanyResponse.  


        :return: The address of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreditCheckCompanyResponse.


        :param address: The address of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._address = address

    @property
    def postal_code(self):
        """Gets the postal_code of this CreditCheckCompanyResponse.  


        :return: The postal_code of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this CreditCheckCompanyResponse.


        :param postal_code: The postal_code of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._postal_code = postal_code

    @property
    def city(self):
        """Gets the city of this CreditCheckCompanyResponse.  


        :return: The city of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CreditCheckCompanyResponse.


        :param city: The city of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._city = city

    @property
    def incorporation_date(self):
        """Gets the incorporation_date of this CreditCheckCompanyResponse.  


        :return: The incorporation_date of this CreditCheckCompanyResponse.  
        :rtype: datetime
        """
        return self._incorporation_date

    @incorporation_date.setter
    def incorporation_date(self, incorporation_date):
        """Sets the incorporation_date of this CreditCheckCompanyResponse.


        :param incorporation_date: The incorporation_date of this CreditCheckCompanyResponse.  
        :type: datetime
        """

        self._incorporation_date = incorporation_date

    @property
    def chair_man(self):
        """Gets the chair_man of this CreditCheckCompanyResponse.  


        :return: The chair_man of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._chair_man

    @chair_man.setter
    def chair_man(self, chair_man):
        """Sets the chair_man of this CreditCheckCompanyResponse.


        :param chair_man: The chair_man of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._chair_man = chair_man

    @property
    def ceo(self):
        """Gets the ceo of this CreditCheckCompanyResponse.  


        :return: The ceo of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._ceo

    @ceo.setter
    def ceo(self, ceo):
        """Sets the ceo of this CreditCheckCompanyResponse.


        :param ceo: The ceo of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._ceo = ceo

    @property
    def economy(self):
        """Gets the economy of this CreditCheckCompanyResponse.  


        :return: The economy of this CreditCheckCompanyResponse.  
        :rtype: Economy
        """
        return self._economy

    @economy.setter
    def economy(self, economy):
        """Sets the economy of this CreditCheckCompanyResponse.


        :param economy: The economy of this CreditCheckCompanyResponse.  
        :type: Economy
        """

        self._economy = economy

    @property
    def bisnode_rating_code(self):
        """Gets the bisnode_rating_code of this CreditCheckCompanyResponse.  


        :return: The bisnode_rating_code of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._bisnode_rating_code

    @bisnode_rating_code.setter
    def bisnode_rating_code(self, bisnode_rating_code):
        """Sets the bisnode_rating_code of this CreditCheckCompanyResponse.


        :param bisnode_rating_code: The bisnode_rating_code of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._bisnode_rating_code = bisnode_rating_code

    @property
    def bisnode_rating_description(self):
        """Gets the bisnode_rating_description of this CreditCheckCompanyResponse.  


        :return: The bisnode_rating_description of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._bisnode_rating_description

    @bisnode_rating_description.setter
    def bisnode_rating_description(self, bisnode_rating_description):
        """Sets the bisnode_rating_description of this CreditCheckCompanyResponse.


        :param bisnode_rating_description: The bisnode_rating_description of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._bisnode_rating_description = bisnode_rating_description

    @property
    def credit_limit(self):
        """Gets the credit_limit of this CreditCheckCompanyResponse.  


        :return: The credit_limit of this CreditCheckCompanyResponse.  
        :rtype: float
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        """Sets the credit_limit of this CreditCheckCompanyResponse.


        :param credit_limit: The credit_limit of this CreditCheckCompanyResponse.  
        :type: float
        """

        self._credit_limit = credit_limit

    @property
    def payment_defaults(self):
        """Gets the payment_defaults of this CreditCheckCompanyResponse.  


        :return: The payment_defaults of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._payment_defaults

    @payment_defaults.setter
    def payment_defaults(self, payment_defaults):
        """Sets the payment_defaults of this CreditCheckCompanyResponse.


        :param payment_defaults: The payment_defaults of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._payment_defaults = payment_defaults

    @property
    def request_id(self):
        """Gets the request_id of this CreditCheckCompanyResponse.  


        :return: The request_id of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreditCheckCompanyResponse.


        :param request_id: The request_id of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._request_id = request_id

    @property
    def report(self):
        """Gets the report of this CreditCheckCompanyResponse.  


        :return: The report of this CreditCheckCompanyResponse.  
        :rtype: str
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this CreditCheckCompanyResponse.


        :param report: The report of this CreditCheckCompanyResponse.  
        :type: str
        """

        self._report = report

    @property
    def detailed_information(self):
        """Gets the detailed_information of this CreditCheckCompanyResponse.  


        :return: The detailed_information of this CreditCheckCompanyResponse.  
        :rtype: HentForetakResponse
        """
        return self._detailed_information

    @detailed_information.setter
    def detailed_information(self, detailed_information):
        """Sets the detailed_information of this CreditCheckCompanyResponse.


        :param detailed_information: The detailed_information of this CreditCheckCompanyResponse.  
        :type: HentForetakResponse
        """

        self._detailed_information = detailed_information

    @property
    def number_of_payment_defaults(self):
        """Gets the number_of_payment_defaults of this CreditCheckCompanyResponse.  


        :return: The number_of_payment_defaults of this CreditCheckCompanyResponse.  
        :rtype: int
        """
        return self._number_of_payment_defaults

    @number_of_payment_defaults.setter
    def number_of_payment_defaults(self, number_of_payment_defaults):
        """Sets the number_of_payment_defaults of this CreditCheckCompanyResponse.


        :param number_of_payment_defaults: The number_of_payment_defaults of this CreditCheckCompanyResponse.  
        :type: int
        """

        self._number_of_payment_defaults = number_of_payment_defaults

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
        if not isinstance(other, CreditCheckCompanyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
