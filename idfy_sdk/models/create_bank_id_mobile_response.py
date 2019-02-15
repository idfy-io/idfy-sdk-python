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

from idfy_sdk.models.error import Error  


class CreateBankIDMobileResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'request_id': 'str',
        'merchant_ref': 'str',
        'error': 'Error',
        'ok': 'bool',
        'invalid_mobile_number_or_date_of_birth': 'bool'
    }

    attribute_map = {
        'request_id': 'RequestId',
        'merchant_ref': 'MerchantRef',
        'error': 'Error',
        'ok': 'OK',
        'invalid_mobile_number_or_date_of_birth': 'InvalidMobileNumberOrDateOfBirth'
    }

    def __init__(self, request_id=None, merchant_ref=None, error=None, ok=None, invalid_mobile_number_or_date_of_birth=None):  
        """CreateBankIDMobileResponse"""  

        self._request_id = None
        self._merchant_ref = None
        self._error = None
        self._ok = None
        self._invalid_mobile_number_or_date_of_birth = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if merchant_ref is not None:
            self.merchant_ref = merchant_ref
        if error is not None:
            self.error = error
        if ok is not None:
            self.ok = ok
        if invalid_mobile_number_or_date_of_birth is not None:
            self.invalid_mobile_number_or_date_of_birth = invalid_mobile_number_or_date_of_birth

    @property
    def request_id(self):
        """Gets the request_id of this CreateBankIDMobileResponse.  

        Signere requestid used to get the reponse form server afterwards  

        :return: The request_id of this CreateBankIDMobileResponse.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this CreateBankIDMobileResponse.

        Signere requestid used to get the reponse form server afterwards  

        :param request_id: The request_id of this CreateBankIDMobileResponse.  
        :type: str
        """

        self._request_id = request_id

    @property
    def merchant_ref(self):
        """Gets the merchant_ref of this CreateBankIDMobileResponse.  

        The merchant ref to show to the end user (SNILL BANK)  

        :return: The merchant_ref of this CreateBankIDMobileResponse.  
        :rtype: str
        """
        return self._merchant_ref

    @merchant_ref.setter
    def merchant_ref(self, merchant_ref):
        """Sets the merchant_ref of this CreateBankIDMobileResponse.

        The merchant ref to show to the end user (SNILL BANK)  

        :param merchant_ref: The merchant_ref of this CreateBankIDMobileResponse.  
        :type: str
        """

        self._merchant_ref = merchant_ref

    @property
    def error(self):
        """Gets the error of this CreateBankIDMobileResponse.  

        Information about error if the identification process failed. (Only set if an error occured, if not is null)  

        :return: The error of this CreateBankIDMobileResponse.  
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CreateBankIDMobileResponse.

        Information about error if the identification process failed. (Only set if an error occured, if not is null)  

        :param error: The error of this CreateBankIDMobileResponse.  
        :type: Error
        """

        self._error = error

    @property
    def ok(self):
        """Gets the ok of this CreateBankIDMobileResponse.  

        Status if the request started without errors  

        :return: The ok of this CreateBankIDMobileResponse.  
        :rtype: bool
        """
        return self._ok

    @ok.setter
    def ok(self, ok):
        """Sets the ok of this CreateBankIDMobileResponse.

        Status if the request started without errors  

        :param ok: The ok of this CreateBankIDMobileResponse.  
        :type: bool
        """

        self._ok = ok

    @property
    def invalid_mobile_number_or_date_of_birth(self):
        """Gets the invalid_mobile_number_or_date_of_birth of this CreateBankIDMobileResponse.  

        Indicates if the Mobile number of the date of birth was invalid. These could be 2 things:   1 the user does not have BankID mobile,   2. Wrong input data (the combination of mobile and date of birth does not match  

        :return: The invalid_mobile_number_or_date_of_birth of this CreateBankIDMobileResponse.  
        :rtype: bool
        """
        return self._invalid_mobile_number_or_date_of_birth

    @invalid_mobile_number_or_date_of_birth.setter
    def invalid_mobile_number_or_date_of_birth(self, invalid_mobile_number_or_date_of_birth):
        """Sets the invalid_mobile_number_or_date_of_birth of this CreateBankIDMobileResponse.

        Indicates if the Mobile number of the date of birth was invalid. These could be 2 things:   1 the user does not have BankID mobile,   2. Wrong input data (the combination of mobile and date of birth does not match  

        :param invalid_mobile_number_or_date_of_birth: The invalid_mobile_number_or_date_of_birth of this CreateBankIDMobileResponse.  
        :type: bool
        """

        self._invalid_mobile_number_or_date_of_birth = invalid_mobile_number_or_date_of_birth

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
        if not isinstance(other, CreateBankIDMobileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
