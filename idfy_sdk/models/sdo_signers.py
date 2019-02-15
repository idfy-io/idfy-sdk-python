# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.certificate import Certificate  


class SDOSigners(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'certificate': 'Certificate',
        'name': 'str',
        'date_of_birth': 'datetime',
        'pid': 'str',
        'ssn': 'str',
        'signed_timestamp': 'datetime',
        'valid': 'bool',
        'ocsp': 'str',
        'environment': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'name': 'name',
        'date_of_birth': 'dateOfBirth',
        'pid': 'pid',
        'ssn': 'ssn',
        'signed_timestamp': 'signedTimestamp',
        'valid': 'valid',
        'ocsp': 'ocsp',
        'environment': 'environment'
    }

    def __init__(self, certificate=None, name=None, date_of_birth=None, pid=None, ssn=None, signed_timestamp=None, valid=None, ocsp=None, environment=None):  
        """SDOSigners"""  

        self._certificate = None
        self._name = None
        self._date_of_birth = None
        self._pid = None
        self._ssn = None
        self._signed_timestamp = None
        self._valid = None
        self._ocsp = None
        self._environment = None
        self.discriminator = None

        if certificate is not None:
            self.certificate = certificate
        if name is not None:
            self.name = name
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if pid is not None:
            self.pid = pid
        if ssn is not None:
            self.ssn = ssn
        if signed_timestamp is not None:
            self.signed_timestamp = signed_timestamp
        if valid is not None:
            self.valid = valid
        if ocsp is not None:
            self.ocsp = ocsp
        if environment is not None:
            self.environment = environment

    @property
    def certificate(self):
        """Gets the certificate of this SDOSigners.  


        :return: The certificate of this SDOSigners.  
        :rtype: Certificate
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this SDOSigners.


        :param certificate: The certificate of this SDOSigners.  
        :type: Certificate
        """

        self._certificate = certificate

    @property
    def name(self):
        """Gets the name of this SDOSigners.  


        :return: The name of this SDOSigners.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SDOSigners.


        :param name: The name of this SDOSigners.  
        :type: str
        """

        self._name = name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this SDOSigners.  


        :return: The date_of_birth of this SDOSigners.  
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this SDOSigners.


        :param date_of_birth: The date_of_birth of this SDOSigners.  
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def pid(self):
        """Gets the pid of this SDOSigners.  


        :return: The pid of this SDOSigners.  
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this SDOSigners.


        :param pid: The pid of this SDOSigners.  
        :type: str
        """

        self._pid = pid

    @property
    def ssn(self):
        """Gets the ssn of this SDOSigners.  


        :return: The ssn of this SDOSigners.  
        :rtype: str
        """
        return self._ssn

    @ssn.setter
    def ssn(self, ssn):
        """Sets the ssn of this SDOSigners.


        :param ssn: The ssn of this SDOSigners.  
        :type: str
        """

        self._ssn = ssn

    @property
    def signed_timestamp(self):
        """Gets the signed_timestamp of this SDOSigners.  


        :return: The signed_timestamp of this SDOSigners.  
        :rtype: datetime
        """
        return self._signed_timestamp

    @signed_timestamp.setter
    def signed_timestamp(self, signed_timestamp):
        """Sets the signed_timestamp of this SDOSigners.


        :param signed_timestamp: The signed_timestamp of this SDOSigners.  
        :type: datetime
        """

        self._signed_timestamp = signed_timestamp

    @property
    def valid(self):
        """Gets the valid of this SDOSigners.  


        :return: The valid of this SDOSigners.  
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this SDOSigners.


        :param valid: The valid of this SDOSigners.  
        :type: bool
        """

        self._valid = valid

    @property
    def ocsp(self):
        """Gets the ocsp of this SDOSigners.  


        :return: The ocsp of this SDOSigners.  
        :rtype: str
        """
        return self._ocsp

    @ocsp.setter
    def ocsp(self, ocsp):
        """Sets the ocsp of this SDOSigners.


        :param ocsp: The ocsp of this SDOSigners.  
        :type: str
        """

        self._ocsp = ocsp

    @property
    def environment(self):
        """Gets the environment of this SDOSigners.  


        :return: The environment of this SDOSigners.  
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this SDOSigners.


        :param environment: The environment of this SDOSigners.  
        :type: str
        """

        self._environment = environment

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
        if not isinstance(other, SDOSigners):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
