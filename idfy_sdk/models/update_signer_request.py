# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.authentication import Authentication  
from idfy_sdk.models.extra_info_signer_request import ExtraInfoSignerRequest  
from idfy_sdk.models.notifications import Notifications  
from idfy_sdk.models.redirect_settings import RedirectSettings  
from idfy_sdk.models.signature_type import SignatureType  
from idfy_sdk.models.signer_info import SignerInfo  
from idfy_sdk.models.ui import UI  


class UpdateSignerRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'external_signer_id': 'str',
        'redirect_settings': 'RedirectSettings',
        'signature_type': 'SignatureType',
        'signer_info': 'SignerInfo',
        'authentication': 'Authentication',
        'extra_info': 'ExtraInfoSignerRequest',
        'ui': 'UI',
        'notifications': 'Notifications',
        'tags': 'list[str]',
        'order': 'int',
        'required': 'bool',
        'sign_url_expires': 'datetime'
    }

    attribute_map = {
        'external_signer_id': 'externalSignerId',
        'redirect_settings': 'redirectSettings',
        'signature_type': 'signatureType',
        'signer_info': 'signerInfo',
        'authentication': 'authentication',
        'extra_info': 'extraInfo',
        'ui': 'ui',
        'notifications': 'notifications',
        'tags': 'tags',
        'order': 'order',
        'required': 'required',
        'sign_url_expires': 'signUrlExpires'
    }

    def __init__(self, external_signer_id=None, redirect_settings=None, signature_type=None, signer_info=None, authentication=None, extra_info=None, ui=None, notifications=None, tags=None, order=None, required=None, sign_url_expires=None):  
        """UpdateSignerRequest"""  

        self._external_signer_id = None
        self._redirect_settings = None
        self._signature_type = None
        self._signer_info = None
        self._authentication = None
        self._extra_info = None
        self._ui = None
        self._notifications = None
        self._tags = None
        self._order = None
        self._required = None
        self._sign_url_expires = None
        self.discriminator = None

        if external_signer_id is not None:
            self.external_signer_id = external_signer_id
        if redirect_settings is not None:
            self.redirect_settings = redirect_settings
        if signature_type is not None:
            self.signature_type = signature_type
        if signer_info is not None:
            self.signer_info = signer_info
        if authentication is not None:
            self.authentication = authentication
        if extra_info is not None:
            self.extra_info = extra_info
        if ui is not None:
            self.ui = ui
        if notifications is not None:
            self.notifications = notifications
        if tags is not None:
            self.tags = tags
        if order is not None:
            self.order = order
        if required is not None:
            self.required = required
        if sign_url_expires is not None:
            self.sign_url_expires = sign_url_expires

    @property
    def external_signer_id(self):
        """Gets the external_signer_id of this UpdateSignerRequest.  

        Your reference for the signer.  

        :return: The external_signer_id of this UpdateSignerRequest.  
        :rtype: str
        """
        return self._external_signer_id

    @external_signer_id.setter
    def external_signer_id(self, external_signer_id):
        """Sets the external_signer_id of this UpdateSignerRequest.

        Your reference for the signer.  

        :param external_signer_id: The external_signer_id of this UpdateSignerRequest.  
        :type: str
        """
        if external_signer_id is not None and len(external_signer_id) > 255:
            raise ValueError("Invalid value for `external_signer_id`, length must be less than or equal to `255`")  
        if external_signer_id is not None and len(external_signer_id) < 4:
            raise ValueError("Invalid value for `external_signer_id`, length must be greater than or equal to `4`")  

        self._external_signer_id = external_signer_id

    @property
    def redirect_settings(self):
        """Gets the redirect_settings of this UpdateSignerRequest.  

        Return URLs and domain settings  

        :return: The redirect_settings of this UpdateSignerRequest.  
        :rtype: RedirectSettings
        """
        return self._redirect_settings

    @redirect_settings.setter
    def redirect_settings(self, redirect_settings):
        """Sets the redirect_settings of this UpdateSignerRequest.

        Return URLs and domain settings  

        :param redirect_settings: The redirect_settings of this UpdateSignerRequest.  
        :type: RedirectSettings
        """

        self._redirect_settings = redirect_settings

    @property
    def signature_type(self):
        """Gets the signature_type of this UpdateSignerRequest.  


        :return: The signature_type of this UpdateSignerRequest.  
        :rtype: SignatureType
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this UpdateSignerRequest.


        :param signature_type: The signature_type of this UpdateSignerRequest.  
        :type: SignatureType
        """

        self._signature_type = signature_type

    @property
    def signer_info(self):
        """Gets the signer_info of this UpdateSignerRequest.  

        Define the signers name, mobile and email if you are using notifications  

        :return: The signer_info of this UpdateSignerRequest.  
        :rtype: SignerInfo
        """
        return self._signer_info

    @signer_info.setter
    def signer_info(self, signer_info):
        """Sets the signer_info of this UpdateSignerRequest.

        Define the signers name, mobile and email if you are using notifications  

        :param signer_info: The signer_info of this UpdateSignerRequest.  
        :type: SignerInfo
        """

        self._signer_info = signer_info

    @property
    def authentication(self):
        """Gets the authentication of this UpdateSignerRequest.  

        Do you want the signer to authenticate before they can see the document?  

        :return: The authentication of this UpdateSignerRequest.  
        :rtype: Authentication
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this UpdateSignerRequest.

        Do you want the signer to authenticate before they can see the document?  

        :param authentication: The authentication of this UpdateSignerRequest.  
        :type: Authentication
        """

        self._authentication = authentication

    @property
    def extra_info(self):
        """Gets the extra_info of this UpdateSignerRequest.  

        Coming soon: Do you want to collect extra info about this specific signer? (for example personal information)  

        :return: The extra_info of this UpdateSignerRequest.  
        :rtype: ExtraInfoSignerRequest
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this UpdateSignerRequest.

        Coming soon: Do you want to collect extra info about this specific signer? (for example personal information)  

        :param extra_info: The extra_info of this UpdateSignerRequest.  
        :type: ExtraInfoSignerRequest
        """

        self._extra_info = extra_info

    @property
    def ui(self):
        """Gets the ui of this UpdateSignerRequest.  


        :return: The ui of this UpdateSignerRequest.  
        :rtype: UI
        """
        return self._ui

    @ui.setter
    def ui(self, ui):
        """Sets the ui of this UpdateSignerRequest.


        :param ui: The ui of this UpdateSignerRequest.  
        :type: UI
        """

        self._ui = ui

    @property
    def notifications(self):
        """Gets the notifications of this UpdateSignerRequest.  


        :return: The notifications of this UpdateSignerRequest.  
        :rtype: Notifications
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this UpdateSignerRequest.


        :param notifications: The notifications of this UpdateSignerRequest.  
        :type: Notifications
        """

        self._notifications = notifications

    @property
    def tags(self):
        """Gets the tags of this UpdateSignerRequest.  

        Coming soon.  

        :return: The tags of this UpdateSignerRequest.  
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateSignerRequest.

        Coming soon.  

        :param tags: The tags of this UpdateSignerRequest.  
        :type: list[str]
        """

        self._tags = tags

    @property
    def order(self):
        """Gets the order of this UpdateSignerRequest.  

        Optional order of signing for the signer.  

        :return: The order of this UpdateSignerRequest.  
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this UpdateSignerRequest.

        Optional order of signing for the signer.  

        :param order: The order of this UpdateSignerRequest.  
        :type: int
        """

        self._order = order

    @property
    def required(self):
        """Gets the required of this UpdateSignerRequest.  

        Determines if the signer is required to sign the document before other signers. Any other signers will not be allowed to sign before all required signers have signed the document.  

        :return: The required of this UpdateSignerRequest.  
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this UpdateSignerRequest.

        Determines if the signer is required to sign the document before other signers. Any other signers will not be allowed to sign before all required signers have signed the document.  

        :param required: The required of this UpdateSignerRequest.  
        :type: bool
        """

        self._required = required

    @property
    def sign_url_expires(self):
        """Gets the sign_url_expires of this UpdateSignerRequest.  

        The time at which the signature URL expires (ISO 8601). Specify this if you want a limited time-to-live for the URL. Defaults to the lifetime of the document.  

        :return: The sign_url_expires of this UpdateSignerRequest.  
        :rtype: datetime
        """
        return self._sign_url_expires

    @sign_url_expires.setter
    def sign_url_expires(self, sign_url_expires):
        """Sets the sign_url_expires of this UpdateSignerRequest.

        The time at which the signature URL expires (ISO 8601). Specify this if you want a limited time-to-live for the URL. Defaults to the lifetime of the document.  

        :param sign_url_expires: The sign_url_expires of this UpdateSignerRequest.  
        :type: datetime
        """

        self._sign_url_expires = sign_url_expires

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
        if not isinstance(other, UpdateSignerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
