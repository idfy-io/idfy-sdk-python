# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.x509_certificate import X509Certificate  


class Certificate(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'issuer_name': 'str',
        'subject_name': 'str',
        'valid_from_date': 'datetime',
        'valid_to_date': 'datetime',
        'version_number': 'str',
        'serial_number': 'str',
        'key_algorithm': 'str',
        'key_size': 'str',
        'unique_id': 'str',
        'originator': 'str',
        'bank_name': 'str',
        'date_of_birth': 'datetime',
        'policy_oid': 'str',
        'common_name': 'str',
        'signing_certficate': 'str',
        'x509_certificate': 'X509Certificate',
        'key_usage': 'str',
        'email_address': 'object',
        'signing_time': 'datetime',
        'phone_number': 'str',
        'certificate_type': 'str'
    }

    attribute_map = {
        'issuer_name': 'issuerName',
        'subject_name': 'subjectName',
        'valid_from_date': 'validFromDate',
        'valid_to_date': 'validToDate',
        'version_number': 'versionNumber',
        'serial_number': 'serialNumber',
        'key_algorithm': 'keyAlgorithm',
        'key_size': 'keySize',
        'unique_id': 'uniqueId',
        'originator': 'originator',
        'bank_name': 'bankName',
        'date_of_birth': 'dateOfBirth',
        'policy_oid': 'policyOid',
        'common_name': 'commonName',
        'signing_certficate': 'signingCertficate',
        'x509_certificate': 'x509Certificate',
        'key_usage': 'keyUsage',
        'email_address': 'emailAddress',
        'signing_time': 'signingTime',
        'phone_number': 'phoneNumber',
        'certificate_type': 'certificateType'
    }

    def __init__(self, issuer_name=None, subject_name=None, valid_from_date=None, valid_to_date=None, version_number=None, serial_number=None, key_algorithm=None, key_size=None, unique_id=None, originator=None, bank_name=None, date_of_birth=None, policy_oid=None, common_name=None, signing_certficate=None, x509_certificate=None, key_usage=None, email_address=None, signing_time=None, phone_number=None, certificate_type=None):  
        """Certificate"""  

        self._issuer_name = None
        self._subject_name = None
        self._valid_from_date = None
        self._valid_to_date = None
        self._version_number = None
        self._serial_number = None
        self._key_algorithm = None
        self._key_size = None
        self._unique_id = None
        self._originator = None
        self._bank_name = None
        self._date_of_birth = None
        self._policy_oid = None
        self._common_name = None
        self._signing_certficate = None
        self._x509_certificate = None
        self._key_usage = None
        self._email_address = None
        self._signing_time = None
        self._phone_number = None
        self._certificate_type = None
        self.discriminator = None

        if issuer_name is not None:
            self.issuer_name = issuer_name
        if subject_name is not None:
            self.subject_name = subject_name
        if valid_from_date is not None:
            self.valid_from_date = valid_from_date
        if valid_to_date is not None:
            self.valid_to_date = valid_to_date
        if version_number is not None:
            self.version_number = version_number
        if serial_number is not None:
            self.serial_number = serial_number
        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if key_size is not None:
            self.key_size = key_size
        if unique_id is not None:
            self.unique_id = unique_id
        if originator is not None:
            self.originator = originator
        if bank_name is not None:
            self.bank_name = bank_name
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if policy_oid is not None:
            self.policy_oid = policy_oid
        if common_name is not None:
            self.common_name = common_name
        if signing_certficate is not None:
            self.signing_certficate = signing_certficate
        if x509_certificate is not None:
            self.x509_certificate = x509_certificate
        if key_usage is not None:
            self.key_usage = key_usage
        if email_address is not None:
            self.email_address = email_address
        if signing_time is not None:
            self.signing_time = signing_time
        if phone_number is not None:
            self.phone_number = phone_number
        if certificate_type is not None:
            self.certificate_type = certificate_type

    @property
    def issuer_name(self):
        """Gets the issuer_name of this Certificate.  


        :return: The issuer_name of this Certificate.  
        :rtype: str
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """Sets the issuer_name of this Certificate.


        :param issuer_name: The issuer_name of this Certificate.  
        :type: str
        """

        self._issuer_name = issuer_name

    @property
    def subject_name(self):
        """Gets the subject_name of this Certificate.  


        :return: The subject_name of this Certificate.  
        :rtype: str
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        """Sets the subject_name of this Certificate.


        :param subject_name: The subject_name of this Certificate.  
        :type: str
        """

        self._subject_name = subject_name

    @property
    def valid_from_date(self):
        """Gets the valid_from_date of this Certificate.  


        :return: The valid_from_date of this Certificate.  
        :rtype: datetime
        """
        return self._valid_from_date

    @valid_from_date.setter
    def valid_from_date(self, valid_from_date):
        """Sets the valid_from_date of this Certificate.


        :param valid_from_date: The valid_from_date of this Certificate.  
        :type: datetime
        """

        self._valid_from_date = valid_from_date

    @property
    def valid_to_date(self):
        """Gets the valid_to_date of this Certificate.  


        :return: The valid_to_date of this Certificate.  
        :rtype: datetime
        """
        return self._valid_to_date

    @valid_to_date.setter
    def valid_to_date(self, valid_to_date):
        """Sets the valid_to_date of this Certificate.


        :param valid_to_date: The valid_to_date of this Certificate.  
        :type: datetime
        """

        self._valid_to_date = valid_to_date

    @property
    def version_number(self):
        """Gets the version_number of this Certificate.  


        :return: The version_number of this Certificate.  
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this Certificate.


        :param version_number: The version_number of this Certificate.  
        :type: str
        """

        self._version_number = version_number

    @property
    def serial_number(self):
        """Gets the serial_number of this Certificate.  


        :return: The serial_number of this Certificate.  
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this Certificate.


        :param serial_number: The serial_number of this Certificate.  
        :type: str
        """

        self._serial_number = serial_number

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this Certificate.  


        :return: The key_algorithm of this Certificate.  
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this Certificate.


        :param key_algorithm: The key_algorithm of this Certificate.  
        :type: str
        """

        self._key_algorithm = key_algorithm

    @property
    def key_size(self):
        """Gets the key_size of this Certificate.  


        :return: The key_size of this Certificate.  
        :rtype: str
        """
        return self._key_size

    @key_size.setter
    def key_size(self, key_size):
        """Sets the key_size of this Certificate.


        :param key_size: The key_size of this Certificate.  
        :type: str
        """

        self._key_size = key_size

    @property
    def unique_id(self):
        """Gets the unique_id of this Certificate.  


        :return: The unique_id of this Certificate.  
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this Certificate.


        :param unique_id: The unique_id of this Certificate.  
        :type: str
        """

        self._unique_id = unique_id

    @property
    def originator(self):
        """Gets the originator of this Certificate.  


        :return: The originator of this Certificate.  
        :rtype: str
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """Sets the originator of this Certificate.


        :param originator: The originator of this Certificate.  
        :type: str
        """

        self._originator = originator

    @property
    def bank_name(self):
        """Gets the bank_name of this Certificate.  


        :return: The bank_name of this Certificate.  
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this Certificate.


        :param bank_name: The bank_name of this Certificate.  
        :type: str
        """

        self._bank_name = bank_name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this Certificate.  


        :return: The date_of_birth of this Certificate.  
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this Certificate.


        :param date_of_birth: The date_of_birth of this Certificate.  
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def policy_oid(self):
        """Gets the policy_oid of this Certificate.  


        :return: The policy_oid of this Certificate.  
        :rtype: str
        """
        return self._policy_oid

    @policy_oid.setter
    def policy_oid(self, policy_oid):
        """Sets the policy_oid of this Certificate.


        :param policy_oid: The policy_oid of this Certificate.  
        :type: str
        """

        self._policy_oid = policy_oid

    @property
    def common_name(self):
        """Gets the common_name of this Certificate.  


        :return: The common_name of this Certificate.  
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this Certificate.


        :param common_name: The common_name of this Certificate.  
        :type: str
        """

        self._common_name = common_name

    @property
    def signing_certficate(self):
        """Gets the signing_certficate of this Certificate.  


        :return: The signing_certficate of this Certificate.  
        :rtype: str
        """
        return self._signing_certficate

    @signing_certficate.setter
    def signing_certficate(self, signing_certficate):
        """Sets the signing_certficate of this Certificate.


        :param signing_certficate: The signing_certficate of this Certificate.  
        :type: str
        """

        self._signing_certficate = signing_certficate

    @property
    def x509_certificate(self):
        """Gets the x509_certificate of this Certificate.  


        :return: The x509_certificate of this Certificate.  
        :rtype: X509Certificate
        """
        return self._x509_certificate

    @x509_certificate.setter
    def x509_certificate(self, x509_certificate):
        """Sets the x509_certificate of this Certificate.


        :param x509_certificate: The x509_certificate of this Certificate.  
        :type: X509Certificate
        """

        self._x509_certificate = x509_certificate

    @property
    def key_usage(self):
        """Gets the key_usage of this Certificate.  


        :return: The key_usage of this Certificate.  
        :rtype: str
        """
        return self._key_usage

    @key_usage.setter
    def key_usage(self, key_usage):
        """Sets the key_usage of this Certificate.


        :param key_usage: The key_usage of this Certificate.  
        :type: str
        """

        self._key_usage = key_usage

    @property
    def email_address(self):
        """Gets the email_address of this Certificate.  


        :return: The email_address of this Certificate.  
        :rtype: object
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Certificate.


        :param email_address: The email_address of this Certificate.  
        :type: object
        """

        self._email_address = email_address

    @property
    def signing_time(self):
        """Gets the signing_time of this Certificate.  


        :return: The signing_time of this Certificate.  
        :rtype: datetime
        """
        return self._signing_time

    @signing_time.setter
    def signing_time(self, signing_time):
        """Sets the signing_time of this Certificate.


        :param signing_time: The signing_time of this Certificate.  
        :type: datetime
        """

        self._signing_time = signing_time

    @property
    def phone_number(self):
        """Gets the phone_number of this Certificate.  


        :return: The phone_number of this Certificate.  
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this Certificate.


        :param phone_number: The phone_number of this Certificate.  
        :type: str
        """

        self._phone_number = phone_number

    @property
    def certificate_type(self):
        """Gets the certificate_type of this Certificate.  


        :return: The certificate_type of this Certificate.  
        :rtype: str
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this Certificate.


        :param certificate_type: The certificate_type of this Certificate.  
        :type: str
        """
        allowed_values = ["HSM_MERCHANT_CERTIFICATE", "MOBILE_PERSONAL_CERTIFICATE", "NETCENTRIC_EMPLOYEE_CERTIFICATE", "NETCENTRIC_PERSONAL_CERTIFICATE", "NETCENTRIC_QUALIFIED_EMPLOYEE_CERTIFICATE", "NETCENTRIC_QUALIFIED_PERSONAL_CERTIFICATE", "SOFT_MERCHANT_CERTIFICATE", "UNKNOWN"]  
        if certificate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `certificate_type` ({0}), must be one of {1}"  
                .format(certificate_type, allowed_values)
            )

        self._certificate_type = certificate_type

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
        if not isinstance(other, Certificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
