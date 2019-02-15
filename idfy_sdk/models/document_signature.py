# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.social_security_number import SocialSecurityNumber  


class DocumentSignature(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'signature_method': 'str',
        'full_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'middle_name': 'str',
        'signed_time': 'datetime',
        'date_of_birth': 'str',
        'signature_method_unique_id': 'str',
        'social_security_number': 'SocialSecurityNumber',
        'client_ip': 'str'
    }

    attribute_map = {
        'signature_method': 'signatureMethod',
        'full_name': 'fullName',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'middle_name': 'middleName',
        'signed_time': 'signedTime',
        'date_of_birth': 'dateOfBirth',
        'signature_method_unique_id': 'signatureMethodUniqueId',
        'social_security_number': 'socialSecurityNumber',
        'client_ip': 'clientIp'
    }

    def __init__(self, signature_method=None, full_name=None, first_name=None, last_name=None, middle_name=None, signed_time=None, date_of_birth=None, signature_method_unique_id=None, social_security_number=None, client_ip=None):  
        """DocumentSignature"""  

        self._signature_method = None
        self._full_name = None
        self._first_name = None
        self._last_name = None
        self._middle_name = None
        self._signed_time = None
        self._date_of_birth = None
        self._signature_method_unique_id = None
        self._social_security_number = None
        self._client_ip = None
        self.discriminator = None

        if signature_method is not None:
            self.signature_method = signature_method
        if full_name is not None:
            self.full_name = full_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if middle_name is not None:
            self.middle_name = middle_name
        if signed_time is not None:
            self.signed_time = signed_time
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if signature_method_unique_id is not None:
            self.signature_method_unique_id = signature_method_unique_id
        if social_security_number is not None:
            self.social_security_number = social_security_number
        if client_ip is not None:
            self.client_ip = client_ip

    @property
    def signature_method(self):
        """Gets the signature_method of this DocumentSignature.  

        The signature method used to sign the document.  

        :return: The signature_method of this DocumentSignature.  
        :rtype: str
        """
        return self._signature_method

    @signature_method.setter
    def signature_method(self, signature_method):
        """Sets the signature_method of this DocumentSignature.

        The signature method used to sign the document.  

        :param signature_method: The signature_method of this DocumentSignature.  
        :type: str
        """
        allowed_values = ["no_bankid", "no_bankid_mobile", "no_bankid_netcentric", "no_buypass", "no_commfides", "se_bankid", "dk_nemid", "fi_tupas", "fi_mobiilivarmenne", "nl_digid", "es_dni", "ee_esteid", "mobile_connect", "sms_otp", "identification_papers", "social", "unknown"]  
        if signature_method not in allowed_values:
            raise ValueError(
                "Invalid value for `signature_method` ({0}), must be one of {1}"  
                .format(signature_method, allowed_values)
            )

        self._signature_method = signature_method

    @property
    def full_name(self):
        """Gets the full_name of this DocumentSignature.  

        The signer's full name, retrieved from the signature-method provider.  

        :return: The full_name of this DocumentSignature.  
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this DocumentSignature.

        The signer's full name, retrieved from the signature-method provider.  

        :param full_name: The full_name of this DocumentSignature.  
        :type: str
        """

        self._full_name = full_name

    @property
    def first_name(self):
        """Gets the first_name of this DocumentSignature.  

        The signer's first name.  

        :return: The first_name of this DocumentSignature.  
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this DocumentSignature.

        The signer's first name.  

        :param first_name: The first_name of this DocumentSignature.  
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this DocumentSignature.  

        The signer's last name.  

        :return: The last_name of this DocumentSignature.  
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this DocumentSignature.

        The signer's last name.  

        :param last_name: The last_name of this DocumentSignature.  
        :type: str
        """

        self._last_name = last_name

    @property
    def middle_name(self):
        """Gets the middle_name of this DocumentSignature.  

        The signer's middle name.  

        :return: The middle_name of this DocumentSignature.  
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this DocumentSignature.

        The signer's middle name.  

        :param middle_name: The middle_name of this DocumentSignature.  
        :type: str
        """

        self._middle_name = middle_name

    @property
    def signed_time(self):
        """Gets the signed_time of this DocumentSignature.  

        Time at which the signature was registered (ISO 8601).  

        :return: The signed_time of this DocumentSignature.  
        :rtype: datetime
        """
        return self._signed_time

    @signed_time.setter
    def signed_time(self, signed_time):
        """Sets the signed_time of this DocumentSignature.

        Time at which the signature was registered (ISO 8601).  

        :param signed_time: The signed_time of this DocumentSignature.  
        :type: datetime
        """

        self._signed_time = signed_time

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this DocumentSignature.  

        The signer's date of birth (ddMMyy).  

        :return: The date_of_birth of this DocumentSignature.  
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this DocumentSignature.

        The signer's date of birth (ddMMyy).  

        :param date_of_birth: The date_of_birth of this DocumentSignature.  
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def signature_method_unique_id(self):
        """Gets the signature_method_unique_id of this DocumentSignature.  

        The signature method unique ID.  

        :return: The signature_method_unique_id of this DocumentSignature.  
        :rtype: str
        """
        return self._signature_method_unique_id

    @signature_method_unique_id.setter
    def signature_method_unique_id(self, signature_method_unique_id):
        """Sets the signature_method_unique_id of this DocumentSignature.

        The signature method unique ID.  

        :param signature_method_unique_id: The signature_method_unique_id of this DocumentSignature.  
        :type: str
        """

        self._signature_method_unique_id = signature_method_unique_id

    @property
    def social_security_number(self):
        """Gets the social_security_number of this DocumentSignature.  


        :return: The social_security_number of this DocumentSignature.  
        :rtype: SocialSecurityNumber
        """
        return self._social_security_number

    @social_security_number.setter
    def social_security_number(self, social_security_number):
        """Sets the social_security_number of this DocumentSignature.


        :param social_security_number: The social_security_number of this DocumentSignature.  
        :type: SocialSecurityNumber
        """

        self._social_security_number = social_security_number

    @property
    def client_ip(self):
        """Gets the client_ip of this DocumentSignature.  

        The IP address of the signer.  

        :return: The client_ip of this DocumentSignature.  
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this DocumentSignature.

        The IP address of the signer.  

        :param client_ip: The client_ip of this DocumentSignature.  
        :type: str
        """

        self._client_ip = client_ip

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
        if not isinstance(other, DocumentSignature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
