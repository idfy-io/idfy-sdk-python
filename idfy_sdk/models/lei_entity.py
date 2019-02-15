# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.lei_entity_address import LeiEntityAddress  
from idfy_sdk.models.lei_legal_form import LeiLegalForm  
from idfy_sdk.models.lei_registration_authority import LeiRegistrationAuthority  


class LeiEntity(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'headquarters_address': 'LeiEntityAddress',
        'legal_address': 'LeiEntityAddress',
        'legal_jurisdiction': 'str',
        'legal_name': 'str',
        'entity_status': 'str',
        'entity_category': 'str',
        'legal_form': 'LeiLegalForm',
        'registration_authority': 'LeiRegistrationAuthority'
    }

    attribute_map = {
        'headquarters_address': 'HeadquartersAddress',
        'legal_address': 'LegalAddress',
        'legal_jurisdiction': 'LegalJurisdiction',
        'legal_name': 'LegalName',
        'entity_status': 'EntityStatus',
        'entity_category': 'EntityCategory',
        'legal_form': 'LegalForm',
        'registration_authority': 'RegistrationAuthority'
    }

    def __init__(self, headquarters_address=None, legal_address=None, legal_jurisdiction=None, legal_name=None, entity_status=None, entity_category=None, legal_form=None, registration_authority=None):  
        """LeiEntity"""  

        self._headquarters_address = None
        self._legal_address = None
        self._legal_jurisdiction = None
        self._legal_name = None
        self._entity_status = None
        self._entity_category = None
        self._legal_form = None
        self._registration_authority = None
        self.discriminator = None

        if headquarters_address is not None:
            self.headquarters_address = headquarters_address
        if legal_address is not None:
            self.legal_address = legal_address
        if legal_jurisdiction is not None:
            self.legal_jurisdiction = legal_jurisdiction
        if legal_name is not None:
            self.legal_name = legal_name
        if entity_status is not None:
            self.entity_status = entity_status
        if entity_category is not None:
            self.entity_category = entity_category
        if legal_form is not None:
            self.legal_form = legal_form
        if registration_authority is not None:
            self.registration_authority = registration_authority

    @property
    def headquarters_address(self):
        """Gets the headquarters_address of this LeiEntity.  


        :return: The headquarters_address of this LeiEntity.  
        :rtype: LeiEntityAddress
        """
        return self._headquarters_address

    @headquarters_address.setter
    def headquarters_address(self, headquarters_address):
        """Sets the headquarters_address of this LeiEntity.


        :param headquarters_address: The headquarters_address of this LeiEntity.  
        :type: LeiEntityAddress
        """

        self._headquarters_address = headquarters_address

    @property
    def legal_address(self):
        """Gets the legal_address of this LeiEntity.  


        :return: The legal_address of this LeiEntity.  
        :rtype: LeiEntityAddress
        """
        return self._legal_address

    @legal_address.setter
    def legal_address(self, legal_address):
        """Sets the legal_address of this LeiEntity.


        :param legal_address: The legal_address of this LeiEntity.  
        :type: LeiEntityAddress
        """

        self._legal_address = legal_address

    @property
    def legal_jurisdiction(self):
        """Gets the legal_jurisdiction of this LeiEntity.  


        :return: The legal_jurisdiction of this LeiEntity.  
        :rtype: str
        """
        return self._legal_jurisdiction

    @legal_jurisdiction.setter
    def legal_jurisdiction(self, legal_jurisdiction):
        """Sets the legal_jurisdiction of this LeiEntity.


        :param legal_jurisdiction: The legal_jurisdiction of this LeiEntity.  
        :type: str
        """

        self._legal_jurisdiction = legal_jurisdiction

    @property
    def legal_name(self):
        """Gets the legal_name of this LeiEntity.  


        :return: The legal_name of this LeiEntity.  
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this LeiEntity.


        :param legal_name: The legal_name of this LeiEntity.  
        :type: str
        """

        self._legal_name = legal_name

    @property
    def entity_status(self):
        """Gets the entity_status of this LeiEntity.  


        :return: The entity_status of this LeiEntity.  
        :rtype: str
        """
        return self._entity_status

    @entity_status.setter
    def entity_status(self, entity_status):
        """Sets the entity_status of this LeiEntity.


        :param entity_status: The entity_status of this LeiEntity.  
        :type: str
        """

        self._entity_status = entity_status

    @property
    def entity_category(self):
        """Gets the entity_category of this LeiEntity.  


        :return: The entity_category of this LeiEntity.  
        :rtype: str
        """
        return self._entity_category

    @entity_category.setter
    def entity_category(self, entity_category):
        """Sets the entity_category of this LeiEntity.


        :param entity_category: The entity_category of this LeiEntity.  
        :type: str
        """

        self._entity_category = entity_category

    @property
    def legal_form(self):
        """Gets the legal_form of this LeiEntity.  


        :return: The legal_form of this LeiEntity.  
        :rtype: LeiLegalForm
        """
        return self._legal_form

    @legal_form.setter
    def legal_form(self, legal_form):
        """Sets the legal_form of this LeiEntity.


        :param legal_form: The legal_form of this LeiEntity.  
        :type: LeiLegalForm
        """

        self._legal_form = legal_form

    @property
    def registration_authority(self):
        """Gets the registration_authority of this LeiEntity.  


        :return: The registration_authority of this LeiEntity.  
        :rtype: LeiRegistrationAuthority
        """
        return self._registration_authority

    @registration_authority.setter
    def registration_authority(self, registration_authority):
        """Sets the registration_authority of this LeiEntity.


        :param registration_authority: The registration_authority of this LeiEntity.  
        :type: LeiRegistrationAuthority
        """

        self._registration_authority = registration_authority

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
        if not isinstance(other, LeiEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
