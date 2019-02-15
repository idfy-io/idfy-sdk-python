# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.i_frame_settings import IFrameSettings  
from idfy_sdk.models.return_urls import ReturnUrls  


class CreateIdentificationRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'identity_provider': 'str',
        'return_urls': 'ReturnUrls',
        'i_frame': 'IFrameSettings',
        'language': 'str',
        'get_social_security_number': 'bool',
        'pre_filled_social_security_number': 'str',
        'page_title': 'str',
        'external_reference': 'str',
        'addonservices': 'dict(str, str)'
    }

    attribute_map = {
        'identity_provider': 'IdentityProvider',
        'return_urls': 'ReturnUrls',
        'i_frame': 'iFrame',
        'language': 'Language',
        'get_social_security_number': 'GetSocialSecurityNumber',
        'pre_filled_social_security_number': 'PreFilledSocialSecurityNumber',
        'page_title': 'PageTitle',
        'external_reference': 'ExternalReference',
        'addonservices': 'Addonservices'
    }

    def __init__(self, identity_provider=None, return_urls=None, i_frame=None, language=None, get_social_security_number=None, pre_filled_social_security_number=None, page_title=None, external_reference=None, addonservices=None):  
        """CreateIdentificationRequest"""  

        self._identity_provider = None
        self._return_urls = None
        self._i_frame = None
        self._language = None
        self._get_social_security_number = None
        self._pre_filled_social_security_number = None
        self._page_title = None
        self._external_reference = None
        self._addonservices = None
        self.discriminator = None

        if identity_provider is not None:
            self.identity_provider = identity_provider
        self.return_urls = return_urls
        if i_frame is not None:
            self.i_frame = i_frame
        if language is not None:
            self.language = language
        if get_social_security_number is not None:
            self.get_social_security_number = get_social_security_number
        if pre_filled_social_security_number is not None:
            self.pre_filled_social_security_number = pre_filled_social_security_number
        if page_title is not None:
            self.page_title = page_title
        if external_reference is not None:
            self.external_reference = external_reference
        if addonservices is not None:
            self.addonservices = addonservices

    @property
    def identity_provider(self):
        """Gets the identity_provider of this CreateIdentificationRequest.  

        The identityprovider to use for the identification, if not set the user will get a list of all the e-ID assosiated with your account to choose from.  

        :return: The identity_provider of this CreateIdentificationRequest.  
        :rtype: str
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        """Sets the identity_provider of this CreateIdentificationRequest.

        The identityprovider to use for the identification, if not set the user will get a list of all the e-ID assosiated with your account to choose from.  

        :param identity_provider: The identity_provider of this CreateIdentificationRequest.  
        :type: str
        """
        allowed_values = ["UNKNOWN", "NO_BANKID_MOBILE", "NO_BANKID_WEB", "SWE_BANKID", "SWE_BANKID_MOBILE", "NO_BUYPASS", "DA_NEMID", "FI_TUPAS"]  
        if identity_provider not in allowed_values:
            raise ValueError(
                "Invalid value for `identity_provider` ({0}), must be one of {1}"  
                .format(identity_provider, allowed_values)
            )

        self._identity_provider = identity_provider

    @property
    def return_urls(self):
        """Gets the return_urls of this CreateIdentificationRequest.  

        The return urls to be redirected to after the identification process is done  

        :return: The return_urls of this CreateIdentificationRequest.  
        :rtype: ReturnUrls
        """
        return self._return_urls

    @return_urls.setter
    def return_urls(self, return_urls):
        """Sets the return_urls of this CreateIdentificationRequest.

        The return urls to be redirected to after the identification process is done  

        :param return_urls: The return_urls of this CreateIdentificationRequest.  
        :type: ReturnUrls
        """
        if return_urls is None:
            raise ValueError("Invalid value for `return_urls`, must not be `None`")  

        self._return_urls = return_urls

    @property
    def i_frame(self):
        """Gets the i_frame of this CreateIdentificationRequest.  

        If the identity process should be done in an iframe this settings object would have to set. The redirect is then done in javascript.  

        :return: The i_frame of this CreateIdentificationRequest.  
        :rtype: IFrameSettings
        """
        return self._i_frame

    @i_frame.setter
    def i_frame(self, i_frame):
        """Sets the i_frame of this CreateIdentificationRequest.

        If the identity process should be done in an iframe this settings object would have to set. The redirect is then done in javascript.  

        :param i_frame: The i_frame of this CreateIdentificationRequest.  
        :type: IFrameSettings
        """

        self._i_frame = i_frame

    @property
    def language(self):
        """Gets the language of this CreateIdentificationRequest.  

        The language to be used for the identification process, if not set the language of the users browser will be used.  

        :return: The language of this CreateIdentificationRequest.  
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreateIdentificationRequest.

        The language to be used for the identification process, if not set the language of the users browser will be used.  

        :param language: The language of this CreateIdentificationRequest.  
        :type: str
        """
        allowed_values = ["NO", "EN", "SV", "DA", "FI"]  
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def get_social_security_number(self):
        """Gets the get_social_security_number of this CreateIdentificationRequest.  

        Should the socialsecuritynumber be fetched from the identityprovider? Beware that there is an extra cost of doing this every time and one need permission to do it.  

        :return: The get_social_security_number of this CreateIdentificationRequest.  
        :rtype: bool
        """
        return self._get_social_security_number

    @get_social_security_number.setter
    def get_social_security_number(self, get_social_security_number):
        """Sets the get_social_security_number of this CreateIdentificationRequest.

        Should the socialsecuritynumber be fetched from the identityprovider? Beware that there is an extra cost of doing this every time and one need permission to do it.  

        :param get_social_security_number: The get_social_security_number of this CreateIdentificationRequest.  
        :type: bool
        """

        self._get_social_security_number = get_social_security_number

    @property
    def pre_filled_social_security_number(self):
        """Gets the pre_filled_social_security_number of this CreateIdentificationRequest.  

        If this is specified then the client will be prefilled with this value. (supported by Norwegian BankID, NemID and Tupas)  

        :return: The pre_filled_social_security_number of this CreateIdentificationRequest.  
        :rtype: str
        """
        return self._pre_filled_social_security_number

    @pre_filled_social_security_number.setter
    def pre_filled_social_security_number(self, pre_filled_social_security_number):
        """Sets the pre_filled_social_security_number of this CreateIdentificationRequest.

        If this is specified then the client will be prefilled with this value. (supported by Norwegian BankID, NemID and Tupas)  

        :param pre_filled_social_security_number: The pre_filled_social_security_number of this CreateIdentificationRequest.  
        :type: str
        """

        self._pre_filled_social_security_number = pre_filled_social_security_number

    @property
    def page_title(self):
        """Gets the page_title of this CreateIdentificationRequest.  

        Title of the identification page (Used when redirecting on larger devices). Not used in iFrame mode  

        :return: The page_title of this CreateIdentificationRequest.  
        :rtype: str
        """
        return self._page_title

    @page_title.setter
    def page_title(self, page_title):
        """Sets the page_title of this CreateIdentificationRequest.

        Title of the identification page (Used when redirecting on larger devices). Not used in iFrame mode  

        :param page_title: The page_title of this CreateIdentificationRequest.  
        :type: str
        """

        self._page_title = page_title

    @property
    def external_reference(self):
        """Gets the external_reference of this CreateIdentificationRequest.  

        The merchants reference to the identification process, this will also be used to identify an identification in a detailed invoice. It is an advantage if this is unique for each API call.  

        :return: The external_reference of this CreateIdentificationRequest.  
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this CreateIdentificationRequest.

        The merchants reference to the identification process, this will also be used to identify an identification in a detailed invoice. It is an advantage if this is unique for each API call.  

        :param external_reference: The external_reference of this CreateIdentificationRequest.  
        :type: str
        """

        self._external_reference = external_reference

    @property
    def addonservices(self):
        """Gets the addonservices of this CreateIdentificationRequest.  

        List of addon data that can be orderd. The result will be in MetaData list of the reponse  

        :return: The addonservices of this CreateIdentificationRequest.  
        :rtype: dict(str, str)
        """
        return self._addonservices

    @addonservices.setter
    def addonservices(self, addonservices):
        """Sets the addonservices of this CreateIdentificationRequest.

        List of addon data that can be orderd. The result will be in MetaData list of the reponse  

        :param addonservices: The addonservices of this CreateIdentificationRequest.  
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
        if not isinstance(other, CreateIdentificationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
