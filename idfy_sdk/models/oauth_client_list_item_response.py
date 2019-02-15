# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class OauthClientListItemResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_id': 'str',
        'enabled': 'bool',
        'client_name': 'str',
        'account_id': 'str',
        'created': 'datetime',
        'last_changed': 'datetime'
    }

    attribute_map = {
        'client_id': 'ClientId',
        'enabled': 'Enabled',
        'client_name': 'ClientName',
        'account_id': 'AccountId',
        'created': 'Created',
        'last_changed': 'LastChanged'
    }

    def __init__(self, client_id=None, enabled=None, client_name=None, account_id=None, created=None, last_changed=None):  
        """OauthClientListItemResponse"""  

        self._client_id = None
        self._enabled = None
        self._client_name = None
        self._account_id = None
        self._created = None
        self._last_changed = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if enabled is not None:
            self.enabled = enabled
        if client_name is not None:
            self.client_name = client_name
        if account_id is not None:
            self.account_id = account_id
        if created is not None:
            self.created = created
        if last_changed is not None:
            self.last_changed = last_changed

    @property
    def client_id(self):
        """Gets the client_id of this OauthClientListItemResponse.  


        :return: The client_id of this OauthClientListItemResponse.  
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OauthClientListItemResponse.


        :param client_id: The client_id of this OauthClientListItemResponse.  
        :type: str
        """

        self._client_id = client_id

    @property
    def enabled(self):
        """Gets the enabled of this OauthClientListItemResponse.  


        :return: The enabled of this OauthClientListItemResponse.  
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this OauthClientListItemResponse.


        :param enabled: The enabled of this OauthClientListItemResponse.  
        :type: bool
        """

        self._enabled = enabled

    @property
    def client_name(self):
        """Gets the client_name of this OauthClientListItemResponse.  


        :return: The client_name of this OauthClientListItemResponse.  
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this OauthClientListItemResponse.


        :param client_name: The client_name of this OauthClientListItemResponse.  
        :type: str
        """

        self._client_name = client_name

    @property
    def account_id(self):
        """Gets the account_id of this OauthClientListItemResponse.  


        :return: The account_id of this OauthClientListItemResponse.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this OauthClientListItemResponse.


        :param account_id: The account_id of this OauthClientListItemResponse.  
        :type: str
        """

        self._account_id = account_id

    @property
    def created(self):
        """Gets the created of this OauthClientListItemResponse.  


        :return: The created of this OauthClientListItemResponse.  
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this OauthClientListItemResponse.


        :param created: The created of this OauthClientListItemResponse.  
        :type: datetime
        """

        self._created = created

    @property
    def last_changed(self):
        """Gets the last_changed of this OauthClientListItemResponse.  


        :return: The last_changed of this OauthClientListItemResponse.  
        :rtype: datetime
        """
        return self._last_changed

    @last_changed.setter
    def last_changed(self, last_changed):
        """Sets the last_changed of this OauthClientListItemResponse.


        :param last_changed: The last_changed of this OauthClientListItemResponse.  
        :type: datetime
        """

        self._last_changed = last_changed

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
        if not isinstance(other, OauthClientListItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
