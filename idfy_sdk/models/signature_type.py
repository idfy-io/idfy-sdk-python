# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class SignatureType(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'signature_methods': 'list[str]',
        'mechanism': 'str',
        'on_eaccept_use_hand_written_signature': 'bool'
    }

    attribute_map = {
        'signature_methods': 'signatureMethods',
        'mechanism': 'mechanism',
        'on_eaccept_use_hand_written_signature': 'onEacceptUseHandWrittenSignature'
    }

    def __init__(self, signature_methods=None, mechanism=None, on_eaccept_use_hand_written_signature=None):  
        """SignatureType"""  

        self._signature_methods = None
        self._mechanism = None
        self._on_eaccept_use_hand_written_signature = None
        self.discriminator = None

        if signature_methods is not None:
            self.signature_methods = signature_methods
        self.mechanism = mechanism
        if on_eaccept_use_hand_written_signature is not None:
            self.on_eaccept_use_hand_written_signature = on_eaccept_use_hand_written_signature

    @property
    def signature_methods(self):
        """Gets the signature_methods of this SignatureType.  

        A list of signature methods that the signer is allowed to use when signing the document.  If not specified, all available signature methods for your Idfy account will be displayed to the signer.  

        :return: The signature_methods of this SignatureType.  
        :rtype: list[str]
        """
        return self._signature_methods

    @signature_methods.setter
    def signature_methods(self, signature_methods):
        """Sets the signature_methods of this SignatureType.

        A list of signature methods that the signer is allowed to use when signing the document.  If not specified, all available signature methods for your Idfy account will be displayed to the signer.  

        :param signature_methods: The signature_methods of this SignatureType.  
        :type: list[str]
        """
        allowed_values = ["no_bankid", "no_bankid_mobile", "no_bankid_netcentric", "no_buypass", "no_commfides", "se_bankid", "dk_nemid", "fi_tupas", "fi_mobiilivarmenne", "nl_digid", "es_dni", "ee_esteid", "mobile_connect", "sms_otp", "identification_papers", "social", "unknown"]  
        if not set(signature_methods).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `signature_methods` [{0}], must be a subset of [{1}]"  
                .format(", ".join(map(str, set(signature_methods) - set(allowed_values))),  
                        ", ".join(map(str, allowed_values)))
            )

        self._signature_methods = signature_methods

    @property
    def mechanism(self):
        """Gets the mechanism of this SignatureType.  


        :return: The mechanism of this SignatureType.  
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """Sets the mechanism of this SignatureType.


        :param mechanism: The mechanism of this SignatureType.  
        :type: str
        """
        if mechanism is None:
            raise ValueError("Invalid value for `mechanism`, must not be `None`")  
        allowed_values = ["pkisignature", "eaccept"]  
        if mechanism not in allowed_values:
            raise ValueError(
                "Invalid value for `mechanism` ({0}), must be one of {1}"  
                .format(mechanism, allowed_values)
            )

        self._mechanism = mechanism

    @property
    def on_eaccept_use_hand_written_signature(self):
        """Gets the on_eaccept_use_hand_written_signature of this SignatureType.  


        :return: The on_eaccept_use_hand_written_signature of this SignatureType.  
        :rtype: bool
        """
        return self._on_eaccept_use_hand_written_signature

    @on_eaccept_use_hand_written_signature.setter
    def on_eaccept_use_hand_written_signature(self, on_eaccept_use_hand_written_signature):
        """Sets the on_eaccept_use_hand_written_signature of this SignatureType.


        :param on_eaccept_use_hand_written_signature: The on_eaccept_use_hand_written_signature of this SignatureType.  
        :type: bool
        """

        self._on_eaccept_use_hand_written_signature = on_eaccept_use_hand_written_signature

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
        if not isinstance(other, SignatureType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
