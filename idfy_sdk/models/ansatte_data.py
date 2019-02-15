# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class AnsatteData(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ansatte_ar_field': 'int',
        'ansatte_antall_field': 'int'
    }

    attribute_map = {
        'ansatte_ar_field': 'ansatteArField',
        'ansatte_antall_field': 'ansatteAntallField'
    }

    def __init__(self, ansatte_ar_field=None, ansatte_antall_field=None):  
        """AnsatteData"""  

        self._ansatte_ar_field = None
        self._ansatte_antall_field = None
        self.discriminator = None

        if ansatte_ar_field is not None:
            self.ansatte_ar_field = ansatte_ar_field
        if ansatte_antall_field is not None:
            self.ansatte_antall_field = ansatte_antall_field

    @property
    def ansatte_ar_field(self):
        """Gets the ansatte_ar_field of this AnsatteData.  


        :return: The ansatte_ar_field of this AnsatteData.  
        :rtype: int
        """
        return self._ansatte_ar_field

    @ansatte_ar_field.setter
    def ansatte_ar_field(self, ansatte_ar_field):
        """Sets the ansatte_ar_field of this AnsatteData.


        :param ansatte_ar_field: The ansatte_ar_field of this AnsatteData.  
        :type: int
        """

        self._ansatte_ar_field = ansatte_ar_field

    @property
    def ansatte_antall_field(self):
        """Gets the ansatte_antall_field of this AnsatteData.  


        :return: The ansatte_antall_field of this AnsatteData.  
        :rtype: int
        """
        return self._ansatte_antall_field

    @ansatte_antall_field.setter
    def ansatte_antall_field(self, ansatte_antall_field):
        """Sets the ansatte_antall_field of this AnsatteData.


        :param ansatte_antall_field: The ansatte_antall_field of this AnsatteData.  
        :type: int
        """

        self._ansatte_antall_field = ansatte_antall_field

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
        if not isinstance(other, AnsatteData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
