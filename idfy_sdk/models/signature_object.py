# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.other_signatures import OtherSignatures  
from idfy_sdk.models.required_signatures import RequiredSignatures  


class SignatureObject(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'requirements_description': 'str',
        'required': 'RequiredSignatures',
        'others': 'OtherSignatures'
    }

    attribute_map = {
        'requirements_description': 'RequirementsDescription',
        'required': 'Required',
        'others': 'Others'
    }

    def __init__(self, requirements_description=None, required=None, others=None):  
        """SignatureObject"""  

        self._requirements_description = None
        self._required = None
        self._others = None
        self.discriminator = None

        if requirements_description is not None:
            self.requirements_description = requirements_description
        if required is not None:
            self.required = required
        if others is not None:
            self.others = others

    @property
    def requirements_description(self):
        """Gets the requirements_description of this SignatureObject.  


        :return: The requirements_description of this SignatureObject.  
        :rtype: str
        """
        return self._requirements_description

    @requirements_description.setter
    def requirements_description(self, requirements_description):
        """Sets the requirements_description of this SignatureObject.


        :param requirements_description: The requirements_description of this SignatureObject.  
        :type: str
        """

        self._requirements_description = requirements_description

    @property
    def required(self):
        """Gets the required of this SignatureObject.  


        :return: The required of this SignatureObject.  
        :rtype: RequiredSignatures
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this SignatureObject.


        :param required: The required of this SignatureObject.  
        :type: RequiredSignatures
        """

        self._required = required

    @property
    def others(self):
        """Gets the others of this SignatureObject.  


        :return: The others of this SignatureObject.  
        :rtype: OtherSignatures
        """
        return self._others

    @others.setter
    def others(self, others):
        """Sets the others of this SignatureObject.


        :param others: The others of this SignatureObject.  
        :type: OtherSignatures
        """

        self._others = others

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
        if not isinstance(other, SignatureObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
