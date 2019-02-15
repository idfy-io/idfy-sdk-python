# coding: utf-8

"""
    Idfy API Reference

    # Introduction The Idfy API is a RESTful API that use the OAuth 2.0 protocol for authorization. All request and response bodies are formatted in JSON.  # Getting started  ## Get an account To use the API you need an account at Idfy. You can get a free test account by signing up through our [onboarding site](https://onboard.idfy.io).  ## Support We’re here to help! Get in touch with support at support@idfy.io and we’ll get back to you as soon as we can.  # Authentication This API uses OAuth2 for authentication. OAuth2 - an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. Be sure to use `client_credentials` as grant type when connecting to this API.   ## Obtaining an access token  An access token can be obtained by making a request to the OAuth2 token endpoint.  The request must include the following parameters:  | Parameter | Value | |----------|----------| | `grant_type` | The type of grant used to authenticate the request. In this case: `client_credentials`. | | `scope` | Space-delimited list of requested scope permissions. |  Example:  ``` POST https://api.idfy.io/oauth/connect/token Content-Type: application/x-www-form-urlencoded Authorization: Basic Y2xpZW50SWQ6Y2xpZW50U2VjcmV0   grant_type=client_credentials scope=document_read ```  **Note**: This request must authenticate using HTTP basic authentication with your *Client Id* as the username and *Client Secret* as the password. The format is the base-64 encoded string `client_id:client_secret`.    If your credentials are valid, the server will respond with a JSON body containing the access token and its expiration time: ``` {     \"access_token\": \"xxxxx.yyyyy.zzzzz\",     \"expires_in\": 3600,     \"token_type\": \"Bearer\" } ```  You can now store and use the access token to make authenticated request by passing it as an authentication header:  `Authorization: Bearer xxxxx.yyyyy.zzzzz`  You can read more about OAuth2 [here](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2).  # REST API  ## HTTP status codes * `200 OK`: The request was successful. * `201 Created`: A new resource was successfully created. * `204 No content`: The request was successful but returns no body. * `400 Bad request`: The request was invalid, often due to missing a required parameter. * `401 Unauthorized`: Authentication failed due to invalid credentials. * `402 Payment Required`: The endpoint is not accessible in your current subscription. Contact sales@idfy.io. * `403 Forbidden`: Authorization failed due to insufficient scope/access. * `404 Not found`: The specified resource does not exist. * `422 Unprocessable Entity`: The server understood the request, but was unable to process it due to a business or logical error (For example creating an XML signature with Swedish BankID which is not supported). * `429 Too Many Requests`: The request was blocked due to rate limiting. * `500 Internal Server Error`: An internal server error occured. * `503 Service Unavailable`: A third party service that this endpoint depends on caused an error or is unavailable.  ## HTTP verbs * `GET`: Retrieves a resource or lists resources. * `POST`: Creates or exceutes a commandand on a resource. * `PUT`: Replaces a resource. * `PATCH`: Partially updates a resoruce. * `DELETE`: Deletes a resoure.  ## Formats The Idfy API only supports JSON format. All request must use the `Content-type` header set to `application/json`. The JSON will use camelCasing. All request must use the UTF-8 encoding, and all responsens will be in UTF-8. All file download wills be a standard HTTP download result.  ## Idempotent Requests The APIs supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a new document fails due to a network connection error, you can retry the request with the same ExternalId  to guarantee that only a single document/identification is created.  ## Compatibility The Idfy API do change from time to time, but all changes will follow strict rules in order to keep the API's backward compatible. All new fields will be optional, and if large changes are required a new endpoint will be created. If an endpoint is being deprecated, all customers will be given notice well in advance.  ## Pagination (linked lists) When using paging the list will be wrapped in a linked list object. The data contains the list-data in the result. There will also be navigation links for next, first, last and previous page. The total amount of results (size) will also be inlcuded. Example: ```json {    \"offset\": 0,    \"limit\": 2,    \"size\": 45,    \"links\": {      \"next\": \"https://api.idfy.io/signature/documents/summary?limit=2&offset=2\",      \"first\": \"https://api.idfy.io/signature/documents/summary?limit=2\",      \"last\": \"\",      \"previous\": \"\"    },    \"data\": [       {          \"id\": \"2519011552909132317BrJ6VqOrcBYfwmgQ2eypM5XP7DEbCm8\",          \"name\": \"Bruce Wayne\",          \"status\": \"SUCCESS\",          \"clientIp\": \"192.168.1.1\",          \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36\",          \"identityProviderType\": \"NO_BANKID_WEB\",          \"language\": \"NO\",          \"externalid\": \"gtWEH8euBHeSWPTcjwB0Bg5o1mjsH106wmjTDMxoFnadzvNSsnSSY0zbJTpy\",          \"timestamp\": \"2017-07-19T18:29:53.7550972Z\",          \"iframe\": false,          \"socialSecurityNumber\": false       },       {          \"id\": \"2519011552909132317BrJ6VqOrcBYfwmgQ2eypM5XP7DEbCm8\",          \"name\": \"Joker\",          \"status\": \"ERROR\",          \"clientIp\": \"192.168.1.1\",          \"userAgent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36\",          \"identityProviderType\": \"FI_TUPAS\",          \"language\": \"NO\",          \"externalid\": \"gtWEH8euBHeSWPTcjwB0Bg5o1mjsH106wmjTDMxoFnadzvNSsnSSY0zbJTpy\",          \"errorcode\": \"TIMEOUT\",          \"timestamp\": \"2017-07-19T18:29:53.7550972Z\",          \"iframe\": false,          \"socialSecurityNumber\": false       }   ] } ```  ## HTTP response headers All API request have some standard HTTP headers: * `X-Idfy-Environment`: (test or prod) this header tells you if you are talking to the test or the production environment. * `X-Idfy-AccountId`: The Idfy accountID for the request. * `RequestId`: Each API request has an associated request identifier. You will also be able to use this to search in the logs in the Idfy dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  <!-- ReDoc-Inject: <security-definitions> -->   

    OpenAPI spec version: 1
    Contact: support@idfy.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  

import six


class CreateBankIDMobileRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mobile_number': 'str',
        'date_of_birth': 'str',
        'get_social_security_number': 'bool',
        'external_reference': 'str',
        'addonservices': 'dict(str, str)'
    }

    attribute_map = {
        'mobile_number': 'MobileNumber',
        'date_of_birth': 'DateOfBirth',
        'get_social_security_number': 'GetSocialSecurityNumber',
        'external_reference': 'ExternalReference',
        'addonservices': 'Addonservices'
    }

    def __init__(self, mobile_number=None, date_of_birth=None, get_social_security_number=None, external_reference=None, addonservices=None):  
        """CreateBankIDMobileRequest"""  

        self._mobile_number = None
        self._date_of_birth = None
        self._get_social_security_number = None
        self._external_reference = None
        self._addonservices = None
        self.discriminator = None

        self.mobile_number = mobile_number
        self.date_of_birth = date_of_birth
        if get_social_security_number is not None:
            self.get_social_security_number = get_social_security_number
        if external_reference is not None:
            self.external_reference = external_reference
        if addonservices is not None:
            self.addonservices = addonservices

    @property
    def mobile_number(self):
        """Gets the mobile_number of this CreateBankIDMobileRequest.  

        Mobile number for the user that is to be identified  

        :return: The mobile_number of this CreateBankIDMobileRequest.  
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """Sets the mobile_number of this CreateBankIDMobileRequest.

        Mobile number for the user that is to be identified  

        :param mobile_number: The mobile_number of this CreateBankIDMobileRequest.  
        :type: str
        """
        if mobile_number is None:
            raise ValueError("Invalid value for `mobile_number`, must not be `None`")  
        if mobile_number is not None and not re.search('[0-9]{1,8}', mobile_number):  
            raise ValueError("Invalid value for `mobile_number`, must be a follow pattern or equal to `/[0-9]{1,8}/`")  

        self._mobile_number = mobile_number

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this CreateBankIDMobileRequest.  

        Date of birth for the user that is to be identified  

        :return: The date_of_birth of this CreateBankIDMobileRequest.  
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this CreateBankIDMobileRequest.

        Date of birth for the user that is to be identified  

        :param date_of_birth: The date_of_birth of this CreateBankIDMobileRequest.  
        :type: str
        """
        if date_of_birth is None:
            raise ValueError("Invalid value for `date_of_birth`, must not be `None`")  
        if date_of_birth is not None and not re.search('[0-9]{1,6}', date_of_birth):  
            raise ValueError("Invalid value for `date_of_birth`, must be a follow pattern or equal to `/[0-9]{1,6}/`")  

        self._date_of_birth = date_of_birth

    @property
    def get_social_security_number(self):
        """Gets the get_social_security_number of this CreateBankIDMobileRequest.  

        Should the socialsecuritynumber be fetched from the identityprovider? Beware that there is an extra cost of doing this every time and one need permission to do it.  

        :return: The get_social_security_number of this CreateBankIDMobileRequest.  
        :rtype: bool
        """
        return self._get_social_security_number

    @get_social_security_number.setter
    def get_social_security_number(self, get_social_security_number):
        """Sets the get_social_security_number of this CreateBankIDMobileRequest.

        Should the socialsecuritynumber be fetched from the identityprovider? Beware that there is an extra cost of doing this every time and one need permission to do it.  

        :param get_social_security_number: The get_social_security_number of this CreateBankIDMobileRequest.  
        :type: bool
        """

        self._get_social_security_number = get_social_security_number

    @property
    def external_reference(self):
        """Gets the external_reference of this CreateBankIDMobileRequest.  

        The merchants reference to the identification process  

        :return: The external_reference of this CreateBankIDMobileRequest.  
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this CreateBankIDMobileRequest.

        The merchants reference to the identification process  

        :param external_reference: The external_reference of this CreateBankIDMobileRequest.  
        :type: str
        """

        self._external_reference = external_reference

    @property
    def addonservices(self):
        """Gets the addonservices of this CreateBankIDMobileRequest.  

        List of addon data that can be orderd. The result will be in MetaData list of the reponse  

        :return: The addonservices of this CreateBankIDMobileRequest.  
        :rtype: dict(str, str)
        """
        return self._addonservices

    @addonservices.setter
    def addonservices(self, addonservices):
        """Sets the addonservices of this CreateBankIDMobileRequest.

        List of addon data that can be orderd. The result will be in MetaData list of the reponse  

        :param addonservices: The addonservices of this CreateBankIDMobileRequest.  
        :type: dict(str, str)
        """

        self._addonservices = addonservices

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
        if not isinstance(other, CreateBankIDMobileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
