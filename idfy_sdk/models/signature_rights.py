# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.signature_object import SignatureObject  


class SignatureRights(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mva_number': 'int',
        'name': 'str',
        'signatur': 'SignatureObject',
        'prokura': 'SignatureObject',
        'report': 'str',
        'request_id': 'str',
        'report_id': 'str'
    }

    attribute_map = {
        'mva_number': 'MvaNumber',
        'name': 'Name',
        'signatur': 'Signatur',
        'prokura': 'Prokura',
        'report': 'Report',
        'request_id': 'RequestId',
        'report_id': 'ReportId'
    }

    def __init__(self, mva_number=None, name=None, signatur=None, prokura=None, report=None, request_id=None, report_id=None):  
        """SignatureRights"""  

        self._mva_number = None
        self._name = None
        self._signatur = None
        self._prokura = None
        self._report = None
        self._request_id = None
        self._report_id = None
        self.discriminator = None

        if mva_number is not None:
            self.mva_number = mva_number
        if name is not None:
            self.name = name
        if signatur is not None:
            self.signatur = signatur
        if prokura is not None:
            self.prokura = prokura
        if report is not None:
            self.report = report
        if request_id is not None:
            self.request_id = request_id
        if report_id is not None:
            self.report_id = report_id

    @property
    def mva_number(self):
        """Gets the mva_number of this SignatureRights.  


        :return: The mva_number of this SignatureRights.  
        :rtype: int
        """
        return self._mva_number

    @mva_number.setter
    def mva_number(self, mva_number):
        """Sets the mva_number of this SignatureRights.


        :param mva_number: The mva_number of this SignatureRights.  
        :type: int
        """

        self._mva_number = mva_number

    @property
    def name(self):
        """Gets the name of this SignatureRights.  


        :return: The name of this SignatureRights.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SignatureRights.


        :param name: The name of this SignatureRights.  
        :type: str
        """

        self._name = name

    @property
    def signatur(self):
        """Gets the signatur of this SignatureRights.  


        :return: The signatur of this SignatureRights.  
        :rtype: SignatureObject
        """
        return self._signatur

    @signatur.setter
    def signatur(self, signatur):
        """Sets the signatur of this SignatureRights.


        :param signatur: The signatur of this SignatureRights.  
        :type: SignatureObject
        """

        self._signatur = signatur

    @property
    def prokura(self):
        """Gets the prokura of this SignatureRights.  


        :return: The prokura of this SignatureRights.  
        :rtype: SignatureObject
        """
        return self._prokura

    @prokura.setter
    def prokura(self, prokura):
        """Sets the prokura of this SignatureRights.


        :param prokura: The prokura of this SignatureRights.  
        :type: SignatureObject
        """

        self._prokura = prokura

    @property
    def report(self):
        """Gets the report of this SignatureRights.  


        :return: The report of this SignatureRights.  
        :rtype: str
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this SignatureRights.


        :param report: The report of this SignatureRights.  
        :type: str
        """

        self._report = report

    @property
    def request_id(self):
        """Gets the request_id of this SignatureRights.  


        :return: The request_id of this SignatureRights.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this SignatureRights.


        :param request_id: The request_id of this SignatureRights.  
        :type: str
        """

        self._request_id = request_id

    @property
    def report_id(self):
        """Gets the report_id of this SignatureRights.  


        :return: The report_id of this SignatureRights.  
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this SignatureRights.


        :param report_id: The report_id of this SignatureRights.  
        :type: str
        """

        self._report_id = report_id

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
        if not isinstance(other, SignatureRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
