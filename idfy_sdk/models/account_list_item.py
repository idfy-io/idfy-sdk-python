import pprint
import re  

import six


class AccountListItem(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'name': 'str',
        'org_no': 'str',
        'uni_customer_no': 'str',
        'created': 'datetime',
        'last_modified': 'datetime',
        'dealer_id': 'str',
        'dealer_name': 'str',
        'dealer_reference': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'name': 'Name',
        'org_no': 'OrgNo',
        'uni_customer_no': 'UniCustomerNo',
        'created': 'Created',
        'last_modified': 'LastModified',
        'dealer_id': 'DealerId',
        'dealer_name': 'DealerName',
        'dealer_reference': 'DealerReference',
        'enabled': 'Enabled'
    }

    def __init__(self, account_id=None, name=None, org_no=None, uni_customer_no=None, created=None, last_modified=None, dealer_id=None, dealer_name=None, dealer_reference=None, enabled=None):  
        """AccountListItem"""  

        self._account_id = None
        self._name = None
        self._org_no = None
        self._uni_customer_no = None
        self._created = None
        self._last_modified = None
        self._dealer_id = None
        self._dealer_name = None
        self._dealer_reference = None
        self._enabled = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if org_no is not None:
            self.org_no = org_no
        if uni_customer_no is not None:
            self.uni_customer_no = uni_customer_no
        if created is not None:
            self.created = created
        if last_modified is not None:
            self.last_modified = last_modified
        if dealer_id is not None:
            self.dealer_id = dealer_id
        if dealer_name is not None:
            self.dealer_name = dealer_name
        if dealer_reference is not None:
            self.dealer_reference = dealer_reference
        if enabled is not None:
            self.enabled = enabled

    @property
    def account_id(self):
        """Gets the account_id of this AccountListItem.  


        :return: The account_id of this AccountListItem.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountListItem.


        :param account_id: The account_id of this AccountListItem.  
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this AccountListItem.  


        :return: The name of this AccountListItem.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountListItem.


        :param name: The name of this AccountListItem.  
        :type: str
        """

        self._name = name

    @property
    def org_no(self):
        """Gets the org_no of this AccountListItem.  


        :return: The org_no of this AccountListItem.  
        :rtype: str
        """
        return self._org_no

    @org_no.setter
    def org_no(self, org_no):
        """Sets the org_no of this AccountListItem.


        :param org_no: The org_no of this AccountListItem.  
        :type: str
        """

        self._org_no = org_no

    @property
    def uni_customer_no(self):
        """Gets the uni_customer_no of this AccountListItem.  


        :return: The uni_customer_no of this AccountListItem.  
        :rtype: str
        """
        return self._uni_customer_no

    @uni_customer_no.setter
    def uni_customer_no(self, uni_customer_no):
        """Sets the uni_customer_no of this AccountListItem.


        :param uni_customer_no: The uni_customer_no of this AccountListItem.  
        :type: str
        """

        self._uni_customer_no = uni_customer_no

    @property
    def created(self):
        """Gets the created of this AccountListItem.  


        :return: The created of this AccountListItem.  
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AccountListItem.


        :param created: The created of this AccountListItem.  
        :type: datetime
        """

        self._created = created

    @property
    def last_modified(self):
        """Gets the last_modified of this AccountListItem.  


        :return: The last_modified of this AccountListItem.  
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this AccountListItem.


        :param last_modified: The last_modified of this AccountListItem.  
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def dealer_id(self):
        """Gets the dealer_id of this AccountListItem.  


        :return: The dealer_id of this AccountListItem.  
        :rtype: str
        """
        return self._dealer_id

    @dealer_id.setter
    def dealer_id(self, dealer_id):
        """Sets the dealer_id of this AccountListItem.


        :param dealer_id: The dealer_id of this AccountListItem.  
        :type: str
        """

        self._dealer_id = dealer_id

    @property
    def dealer_name(self):
        """Gets the dealer_name of this AccountListItem.  


        :return: The dealer_name of this AccountListItem.  
        :rtype: str
        """
        return self._dealer_name

    @dealer_name.setter
    def dealer_name(self, dealer_name):
        """Sets the dealer_name of this AccountListItem.


        :param dealer_name: The dealer_name of this AccountListItem.  
        :type: str
        """

        self._dealer_name = dealer_name

    @property
    def dealer_reference(self):
        """Gets the dealer_reference of this AccountListItem.  


        :return: The dealer_reference of this AccountListItem.  
        :rtype: str
        """
        return self._dealer_reference

    @dealer_reference.setter
    def dealer_reference(self, dealer_reference):
        """Sets the dealer_reference of this AccountListItem.


        :param dealer_reference: The dealer_reference of this AccountListItem.  
        :type: str
        """

        self._dealer_reference = dealer_reference

    @property
    def enabled(self):
        """Gets the enabled of this AccountListItem.  


        :return: The enabled of this AccountListItem.  
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AccountListItem.


        :param enabled: The enabled of this AccountListItem.  
        :type: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, AccountListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
