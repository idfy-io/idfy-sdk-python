# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class IdentificationLogItem(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'client_ip': 'str',
        'user_agent': 'str',
        'identity_provider_type': 'str',
        'language': 'str',
        'externalid': 'str',
        'errorcode': 'str',
        'timestamp': 'datetime',
        'i_frame': 'bool',
        'social_security_number': 'bool',
        'account_id': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'status': 'Status',
        'client_ip': 'ClientIp',
        'user_agent': 'UserAgent',
        'identity_provider_type': 'IdentityProviderType',
        'language': 'Language',
        'externalid': 'Externalid',
        'errorcode': 'Errorcode',
        'timestamp': 'Timestamp',
        'i_frame': 'iFrame',
        'social_security_number': 'SocialSecurityNumber',
        'account_id': 'AccountId'
    }

    def __init__(self, id=None, name=None, status=None, client_ip=None, user_agent=None, identity_provider_type=None, language=None, externalid=None, errorcode=None, timestamp=None, i_frame=None, social_security_number=None, account_id=None):  
        """IdentificationLogItem"""  

        self._id = None
        self._name = None
        self._status = None
        self._client_ip = None
        self._user_agent = None
        self._identity_provider_type = None
        self._language = None
        self._externalid = None
        self._errorcode = None
        self._timestamp = None
        self._i_frame = None
        self._social_security_number = None
        self._account_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if client_ip is not None:
            self.client_ip = client_ip
        if user_agent is not None:
            self.user_agent = user_agent
        if identity_provider_type is not None:
            self.identity_provider_type = identity_provider_type
        if language is not None:
            self.language = language
        if externalid is not None:
            self.externalid = externalid
        if errorcode is not None:
            self.errorcode = errorcode
        if timestamp is not None:
            self.timestamp = timestamp
        if i_frame is not None:
            self.i_frame = i_frame
        if social_security_number is not None:
            self.social_security_number = social_security_number
        if account_id is not None:
            self.account_id = account_id

    @property
    def id(self):
        """Gets the id of this IdentificationLogItem.  

        The sessionID for the identitication  

        :return: The id of this IdentificationLogItem.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentificationLogItem.

        The sessionID for the identitication  

        :param id: The id of this IdentificationLogItem.  
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this IdentificationLogItem.  

        The fullname of the user as reported back from the IdentityProvider if the identification was a success  

        :return: The name of this IdentificationLogItem.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentificationLogItem.

        The fullname of the user as reported back from the IdentityProvider if the identification was a success  

        :param name: The name of this IdentificationLogItem.  
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this IdentificationLogItem.  

        The status of the identification process. If not success the identification process is not completed.  

        :return: The status of this IdentificationLogItem.  
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IdentificationLogItem.

        The status of the identification process. If not success the identification process is not completed.  

        :param status: The status of this IdentificationLogItem.  
        :type: str
        """
        allowed_values = ["UNKNOWN", "SUCCESS", "ERROR", "USERABORTED", "INVALIDATED", "TIMEOUT", "CREATED", "USERINITIATED"]  
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def client_ip(self):
        """Gets the client_ip of this IdentificationLogItem.  

        The IP-address of the user  

        :return: The client_ip of this IdentificationLogItem.  
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this IdentificationLogItem.

        The IP-address of the user  

        :param client_ip: The client_ip of this IdentificationLogItem.  
        :type: str
        """

        self._client_ip = client_ip

    @property
    def user_agent(self):
        """Gets the user_agent of this IdentificationLogItem.  

        The users user-agent (browser/device)  

        :return: The user_agent of this IdentificationLogItem.  
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this IdentificationLogItem.

        The users user-agent (browser/device)  

        :param user_agent: The user_agent of this IdentificationLogItem.  
        :type: str
        """

        self._user_agent = user_agent

    @property
    def identity_provider_type(self):
        """Gets the identity_provider_type of this IdentificationLogItem.  

        The identityprovider type (Norwegian BanKID, SwedishBankID, Nemid, etc)  

        :return: The identity_provider_type of this IdentificationLogItem.  
        :rtype: str
        """
        return self._identity_provider_type

    @identity_provider_type.setter
    def identity_provider_type(self, identity_provider_type):
        """Sets the identity_provider_type of this IdentificationLogItem.

        The identityprovider type (Norwegian BanKID, SwedishBankID, Nemid, etc)  

        :param identity_provider_type: The identity_provider_type of this IdentificationLogItem.  
        :type: str
        """

        self._identity_provider_type = identity_provider_type

    @property
    def language(self):
        """Gets the language of this IdentificationLogItem.  

        The language  used for the identification process  

        :return: The language of this IdentificationLogItem.  
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this IdentificationLogItem.

        The language  used for the identification process  

        :param language: The language of this IdentificationLogItem.  
        :type: str
        """

        self._language = language

    @property
    def externalid(self):
        """Gets the externalid of this IdentificationLogItem.  

        The merchants reference to the identification process, this will also be used to identify an identification in a detailed invoice.  

        :return: The externalid of this IdentificationLogItem.  
        :rtype: str
        """
        return self._externalid

    @externalid.setter
    def externalid(self, externalid):
        """Sets the externalid of this IdentificationLogItem.

        The merchants reference to the identification process, this will also be used to identify an identification in a detailed invoice.  

        :param externalid: The externalid of this IdentificationLogItem.  
        :type: str
        """

        self._externalid = externalid

    @property
    def errorcode(self):
        """Gets the errorcode of this IdentificationLogItem.  

        The error code for the error  

        :return: The errorcode of this IdentificationLogItem.  
        :rtype: str
        """
        return self._errorcode

    @errorcode.setter
    def errorcode(self, errorcode):
        """Sets the errorcode of this IdentificationLogItem.

        The error code for the error  

        :param errorcode: The errorcode of this IdentificationLogItem.  
        :type: str
        """

        self._errorcode = errorcode

    @property
    def timestamp(self):
        """Gets the timestamp of this IdentificationLogItem.  

        The timestamp for the creation of the identification process  

        :return: The timestamp of this IdentificationLogItem.  
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this IdentificationLogItem.

        The timestamp for the creation of the identification process  

        :param timestamp: The timestamp of this IdentificationLogItem.  
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def i_frame(self):
        """Gets the i_frame of this IdentificationLogItem.  

        Was an iFrame used  

        :return: The i_frame of this IdentificationLogItem.  
        :rtype: bool
        """
        return self._i_frame

    @i_frame.setter
    def i_frame(self, i_frame):
        """Sets the i_frame of this IdentificationLogItem.

        Was an iFrame used  

        :param i_frame: The i_frame of this IdentificationLogItem.  
        :type: bool
        """

        self._i_frame = i_frame

    @property
    def social_security_number(self):
        """Gets the social_security_number of this IdentificationLogItem.  

        Was social securitynumber fetched  

        :return: The social_security_number of this IdentificationLogItem.  
        :rtype: bool
        """
        return self._social_security_number

    @social_security_number.setter
    def social_security_number(self, social_security_number):
        """Sets the social_security_number of this IdentificationLogItem.

        Was social securitynumber fetched  

        :param social_security_number: The social_security_number of this IdentificationLogItem.  
        :type: bool
        """

        self._social_security_number = social_security_number

    @property
    def account_id(self):
        """Gets the account_id of this IdentificationLogItem.  


        :return: The account_id of this IdentificationLogItem.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this IdentificationLogItem.


        :param account_id: The account_id of this IdentificationLogItem.  
        :type: str
        """

        self._account_id = account_id

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
        if not isinstance(other, IdentificationLogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
