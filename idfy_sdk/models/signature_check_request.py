# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.organization_request import OrganizationRequest  


class SignatureCheckRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'organizations': 'list[OrganizationRequest]'
    }

    attribute_map = {
        'organizations': 'Organizations'
    }

    def __init__(self, organizations=None):  
        """SignatureCheckRequest"""  

        self._organizations = None
        self.discriminator = None

        if organizations is not None:
            self.organizations = organizations

    @property
    def organizations(self):
        """Gets the organizations of this SignatureCheckRequest.  


        :return: The organizations of this SignatureCheckRequest.  
        :rtype: list[OrganizationRequest]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this SignatureCheckRequest.


        :param organizations: The organizations of this SignatureCheckRequest.  
        :type: list[OrganizationRequest]
        """

        self._organizations = organizations

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
        if not isinstance(other, SignatureCheckRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
