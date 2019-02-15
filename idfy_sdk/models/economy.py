# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Economy(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'year': 'int',
        'turnover': 'int',
        'operating_profit': 'int',
        'equity': 'float',
        'employees': 'int'
    }

    attribute_map = {
        'year': 'Year',
        'turnover': 'Turnover',
        'operating_profit': 'OperatingProfit',
        'equity': 'Equity',
        'employees': 'Employees'
    }

    def __init__(self, year=None, turnover=None, operating_profit=None, equity=None, employees=None):  
        """Economy"""  

        self._year = None
        self._turnover = None
        self._operating_profit = None
        self._equity = None
        self._employees = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if turnover is not None:
            self.turnover = turnover
        if operating_profit is not None:
            self.operating_profit = operating_profit
        if equity is not None:
            self.equity = equity
        if employees is not None:
            self.employees = employees

    @property
    def year(self):
        """Gets the year of this Economy.  


        :return: The year of this Economy.  
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this Economy.


        :param year: The year of this Economy.  
        :type: int
        """

        self._year = year

    @property
    def turnover(self):
        """Gets the turnover of this Economy.  


        :return: The turnover of this Economy.  
        :rtype: int
        """
        return self._turnover

    @turnover.setter
    def turnover(self, turnover):
        """Sets the turnover of this Economy.


        :param turnover: The turnover of this Economy.  
        :type: int
        """

        self._turnover = turnover

    @property
    def operating_profit(self):
        """Gets the operating_profit of this Economy.  


        :return: The operating_profit of this Economy.  
        :rtype: int
        """
        return self._operating_profit

    @operating_profit.setter
    def operating_profit(self, operating_profit):
        """Sets the operating_profit of this Economy.


        :param operating_profit: The operating_profit of this Economy.  
        :type: int
        """

        self._operating_profit = operating_profit

    @property
    def equity(self):
        """Gets the equity of this Economy.  


        :return: The equity of this Economy.  
        :rtype: float
        """
        return self._equity

    @equity.setter
    def equity(self, equity):
        """Sets the equity of this Economy.


        :param equity: The equity of this Economy.  
        :type: float
        """

        self._equity = equity

    @property
    def employees(self):
        """Gets the employees of this Economy.  


        :return: The employees of this Economy.  
        :rtype: int
        """
        return self._employees

    @employees.setter
    def employees(self, employees):
        """Sets the employees of this Economy.


        :param employees: The employees of this Economy.  
        :type: int
        """

        self._employees = employees

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
        if not isinstance(other, Economy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
