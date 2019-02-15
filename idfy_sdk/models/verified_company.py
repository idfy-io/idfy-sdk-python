# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class VerifiedCompany(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'reg_no': 'str',
        'duns_no': 'str',
        'status': 'list[str]',
        'name': 'str',
        'nationality': 'str',
        'provider': 'str'
    }

    attribute_map = {
        'reg_no': 'regNo',
        'duns_no': 'dunsNo',
        'status': 'status',
        'name': 'name',
        'nationality': 'nationality',
        'provider': 'provider'
    }

    def __init__(self, reg_no=None, duns_no=None, status=None, name=None, nationality=None, provider=None):  
        """VerifiedCompany"""  

        self._reg_no = None
        self._duns_no = None
        self._status = None
        self._name = None
        self._nationality = None
        self._provider = None
        self.discriminator = None

        if reg_no is not None:
            self.reg_no = reg_no
        if duns_no is not None:
            self.duns_no = duns_no
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if nationality is not None:
            self.nationality = nationality
        if provider is not None:
            self.provider = provider

    @property
    def reg_no(self):
        """Gets the reg_no of this VerifiedCompany.  

        Business registration number  

        :return: The reg_no of this VerifiedCompany.  
        :rtype: str
        """
        return self._reg_no

    @reg_no.setter
    def reg_no(self, reg_no):
        """Sets the reg_no of this VerifiedCompany.

        Business registration number  

        :param reg_no: The reg_no of this VerifiedCompany.  
        :type: str
        """

        self._reg_no = reg_no

    @property
    def duns_no(self):
        """Gets the duns_no of this VerifiedCompany.  

        D-U-N-S number  

        :return: The duns_no of this VerifiedCompany.  
        :rtype: str
        """
        return self._duns_no

    @duns_no.setter
    def duns_no(self, duns_no):
        """Sets the duns_no of this VerifiedCompany.

        D-U-N-S number  

        :param duns_no: The duns_no of this VerifiedCompany.  
        :type: str
        """

        self._duns_no = duns_no

    @property
    def status(self):
        """Gets the status of this VerifiedCompany.  

        Status code  

        :return: The status of this VerifiedCompany.  
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VerifiedCompany.

        Status code  

        :param status: The status of this VerifiedCompany.  
        :type: list[str]
        """

        self._status = status

    @property
    def name(self):
        """Gets the name of this VerifiedCompany.  

        Name of company  

        :return: The name of this VerifiedCompany.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VerifiedCompany.

        Name of company  

        :param name: The name of this VerifiedCompany.  
        :type: str
        """

        self._name = name

    @property
    def nationality(self):
        """Gets the nationality of this VerifiedCompany.  

        Two-letter code as specified in the ISO 3166 standard  

        :return: The nationality of this VerifiedCompany.  
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this VerifiedCompany.

        Two-letter code as specified in the ISO 3166 standard  

        :param nationality: The nationality of this VerifiedCompany.  
        :type: str
        """

        self._nationality = nationality

    @property
    def provider(self):
        """Gets the provider of this VerifiedCompany.  

        Name of data provider  

        :return: The provider of this VerifiedCompany.  
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this VerifiedCompany.

        Name of data provider  

        :param provider: The provider of this VerifiedCompany.  
        :type: str
        """

        self._provider = provider

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
        if not isinstance(other, VerifiedCompany):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
