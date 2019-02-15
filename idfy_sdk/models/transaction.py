# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Transaction(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'date': 'datetime',
        'product_id': 'str',
        'description': 'str',
        'count': 'int',
        'customer_number': 'int',
        'external_reference': 'str',
        'department_id': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'date': 'Date',
        'product_id': 'ProductID',
        'description': 'Description',
        'count': 'Count',
        'customer_number': 'CustomerNumber',
        'external_reference': 'ExternalReference',
        'department_id': 'DepartmentId'
    }

    def __init__(self, id=None, date=None, product_id=None, description=None, count=None, customer_number=None, external_reference=None, department_id=None):  
        """Transaction"""  

        self._id = None
        self._date = None
        self._product_id = None
        self._description = None
        self._count = None
        self._customer_number = None
        self._external_reference = None
        self._department_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if date is not None:
            self.date = date
        if product_id is not None:
            self.product_id = product_id
        if description is not None:
            self.description = description
        if count is not None:
            self.count = count
        if customer_number is not None:
            self.customer_number = customer_number
        if external_reference is not None:
            self.external_reference = external_reference
        if department_id is not None:
            self.department_id = department_id

    @property
    def id(self):
        """Gets the id of this Transaction.  

        Transaction ID  

        :return: The id of this Transaction.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transaction.

        Transaction ID  

        :param id: The id of this Transaction.  
        :type: str
        """

        self._id = id

    @property
    def date(self):
        """Gets the date of this Transaction.  

        The date for the transaction  

        :return: The date of this Transaction.  
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Transaction.

        The date for the transaction  

        :param date: The date of this Transaction.  
        :type: datetime
        """

        self._date = date

    @property
    def product_id(self):
        """Gets the product_id of this Transaction.  

        Product ID (SIGN, IDENTIFICATION etc)  

        :return: The product_id of this Transaction.  
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Transaction.

        Product ID (SIGN, IDENTIFICATION etc)  

        :param product_id: The product_id of this Transaction.  
        :type: str
        """

        self._product_id = product_id

    @property
    def description(self):
        """Gets the description of this Transaction.  

        Transaction description  

        :return: The description of this Transaction.  
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Transaction.

        Transaction description  

        :param description: The description of this Transaction.  
        :type: str
        """

        self._description = description

    @property
    def count(self):
        """Gets the count of this Transaction.  

        Number of transactions for the selected date  

        :return: The count of this Transaction.  
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Transaction.

        Number of transactions for the selected date  

        :param count: The count of this Transaction.  
        :type: int
        """

        self._count = count

    @property
    def customer_number(self):
        """Gets the customer_number of this Transaction.  

        Your customer number in our invocing system  

        :return: The customer_number of this Transaction.  
        :rtype: int
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this Transaction.

        Your customer number in our invocing system  

        :param customer_number: The customer_number of this Transaction.  
        :type: int
        """

        self._customer_number = customer_number

    @property
    def external_reference(self):
        """Gets the external_reference of this Transaction.  

        Your reference to the transaction (by ExternalRef in the API call)  

        :return: The external_reference of this Transaction.  
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this Transaction.

        Your reference to the transaction (by ExternalRef in the API call)  

        :param external_reference: The external_reference of this Transaction.  
        :type: str
        """

        self._external_reference = external_reference

    @property
    def department_id(self):
        """Gets the department_id of this Transaction.  

        The Departments ID if specified  

        :return: The department_id of this Transaction.  
        :rtype: str
        """
        return self._department_id

    @department_id.setter
    def department_id(self, department_id):
        """Sets the department_id of this Transaction.

        The Departments ID if specified  

        :param department_id: The department_id of this Transaction.  
        :type: str
        """

        self._department_id = department_id

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
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
