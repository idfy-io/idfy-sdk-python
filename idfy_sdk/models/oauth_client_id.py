# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class OauthClientId(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_id': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'client_id': 'ClientId',
        'account_id': 'AccountId'
    }

    def __init__(self, client_id=None, account_id=None):  
        """OauthClientId"""  

        self._client_id = None
        self._account_id = None
        self.discriminator = None

        self.client_id = client_id
        self.account_id = account_id

    @property
    def client_id(self):
        """Gets the client_id of this OauthClientId.  


        :return: The client_id of this OauthClientId.  
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OauthClientId.


        :param client_id: The client_id of this OauthClientId.  
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  

        self._client_id = client_id

    @property
    def account_id(self):
        """Gets the account_id of this OauthClientId.  


        :return: The account_id of this OauthClientId.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this OauthClientId.


        :param account_id: The account_id of this OauthClientId.  
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  

        self._account_id = account_id

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
        if not isinstance(other, OauthClientId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
