# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonEconomy(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'year': 'int',
        'net_income': 'float',
        'income_change': 'float',
        'fortune': 'float',
        'assessed_tax': 'float',
        'tax_class': 'str',
        'municipal': 'str',
        'municipal_number': 'str'
    }

    attribute_map = {
        'year': 'Year',
        'net_income': 'NetIncome',
        'income_change': 'IncomeChange',
        'fortune': 'Fortune',
        'assessed_tax': 'AssessedTax',
        'tax_class': 'TaxClass',
        'municipal': 'Municipal',
        'municipal_number': 'MunicipalNumber'
    }

    def __init__(self, year=None, net_income=None, income_change=None, fortune=None, assessed_tax=None, tax_class=None, municipal=None, municipal_number=None):  
        """PersonEconomy"""  

        self._year = None
        self._net_income = None
        self._income_change = None
        self._fortune = None
        self._assessed_tax = None
        self._tax_class = None
        self._municipal = None
        self._municipal_number = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if net_income is not None:
            self.net_income = net_income
        if income_change is not None:
            self.income_change = income_change
        if fortune is not None:
            self.fortune = fortune
        if assessed_tax is not None:
            self.assessed_tax = assessed_tax
        if tax_class is not None:
            self.tax_class = tax_class
        if municipal is not None:
            self.municipal = municipal
        if municipal_number is not None:
            self.municipal_number = municipal_number

    @property
    def year(self):
        """Gets the year of this PersonEconomy.  


        :return: The year of this PersonEconomy.  
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this PersonEconomy.


        :param year: The year of this PersonEconomy.  
        :type: int
        """

        self._year = year

    @property
    def net_income(self):
        """Gets the net_income of this PersonEconomy.  


        :return: The net_income of this PersonEconomy.  
        :rtype: float
        """
        return self._net_income

    @net_income.setter
    def net_income(self, net_income):
        """Sets the net_income of this PersonEconomy.


        :param net_income: The net_income of this PersonEconomy.  
        :type: float
        """

        self._net_income = net_income

    @property
    def income_change(self):
        """Gets the income_change of this PersonEconomy.  


        :return: The income_change of this PersonEconomy.  
        :rtype: float
        """
        return self._income_change

    @income_change.setter
    def income_change(self, income_change):
        """Sets the income_change of this PersonEconomy.


        :param income_change: The income_change of this PersonEconomy.  
        :type: float
        """

        self._income_change = income_change

    @property
    def fortune(self):
        """Gets the fortune of this PersonEconomy.  


        :return: The fortune of this PersonEconomy.  
        :rtype: float
        """
        return self._fortune

    @fortune.setter
    def fortune(self, fortune):
        """Sets the fortune of this PersonEconomy.


        :param fortune: The fortune of this PersonEconomy.  
        :type: float
        """

        self._fortune = fortune

    @property
    def assessed_tax(self):
        """Gets the assessed_tax of this PersonEconomy.  


        :return: The assessed_tax of this PersonEconomy.  
        :rtype: float
        """
        return self._assessed_tax

    @assessed_tax.setter
    def assessed_tax(self, assessed_tax):
        """Sets the assessed_tax of this PersonEconomy.


        :param assessed_tax: The assessed_tax of this PersonEconomy.  
        :type: float
        """

        self._assessed_tax = assessed_tax

    @property
    def tax_class(self):
        """Gets the tax_class of this PersonEconomy.  


        :return: The tax_class of this PersonEconomy.  
        :rtype: str
        """
        return self._tax_class

    @tax_class.setter
    def tax_class(self, tax_class):
        """Sets the tax_class of this PersonEconomy.


        :param tax_class: The tax_class of this PersonEconomy.  
        :type: str
        """

        self._tax_class = tax_class

    @property
    def municipal(self):
        """Gets the municipal of this PersonEconomy.  


        :return: The municipal of this PersonEconomy.  
        :rtype: str
        """
        return self._municipal

    @municipal.setter
    def municipal(self, municipal):
        """Sets the municipal of this PersonEconomy.


        :param municipal: The municipal of this PersonEconomy.  
        :type: str
        """

        self._municipal = municipal

    @property
    def municipal_number(self):
        """Gets the municipal_number of this PersonEconomy.  


        :return: The municipal_number of this PersonEconomy.  
        :rtype: str
        """
        return self._municipal_number

    @municipal_number.setter
    def municipal_number(self, municipal_number):
        """Sets the municipal_number of this PersonEconomy.


        :param municipal_number: The municipal_number of this PersonEconomy.  
        :type: str
        """

        self._municipal_number = municipal_number

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
        if not isinstance(other, PersonEconomy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
