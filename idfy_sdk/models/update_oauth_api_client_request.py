# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.oauth_secret import OauthSecret  


class UpdateOauthAPIClientRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'client_id': 'str',
        'client_name': 'str',
        'enabled': 'bool',
        'client_secrets': 'list[OauthSecret]',
        'allowed_scopes': 'list[str]',
        'access_token_lifetime': 'int',
        'absolute_refresh_token_lifetime': 'int',
        'sliding_refresh_token_lifetime': 'int',
        'refresh_token_usage': 'str',
        'update_access_token_claims_on_refresh': 'bool',
        'refresh_token_expiration': 'str',
        'access_token_type': 'str',
        'allowed_cors_origins': 'list[str]'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'client_id': 'ClientId',
        'client_name': 'ClientName',
        'enabled': 'Enabled',
        'client_secrets': 'ClientSecrets',
        'allowed_scopes': 'AllowedScopes',
        'access_token_lifetime': 'AccessTokenLifetime',
        'absolute_refresh_token_lifetime': 'AbsoluteRefreshTokenLifetime',
        'sliding_refresh_token_lifetime': 'SlidingRefreshTokenLifetime',
        'refresh_token_usage': 'RefreshTokenUsage',
        'update_access_token_claims_on_refresh': 'UpdateAccessTokenClaimsOnRefresh',
        'refresh_token_expiration': 'RefreshTokenExpiration',
        'access_token_type': 'AccessTokenType',
        'allowed_cors_origins': 'AllowedCorsOrigins'
    }

    def __init__(self, account_id=None, client_id=None, client_name=None, enabled=None, client_secrets=None, allowed_scopes=None, access_token_lifetime=None, absolute_refresh_token_lifetime=None, sliding_refresh_token_lifetime=None, refresh_token_usage=None, update_access_token_claims_on_refresh=None, refresh_token_expiration=None, access_token_type=None, allowed_cors_origins=None):  
        """UpdateOauthAPIClientRequest"""  

        self._account_id = None
        self._client_id = None
        self._client_name = None
        self._enabled = None
        self._client_secrets = None
        self._allowed_scopes = None
        self._access_token_lifetime = None
        self._absolute_refresh_token_lifetime = None
        self._sliding_refresh_token_lifetime = None
        self._refresh_token_usage = None
        self._update_access_token_claims_on_refresh = None
        self._refresh_token_expiration = None
        self._access_token_type = None
        self._allowed_cors_origins = None
        self.discriminator = None

        self.account_id = account_id
        self.client_id = client_id
        self.client_name = client_name
        if enabled is not None:
            self.enabled = enabled
        if client_secrets is not None:
            self.client_secrets = client_secrets
        if allowed_scopes is not None:
            self.allowed_scopes = allowed_scopes
        if access_token_lifetime is not None:
            self.access_token_lifetime = access_token_lifetime
        if absolute_refresh_token_lifetime is not None:
            self.absolute_refresh_token_lifetime = absolute_refresh_token_lifetime
        if sliding_refresh_token_lifetime is not None:
            self.sliding_refresh_token_lifetime = sliding_refresh_token_lifetime
        if refresh_token_usage is not None:
            self.refresh_token_usage = refresh_token_usage
        if update_access_token_claims_on_refresh is not None:
            self.update_access_token_claims_on_refresh = update_access_token_claims_on_refresh
        if refresh_token_expiration is not None:
            self.refresh_token_expiration = refresh_token_expiration
        if access_token_type is not None:
            self.access_token_type = access_token_type
        if allowed_cors_origins is not None:
            self.allowed_cors_origins = allowed_cors_origins

    @property
    def account_id(self):
        """Gets the account_id of this UpdateOauthAPIClientRequest.  


        :return: The account_id of this UpdateOauthAPIClientRequest.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this UpdateOauthAPIClientRequest.


        :param account_id: The account_id of this UpdateOauthAPIClientRequest.  
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  

        self._account_id = account_id

    @property
    def client_id(self):
        """Gets the client_id of this UpdateOauthAPIClientRequest.  


        :return: The client_id of this UpdateOauthAPIClientRequest.  
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this UpdateOauthAPIClientRequest.


        :param client_id: The client_id of this UpdateOauthAPIClientRequest.  
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this UpdateOauthAPIClientRequest.  


        :return: The client_name of this UpdateOauthAPIClientRequest.  
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this UpdateOauthAPIClientRequest.


        :param client_name: The client_name of this UpdateOauthAPIClientRequest.  
        :type: str
        """
        if client_name is None:
            raise ValueError("Invalid value for `client_name`, must not be `None`")  

        self._client_name = client_name

    @property
    def enabled(self):
        """Gets the enabled of this UpdateOauthAPIClientRequest.  


        :return: The enabled of this UpdateOauthAPIClientRequest.  
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateOauthAPIClientRequest.


        :param enabled: The enabled of this UpdateOauthAPIClientRequest.  
        :type: bool
        """

        self._enabled = enabled

    @property
    def client_secrets(self):
        """Gets the client_secrets of this UpdateOauthAPIClientRequest.  


        :return: The client_secrets of this UpdateOauthAPIClientRequest.  
        :rtype: list[OauthSecret]
        """
        return self._client_secrets

    @client_secrets.setter
    def client_secrets(self, client_secrets):
        """Sets the client_secrets of this UpdateOauthAPIClientRequest.


        :param client_secrets: The client_secrets of this UpdateOauthAPIClientRequest.  
        :type: list[OauthSecret]
        """

        self._client_secrets = client_secrets

    @property
    def allowed_scopes(self):
        """Gets the allowed_scopes of this UpdateOauthAPIClientRequest.  


        :return: The allowed_scopes of this UpdateOauthAPIClientRequest.  
        :rtype: list[str]
        """
        return self._allowed_scopes

    @allowed_scopes.setter
    def allowed_scopes(self, allowed_scopes):
        """Sets the allowed_scopes of this UpdateOauthAPIClientRequest.


        :param allowed_scopes: The allowed_scopes of this UpdateOauthAPIClientRequest.  
        :type: list[str]
        """

        self._allowed_scopes = allowed_scopes

    @property
    def access_token_lifetime(self):
        """Gets the access_token_lifetime of this UpdateOauthAPIClientRequest.  

        Lifetime of access token in seconds (defaults to 3600 seconds / 1 hour)  

        :return: The access_token_lifetime of this UpdateOauthAPIClientRequest.  
        :rtype: int
        """
        return self._access_token_lifetime

    @access_token_lifetime.setter
    def access_token_lifetime(self, access_token_lifetime):
        """Sets the access_token_lifetime of this UpdateOauthAPIClientRequest.

        Lifetime of access token in seconds (defaults to 3600 seconds / 1 hour)  

        :param access_token_lifetime: The access_token_lifetime of this UpdateOauthAPIClientRequest.  
        :type: int
        """

        self._access_token_lifetime = access_token_lifetime

    @property
    def absolute_refresh_token_lifetime(self):
        """Gets the absolute_refresh_token_lifetime of this UpdateOauthAPIClientRequest.  

        Maximum lifetime of a refresh token in seconds. Defaults to 2592000 seconds / 30 days  

        :return: The absolute_refresh_token_lifetime of this UpdateOauthAPIClientRequest.  
        :rtype: int
        """
        return self._absolute_refresh_token_lifetime

    @absolute_refresh_token_lifetime.setter
    def absolute_refresh_token_lifetime(self, absolute_refresh_token_lifetime):
        """Sets the absolute_refresh_token_lifetime of this UpdateOauthAPIClientRequest.

        Maximum lifetime of a refresh token in seconds. Defaults to 2592000 seconds / 30 days  

        :param absolute_refresh_token_lifetime: The absolute_refresh_token_lifetime of this UpdateOauthAPIClientRequest.  
        :type: int
        """

        self._absolute_refresh_token_lifetime = absolute_refresh_token_lifetime

    @property
    def sliding_refresh_token_lifetime(self):
        """Gets the sliding_refresh_token_lifetime of this UpdateOauthAPIClientRequest.  

        Sliding lifetime of a refresh token in seconds. Defaults to 1296000 seconds / 15 days  

        :return: The sliding_refresh_token_lifetime of this UpdateOauthAPIClientRequest.  
        :rtype: int
        """
        return self._sliding_refresh_token_lifetime

    @sliding_refresh_token_lifetime.setter
    def sliding_refresh_token_lifetime(self, sliding_refresh_token_lifetime):
        """Sets the sliding_refresh_token_lifetime of this UpdateOauthAPIClientRequest.

        Sliding lifetime of a refresh token in seconds. Defaults to 1296000 seconds / 15 days  

        :param sliding_refresh_token_lifetime: The sliding_refresh_token_lifetime of this UpdateOauthAPIClientRequest.  
        :type: int
        """

        self._sliding_refresh_token_lifetime = sliding_refresh_token_lifetime

    @property
    def refresh_token_usage(self):
        """Gets the refresh_token_usage of this UpdateOauthAPIClientRequest.  


        :return: The refresh_token_usage of this UpdateOauthAPIClientRequest.  
        :rtype: str
        """
        return self._refresh_token_usage

    @refresh_token_usage.setter
    def refresh_token_usage(self, refresh_token_usage):
        """Sets the refresh_token_usage of this UpdateOauthAPIClientRequest.


        :param refresh_token_usage: The refresh_token_usage of this UpdateOauthAPIClientRequest.  
        :type: str
        """
        allowed_values = ["ReUse", "OneTimeOnly"]  
        if refresh_token_usage not in allowed_values:
            raise ValueError(
                "Invalid value for `refresh_token_usage` ({0}), must be one of {1}"  
                .format(refresh_token_usage, allowed_values)
            )

        self._refresh_token_usage = refresh_token_usage

    @property
    def update_access_token_claims_on_refresh(self):
        """Gets the update_access_token_claims_on_refresh of this UpdateOauthAPIClientRequest.  

        Gets or sets a value indicating whether the access token (and its claims) should be updated on a refresh token request.  

        :return: The update_access_token_claims_on_refresh of this UpdateOauthAPIClientRequest.  
        :rtype: bool
        """
        return self._update_access_token_claims_on_refresh

    @update_access_token_claims_on_refresh.setter
    def update_access_token_claims_on_refresh(self, update_access_token_claims_on_refresh):
        """Sets the update_access_token_claims_on_refresh of this UpdateOauthAPIClientRequest.

        Gets or sets a value indicating whether the access token (and its claims) should be updated on a refresh token request.  

        :param update_access_token_claims_on_refresh: The update_access_token_claims_on_refresh of this UpdateOauthAPIClientRequest.  
        :type: bool
        """

        self._update_access_token_claims_on_refresh = update_access_token_claims_on_refresh

    @property
    def refresh_token_expiration(self):
        """Gets the refresh_token_expiration of this UpdateOauthAPIClientRequest.  


        :return: The refresh_token_expiration of this UpdateOauthAPIClientRequest.  
        :rtype: str
        """
        return self._refresh_token_expiration

    @refresh_token_expiration.setter
    def refresh_token_expiration(self, refresh_token_expiration):
        """Sets the refresh_token_expiration of this UpdateOauthAPIClientRequest.


        :param refresh_token_expiration: The refresh_token_expiration of this UpdateOauthAPIClientRequest.  
        :type: str
        """
        allowed_values = ["Sliding", "Absolute"]  
        if refresh_token_expiration not in allowed_values:
            raise ValueError(
                "Invalid value for `refresh_token_expiration` ({0}), must be one of {1}"  
                .format(refresh_token_expiration, allowed_values)
            )

        self._refresh_token_expiration = refresh_token_expiration

    @property
    def access_token_type(self):
        """Gets the access_token_type of this UpdateOauthAPIClientRequest.  


        :return: The access_token_type of this UpdateOauthAPIClientRequest.  
        :rtype: str
        """
        return self._access_token_type

    @access_token_type.setter
    def access_token_type(self, access_token_type):
        """Sets the access_token_type of this UpdateOauthAPIClientRequest.


        :param access_token_type: The access_token_type of this UpdateOauthAPIClientRequest.  
        :type: str
        """
        allowed_values = ["Jwt", "Reference"]  
        if access_token_type not in allowed_values:
            raise ValueError(
                "Invalid value for `access_token_type` ({0}), must be one of {1}"  
                .format(access_token_type, allowed_values)
            )

        self._access_token_type = access_token_type

    @property
    def allowed_cors_origins(self):
        """Gets the allowed_cors_origins of this UpdateOauthAPIClientRequest.  


        :return: The allowed_cors_origins of this UpdateOauthAPIClientRequest.  
        :rtype: list[str]
        """
        return self._allowed_cors_origins

    @allowed_cors_origins.setter
    def allowed_cors_origins(self, allowed_cors_origins):
        """Sets the allowed_cors_origins of this UpdateOauthAPIClientRequest.


        :param allowed_cors_origins: The allowed_cors_origins of this UpdateOauthAPIClientRequest.  
        :type: list[str]
        """

        self._allowed_cors_origins = allowed_cors_origins

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
        if not isinstance(other, UpdateOauthAPIClientRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
