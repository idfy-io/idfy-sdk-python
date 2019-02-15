import pprint
import re  

import six


class AccountNameItem(object):
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
        'enabled': 'bool'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'name': 'Name',
        'enabled': 'Enabled'
    }

    def __init__(self, account_id=None, name=None, enabled=None):  
        """AccountNameItem"""  

        self._account_id = None
        self._name = None
        self._enabled = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled

    @property
    def account_id(self):
        """Gets the account_id of this AccountNameItem.  


        :return: The account_id of this AccountNameItem.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountNameItem.


        :param account_id: The account_id of this AccountNameItem.  
        :type: str
        """

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this AccountNameItem.  


        :return: The name of this AccountNameItem.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountNameItem.


        :param name: The name of this AccountNameItem.  
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this AccountNameItem.  


        :return: The enabled of this AccountNameItem.  
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AccountNameItem.


        :param enabled: The enabled of this AccountNameItem.  
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
        if not isinstance(other, AccountNameItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
