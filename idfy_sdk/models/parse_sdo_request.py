# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class ParseSDORequest(object):

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
        'fetch_ssn': 'bool'
    }

    attribute_map = {
        'sdo_data': 'sdoData',
        'external_reference': 'externalReference',
        'fetch_ssn': 'fetchSSN'
    }

    def __init__(self, sdo_data=None, external_reference=None, fetch_ssn=None):  
        """ParseSDORequest"""  

        self._sdo_data = None
        self._external_reference = None
        self._fetch_ssn = None
        self.discriminator = None

        self.sdo_data = sdo_data
        self.external_reference = external_reference
        if fetch_ssn is not None:
            self.fetch_ssn = fetch_ssn

    @property
    def sdo_data(self):
        """Gets the sdo_data of this ParseSDORequest.  

        Base 64 encoded SDO (Signed document)  

        :return: The sdo_data of this ParseSDORequest.  
        :rtype: str
        """
        return self._sdo_data

    @sdo_data.setter
    def sdo_data(self, sdo_data):
        """Sets the sdo_data of this ParseSDORequest.

        Base 64 encoded SDO (Signed document)  

        :param sdo_data: The sdo_data of this ParseSDORequest.  
        :type: str
        """
        if sdo_data is None:
            raise ValueError("Invalid value for `sdo_data`, must not be `None`")  

        self._sdo_data = sdo_data

    @property
    def external_reference(self):
        """Gets the external_reference of this ParseSDORequest.  

        The service reference for the signing. Will be used for auditlog, and invoicing  

        :return: The external_reference of this ParseSDORequest.  
        :rtype: str
        """
        return self._external_reference

    @external_reference.setter
    def external_reference(self, external_reference):
        """Sets the external_reference of this ParseSDORequest.

        The service reference for the signing. Will be used for auditlog, and invoicing  

        :param external_reference: The external_reference of this ParseSDORequest.  
        :type: str
        """
        if external_reference is None:
            raise ValueError("Invalid value for `external_reference`, must not be `None`")  

        self._external_reference = external_reference

    @property
    def fetch_ssn(self):
        """Gets the fetch_ssn of this ParseSDORequest.  

        Fetch social security number (Requires valid scope)  

        :return: The fetch_ssn of this ParseSDORequest.  
        :rtype: bool
        """
        return self._fetch_ssn

    @fetch_ssn.setter
    def fetch_ssn(self, fetch_ssn):
        """Sets the fetch_ssn of this ParseSDORequest.

        Fetch social security number (Requires valid scope)  

        :param fetch_ssn: The fetch_ssn of this ParseSDORequest.  
        :type: bool
        """

        self._fetch_ssn = fetch_ssn

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
        if not isinstance(other, ParseSDORequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
