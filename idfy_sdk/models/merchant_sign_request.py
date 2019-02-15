# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class MerchantSignRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data_to_sign': 'str',
        'xslt': 'str',
        'data_format': 'str',
        'data_encoding_format': 'str',
        'external_reference': 'str',
        'signing_format': 'str',
        'department_id': 'str'
    }

    attribute_map = {
        'data_to_sign': 'dataToSign',
        'xslt': 'xslt',
        'data_format': 'dataFormat',
        'data_encoding_format': 'dataEncodingFormat',
        'external_reference': 'externalReference',
        'signing_format': 'signingFormat',
        'department_id': 'departmentId'
    }

    def __init__(self, data_to_sign=None, xslt=None, data_format=None, data_encoding_format=None, external_reference=None, signing_format=None, department_id=None):  
        """MerchantSignRequest"""  

        self._data_to_sign = None
        self._xslt = None
        self._data_format = None
        self._data_encoding_format = None
        self._external_reference = None
        self._signing_format = None
        self._department_id = None
        self.discriminator = None

        self.data_to_sign = data_to_sign
        if xslt is not None:
            self.xslt = xslt
        self.data_format = data_format
        if data_encoding_format is not None:
            self.data_encoding_format = data_encoding_format
        self.external_reference = external_reference
        if signing_format is not None:
            self.signing_format = signing_format
        if department_id is not None:
            self.department_id = department_id

    @property
    def data_encoding_format(self):
        return self._data_encoding_format

    @data_encoding_format.setter
    def data_encoding_format(self, data_encoding_format):
        self._data_encoding_format = data_encoding_format
    
    @property
    def department_id(self):
        return self._department_id
    
    @department_id.setter
    def department_id(self, department_id):
        self._department_id = department_id

    @property
    def data_to_sign(self):
        """Gets the data_to_sign of this MerchantSignRequest.  

        Base 64 encoded data  

        :return: The data_to_sign of this MerchantSignRequest.  
        :rtype: str
        """
        return self._data_to_sign

    @data_to_sign.setter
    def data_to_sign(self, data_to_sign):
        """Sets the data_to_sign of this MerchantSignRequest.

        Base 64 encoded data  

        :param data_to_sign: The data_to_sign of this MerchantSignRequest.  
        :type: str
        """
        if data_to_sign is None:
            raise ValueError("Invalid value for `data_to_sign`, must not be `None`")  

        self._data_to_sign = data_to_sign

    @property
    def xslt(self):
        """Gets the xslt of this MerchantSignRequest.  

        Base 64 encoded xslt (optional)  

        :return: The xslt of this MerchantSignRequest.  
        :rtype: str
        """
        return self._xslt

    @xslt.setter
    def xslt(self, xslt):
        """Sets the xslt of this MerchantSignRequest.

        Base 64 encoded xslt (optional)  

        :param xslt: The xslt of this MerchantSignRequest.  
        :type: str
        """

        self._xslt = xslt

    @property
    def data_format(self):
        """Gets the data_format of this MerchantSignRequest.  

        Format of data (i.e xml)  

        :return: The data_format of this MerchantSignRequest.  
        :rtype: str
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """Sets the data_format of this MerchantSignRequest.

        Format of data (i.e xml)  

        :param data_format: The data_format of this MerchantSignRequest.  
        :type: str
        """
        if data_format is None:
            raise ValueError("Invalid value for `data_format`, must not be `None`")  
        allowed_values = ["xml", "pdf", "txt"]  
        if data_format not in allowed_values:
            raise ValueError(
                "Invalid value for `data_format` ({0}), must be one of {1}"  
                .format(data_format, allowed_values)
            )

        self._data_format = data_format

    @property
    def external_reference(self):
        """Gets the external_reference of this MerchantSignRequest.  

        The service reference for the signing. Will be used for auditlog, and invoicing  

        :return: The external_reference of this MerchantSignRequest.  
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this MerchantSignRequest.

        The service reference for the signing. Will be used for auditlog, and invoicing  

        :param external_reference: The external_reference of this MerchantSignRequest.  
        :type: str
        """
        if external_reference is None:
            raise ValueError("Invalid value for `external_reference`, must not be `None`")  

        self._external_reference = external_reference

    @property
    def signing_format(self):
        """Gets the signing_format of this MerchantSignRequest.  

        Optional, if not set the default setting for the account will be used  

        :return: The signing_format of this MerchantSignRequest.  
        :rtype: str
        """
        return self._signing_format

    @signing_format.setter
    def signing_format(self, signing_format):
        """Sets the signing_format of this MerchantSignRequest.

        Optional, if not set the default setting for the account will be used  

        :param signing_format: The signing_format of this MerchantSignRequest.  
        :type: str
        """
        allowed_values = ["use_provider_setting", "no_bankid_seid_sdo", "no_bankid_pades", "no_buypass_seid_sdo", "da_nemid_xmldsig", "sv_bankid_native_pkcs7"]  
        if signing_format not in allowed_values:
            raise ValueError(
                "Invalid value for `signing_format` ({0}), must be one of {1}"  
                .format(signing_format, allowed_values)
            )

        self._signing_format = signing_format

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
        if not isinstance(other, MerchantSignRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
