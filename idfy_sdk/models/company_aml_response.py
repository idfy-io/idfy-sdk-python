# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six




class CompanyAmlResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bisnode_reference': 'str',
        'verified_company': 'VerifiedCompany',
        'sanction_results': 'list[CompanySanctionResult]',
        'message': 'str',
        'owners_and_board_members': 'OwnersAndBoardMembers',
        'report': 'str'
    }

    attribute_map = {
        'bisnode_reference': 'bisnodeReference',
        'verified_company': 'verifiedCompany',
        'sanction_results': 'sanctionResults',
        'message': 'message',
        'owners_and_board_members': 'ownersAndBoardMembers',
        'report': 'Report'
    }

    def __init__(self, bisnode_reference=None, verified_company=None, sanction_results=None, message=None, owners_and_board_members=None, report=None):  
        """CompanyAmlResponse"""  

        self._bisnode_reference = None
        self._verified_company = None
        self._sanction_results = None
        self._message = None
        self._owners_and_board_members = None
        self._report = None
        self.discriminator = None

        if bisnode_reference is not None:
            self.bisnode_reference = bisnode_reference
        if verified_company is not None:
            self.verified_company = verified_company
        if sanction_results is not None:
            self.sanction_results = sanction_results
        if message is not None:
            self.message = message
        if owners_and_board_members is not None:
            self.owners_and_board_members = owners_and_board_members
        if report is not None:
            self.report = report

    @property
    def bisnode_reference(self):
        """Gets the bisnode_reference of this CompanyAmlResponse.  

        Reference identifying the current request. May be used for tracing  

        :return: The bisnode_reference of this CompanyAmlResponse.  
        :rtype: str
        """
        return self._bisnode_reference

    @bisnode_reference.setter
    def bisnode_reference(self, bisnode_reference):
        """Sets the bisnode_reference of this CompanyAmlResponse.

        Reference identifying the current request. May be used for tracing  

        :param bisnode_reference: The bisnode_reference of this CompanyAmlResponse.  
        :type: str
        """

        self._bisnode_reference = bisnode_reference

    @property
    def verified_company(self):
        """Gets the verified_company of this CompanyAmlResponse.  

        Data retrieved before the actual screening (data enhancement).  

        :return: The verified_company of this CompanyAmlResponse.  
        :rtype: VerifiedCompany
        """
        return self._verified_company

    @verified_company.setter
    def verified_company(self, verified_company):
        """Sets the verified_company of this CompanyAmlResponse.

        Data retrieved before the actual screening (data enhancement).  

        :param verified_company: The verified_company of this CompanyAmlResponse.  
        :type: VerifiedCompany
        """

        self._verified_company = verified_company

    @property
    def sanction_results(self):
        """Gets the sanction_results of this CompanyAmlResponse.  

        List of all Sanction items with match for the input request.  

        :return: The sanction_results of this CompanyAmlResponse.  
        :rtype: list[CompanySanctionResult]
        """
        return self._sanction_results

    @sanction_results.setter
    def sanction_results(self, sanction_results):
        """Sets the sanction_results of this CompanyAmlResponse.

        List of all Sanction items with match for the input request.  

        :param sanction_results: The sanction_results of this CompanyAmlResponse.  
        :type: list[CompanySanctionResult]
        """

        self._sanction_results = sanction_results

    @property
    def message(self):
        """Gets the message of this CompanyAmlResponse.  

        Response message could for example be: No result from PEP and/or SANCTION screening.  

        :return: The message of this CompanyAmlResponse.  
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CompanyAmlResponse.

        Response message could for example be: No result from PEP and/or SANCTION screening.  

        :param message: The message of this CompanyAmlResponse.  
        :type: str
        """

        self._message = message

    @property
    def owners_and_board_members(self):
        """Gets the owners_and_board_members of this CompanyAmlResponse.  

        Results for owners and board members  

        :return: The owners_and_board_members of this CompanyAmlResponse.  
        :rtype: OwnersAndBoardMembers
        """
        return self._owners_and_board_members

    @owners_and_board_members.setter
    def owners_and_board_members(self, owners_and_board_members):
        """Sets the owners_and_board_members of this CompanyAmlResponse.

        Results for owners and board members  

        :param owners_and_board_members: The owners_and_board_members of this CompanyAmlResponse.  
        :type: OwnersAndBoardMembers
        """

        self._owners_and_board_members = owners_and_board_members

    @property
    def report(self):
        """Gets the report of this CompanyAmlResponse.  

        Reference to downloadable PDF report (if includeReport is set to true in request)  

        :return: The report of this CompanyAmlResponse.  
        :rtype: str
        """
        return self._report

    @report.setter
    def report(self, report):
        """Sets the report of this CompanyAmlResponse.

        Reference to downloadable PDF report (if includeReport is set to true in request)  

        :param report: The report of this CompanyAmlResponse.  
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
        if not isinstance(other, CompanyAmlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

from idfy_sdk.models.company_sanction_result import CompanySanctionResult  
from idfy_sdk.models.owners_and_board_members import OwnersAndBoardMembers  
from idfy_sdk.models.verified_company import VerifiedCompany  