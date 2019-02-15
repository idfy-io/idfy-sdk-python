# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.certificate import Certificate  


class Seal(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sealed_by': 'str',
        'sealed_timestamp': 'datetime',
        'certificate': 'Certificate',
        'seal_valid': 'bool'
    }

    attribute_map = {
        'sealed_by': 'sealedBy',
        'sealed_timestamp': 'sealedTimestamp',
        'certificate': 'certificate',
        'seal_valid': 'sealValid'
    }

    def __init__(self, sealed_by=None, sealed_timestamp=None, certificate=None, seal_valid=None):  
        """Seal"""  

        self._sealed_by = None
        self._sealed_timestamp = None
        self._certificate = None
        self._seal_valid = None
        self.discriminator = None

        if sealed_by is not None:
            self.sealed_by = sealed_by
        if sealed_timestamp is not None:
            self.sealed_timestamp = sealed_timestamp
        if certificate is not None:
            self.certificate = certificate
        if seal_valid is not None:
            self.seal_valid = seal_valid

    @property
    def sealed_by(self):
        """Gets the sealed_by of this Seal.  


        :return: The sealed_by of this Seal.  
        :rtype: str
        """
        return self._sealed_by

    @sealed_by.setter
    def sealed_by(self, sealed_by):
        """Sets the sealed_by of this Seal.


        :param sealed_by: The sealed_by of this Seal.  
        :type: str
        """

        self._sealed_by = sealed_by

    @property
    def sealed_timestamp(self):
        """Gets the sealed_timestamp of this Seal.  


        :return: The sealed_timestamp of this Seal.  
        :rtype: datetime
        """
        return self._sealed_timestamp

    @sealed_timestamp.setter
    def sealed_timestamp(self, sealed_timestamp):
        """Sets the sealed_timestamp of this Seal.


        :param sealed_timestamp: The sealed_timestamp of this Seal.  
        :type: datetime
        """

        self._sealed_timestamp = sealed_timestamp

    @property
    def certificate(self):
        """Gets the certificate of this Seal.  


        :return: The certificate of this Seal.  
        :rtype: Certificate
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this Seal.


        :param certificate: The certificate of this Seal.  
        :type: Certificate
        """

        self._certificate = certificate

    @property
    def seal_valid(self):
        """Gets the seal_valid of this Seal.  


        :return: The seal_valid of this Seal.  
        :rtype: bool
        """
        return self._seal_valid

    @seal_valid.setter
    def seal_valid(self, seal_valid):
        """Sets the seal_valid of this Seal.


        :param seal_valid: The seal_valid of this Seal.  
        :type: bool
        """

        self._seal_valid = seal_valid

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
        if not isinstance(other, Seal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
