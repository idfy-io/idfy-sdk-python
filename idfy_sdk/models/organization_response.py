# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class OrganizationResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mva_number': 'int',
        'prokura': 'str',
        'signature': 'str',
        'report': 'str'
    }

    attribute_map = {
        'mva_number': 'MvaNumber',
        'prokura': 'Prokura',
        'signature': 'Signature',
        'report': 'Report'
    }

    def __init__(self, mva_number=None, prokura=None, signature=None, report=None):  
        """OrganizationResponse"""  

        self._mva_number = None
        self._prokura = None
        self._signature = None
        self._report = None
        self.discriminator = None

        if mva_number is not None:
            self.mva_number = mva_number
        if prokura is not None:
            self.prokura = prokura
        if signature is not None:
            self.signature = signature
        if report is not None:
            self.report = report

    @property
    def mva_number(self):
        """Gets the mva_number of this OrganizationResponse.  


        :return: The mva_number of this OrganizationResponse.  
        :rtype: int
        """
        return self._mva_number

    @mva_number.setter
    def mva_number(self, mva_number):
        """Sets the mva_number of this OrganizationResponse.


        :param mva_number: The mva_number of this OrganizationResponse.  
        :type: int
        """

        self._mva_number = mva_number

    @property
    def prokura(self):
        """Gets the prokura of this OrganizationResponse.  


        :return: The prokura of this OrganizationResponse.  
        :rtype: str
        """
        return self._prokura

    @prokura.setter
    def prokura(self, prokura):
        """Sets the prokura of this OrganizationResponse.


        :param prokura: The prokura of this OrganizationResponse.  
        :type: str
        """

        self._prokura = prokura

    @property
    def signature(self):
        """Gets the signature of this OrganizationResponse.  


        :return: The signature of this OrganizationResponse.  
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this OrganizationResponse.


        :param signature: The signature of this OrganizationResponse.  
        :type: str
        """

        self._signature = signature

    @property
    def report(self):
        """Gets the report of this OrganizationResponse.  


        :return: The report of this OrganizationResponse.  
        :rtype: str
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this OrganizationResponse.


        :param report: The report of this OrganizationResponse.  
        :type: str
        """

        self._report = report

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
        if not isinstance(other, OrganizationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
