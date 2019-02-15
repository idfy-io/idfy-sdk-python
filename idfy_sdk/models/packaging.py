# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.pades_settings import PadesSettings  


class Packaging(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'signature_package_formats': 'list[str]',
        'pades_settings': 'PadesSettings'
    }

    attribute_map = {
        'signature_package_formats': 'signaturePackageFormats',
        'pades_settings': 'padesSettings'
    }

    def __init__(self, signature_package_formats=None, pades_settings=None):  
        """Packaging"""  

        self._signature_package_formats = None
        self._pades_settings = None
        self.discriminator = None

        if signature_package_formats is not None:
            self.signature_package_formats = signature_package_formats
        if pades_settings is not None:
            self.pades_settings = pades_settings

    @property
    def signature_package_formats(self):
        """Gets the signature_package_formats of this Packaging.  

        A list of signature formats that will be created and made available for download after the document is signed.  See our documentation for more information about these formats. The native package format is included automatically (i.e. BankID SDO).  

        :return: The signature_package_formats of this Packaging.  
        :rtype: list[str]
        """
        return self._signature_package_formats

    @signature_package_formats.setter
    def signature_package_formats(self, signature_package_formats):
        """Sets the signature_package_formats of this Packaging.

        A list of signature formats that will be created and made available for download after the document is signed.  See our documentation for more information about these formats. The native package format is included automatically (i.e. BankID SDO).  

        :param signature_package_formats: The signature_package_formats of this Packaging.  
        :type: list[str]
        """
        allowed_values = ["xades", "pades", "no_bankid_pades"]  
        if not set(signature_package_formats).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `signature_package_formats` [{0}], must be a subset of [{1}]"  
                .format(", ".join(map(str, set(signature_package_formats) - set(allowed_values))),  
                        ", ".join(map(str, allowed_values)))
            )

        self._signature_package_formats = signature_package_formats

    @property
    def pades_settings(self):
        """Gets the pades_settings of this Packaging.  


        :return: The pades_settings of this Packaging.  
        :rtype: PadesSettings
        """
        return self._pades_settings

    @pades_settings.setter
    def pades_settings(self, pades_settings):
        """Sets the pades_settings of this Packaging.


        :param pades_settings: The pades_settings of this Packaging.  
        :type: PadesSettings
        """

        self._pades_settings = pades_settings

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
        if not isinstance(other, Packaging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
