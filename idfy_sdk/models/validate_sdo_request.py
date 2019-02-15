# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.signers import Signers  


class ValidateSDORequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sdo_data': 'str',
        'external_reference': 'str',
        'data_to_validate': 'str',
        'signers_to_validate': 'list[Signers]'
    }

    attribute_map = {
        'sdo_data': 'sdoData',
        'external_reference': 'externalReference',
        'data_to_validate': 'dataToValidate',
        'signers_to_validate': 'signersToValidate'
    }

    def __init__(self, sdo_data=None, external_reference=None, data_to_validate=None, signers_to_validate=None):  
        """ValidateSDORequest"""  

        self._sdo_data = None
        self._external_reference = None
        self._data_to_validate = None
        self._signers_to_validate = None
        self.discriminator = None

        self.sdo_data = sdo_data
        self.external_reference = external_reference
        if data_to_validate is not None:
            self.data_to_validate = data_to_validate
        if signers_to_validate is not None:
            self.signers_to_validate = signers_to_validate

    @property
    def sdo_data(self):
        """Gets the sdo_data of this ValidateSDORequest.  

        Base 64 encoded SDO (Signed document)  

        :return: The sdo_data of this ValidateSDORequest.  
        :rtype: str
        """
        return self._sdo_data

    @sdo_data.setter
    def sdo_data(self, sdo_data):
        """Sets the sdo_data of this ValidateSDORequest.

        Base 64 encoded SDO (Signed document)  

        :param sdo_data: The sdo_data of this ValidateSDORequest.  
        :type: str
        """
        if sdo_data is None:
            raise ValueError("Invalid value for `sdo_data`, must not be `None`")  

        self._sdo_data = sdo_data

    @property
    def external_reference(self):
        """Gets the external_reference of this ValidateSDORequest.  

        The service reference for the signing. Will be used for auditlog, and invoicing  

        :return: The external_reference of this ValidateSDORequest.  
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this ValidateSDORequest.

        The service reference for the signing. Will be used for auditlog, and invoicing  

        :param external_reference: The external_reference of this ValidateSDORequest.  
        :type: str
        """
        if external_reference is None:
            raise ValueError("Invalid value for `external_reference`, must not be `None`")  

        self._external_reference = external_reference

    @property
    def data_to_validate(self):
        """Gets the data_to_validate of this ValidateSDORequest.  

        Check that the original data matches the sdo data (optional, base64 encoded)  

        :return: The data_to_validate of this ValidateSDORequest.  
        :rtype: str
        """
        return self._data_to_validate

    @data_to_validate.setter
    def data_to_validate(self, data_to_validate):
        """Sets the data_to_validate of this ValidateSDORequest.

        Check that the original data matches the sdo data (optional, base64 encoded)  

        :param data_to_validate: The data_to_validate of this ValidateSDORequest.  
        :type: str
        """

        self._data_to_validate = data_to_validate

    @property
    def signers_to_validate(self):
        """Gets the signers_to_validate of this ValidateSDORequest.  

        Add signers to validate (optional)  

        :return: The signers_to_validate of this ValidateSDORequest.  
        :rtype: list[Signers]
        """
        return self._signers_to_validate

    @signers_to_validate.setter
    def signers_to_validate(self, signers_to_validate):
        """Sets the signers_to_validate of this ValidateSDORequest.

        Add signers to validate (optional)  

        :param signers_to_validate: The signers_to_validate of this ValidateSDORequest.  
        :type: list[Signers]
        """

        self._signers_to_validate = signers_to_validate

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
        if not isinstance(other, ValidateSDORequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
