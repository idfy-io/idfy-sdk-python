# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.role import Role  


class VerifiedPerson(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'status': 'list[str]',
        'deceased_date': 'datetime',
        'emigrated_date': 'datetime',
        'roles': 'list[Role]',
        'provider': 'str',
        'name': 'str',
        'gender': 'str',
        'nat_id_no': 'str',
        'nationality': 'str',
        'birth_date': 'str'
    }

    attribute_map = {
        'status': 'status',
        'deceased_date': 'deceasedDate',
        'emigrated_date': 'emigratedDate',
        'roles': 'roles',
        'provider': 'provider',
        'name': 'name',
        'gender': 'gender',
        'nat_id_no': 'natIdNo',
        'nationality': 'nationality',
        'birth_date': 'birthDate'
    }

    def __init__(self, status=None, deceased_date=None, emigrated_date=None, roles=None, provider=None, name=None, gender=None, nat_id_no=None, nationality=None, birth_date=None):  
        """VerifiedPerson"""  

        self._status = None
        self._deceased_date = None
        self._emigrated_date = None
        self._roles = None
        self._provider = None
        self._name = None
        self._gender = None
        self._nat_id_no = None
        self._nationality = None
        self._birth_date = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if deceased_date is not None:
            self.deceased_date = deceased_date
        if emigrated_date is not None:
            self.emigrated_date = emigrated_date
        if roles is not None:
            self.roles = roles
        if provider is not None:
            self.provider = provider
        if name is not None:
            self.name = name
        if gender is not None:
            self.gender = gender
        if nat_id_no is not None:
            self.nat_id_no = nat_id_no
        if nationality is not None:
            self.nationality = nationality
        if birth_date is not None:
            self.birth_date = birth_date

    @property
    def status(self):
        """Gets the status of this VerifiedPerson.  

        Person status code, e.g. DECEASED, EMIGRATED  

        :return: The status of this VerifiedPerson.  
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VerifiedPerson.

        Person status code, e.g. DECEASED, EMIGRATED  

        :param status: The status of this VerifiedPerson.  
        :type: list[str]
        """
        allowed_values = ["UNKNOWN", "EMIGRATED", "BANKRUPT", "PROTECTED", "NO_ADDRESS", "DECEASED", "GUARDIANSHIP"]  
        if not set(status).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `status` [{0}], must be a subset of [{1}]"  
                .format(", ".join(map(str, set(status) - set(allowed_values))),  
                        ", ".join(map(str, allowed_values)))
            )

        self._status = status

    @property
    def deceased_date(self):
        """Gets the deceased_date of this VerifiedPerson.  

        Date of death  

        :return: The deceased_date of this VerifiedPerson.  
        :rtype: datetime
        """
        return self._deceased_date

    @deceased_date.setter
    def deceased_date(self, deceased_date):
        """Sets the deceased_date of this VerifiedPerson.

        Date of death  

        :param deceased_date: The deceased_date of this VerifiedPerson.  
        :type: datetime
        """

        self._deceased_date = deceased_date

    @property
    def emigrated_date(self):
        """Gets the emigrated_date of this VerifiedPerson.  

        Date of emigration  

        :return: The emigrated_date of this VerifiedPerson.  
        :rtype: datetime
        """
        return self._emigrated_date

    @emigrated_date.setter
    def emigrated_date(self, emigrated_date):
        """Sets the emigrated_date of this VerifiedPerson.

        Date of emigration  

        :param emigrated_date: The emigrated_date of this VerifiedPerson.  
        :type: datetime
        """

        self._emigrated_date = emigrated_date

    @property
    def roles(self):
        """Gets the roles of this VerifiedPerson.  

        Role in company  

        :return: The roles of this VerifiedPerson.  
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this VerifiedPerson.

        Role in company  

        :param roles: The roles of this VerifiedPerson.  
        :type: list[Role]
        """

        self._roles = roles

    @property
    def provider(self):
        """Gets the provider of this VerifiedPerson.  

        Name of data provider  

        :return: The provider of this VerifiedPerson.  
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this VerifiedPerson.

        Name of data provider  

        :param provider: The provider of this VerifiedPerson.  
        :type: str
        """

        self._provider = provider

    @property
    def name(self):
        """Gets the name of this VerifiedPerson.  

        Name of person  

        :return: The name of this VerifiedPerson.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VerifiedPerson.

        Name of person  

        :param name: The name of this VerifiedPerson.  
        :type: str
        """

        self._name = name

    @property
    def gender(self):
        """Gets the gender of this VerifiedPerson.  

        Gender of person  

        :return: The gender of this VerifiedPerson.  
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this VerifiedPerson.

        Gender of person  

        :param gender: The gender of this VerifiedPerson.  
        :type: str
        """
        allowed_values = ["MALE", "FEMALE", "UNKNOWN"]  
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def nat_id_no(self):
        """Gets the nat_id_no of this VerifiedPerson.  

        National Identification Number  

        :return: The nat_id_no of this VerifiedPerson.  
        :rtype: str
        """
        return self._nat_id_no

    @nat_id_no.setter
    def nat_id_no(self, nat_id_no):
        """Sets the nat_id_no of this VerifiedPerson.

        National Identification Number  

        :param nat_id_no: The nat_id_no of this VerifiedPerson.  
        :type: str
        """

        self._nat_id_no = nat_id_no

    @property
    def nationality(self):
        """Gets the nationality of this VerifiedPerson.  

        Two-letter code as specified in the ISO 3166 standard  

        :return: The nationality of this VerifiedPerson.  
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this VerifiedPerson.

        Two-letter code as specified in the ISO 3166 standard  

        :param nationality: The nationality of this VerifiedPerson.  
        :type: str
        """

        self._nationality = nationality

    @property
    def birth_date(self):
        """Gets the birth_date of this VerifiedPerson.  

        Date of birth for the person  

        :return: The birth_date of this VerifiedPerson.  
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this VerifiedPerson.

        Date of birth for the person  

        :param birth_date: The birth_date of this VerifiedPerson.  
        :type: str
        """

        self._birth_date = birth_date

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
        if not isinstance(other, VerifiedPerson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
