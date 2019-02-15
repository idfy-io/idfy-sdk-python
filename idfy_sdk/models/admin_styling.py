# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class AdminStyling(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'base64_encoded_css_data': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'base64_encoded_css_data': 'Base64EncodedCssData',
        'file_name': 'FileName'
    }

    def __init__(self, account_id=None, base64_encoded_css_data=None, file_name=None):  
        """AdminStyling"""  

        self._account_id = None
        self._base64_encoded_css_data = None
        self._file_name = None
        self.discriminator = None

        self.account_id = account_id
        self.base64_encoded_css_data = base64_encoded_css_data
        self.file_name = file_name

    @property
    def account_id(self):
        """Gets the account_id of this AdminStyling.  


        :return: The account_id of this AdminStyling.  
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AdminStyling.


        :param account_id: The account_id of this AdminStyling.  
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  

        self._account_id = account_id

    @property
    def base64_encoded_css_data(self):
        """Gets the base64_encoded_css_data of this AdminStyling.  


        :return: The base64_encoded_css_data of this AdminStyling.  
        :rtype: str
        """
        return self._base64_encoded_css_data

    @base64_encoded_css_data.setter
    def base64_encoded_css_data(self, base64_encoded_css_data):
        """Sets the base64_encoded_css_data of this AdminStyling.


        :param base64_encoded_css_data: The base64_encoded_css_data of this AdminStyling.  
        :type: str
        """
        if base64_encoded_css_data is None:
            raise ValueError("Invalid value for `base64_encoded_css_data`, must not be `None`")  

        self._base64_encoded_css_data = base64_encoded_css_data

    @property
    def file_name(self):
        """Gets the file_name of this AdminStyling.  


        :return: The file_name of this AdminStyling.  
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this AdminStyling.


        :param file_name: The file_name of this AdminStyling.  
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  

        self._file_name = file_name

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
        if not isinstance(other, AdminStyling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
