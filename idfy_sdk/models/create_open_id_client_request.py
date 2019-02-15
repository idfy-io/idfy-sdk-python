# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class CreateOpenIdClientRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'client_name': 'str',
        'client_uri': 'str',
        'require_consent': 'bool',
        'allow_remember_consent': 'bool',
        'flow': 'str',
        'allow_client_credentials_only': 'bool',
        'redirect_uris': 'list[str]',
        'post_logout_redirect_uris': 'list[str]',
        'logout_uri': 'str',
        'require_sign_out_prompt': 'bool',
        'allowed_scopes': 'list[str]',
        'identity_provider_restrictions': 'list[str]',
        'identity_token_lifetime': 'int',
        'access_token_lifetime': 'int',
        'absolute_refresh_token_lifetime': 'int',
        'sliding_refresh_token_lifetime': 'int',
        'refresh_token_usage': 'str',
        'update_access_token_claims_on_refresh': 'bool',
        'refresh_token_expiration': 'str',
        'access_token_type': 'str',
        'include_jwt_id': 'bool',
        'always_send_client_claims': 'bool',
        'allowed_cors_origins': 'list[str]',
        'allow_access_tokens_via_browser': 'bool'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'client_name': 'ClientName',
        'client_uri': 'ClientUri',
        'require_consent': 'RequireConsent',
        'allow_remember_consent': 'AllowRememberConsent',
        'flow': 'Flow',
        'allow_client_credentials_only': 'AllowClientCredentialsOnly',
        'redirect_uris': 'RedirectUris',
        'post_logout_redirect_uris': 'PostLogoutRedirectUris',
        'logout_uri': 'LogoutUri',
        'require_sign_out_prompt': 'RequireSignOutPrompt',
        'allowed_scopes': 'AllowedScopes',
        'identity_provider_restrictions': 'IdentityProviderRestrictions',
        'identity_token_lifetime': 'IdentityTokenLifetime',
        'access_token_lifetime': 'AccessTokenLifetime',
        'absolute_refresh_token_lifetime': 'AbsoluteRefreshTokenLifetime',
        'sliding_refresh_token_lifetime': 'SlidingRefreshTokenLifetime',
        'refresh_token_usage': 'RefreshTokenUsage',
        'update_access_token_claims_on_refresh': 'UpdateAccessTokenClaimsOnRefresh',
        'refresh_token_expiration': 'RefreshTokenExpiration',
        'access_token_type': 'AccessTokenType',
        'include_jwt_id': 'IncludeJwtId',
        'always_send_client_claims': 'AlwaysSendClientClaims',
        'allowed_cors_origins': 'AllowedCorsOrigins',
        'allow_access_tokens_via_browser': 'AllowAccessTokensViaBrowser'
    }

    def __init__(self, account_id=None, client_name=None, client_uri=None, require_consent=None, allow_remember_consent=None, flow=None, allow_client_credentials_only=None, redirect_uris=None, post_logout_redirect_uris=None, logout_uri=None, require_sign_out_prompt=None, allowed_scopes=None, identity_provider_restrictions=None, identity_token_lifetime=None, access_token_lifetime=None, absolute_refresh_token_lifetime=None, sliding_refresh_token_lifetime=None, refresh_token_usage=None, update_access_token_claims_on_refresh=None, refresh_token_expiration=None, access_token_type=None, include_jwt_id=None, always_send_client_claims=None, allowed_cors_origins=None, allow_access_tokens_via_browser=None):  
        """CreateOpenIdClientRequest"""  

        self._account_id = None
        self._client_name = None
        self._client_uri = None
        self._require_consent = None
        self._allow_remember_consent = None
        self._flow = None
        self._allow_client_credentials_only = None
        self._redirect_uris = None
        self._post_logout_redirect_uris = None
        self._logout_uri = None
        self._require_sign_out_prompt = None
        self._allowed_scopes = None
        self._identity_provider_restrictions = None
        self._identity_token_lifetime = None
        self._access_token_lifetime = None
        self._absolute_refresh_token_lifetime = None
        self._sliding_refresh_token_lifetime = None
        self._refresh_token_usage = None
        self._update_access_token_claims_on_refresh = None
        self._refresh_token_expiration = None
        self._access_token_type = None
        self._include_jwt_id = None
        self._always_send_client_claims = None
        self._allowed_cors_origins = None
        self._allow_access_tokens_via_browser = None
        self.discriminator = None

        self.account_id = account_id
        self.client_name = client_name
        if client_uri is not None:
            self.client_uri = client_uri
        if require_consent is not None:
            self.require_consent = require_consent
        if allow_remember_consent is not None:
            self.allow_remember_consent = allow_remember_consent
        if flow is not None:
            self.flow = flow
        if allow_client_credentials_only is not None:
            self.allow_client_credentials_only = allow_client_credentials_only
        if redirect_uris is not None:
            self.redirect_uris = redirect_uris
        if post_logout_redirect_uris is not None:
            self.post_logout_redirect_uris = post_logout_redirect_uris
        if logout_uri is not None:
            self.logout_uri = logout_uri
        if require_sign_out_prompt is not None:
            self.require_sign_out_prompt = require_sign_out_prompt
        if allowed_scopes is not None:
            self.allowed_scopes = allowed_scopes
        if identity_provider_restrictions is not None:
            self.identity_provider_restrictions = identity_provider_restrictions
        if identity_token_lifetime is not None:
            self.identity_token_lifetime = identity_token_lifetime
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
        if include_jwt_id is not None:
            self.include_jwt_id = include_jwt_id
        if always_send_client_claims is not None:
            self.always_send_client_claims = always_send_client_claims
        if allowed_cors_origins is not None:
            self.allowed_cors_origins = allowed_cors_origins
        if allow_access_tokens_via_browser is not None:
            self.allow_access_tokens_via_browser = allow_access_tokens_via_browser

    @property
    def account_id(self):
        """Gets the account_id of this CreateOpenIdClientRequest.  


        :return: The account_id of this CreateOpenIdClientRequest.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CreateOpenIdClientRequest.


        :param account_id: The account_id of this CreateOpenIdClientRequest.  
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  

        self._account_id = account_id

    @property
    def client_name(self):
        """Gets the client_name of this CreateOpenIdClientRequest.  


        :return: The client_name of this CreateOpenIdClientRequest.  
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this CreateOpenIdClientRequest.


        :param client_name: The client_name of this CreateOpenIdClientRequest.  
        :type: str
        """
        if client_name is None:
            raise ValueError("Invalid value for `client_name`, must not be `None`")  

        self._client_name = client_name

    @property
    def client_uri(self):
        """Gets the client_uri of this CreateOpenIdClientRequest.  


        :return: The client_uri of this CreateOpenIdClientRequest.  
        :rtype: str
        """
        return self._client_uri

    @client_uri.setter
    def client_uri(self, client_uri):
        """Sets the client_uri of this CreateOpenIdClientRequest.


        :param client_uri: The client_uri of this CreateOpenIdClientRequest.  
        :type: str
        """

        self._client_uri = client_uri

    @property
    def require_consent(self):
        """Gets the require_consent of this CreateOpenIdClientRequest.  


        :return: The require_consent of this CreateOpenIdClientRequest.  
        :rtype: bool
        """
        return self._require_consent

    @require_consent.setter
    def require_consent(self, require_consent):
        """Sets the require_consent of this CreateOpenIdClientRequest.


        :param require_consent: The require_consent of this CreateOpenIdClientRequest.  
        :type: bool
        """

        self._require_consent = require_consent

    @property
    def allow_remember_consent(self):
        """Gets the allow_remember_consent of this CreateOpenIdClientRequest.  


        :return: The allow_remember_consent of this CreateOpenIdClientRequest.  
        :rtype: bool
        """
        return self._allow_remember_consent

    @allow_remember_consent.setter
    def allow_remember_consent(self, allow_remember_consent):
        """Sets the allow_remember_consent of this CreateOpenIdClientRequest.


        :param allow_remember_consent: The allow_remember_consent of this CreateOpenIdClientRequest.  
        :type: bool
        """

        self._allow_remember_consent = allow_remember_consent

    @property
    def flow(self):
        """Gets the flow of this CreateOpenIdClientRequest.  


        :return: The flow of this CreateOpenIdClientRequest.  
        :rtype: str
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this CreateOpenIdClientRequest.


        :param flow: The flow of this CreateOpenIdClientRequest.  
        :type: str
        """
        allowed_values = ["AuthorizationCode", "Implicit", "Hybrid", "ClientCredentials", "ResourceOwner", "Custom", "AuthorizationCodeWithProofKey", "HybridWithProofKey"]  
        if flow not in allowed_values:
            raise ValueError(
                "Invalid value for `flow` ({0}), must be one of {1}"  
                .format(flow, allowed_values)
            )

        self._flow = flow

    @property
    def allow_client_credentials_only(self):
        """Gets the allow_client_credentials_only of this CreateOpenIdClientRequest.  


        :return: The allow_client_credentials_only of this CreateOpenIdClientRequest.  
        :rtype: bool
        """
        return self._allow_client_credentials_only

    @allow_client_credentials_only.setter
    def allow_client_credentials_only(self, allow_client_credentials_only):
        """Sets the allow_client_credentials_only of this CreateOpenIdClientRequest.


        :param allow_client_credentials_only: The allow_client_credentials_only of this CreateOpenIdClientRequest.  
        :type: bool
        """

        self._allow_client_credentials_only = allow_client_credentials_only

    @property
    def redirect_uris(self):
        """Gets the redirect_uris of this CreateOpenIdClientRequest.  


        :return: The redirect_uris of this CreateOpenIdClientRequest.  
        :rtype: list[str]
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """Sets the redirect_uris of this CreateOpenIdClientRequest.


        :param redirect_uris: The redirect_uris of this CreateOpenIdClientRequest.  
        :type: list[str]
        """

        self._redirect_uris = redirect_uris

    @property
    def post_logout_redirect_uris(self):
        """Gets the post_logout_redirect_uris of this CreateOpenIdClientRequest.  


        :return: The post_logout_redirect_uris of this CreateOpenIdClientRequest.  
        :rtype: list[str]
        """
        return self._post_logout_redirect_uris

    @post_logout_redirect_uris.setter
    def post_logout_redirect_uris(self, post_logout_redirect_uris):
        """Sets the post_logout_redirect_uris of this CreateOpenIdClientRequest.


        :param post_logout_redirect_uris: The post_logout_redirect_uris of this CreateOpenIdClientRequest.  
        :type: list[str]
        """

        self._post_logout_redirect_uris = post_logout_redirect_uris

    @property
    def logout_uri(self):
        """Gets the logout_uri of this CreateOpenIdClientRequest.  

        Specifies logout URI at client for HTTP based logout.  

        :return: The logout_uri of this CreateOpenIdClientRequest.  
        :rtype: str
        """
        return self._logout_uri

    @logout_uri.setter
    def logout_uri(self, logout_uri):
        """Sets the logout_uri of this CreateOpenIdClientRequest.

        Specifies logout URI at client for HTTP based logout.  

        :param logout_uri: The logout_uri of this CreateOpenIdClientRequest.  
        :type: str
        """

        self._logout_uri = logout_uri

    @property
    def require_sign_out_prompt(self):
        """Gets the require_sign_out_prompt of this CreateOpenIdClientRequest.  

        Specifies if the client will always show a confirmation page for sign-out. Defaults to false.  

        :return: The require_sign_out_prompt of this CreateOpenIdClientRequest.  
        :rtype: bool
        """
        return self._require_sign_out_prompt

    @require_sign_out_prompt.setter
    def require_sign_out_prompt(self, require_sign_out_prompt):
        """Sets the require_sign_out_prompt of this CreateOpenIdClientRequest.

        Specifies if the client will always show a confirmation page for sign-out. Defaults to false.  

        :param require_sign_out_prompt: The require_sign_out_prompt of this CreateOpenIdClientRequest.  
        :type: bool
        """

        self._require_sign_out_prompt = require_sign_out_prompt

    @property
    def allowed_scopes(self):
        """Gets the allowed_scopes of this CreateOpenIdClientRequest.  


        :return: The allowed_scopes of this CreateOpenIdClientRequest.  
        :rtype: list[str]
        """
        return self._allowed_scopes

    @allowed_scopes.setter
    def allowed_scopes(self, allowed_scopes):
        """Sets the allowed_scopes of this CreateOpenIdClientRequest.


        :param allowed_scopes: The allowed_scopes of this CreateOpenIdClientRequest.  
        :type: list[str]
        """

        self._allowed_scopes = allowed_scopes

    @property
    def identity_provider_restrictions(self):
        """Gets the identity_provider_restrictions of this CreateOpenIdClientRequest.  

        Setup which id providers that should be allowed to use  

        :return: The identity_provider_restrictions of this CreateOpenIdClientRequest.  
        :rtype: list[str]
        """
        return self._identity_provider_restrictions

    @identity_provider_restrictions.setter
    def identity_provider_restrictions(self, identity_provider_restrictions):
        """Sets the identity_provider_restrictions of this CreateOpenIdClientRequest.

        Setup which id providers that should be allowed to use  

        :param identity_provider_restrictions: The identity_provider_restrictions of this CreateOpenIdClientRequest.  
        :type: list[str]
        """
        allowed_values = ["NO_BANKID_MOBILE", "NO_BANKID_WEB", "SWE_BANKID", "NO_BUYPASS", "DA_NEMID", "FI_TUPAS", "MOBILECONNECT", "SMS_OTP", "Facebook", "Google", "LinkedIn", "GitHub", "Microsoft"]  
        if not set(identity_provider_restrictions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `identity_provider_restrictions` [{0}], must be a subset of [{1}]"  
                .format(", ".join(map(str, set(identity_provider_restrictions) - set(allowed_values))),  
                        ", ".join(map(str, allowed_values)))
            )

        self._identity_provider_restrictions = identity_provider_restrictions

    @property
    def identity_token_lifetime(self):
        """Gets the identity_token_lifetime of this CreateOpenIdClientRequest.  

        Lifetime of identity token in seconds (defaults to 300 seconds / 5 minutes)  

        :return: The identity_token_lifetime of this CreateOpenIdClientRequest.  
        :rtype: int
        """
        return self._identity_token_lifetime

    @identity_token_lifetime.setter
    def identity_token_lifetime(self, identity_token_lifetime):
        """Sets the identity_token_lifetime of this CreateOpenIdClientRequest.

        Lifetime of identity token in seconds (defaults to 300 seconds / 5 minutes)  

        :param identity_token_lifetime: The identity_token_lifetime of this CreateOpenIdClientRequest.  
        :type: int
        """

        self._identity_token_lifetime = identity_token_lifetime

    @property
    def access_token_lifetime(self):
        """Gets the access_token_lifetime of this CreateOpenIdClientRequest.  

        Lifetime of access token in seconds (defaults to 3600 seconds / 1 hour)  

        :return: The access_token_lifetime of this CreateOpenIdClientRequest.  
        :rtype: int
        """
        return self._access_token_lifetime

    @access_token_lifetime.setter
    def access_token_lifetime(self, access_token_lifetime):
        """Sets the access_token_lifetime of this CreateOpenIdClientRequest.

        Lifetime of access token in seconds (defaults to 3600 seconds / 1 hour)  

        :param access_token_lifetime: The access_token_lifetime of this CreateOpenIdClientRequest.  
        :type: int
        """

        self._access_token_lifetime = access_token_lifetime

    @property
    def absolute_refresh_token_lifetime(self):
        """Gets the absolute_refresh_token_lifetime of this CreateOpenIdClientRequest.  

        Maximum lifetime of a refresh token in seconds. Defaults to 2592000 seconds / 30 days  

        :return: The absolute_refresh_token_lifetime of this CreateOpenIdClientRequest.  
        :rtype: int
        """
        return self._absolute_refresh_token_lifetime

    @absolute_refresh_token_lifetime.setter
    def absolute_refresh_token_lifetime(self, absolute_refresh_token_lifetime):
        """Sets the absolute_refresh_token_lifetime of this CreateOpenIdClientRequest.

        Maximum lifetime of a refresh token in seconds. Defaults to 2592000 seconds / 30 days  

        :param absolute_refresh_token_lifetime: The absolute_refresh_token_lifetime of this CreateOpenIdClientRequest.  
        :type: int
        """

        self._absolute_refresh_token_lifetime = absolute_refresh_token_lifetime

    @property
    def sliding_refresh_token_lifetime(self):
        """Gets the sliding_refresh_token_lifetime of this CreateOpenIdClientRequest.  

        Sliding lifetime of a refresh token in seconds. Defaults to 1296000 seconds / 15 days  

        :return: The sliding_refresh_token_lifetime of this CreateOpenIdClientRequest.  
        :rtype: int
        """
        return self._sliding_refresh_token_lifetime

    @sliding_refresh_token_lifetime.setter
    def sliding_refresh_token_lifetime(self, sliding_refresh_token_lifetime):
        """Sets the sliding_refresh_token_lifetime of this CreateOpenIdClientRequest.

        Sliding lifetime of a refresh token in seconds. Defaults to 1296000 seconds / 15 days  

        :param sliding_refresh_token_lifetime: The sliding_refresh_token_lifetime of this CreateOpenIdClientRequest.  
        :type: int
        """

        self._sliding_refresh_token_lifetime = sliding_refresh_token_lifetime

    @property
    def refresh_token_usage(self):
        """Gets the refresh_token_usage of this CreateOpenIdClientRequest.  


        :return: The refresh_token_usage of this CreateOpenIdClientRequest.  
        :rtype: str
        """
        return self._refresh_token_usage

    @refresh_token_usage.setter
    def refresh_token_usage(self, refresh_token_usage):
        """Sets the refresh_token_usage of this CreateOpenIdClientRequest.


        :param refresh_token_usage: The refresh_token_usage of this CreateOpenIdClientRequest.  
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
        """Gets the update_access_token_claims_on_refresh of this CreateOpenIdClientRequest.  

        Gets or sets a value indicating whether the access token (and its claims) should be updated on a refresh token request.  

        :return: The update_access_token_claims_on_refresh of this CreateOpenIdClientRequest.  
        :rtype: bool
        """
        return self._update_access_token_claims_on_refresh

    @update_access_token_claims_on_refresh.setter
    def update_access_token_claims_on_refresh(self, update_access_token_claims_on_refresh):
        """Sets the update_access_token_claims_on_refresh of this CreateOpenIdClientRequest.

        Gets or sets a value indicating whether the access token (and its claims) should be updated on a refresh token request.  

        :param update_access_token_claims_on_refresh: The update_access_token_claims_on_refresh of this CreateOpenIdClientRequest.  
        :type: bool
        """

        self._update_access_token_claims_on_refresh = update_access_token_claims_on_refresh

    @property
    def refresh_token_expiration(self):
        """Gets the refresh_token_expiration of this CreateOpenIdClientRequest.  


        :return: The refresh_token_expiration of this CreateOpenIdClientRequest.  
        :rtype: str
        """
        return self._refresh_token_expiration

    @refresh_token_expiration.setter
    def refresh_token_expiration(self, refresh_token_expiration):
        """Sets the refresh_token_expiration of this CreateOpenIdClientRequest.


        :param refresh_token_expiration: The refresh_token_expiration of this CreateOpenIdClientRequest.  
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
        """Gets the access_token_type of this CreateOpenIdClientRequest.  


        :return: The access_token_type of this CreateOpenIdClientRequest.  
        :rtype: str
        """
        return self._access_token_type

    @access_token_type.setter
    def access_token_type(self, access_token_type):
        """Sets the access_token_type of this CreateOpenIdClientRequest.


        :param access_token_type: The access_token_type of this CreateOpenIdClientRequest.  
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
    def include_jwt_id(self):
        """Gets the include_jwt_id of this CreateOpenIdClientRequest.  

        Gets or sets a value indicating whether JWT access tokens should include an identifier  

        :return: The include_jwt_id of this CreateOpenIdClientRequest.  
        :rtype: bool
        """
        return self._include_jwt_id

    @include_jwt_id.setter
    def include_jwt_id(self, include_jwt_id):
        """Sets the include_jwt_id of this CreateOpenIdClientRequest.

        Gets or sets a value indicating whether JWT access tokens should include an identifier  

        :param include_jwt_id: The include_jwt_id of this CreateOpenIdClientRequest.  
        :type: bool
        """

        self._include_jwt_id = include_jwt_id

    @property
    def always_send_client_claims(self):
        """Gets the always_send_client_claims of this CreateOpenIdClientRequest.  

        Gets or sets a value indicating whether client claims should be always included in the access tokens - or only for client credentials flow.  

        :return: The always_send_client_claims of this CreateOpenIdClientRequest.  
        :rtype: bool
        """
        return self._always_send_client_claims

    @always_send_client_claims.setter
    def always_send_client_claims(self, always_send_client_claims):
        """Sets the always_send_client_claims of this CreateOpenIdClientRequest.

        Gets or sets a value indicating whether client claims should be always included in the access tokens - or only for client credentials flow.  

        :param always_send_client_claims: The always_send_client_claims of this CreateOpenIdClientRequest.  
        :type: bool
        """

        self._always_send_client_claims = always_send_client_claims

    @property
    def allowed_cors_origins(self):
        """Gets the allowed_cors_origins of this CreateOpenIdClientRequest.  


        :return: The allowed_cors_origins of this CreateOpenIdClientRequest.  
        :rtype: list[str]
        """
        return self._allowed_cors_origins

    @allowed_cors_origins.setter
    def allowed_cors_origins(self, allowed_cors_origins):
        """Sets the allowed_cors_origins of this CreateOpenIdClientRequest.


        :param allowed_cors_origins: The allowed_cors_origins of this CreateOpenIdClientRequest.  
        :type: list[str]
        """

        self._allowed_cors_origins = allowed_cors_origins

    @property
    def allow_access_tokens_via_browser(self):
        """Gets the allow_access_tokens_via_browser of this CreateOpenIdClientRequest.  


        :return: The allow_access_tokens_via_browser of this CreateOpenIdClientRequest.  
        :rtype: bool
        """
        return self._allow_access_tokens_via_browser

    @allow_access_tokens_via_browser.setter
    def allow_access_tokens_via_browser(self, allow_access_tokens_via_browser):
        """Sets the allow_access_tokens_via_browser of this CreateOpenIdClientRequest.


        :param allow_access_tokens_via_browser: The allow_access_tokens_via_browser of this CreateOpenIdClientRequest.  
        :type: bool
        """

        self._allow_access_tokens_via_browser = allow_access_tokens_via_browser

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
        if not isinstance(other, CreateOpenIdClientRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
