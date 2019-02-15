# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class ExtraInfoSignerRequestSpecialProperties(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bisnode_username': 'str',
        'bisnode_password': 'str',
        'include_pdf_reports': 'str',
        'official_username': 'str',
        'official_password': 'str',
        'official_reason': 'str',
        'official_system': 'str',
        'aml_nationality': 'str',
        'aml_language': 'str',
        'aml_mode': 'str'
    }

    attribute_map = {
        'bisnode_username': 'bisnodeUsername',
        'bisnode_password': 'bisnodePassword',
        'include_pdf_reports': 'includePdfReports',
        'official_username': 'officialUsername',
        'official_password': 'officialPassword',
        'official_reason': 'officialReason',
        'official_system': 'officialSystem',
        'aml_nationality': 'amlNationality',
        'aml_language': 'amlLanguage',
        'aml_mode': 'amlMode'
    }

    def __init__(self, bisnode_username=None, bisnode_password=None, include_pdf_reports=None, official_username=None, official_password=None, official_reason=None, official_system=None, aml_nationality=None, aml_language=None, aml_mode=None):  
        """ExtraInfoSignerRequestSpecialProperties"""  

        self._bisnode_username = None
        self._bisnode_password = None
        self._include_pdf_reports = None
        self._official_username = None
        self._official_password = None
        self._official_reason = None
        self._official_system = None
        self._aml_nationality = None
        self._aml_language = None
        self._aml_mode = None
        self.discriminator = None

        if bisnode_username is not None:
            self.bisnode_username = bisnode_username
        if bisnode_password is not None:
            self.bisnode_password = bisnode_password
        if include_pdf_reports is not None:
            self.include_pdf_reports = include_pdf_reports
        if official_username is not None:
            self.official_username = official_username
        if official_password is not None:
            self.official_password = official_password
        if official_reason is not None:
            self.official_reason = official_reason
        if official_system is not None:
            self.official_system = official_system
        if aml_nationality is not None:
            self.aml_nationality = aml_nationality
        if aml_language is not None:
            self.aml_language = aml_language
        if aml_mode is not None:
            self.aml_mode = aml_mode

    @property
    def bisnode_username(self):
        """Gets the bisnode_username of this ExtraInfoSignerRequestSpecialProperties.  


        :return: The bisnode_username of this ExtraInfoSignerRequestSpecialProperties.  
        :rtype: str
        """
        return self._bisnode_username

    @bisnode_username.setter
    def bisnode_username(self, bisnode_username):
        """Sets the bisnode_username of this ExtraInfoSignerRequestSpecialProperties.


        :param bisnode_username: The bisnode_username of this ExtraInfoSignerRequestSpecialProperties.  
        :type: str
        """

        self._bisnode_username = bisnode_username

    @property
    def bisnode_password(self):
        """Gets the bisnode_password of this ExtraInfoSignerRequestSpecialProperties.  


        :return: The bisnode_password of this ExtraInfoSignerRequestSpecialProperties.  
        :rtype: str
        """
        return self._bisnode_password

    @bisnode_password.setter
    def bisnode_password(self, bisnode_password):
        """Sets the bisnode_password of this ExtraInfoSignerRequestSpecialProperties.


        :param bisnode_password: The bisnode_password of this ExtraInfoSignerRequestSpecialProperties.  
        :type: str
        """

        self._bisnode_password = bisnode_password

    @property
    def include_pdf_reports(self):
        """Gets the include_pdf_reports of this ExtraInfoSignerRequestSpecialProperties.  


        :return: The include_pdf_reports of this ExtraInfoSignerRequestSpecialProperties.  
        :rtype: str
        """
        return self._include_pdf_reports

    @include_pdf_reports.setter
    def include_pdf_reports(self, include_pdf_reports):
        """Sets the include_pdf_reports of this ExtraInfoSignerRequestSpecialProperties.


        :param include_pdf_reports: The include_pdf_reports of this ExtraInfoSignerRequestSpecialProperties.  
        :type: str
        """

        self._include_pdf_reports = include_pdf_reports

    @property
    def official_username(self):
        """Gets the official_username of this ExtraInfoSignerRequestSpecialProperties.  


        :return: The official_username of this ExtraInfoSignerRequestSpecialProperties.  
        :rtype: str
        """
        return self._official_username

    @official_username.setter
    def official_username(self, official_username):
        """Sets the official_username of this ExtraInfoSignerRequestSpecialProperties.


        :param official_username: The official_username of this ExtraInfoSignerRequestSpecialProperties.  
        :type: str
        """

        self._official_username = official_username

    @property
    def official_password(self):
        """Gets the official_password of this ExtraInfoSignerRequestSpecialProperties.  


        :return: The official_password of this ExtraInfoSignerRequestSpecialProperties.  
        :rtype: str
        """
        return self._official_password

    @official_password.setter
    def official_password(self, official_password):
        """Sets the official_password of this ExtraInfoSignerRequestSpecialProperties.


        :param official_password: The official_password of this ExtraInfoSignerRequestSpecialProperties.  
        :type: str
        """

        self._official_password = official_password

    @property
    def official_reason(self):
        """Gets the official_reason of this ExtraInfoSignerRequestSpecialProperties.  


        :return: The official_reason of this ExtraInfoSignerRequestSpecialProperties.  
        :rtype: str
        """
        return self._official_reason

    @official_reason.setter
    def official_reason(self, official_reason):
        """Sets the official_reason of this ExtraInfoSignerRequestSpecialProperties.


        :param official_reason: The official_reason of this ExtraInfoSignerRequestSpecialProperties.  
        :type: str
        """

        self._official_reason = official_reason

    @property
    def official_system(self):
        """Gets the official_system of this ExtraInfoSignerRequestSpecialProperties.  


        :return: The official_system of this ExtraInfoSignerRequestSpecialProperties.  
        :rtype: str
        """
        return self._official_system

    @official_system.setter
    def official_system(self, official_system):
        """Sets the official_system of this ExtraInfoSignerRequestSpecialProperties.


        :param official_system: The official_system of this ExtraInfoSignerRequestSpecialProperties.  
        :type: str
        """

        self._official_system = official_system

    @property
    def aml_nationality(self):
        """Gets the aml_nationality of this ExtraInfoSignerRequestSpecialProperties.  


        :return: The aml_nationality of this ExtraInfoSignerRequestSpecialProperties.  
        :rtype: str
        """
        return self._aml_nationality

    @aml_nationality.setter
    def aml_nationality(self, aml_nationality):
        """Sets the aml_nationality of this ExtraInfoSignerRequestSpecialProperties.


        :param aml_nationality: The aml_nationality of this ExtraInfoSignerRequestSpecialProperties.  
        :type: str
        """

        self._aml_nationality = aml_nationality

    @property
    def aml_language(self):
        """Gets the aml_language of this ExtraInfoSignerRequestSpecialProperties.  


        :return: The aml_language of this ExtraInfoSignerRequestSpecialProperties.  
        :rtype: str
        """
        return self._aml_language

    @aml_language.setter
    def aml_language(self, aml_language):
        """Sets the aml_language of this ExtraInfoSignerRequestSpecialProperties.


        :param aml_language: The aml_language of this ExtraInfoSignerRequestSpecialProperties.  
        :type: str
        """

        self._aml_language = aml_language

    @property
    def aml_mode(self):
        """Gets the aml_mode of this ExtraInfoSignerRequestSpecialProperties.  


        :return: The aml_mode of this ExtraInfoSignerRequestSpecialProperties.  
        :rtype: str
        """
        return self._aml_mode

    @aml_mode.setter
    def aml_mode(self, aml_mode):
        """Sets the aml_mode of this ExtraInfoSignerRequestSpecialProperties.


        :param aml_mode: The aml_mode of this ExtraInfoSignerRequestSpecialProperties.  
        :type: str
        """

        self._aml_mode = aml_mode

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
        if not isinstance(other, ExtraInfoSignerRequestSpecialProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
