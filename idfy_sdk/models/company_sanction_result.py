# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.address_list import AddressList  


class CompanySanctionResult(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'match_indicator': 'int',
        'title': 'str',
        'function': 'str',
        'comment': 'str',
        'alias_list': 'list[str]',
        'address_list': 'list[AddressList]',
        'url_list': 'list[str]',
        'source': 'str',
        'external_id': 'str',
        'last_update': 'datetime',
        'first_update': 'datetime',
        'name': 'str',
        'nationality': 'str',
        'provider': 'str'
    }

    attribute_map = {
        'match_indicator': 'matchIndicator',
        'title': 'title',
        'function': 'function',
        'comment': 'comment',
        'alias_list': 'aliasList',
        'address_list': 'addressList',
        'url_list': 'urlList',
        'source': 'source',
        'external_id': 'externalId',
        'last_update': 'lastUpdate',
        'first_update': 'firstUpdate',
        'name': 'name',
        'nationality': 'nationality',
        'provider': 'provider'
    }

    def __init__(self, match_indicator=None, title=None, function=None, comment=None, alias_list=None, address_list=None, url_list=None, source=None, external_id=None, last_update=None, first_update=None, name=None, nationality=None, provider=None):  
        """CompanySanctionResult"""  

        self._match_indicator = None
        self._title = None
        self._function = None
        self._comment = None
        self._alias_list = None
        self._address_list = None
        self._url_list = None
        self._source = None
        self._external_id = None
        self._last_update = None
        self._first_update = None
        self._name = None
        self._nationality = None
        self._provider = None
        self.discriminator = None

        if match_indicator is not None:
            self.match_indicator = match_indicator
        if title is not None:
            self.title = title
        if function is not None:
            self.function = function
        if comment is not None:
            self.comment = comment
        if alias_list is not None:
            self.alias_list = alias_list
        if address_list is not None:
            self.address_list = address_list
        if url_list is not None:
            self.url_list = url_list
        if source is not None:
            self.source = source
        if external_id is not None:
            self.external_id = external_id
        if last_update is not None:
            self.last_update = last_update
        if first_update is not None:
            self.first_update = first_update
        if name is not None:
            self.name = name
        if nationality is not None:
            self.nationality = nationality
        if provider is not None:
            self.provider = provider

    @property
    def match_indicator(self):
        """Gets the match_indicator of this CompanySanctionResult.  

        Quality indicator of match. Higher number means better match.  

        :return: The match_indicator of this CompanySanctionResult.  
        :rtype: int
        """
        return self._match_indicator

    @match_indicator.setter
    def match_indicator(self, match_indicator):
        """Sets the match_indicator of this CompanySanctionResult.

        Quality indicator of match. Higher number means better match.  

        :param match_indicator: The match_indicator of this CompanySanctionResult.  
        :type: int
        """

        self._match_indicator = match_indicator

    @property
    def title(self):
        """Gets the title of this CompanySanctionResult.  

        May be a text string denoting title of position, job title, etc  

        :return: The title of this CompanySanctionResult.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CompanySanctionResult.

        May be a text string denoting title of position, job title, etc  

        :param title: The title of this CompanySanctionResult.  
        :type: str
        """

        self._title = title

    @property
    def function(self):
        """Gets the function of this CompanySanctionResult.  

        Additional details about what the company does  

        :return: The function of this CompanySanctionResult.  
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this CompanySanctionResult.

        Additional details about what the company does  

        :param function: The function of this CompanySanctionResult.  
        :type: str
        """

        self._function = function

    @property
    def comment(self):
        """Gets the comment of this CompanySanctionResult.  

        A comment of some kind may be present in some lists  

        :return: The comment of this CompanySanctionResult.  
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this CompanySanctionResult.

        A comment of some kind may be present in some lists  

        :param comment: The comment of this CompanySanctionResult.  
        :type: str
        """

        self._comment = comment

    @property
    def alias_list(self):
        """Gets the alias_list of this CompanySanctionResult.  

        Name aliases for the company. May be none, one or more.  

        :return: The alias_list of this CompanySanctionResult.  
        :rtype: list[str]
        """
        return self._alias_list

    @alias_list.setter
    def alias_list(self, alias_list):
        """Sets the alias_list of this CompanySanctionResult.

        Name aliases for the company. May be none, one or more.  

        :param alias_list: The alias_list of this CompanySanctionResult.  
        :type: list[str]
        """

        self._alias_list = alias_list

    @property
    def address_list(self):
        """Gets the address_list of this CompanySanctionResult.  

        List of addresses found in the lists  

        :return: The address_list of this CompanySanctionResult.  
        :rtype: list[AddressList]
        """
        return self._address_list

    @address_list.setter
    def address_list(self, address_list):
        """Sets the address_list of this CompanySanctionResult.

        List of addresses found in the lists  

        :param address_list: The address_list of this CompanySanctionResult.  
        :type: list[AddressList]
        """

        self._address_list = address_list

    @property
    def url_list(self):
        """Gets the url_list of this CompanySanctionResult.  

        URLs to source documents (May be used for further investigations)  

        :return: The url_list of this CompanySanctionResult.  
        :rtype: list[str]
        """
        return self._url_list

    @url_list.setter
    def url_list(self, url_list):
        """Sets the url_list of this CompanySanctionResult.

        URLs to source documents (May be used for further investigations)  

        :param url_list: The url_list of this CompanySanctionResult.  
        :type: list[str]
        """

        self._url_list = url_list

    @property
    def source(self):
        """Gets the source of this CompanySanctionResult.  

        The name of the source list, e.g. 'EU_GLOBAL', 'PEP_Edge', 'UN_CONSOLIDATED'  

        :return: The source of this CompanySanctionResult.  
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CompanySanctionResult.

        The name of the source list, e.g. 'EU_GLOBAL', 'PEP_Edge', 'UN_CONSOLIDATED'  

        :param source: The source of this CompanySanctionResult.  
        :type: str
        """

        self._source = source

    @property
    def external_id(self):
        """Gets the external_id of this CompanySanctionResult.  

        External identification  

        :return: The external_id of this CompanySanctionResult.  
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this CompanySanctionResult.

        External identification  

        :param external_id: The external_id of this CompanySanctionResult.  
        :type: str
        """

        self._external_id = external_id

    @property
    def last_update(self):
        """Gets the last_update of this CompanySanctionResult.  

        Date of last update  

        :return: The last_update of this CompanySanctionResult.  
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this CompanySanctionResult.

        Date of last update  

        :param last_update: The last_update of this CompanySanctionResult.  
        :type: datetime
        """

        self._last_update = last_update

    @property
    def first_update(self):
        """Gets the first_update of this CompanySanctionResult.  

        Date of first update  

        :return: The first_update of this CompanySanctionResult.  
        :rtype: datetime
        """
        return self._first_update

    @first_update.setter
    def first_update(self, first_update):
        """Sets the first_update of this CompanySanctionResult.

        Date of first update  

        :param first_update: The first_update of this CompanySanctionResult.  
        :type: datetime
        """

        self._first_update = first_update

    @property
    def name(self):
        """Gets the name of this CompanySanctionResult.  

        Name of company  

        :return: The name of this CompanySanctionResult.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompanySanctionResult.

        Name of company  

        :param name: The name of this CompanySanctionResult.  
        :type: str
        """

        self._name = name

    @property
    def nationality(self):
        """Gets the nationality of this CompanySanctionResult.  

        Two-letter code as specified in the ISO 3166 standard  

        :return: The nationality of this CompanySanctionResult.  
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this CompanySanctionResult.

        Two-letter code as specified in the ISO 3166 standard  

        :param nationality: The nationality of this CompanySanctionResult.  
        :type: str
        """

        self._nationality = nationality

    @property
    def provider(self):
        """Gets the provider of this CompanySanctionResult.  

        Name of data provider  

        :return: The provider of this CompanySanctionResult.  
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CompanySanctionResult.

        Name of data provider  

        :param provider: The provider of this CompanySanctionResult.  
        :type: str
        """

        self._provider = provider

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
        if not isinstance(other, CompanySanctionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
