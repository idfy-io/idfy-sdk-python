# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Authentication(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mechanism': 'str',
        'social_security_number': 'str',
        'signature_method_unique_id': 'str'
    }

    attribute_map = {
        'mechanism': 'mechanism',
        'social_security_number': 'socialSecurityNumber',
        'signature_method_unique_id': 'signatureMethodUniqueId'
    }

    def __init__(self, mechanism=None, social_security_number=None, signature_method_unique_id=None):  
        """Authentication"""  

        self._mechanism = None
        self._social_security_number = None
        self._signature_method_unique_id = None
        self.discriminator = None

        if mechanism is not None:
            self.mechanism = mechanism
        if social_security_number is not None:
            self.social_security_number = social_security_number
        if signature_method_unique_id is not None:
            self.signature_method_unique_id = signature_method_unique_id

    @property
    def mechanism(self):
        """Gets the mechanism of this Authentication.  

        Set the type of authentication you want before the user is allowed to view the document(s), sms otp will use the mobile number specified in signerinfo  

        :return: The mechanism of this Authentication.  
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """Sets the mechanism of this Authentication.

        Set the type of authentication you want before the user is allowed to view the document(s), sms otp will use the mobile number specified in signerinfo  

        :param mechanism: The mechanism of this Authentication.  
        :type: str
        """
        allowed_values = ["off", "eid", "smsOtp", "eidAndSmsOtp"]  
        if mechanism not in allowed_values:
            raise ValueError(
                "Invalid value for `mechanism` ({0}), must be one of {1}"  
                .format(mechanism, allowed_values)
            )

        self._mechanism = mechanism

    @property
    def social_security_number(self):
        """Gets the social_security_number of this Authentication.  

        The signer's social security number.  

        :return: The social_security_number of this Authentication.  
        :rtype: str
        """
        return self._social_security_number

    @social_security_number.setter
    def social_security_number(self, social_security_number):
        """Sets the social_security_number of this Authentication.

        The signer's social security number.  

        :param social_security_number: The social_security_number of this Authentication.  
        :type: str
        """

        self._social_security_number = social_security_number

    @property
    def signature_method_unique_id(self):
        """Gets the signature_method_unique_id of this Authentication.  

        The signer's unique ID for a signature method (for example the Norwegian BankID PID).  

        :return: The signature_method_unique_id of this Authentication.  
        :rtype: str
        """
        return self._signature_method_unique_id

    @signature_method_unique_id.setter
    def signature_method_unique_id(self, signature_method_unique_id):
        """Sets the signature_method_unique_id of this Authentication.

        The signer's unique ID for a signature method (for example the Norwegian BankID PID).  

        :param signature_method_unique_id: The signature_method_unique_id of this Authentication.  
        :type: str
        """

        self._signature_method_unique_id = signature_method_unique_id

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
        if not isinstance(other, Authentication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
