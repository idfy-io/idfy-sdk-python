# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.pep_result import PepResult  
from idfy_sdk.models.person_sanction_result import PersonSanctionResult  
from idfy_sdk.models.verified_person import VerifiedPerson  


class PersonAmlResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bisnode_reference': 'str',
        'sanction_results': 'list[PersonSanctionResult]',
        'pep_results': 'list[PepResult]',
        'verified_person': 'VerifiedPerson',
        'message': 'str',
        'report': 'str'
    }

    attribute_map = {
        'bisnode_reference': 'bisnodeReference',
        'sanction_results': 'sanctionResults',
        'pep_results': 'pepResults',
        'verified_person': 'verifiedPerson',
        'message': 'message',
        'report': 'Report'
    }

    def __init__(self, bisnode_reference=None, sanction_results=None, pep_results=None, verified_person=None, message=None, report=None):  
        """PersonAmlResponse"""  

        self._bisnode_reference = None
        self._sanction_results = None
        self._pep_results = None
        self._verified_person = None
        self._message = None
        self._report = None
        self.discriminator = None

        if bisnode_reference is not None:
            self.bisnode_reference = bisnode_reference
        if sanction_results is not None:
            self.sanction_results = sanction_results
        if pep_results is not None:
            self.pep_results = pep_results
        if verified_person is not None:
            self.verified_person = verified_person
        if message is not None:
            self.message = message
        if report is not None:
            self.report = report

    @property
    def bisnode_reference(self):
        """Gets the bisnode_reference of this PersonAmlResponse.  

        Reference identifying the current request. May be used for tracing  

        :return: The bisnode_reference of this PersonAmlResponse.  
        :rtype: str
        """
        return self._bisnode_reference

    @bisnode_reference.setter
    def bisnode_reference(self, bisnode_reference):
        """Sets the bisnode_reference of this PersonAmlResponse.

        Reference identifying the current request. May be used for tracing  

        :param bisnode_reference: The bisnode_reference of this PersonAmlResponse.  
        :type: str
        """

        self._bisnode_reference = bisnode_reference

    @property
    def sanction_results(self):
        """Gets the sanction_results of this PersonAmlResponse.  

        List of all Sanction items with match for the input request.  

        :return: The sanction_results of this PersonAmlResponse.  
        :rtype: list[PersonSanctionResult]
        """
        return self._sanction_results

    @sanction_results.setter
    def sanction_results(self, sanction_results):
        """Sets the sanction_results of this PersonAmlResponse.

        List of all Sanction items with match for the input request.  

        :param sanction_results: The sanction_results of this PersonAmlResponse.  
        :type: list[PersonSanctionResult]
        """

        self._sanction_results = sanction_results

    @property
    def pep_results(self):
        """Gets the pep_results of this PersonAmlResponse.  

        List of all PEP items with match for the input request.  

        :return: The pep_results of this PersonAmlResponse.  
        :rtype: list[PepResult]
        """
        return self._pep_results

    @pep_results.setter
    def pep_results(self, pep_results):
        """Sets the pep_results of this PersonAmlResponse.

        List of all PEP items with match for the input request.  

        :param pep_results: The pep_results of this PersonAmlResponse.  
        :type: list[PepResult]
        """

        self._pep_results = pep_results

    @property
    def verified_person(self):
        """Gets the verified_person of this PersonAmlResponse.  

        Data retrieved before the actual screening (data enhancement).  

        :return: The verified_person of this PersonAmlResponse.  
        :rtype: VerifiedPerson
        """
        return self._verified_person

    @verified_person.setter
    def verified_person(self, verified_person):
        """Sets the verified_person of this PersonAmlResponse.

        Data retrieved before the actual screening (data enhancement).  

        :param verified_person: The verified_person of this PersonAmlResponse.  
        :type: VerifiedPerson
        """

        self._verified_person = verified_person

    @property
    def message(self):
        """Gets the message of this PersonAmlResponse.  

        Response message could for example be: No result from PEP and/or SANCTION screening.  

        :return: The message of this PersonAmlResponse.  
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PersonAmlResponse.

        Response message could for example be: No result from PEP and/or SANCTION screening.  

        :param message: The message of this PersonAmlResponse.  
        :type: str
        """

        self._message = message

    @property
    def report(self):
        """Gets the report of this PersonAmlResponse.  

        Reference to downloadable PDF report (if includeReport is set to true in request)  

        :return: The report of this PersonAmlResponse.  
        :rtype: str
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this PersonAmlResponse.

        Reference to downloadable PDF report (if includeReport is set to true in request)  

        :param report: The report of this PersonAmlResponse.  
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
        if not isinstance(other, PersonAmlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
