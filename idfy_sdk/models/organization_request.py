# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.check_signature import CheckSignature  


class OrganizationRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'org_number': 'str',
        'prokura': 'bool',
        'signature': 'bool',
        'signatures': 'list[CheckSignature]'
    }

    attribute_map = {
        'org_number': 'OrgNumber',
        'prokura': 'Prokura',
        'signature': 'Signature',
        'signatures': 'Signatures'
    }

    def __init__(self, org_number=None, prokura=None, signature=None, signatures=None):  
        """OrganizationRequest"""  

        self._org_number = None
        self._prokura = None
        self._signature = None
        self._signatures = None
        self.discriminator = None

        if org_number is not None:
            self.org_number = org_number
        if prokura is not None:
            self.prokura = prokura
        if signature is not None:
            self.signature = signature
        if signatures is not None:
            self.signatures = signatures

    @property
    def org_number(self):
        """Gets the org_number of this OrganizationRequest.  


        :return: The org_number of this OrganizationRequest.  
        :rtype: str
        """
        return self._org_number

    @org_number.setter
    def org_number(self, org_number):
        """Sets the org_number of this OrganizationRequest.


        :param org_number: The org_number of this OrganizationRequest.  
        :type: str
        """

        self._org_number = org_number

    @property
    def prokura(self):
        """Gets the prokura of this OrganizationRequest.  


        :return: The prokura of this OrganizationRequest.  
        :rtype: bool
        """
        return self._prokura

    @prokura.setter
    def prokura(self, prokura):
        """Sets the prokura of this OrganizationRequest.


        :param prokura: The prokura of this OrganizationRequest.  
        :type: bool
        """

        self._prokura = prokura

    @property
    def signature(self):
        """Gets the signature of this OrganizationRequest.  


        :return: The signature of this OrganizationRequest.  
        :rtype: bool
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this OrganizationRequest.


        :param signature: The signature of this OrganizationRequest.  
        :type: bool
        """

        self._signature = signature

    @property
    def signatures(self):
        """Gets the signatures of this OrganizationRequest.  


        :return: The signatures of this OrganizationRequest.  
        :rtype: list[CheckSignature]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """Sets the signatures of this OrganizationRequest.


        :param signatures: The signatures of this OrganizationRequest.  
        :type: list[CheckSignature]
        """

        self._signatures = signatures

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
        if not isinstance(other, OrganizationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
