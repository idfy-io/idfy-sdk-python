# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.signature import Signature  


class OtherSignatures(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'required_number_of_others': 'int',
        'list': 'list[Signature]'
    }

    attribute_map = {
        'required_number_of_others': 'RequiredNumberOfOthers',
        'list': 'List'
    }

    def __init__(self, required_number_of_others=None, list=None):  
        """OtherSignatures"""  

        self._required_number_of_others = None
        self._list = None
        self.discriminator = None

        if required_number_of_others is not None:
            self.required_number_of_others = required_number_of_others
        if list is not None:
            self.list = list

    @property
    def required_number_of_others(self):
        """Gets the required_number_of_others of this OtherSignatures.  


        :return: The required_number_of_others of this OtherSignatures.  
        :rtype: int
        """
        return self._required_number_of_others

    @required_number_of_others.setter
    def required_number_of_others(self, required_number_of_others):
        """Sets the required_number_of_others of this OtherSignatures.


        :param required_number_of_others: The required_number_of_others of this OtherSignatures.  
        :type: int
        """

        self._required_number_of_others = required_number_of_others

    @property
    def list(self):
        """Gets the list of this OtherSignatures.  


        :return: The list of this OtherSignatures.  
        :rtype: list[Signature]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this OtherSignatures.


        :param list: The list of this OtherSignatures.  
        :type: list[Signature]
        """

        self._list = list

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
        if not isinstance(other, OtherSignatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
