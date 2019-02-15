# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.managing_lou import ManagingLou  


class LeiRegistration(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'initial_registration_date': 'datetime',
        'registration_status': 'str',
        'validation_sources': 'str',
        'last_update_date': 'datetime',
        'next_renewal_date': 'datetime',
        'managing_lou': 'ManagingLou'
    }

    attribute_map = {
        'initial_registration_date': 'InitialRegistrationDate',
        'registration_status': 'RegistrationStatus',
        'validation_sources': 'ValidationSources',
        'last_update_date': 'LastUpdateDate',
        'next_renewal_date': 'NextRenewalDate',
        'managing_lou': 'ManagingLou'
    }

    def __init__(self, initial_registration_date=None, registration_status=None, validation_sources=None, last_update_date=None, next_renewal_date=None, managing_lou=None):  
        """LeiRegistration"""  

        self._initial_registration_date = None
        self._registration_status = None
        self._validation_sources = None
        self._last_update_date = None
        self._next_renewal_date = None
        self._managing_lou = None
        self.discriminator = None

        if initial_registration_date is not None:
            self.initial_registration_date = initial_registration_date
        if registration_status is not None:
            self.registration_status = registration_status
        if validation_sources is not None:
            self.validation_sources = validation_sources
        if last_update_date is not None:
            self.last_update_date = last_update_date
        if next_renewal_date is not None:
            self.next_renewal_date = next_renewal_date
        if managing_lou is not None:
            self.managing_lou = managing_lou

    @property
    def initial_registration_date(self):
        """Gets the initial_registration_date of this LeiRegistration.  


        :return: The initial_registration_date of this LeiRegistration.  
        :rtype: datetime
        """
        return self._initial_registration_date

    @initial_registration_date.setter
    def initial_registration_date(self, initial_registration_date):
        """Sets the initial_registration_date of this LeiRegistration.


        :param initial_registration_date: The initial_registration_date of this LeiRegistration.  
        :type: datetime
        """

        self._initial_registration_date = initial_registration_date

    @property
    def registration_status(self):
        """Gets the registration_status of this LeiRegistration.  


        :return: The registration_status of this LeiRegistration.  
        :rtype: str
        """
        return self._registration_status

    @registration_status.setter
    def registration_status(self, registration_status):
        """Sets the registration_status of this LeiRegistration.


        :param registration_status: The registration_status of this LeiRegistration.  
        :type: str
        """

        self._registration_status = registration_status

    @property
    def validation_sources(self):
        """Gets the validation_sources of this LeiRegistration.  


        :return: The validation_sources of this LeiRegistration.  
        :rtype: str
        """
        return self._validation_sources

    @validation_sources.setter
    def validation_sources(self, validation_sources):
        """Sets the validation_sources of this LeiRegistration.


        :param validation_sources: The validation_sources of this LeiRegistration.  
        :type: str
        """

        self._validation_sources = validation_sources

    @property
    def last_update_date(self):
        """Gets the last_update_date of this LeiRegistration.  


        :return: The last_update_date of this LeiRegistration.  
        :rtype: datetime
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this LeiRegistration.


        :param last_update_date: The last_update_date of this LeiRegistration.  
        :type: datetime
        """

        self._last_update_date = last_update_date

    @property
    def next_renewal_date(self):
        """Gets the next_renewal_date of this LeiRegistration.  


        :return: The next_renewal_date of this LeiRegistration.  
        :rtype: datetime
        """
        return self._next_renewal_date

    @next_renewal_date.setter
    def next_renewal_date(self, next_renewal_date):
        """Sets the next_renewal_date of this LeiRegistration.


        :param next_renewal_date: The next_renewal_date of this LeiRegistration.  
        :type: datetime
        """

        self._next_renewal_date = next_renewal_date

    @property
    def managing_lou(self):
        """Gets the managing_lou of this LeiRegistration.  


        :return: The managing_lou of this LeiRegistration.  
        :rtype: ManagingLou
        """
        return self._managing_lou

    @managing_lou.setter
    def managing_lou(self, managing_lou):
        """Sets the managing_lou of this LeiRegistration.


        :param managing_lou: The managing_lou of this LeiRegistration.  
        :type: ManagingLou
        """

        self._managing_lou = managing_lou

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
        if not isinstance(other, LeiRegistration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
