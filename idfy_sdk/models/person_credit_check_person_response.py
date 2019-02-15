# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.person_economy import PersonEconomy  
from idfy_sdk.models.person_hent_person_response import PersonHentPersonResponse  


class PersonCreditCheckPersonResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'report': 'str',
        'name': 'str',
        'address': 'str',
        'city': 'str',
        'postal_code': 'str',
        'score': 'int',
        'score_decision': 'str',
        'date_of_birth': 'str',
        'age': 'int',
        'gender': 'str',
        'number_of_payment_defaults': 'int',
        'payment_defaults_amount': 'float',
        'income_and_fortune': 'list[PersonEconomy]',
        'detailed_information': 'PersonHentPersonResponse'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'report': 'Report',
        'name': 'Name',
        'address': 'Address',
        'city': 'City',
        'postal_code': 'PostalCode',
        'score': 'Score',
        'score_decision': 'ScoreDecision',
        'date_of_birth': 'DateOfBirth',
        'age': 'Age',
        'gender': 'Gender',
        'number_of_payment_defaults': 'NumberOfPaymentDefaults',
        'payment_defaults_amount': 'PaymentDefaultsAmount',
        'income_and_fortune': 'IncomeAndFortune',
        'detailed_information': 'DetailedInformation'
    }

    def __init__(self, request_id=None, report=None, name=None, address=None, city=None, postal_code=None, score=None, score_decision=None, date_of_birth=None, age=None, gender=None, number_of_payment_defaults=None, payment_defaults_amount=None, income_and_fortune=None, detailed_information=None):  
        """PersonCreditCheckPersonResponse"""  

        self._request_id = None
        self._report = None
        self._name = None
        self._address = None
        self._city = None
        self._postal_code = None
        self._score = None
        self._score_decision = None
        self._date_of_birth = None
        self._age = None
        self._gender = None
        self._number_of_payment_defaults = None
        self._payment_defaults_amount = None
        self._income_and_fortune = None
        self._detailed_information = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if report is not None:
            self.report = report
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if city is not None:
            self.city = city
        if postal_code is not None:
            self.postal_code = postal_code
        if score is not None:
            self.score = score
        if score_decision is not None:
            self.score_decision = score_decision
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if age is not None:
            self.age = age
        if gender is not None:
            self.gender = gender
        if number_of_payment_defaults is not None:
            self.number_of_payment_defaults = number_of_payment_defaults
        if payment_defaults_amount is not None:
            self.payment_defaults_amount = payment_defaults_amount
        if income_and_fortune is not None:
            self.income_and_fortune = income_and_fortune
        if detailed_information is not None:
            self.detailed_information = detailed_information

    @property
    def request_id(self):
        """Gets the request_id of this PersonCreditCheckPersonResponse.  


        :return: The request_id of this PersonCreditCheckPersonResponse.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PersonCreditCheckPersonResponse.


        :param request_id: The request_id of this PersonCreditCheckPersonResponse.  
        :type: str
        """

        self._request_id = request_id

    @property
    def report(self):
        """Gets the report of this PersonCreditCheckPersonResponse.  


        :return: The report of this PersonCreditCheckPersonResponse.  
        :rtype: str
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this PersonCreditCheckPersonResponse.


        :param report: The report of this PersonCreditCheckPersonResponse.  
        :type: str
        """

        self._report = report

    @property
    def name(self):
        """Gets the name of this PersonCreditCheckPersonResponse.  


        :return: The name of this PersonCreditCheckPersonResponse.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PersonCreditCheckPersonResponse.


        :param name: The name of this PersonCreditCheckPersonResponse.  
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this PersonCreditCheckPersonResponse.  


        :return: The address of this PersonCreditCheckPersonResponse.  
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PersonCreditCheckPersonResponse.


        :param address: The address of this PersonCreditCheckPersonResponse.  
        :type: str
        """

        self._address = address

    @property
    def city(self):
        """Gets the city of this PersonCreditCheckPersonResponse.  


        :return: The city of this PersonCreditCheckPersonResponse.  
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PersonCreditCheckPersonResponse.


        :param city: The city of this PersonCreditCheckPersonResponse.  
        :type: str
        """

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this PersonCreditCheckPersonResponse.  


        :return: The postal_code of this PersonCreditCheckPersonResponse.  
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this PersonCreditCheckPersonResponse.


        :param postal_code: The postal_code of this PersonCreditCheckPersonResponse.  
        :type: str
        """

        self._postal_code = postal_code

    @property
    def score(self):
        """Gets the score of this PersonCreditCheckPersonResponse.  


        :return: The score of this PersonCreditCheckPersonResponse.  
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this PersonCreditCheckPersonResponse.


        :param score: The score of this PersonCreditCheckPersonResponse.  
        :type: int
        """

        self._score = score

    @property
    def score_decision(self):
        """Gets the score_decision of this PersonCreditCheckPersonResponse.  


        :return: The score_decision of this PersonCreditCheckPersonResponse.  
        :rtype: str
        """
        return self._score_decision

    @score_decision.setter
    def score_decision(self, score_decision):
        """Sets the score_decision of this PersonCreditCheckPersonResponse.


        :param score_decision: The score_decision of this PersonCreditCheckPersonResponse.  
        :type: str
        """

        self._score_decision = score_decision

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this PersonCreditCheckPersonResponse.  


        :return: The date_of_birth of this PersonCreditCheckPersonResponse.  
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this PersonCreditCheckPersonResponse.


        :param date_of_birth: The date_of_birth of this PersonCreditCheckPersonResponse.  
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def age(self):
        """Gets the age of this PersonCreditCheckPersonResponse.  


        :return: The age of this PersonCreditCheckPersonResponse.  
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this PersonCreditCheckPersonResponse.


        :param age: The age of this PersonCreditCheckPersonResponse.  
        :type: int
        """

        self._age = age

    @property
    def gender(self):
        """Gets the gender of this PersonCreditCheckPersonResponse.  


        :return: The gender of this PersonCreditCheckPersonResponse.  
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this PersonCreditCheckPersonResponse.


        :param gender: The gender of this PersonCreditCheckPersonResponse.  
        :type: str
        """

        self._gender = gender

    @property
    def number_of_payment_defaults(self):
        """Gets the number_of_payment_defaults of this PersonCreditCheckPersonResponse.  


        :return: The number_of_payment_defaults of this PersonCreditCheckPersonResponse.  
        :rtype: int
        """
        return self._number_of_payment_defaults

    @number_of_payment_defaults.setter
    def number_of_payment_defaults(self, number_of_payment_defaults):
        """Sets the number_of_payment_defaults of this PersonCreditCheckPersonResponse.


        :param number_of_payment_defaults: The number_of_payment_defaults of this PersonCreditCheckPersonResponse.  
        :type: int
        """

        self._number_of_payment_defaults = number_of_payment_defaults

    @property
    def payment_defaults_amount(self):
        """Gets the payment_defaults_amount of this PersonCreditCheckPersonResponse.  


        :return: The payment_defaults_amount of this PersonCreditCheckPersonResponse.  
        :rtype: float
        """
        return self._payment_defaults_amount

    @payment_defaults_amount.setter
    def payment_defaults_amount(self, payment_defaults_amount):
        """Sets the payment_defaults_amount of this PersonCreditCheckPersonResponse.


        :param payment_defaults_amount: The payment_defaults_amount of this PersonCreditCheckPersonResponse.  
        :type: float
        """

        self._payment_defaults_amount = payment_defaults_amount

    @property
    def income_and_fortune(self):
        """Gets the income_and_fortune of this PersonCreditCheckPersonResponse.  


        :return: The income_and_fortune of this PersonCreditCheckPersonResponse.  
        :rtype: list[PersonEconomy]
        """
        return self._income_and_fortune

    @income_and_fortune.setter
    def income_and_fortune(self, income_and_fortune):
        """Sets the income_and_fortune of this PersonCreditCheckPersonResponse.


        :param income_and_fortune: The income_and_fortune of this PersonCreditCheckPersonResponse.  
        :type: list[PersonEconomy]
        """

        self._income_and_fortune = income_and_fortune

    @property
    def detailed_information(self):
        """Gets the detailed_information of this PersonCreditCheckPersonResponse.  


        :return: The detailed_information of this PersonCreditCheckPersonResponse.  
        :rtype: PersonHentPersonResponse
        """
        return self._detailed_information

    @detailed_information.setter
    def detailed_information(self, detailed_information):
        """Sets the detailed_information of this PersonCreditCheckPersonResponse.


        :param detailed_information: The detailed_information of this PersonCreditCheckPersonResponse.  
        :type: PersonHentPersonResponse
        """

        self._detailed_information = detailed_information

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
        if not isinstance(other, PersonCreditCheckPersonResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
