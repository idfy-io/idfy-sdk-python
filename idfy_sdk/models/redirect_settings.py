# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class RedirectSettings(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'redirect_mode': 'str',
        'domain': 'str',
        'error': 'str',
        'cancel': 'str',
        'success': 'str'
    }

    attribute_map = {
        'redirect_mode': 'redirectMode',
        'domain': 'domain',
        'error': 'error',
        'cancel': 'cancel',
        'success': 'success'
    }

    def __init__(self, redirect_mode=None, domain=None, error=None, cancel=None, success=None):  
        """RedirectSettings"""  

        self._redirect_mode = None
        self._domain = None
        self._error = None
        self._cancel = None
        self._success = None
        self.discriminator = None

        self.redirect_mode = redirect_mode
        if domain is not None:
            self.domain = domain
        if error is not None:
            self.error = error
        if cancel is not None:
            self.cancel = cancel
        if success is not None:
            self.success = success

    @property
    def redirect_mode(self):
        """Gets the redirect_mode of this RedirectSettings.  

        Defines the redirect mode to use for the signer.  

        :return: The redirect_mode of this RedirectSettings.  
        :rtype: str
        """
        return self._redirect_mode

    @redirect_mode.setter
    def redirect_mode(self, redirect_mode):
        """Sets the redirect_mode of this RedirectSettings.

        Defines the redirect mode to use for the signer.  

        :param redirect_mode: The redirect_mode of this RedirectSettings.  
        :type: str
        """
        if redirect_mode is None:
            raise ValueError("Invalid value for `redirect_mode`, must not be `None`")  
        allowed_values = ["donot_redirect", "redirect", "iframe_with_webmessaging", "iframe_with_redirect", "iframe_with_redirect_and_webmessaging"]  
        if redirect_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `redirect_mode` ({0}), must be one of {1}"  
                .format(redirect_mode, allowed_values)
            )

        self._redirect_mode = redirect_mode

    @property
    def domain(self):
        """Gets the domain of this RedirectSettings.  

        The domain your website is hosted on.  <span style=\"color: red;\">Required if you specify one of the iframe redirect modes for the signer.</span>  

        :return: The domain of this RedirectSettings.  
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this RedirectSettings.

        The domain your website is hosted on.  <span style=\"color: red;\">Required if you specify one of the iframe redirect modes for the signer.</span>  

        :param domain: The domain of this RedirectSettings.  
        :type: str
        """

        self._domain = domain

    @property
    def error(self):
        """Gets the error of this RedirectSettings.  

        The URL that the signer is redirected to if something goes wrong. <span style=\"color: red;\">Required if you use redirect for the signer.</span>  

        :return: The error of this RedirectSettings.  
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RedirectSettings.

        The URL that the signer is redirected to if something goes wrong. <span style=\"color: red;\">Required if you use redirect for the signer.</span>  

        :param error: The error of this RedirectSettings.  
        :type: str
        """

        self._error = error

    @property
    def cancel(self):
        """Gets the cancel of this RedirectSettings.  

        The URL that the signer is redirected to if the signing is cancelled. <span style=\"color: red;\">Required if you use redirect for the signer.</span>  

        :return: The cancel of this RedirectSettings.  
        :rtype: str
        """
        return self._cancel

    @cancel.setter
    def cancel(self, cancel):
        """Sets the cancel of this RedirectSettings.

        The URL that the signer is redirected to if the signing is cancelled. <span style=\"color: red;\">Required if you use redirect for the signer.</span>  

        :param cancel: The cancel of this RedirectSettings.  
        :type: str
        """

        self._cancel = cancel

    @property
    def success(self):
        """Gets the success of this RedirectSettings.  

        The URL that the signer is redirected to after a successful signing. <span style=\"color: red;\">Required if you use redirect for the signer.</span>  

        :return: The success of this RedirectSettings.  
        :rtype: str
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this RedirectSettings.

        The URL that the signer is redirected to after a successful signing. <span style=\"color: red;\">Required if you use redirect for the signer.</span>  

        :param success: The success of this RedirectSettings.  
        :type: str
        """

        self._success = success

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
        if not isinstance(other, RedirectSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
