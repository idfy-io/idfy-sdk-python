# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class PersonDelomrader(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'delomrade_kode_field': 'str',
        'delomrade_tekst_field': 'str',
        'bedommelse_kode_field': 'str',
        'bedommelse_tekst_field': 'str'
    }

    attribute_map = {
        'delomrade_kode_field': 'delomradeKodeField',
        'delomrade_tekst_field': 'delomradeTekstField',
        'bedommelse_kode_field': 'bedommelseKodeField',
        'bedommelse_tekst_field': 'bedommelseTekstField'
    }

    def __init__(self, delomrade_kode_field=None, delomrade_tekst_field=None, bedommelse_kode_field=None, bedommelse_tekst_field=None):  
        """PersonDelomrader"""  

        self._delomrade_kode_field = None
        self._delomrade_tekst_field = None
        self._bedommelse_kode_field = None
        self._bedommelse_tekst_field = None
        self.discriminator = None

        if delomrade_kode_field is not None:
            self.delomrade_kode_field = delomrade_kode_field
        if delomrade_tekst_field is not None:
            self.delomrade_tekst_field = delomrade_tekst_field
        if bedommelse_kode_field is not None:
            self.bedommelse_kode_field = bedommelse_kode_field
        if bedommelse_tekst_field is not None:
            self.bedommelse_tekst_field = bedommelse_tekst_field

    @property
    def delomrade_kode_field(self):
        """Gets the delomrade_kode_field of this PersonDelomrader.  


        :return: The delomrade_kode_field of this PersonDelomrader.  
        :rtype: str
        """
        return self._delomrade_kode_field

    @delomrade_kode_field.setter
    def delomrade_kode_field(self, delomrade_kode_field):
        """Sets the delomrade_kode_field of this PersonDelomrader.


        :param delomrade_kode_field: The delomrade_kode_field of this PersonDelomrader.  
        :type: str
        """

        self._delomrade_kode_field = delomrade_kode_field

    @property
    def delomrade_tekst_field(self):
        """Gets the delomrade_tekst_field of this PersonDelomrader.  


        :return: The delomrade_tekst_field of this PersonDelomrader.  
        :rtype: str
        """
        return self._delomrade_tekst_field

    @delomrade_tekst_field.setter
    def delomrade_tekst_field(self, delomrade_tekst_field):
        """Sets the delomrade_tekst_field of this PersonDelomrader.


        :param delomrade_tekst_field: The delomrade_tekst_field of this PersonDelomrader.  
        :type: str
        """

        self._delomrade_tekst_field = delomrade_tekst_field

    @property
    def bedommelse_kode_field(self):
        """Gets the bedommelse_kode_field of this PersonDelomrader.  


        :return: The bedommelse_kode_field of this PersonDelomrader.  
        :rtype: str
        """
        return self._bedommelse_kode_field

    @bedommelse_kode_field.setter
    def bedommelse_kode_field(self, bedommelse_kode_field):
        """Sets the bedommelse_kode_field of this PersonDelomrader.


        :param bedommelse_kode_field: The bedommelse_kode_field of this PersonDelomrader.  
        :type: str
        """

        self._bedommelse_kode_field = bedommelse_kode_field

    @property
    def bedommelse_tekst_field(self):
        """Gets the bedommelse_tekst_field of this PersonDelomrader.  


        :return: The bedommelse_tekst_field of this PersonDelomrader.  
        :rtype: str
        """
        return self._bedommelse_tekst_field

    @bedommelse_tekst_field.setter
    def bedommelse_tekst_field(self, bedommelse_tekst_field):
        """Sets the bedommelse_tekst_field of this PersonDelomrader.


        :param bedommelse_tekst_field: The bedommelse_tekst_field of this PersonDelomrader.  
        :type: str
        """

        self._bedommelse_tekst_field = bedommelse_tekst_field

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
        if not isinstance(other, PersonDelomrader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
