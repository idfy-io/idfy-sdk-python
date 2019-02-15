# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Signers(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'identificator': 'str',
        'identificator_type': 'str'
    }

    attribute_map = {
        'identificator': 'identificator',
        'identificator_type': 'identificatorType'
    }

    def __init__(self, identificator=None, identificator_type=None):  
        """Signers"""  

        self._identificator = None
        self._identificator_type = None
        self.discriminator = None

        if identificator is not None:
            self.identificator = identificator
        if identificator_type is not None:
            self.identificator_type = identificator_type

    @property
    def identificator(self):
        """Gets the identificator of this Signers.  


        :return: The identificator of this Signers.  
        :rtype: str
        """
        return self._identificator

    @identificator.setter
    def identificator(self, identificator):
        """Sets the identificator of this Signers.


        :param identificator: The identificator of this Signers.  
        :type: str
        """

        self._identificator = identificator

    @property
    def identificator_type(self):
        """Gets the identificator_type of this Signers.  


        :return: The identificator_type of this Signers.  
        :rtype: str
        """
        return self._identificator_type

    @identificator_type.setter
    def identificator_type(self, identificator_type):
        """Sets the identificator_type of this Signers.


        :param identificator_type: The identificator_type of this Signers.  
        :type: str
        """
        allowed_values = ["Unknown", "BankIDUniqueId", "SSN", "OrganizationNumber"]  
        if identificator_type not in allowed_values:
            raise ValueError(
                "Invalid value for `identificator_type` ({0}), must be one of {1}"  
                .format(identificator_type, allowed_values)
            )

        self._identificator_type = identificator_type

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
        if not isinstance(other, Signers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
