# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class ManagingLou(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'lei': 'str',
        'prefix': 'str',
        'name': 'str',
        'website': 'str',
        'operational': 'str',
        'endorsement_date': 'datetime',
        'sponsor': 'str',
        'sponsor_country': 'str'
    }

    attribute_map = {
        'lei': 'Lei',
        'prefix': 'Prefix',
        'name': 'Name',
        'website': 'Website',
        'operational': 'Operational',
        'endorsement_date': 'EndorsementDate',
        'sponsor': 'Sponsor',
        'sponsor_country': 'SponsorCountry'
    }

    def __init__(self, lei=None, prefix=None, name=None, website=None, operational=None, endorsement_date=None, sponsor=None, sponsor_country=None):  
        """ManagingLou"""  

        self._lei = None
        self._prefix = None
        self._name = None
        self._website = None
        self._operational = None
        self._endorsement_date = None
        self._sponsor = None
        self._sponsor_country = None
        self.discriminator = None

        if lei is not None:
            self.lei = lei
        if prefix is not None:
            self.prefix = prefix
        if name is not None:
            self.name = name
        if website is not None:
            self.website = website
        if operational is not None:
            self.operational = operational
        if endorsement_date is not None:
            self.endorsement_date = endorsement_date
        if sponsor is not None:
            self.sponsor = sponsor
        if sponsor_country is not None:
            self.sponsor_country = sponsor_country

    @property
    def lei(self):
        """Gets the lei of this ManagingLou.  


        :return: The lei of this ManagingLou.  
        :rtype: str
        """
        return self._lei

    @lei.setter
    def lei(self, lei):
        """Sets the lei of this ManagingLou.


        :param lei: The lei of this ManagingLou.  
        :type: str
        """

        self._lei = lei

    @property
    def prefix(self):
        """Gets the prefix of this ManagingLou.  


        :return: The prefix of this ManagingLou.  
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this ManagingLou.


        :param prefix: The prefix of this ManagingLou.  
        :type: str
        """

        self._prefix = prefix

    @property
    def name(self):
        """Gets the name of this ManagingLou.  


        :return: The name of this ManagingLou.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ManagingLou.


        :param name: The name of this ManagingLou.  
        :type: str
        """

        self._name = name

    @property
    def website(self):
        """Gets the website of this ManagingLou.  


        :return: The website of this ManagingLou.  
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this ManagingLou.


        :param website: The website of this ManagingLou.  
        :type: str
        """

        self._website = website

    @property
    def operational(self):
        """Gets the operational of this ManagingLou.  


        :return: The operational of this ManagingLou.  
        :rtype: str
        """
        return self._operational

    @operational.setter
    def operational(self, operational):
        """Sets the operational of this ManagingLou.


        :param operational: The operational of this ManagingLou.  
        :type: str
        """

        self._operational = operational

    @property
    def endorsement_date(self):
        """Gets the endorsement_date of this ManagingLou.  


        :return: The endorsement_date of this ManagingLou.  
        :rtype: datetime
        """
        return self._endorsement_date

    @endorsement_date.setter
    def endorsement_date(self, endorsement_date):
        """Sets the endorsement_date of this ManagingLou.


        :param endorsement_date: The endorsement_date of this ManagingLou.  
        :type: datetime
        """

        self._endorsement_date = endorsement_date

    @property
    def sponsor(self):
        """Gets the sponsor of this ManagingLou.  


        :return: The sponsor of this ManagingLou.  
        :rtype: str
        """
        return self._sponsor

    @sponsor.setter
    def sponsor(self, sponsor):
        """Sets the sponsor of this ManagingLou.


        :param sponsor: The sponsor of this ManagingLou.  
        :type: str
        """

        self._sponsor = sponsor

    @property
    def sponsor_country(self):
        """Gets the sponsor_country of this ManagingLou.  


        :return: The sponsor_country of this ManagingLou.  
        :rtype: str
        """
        return self._sponsor_country

    @sponsor_country.setter
    def sponsor_country(self, sponsor_country):
        """Sets the sponsor_country of this ManagingLou.


        :param sponsor_country: The sponsor_country of this ManagingLou.  
        :type: str
        """

        self._sponsor_country = sponsor_country

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
        if not isinstance(other, ManagingLou):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
