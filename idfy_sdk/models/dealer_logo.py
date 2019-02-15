# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class DealerLogo(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dealer_id': 'str',
        'base64_encoded_logo': 'str',
        'file_name': 'str'
    }

    attribute_map = {
        'dealer_id': 'DealerId',
        'base64_encoded_logo': 'Base64EncodedLogo',
        'file_name': 'FileName'
    }

    def __init__(self, dealer_id=None, base64_encoded_logo=None, file_name=None):  
        """DealerLogo"""  

        self._dealer_id = None
        self._base64_encoded_logo = None
        self._file_name = None
        self.discriminator = None

        self.dealer_id = dealer_id
        self.base64_encoded_logo = base64_encoded_logo
        self.file_name = file_name

    @property
    def dealer_id(self):
        """Gets the dealer_id of this DealerLogo.  


        :return: The dealer_id of this DealerLogo.  
        :rtype: str
        """
        return self._dealer_id

    @dealer_id.setter
    def dealer_id(self, dealer_id):
        """Sets the dealer_id of this DealerLogo.


        :param dealer_id: The dealer_id of this DealerLogo.  
        :type: str
        """
        if dealer_id is None:
            raise ValueError("Invalid value for `dealer_id`, must not be `None`")  

        self._dealer_id = dealer_id

    @property
    def base64_encoded_logo(self):
        """Gets the base64_encoded_logo of this DealerLogo.  


        :return: The base64_encoded_logo of this DealerLogo.  
        :rtype: str
        """
        return self._base64_encoded_logo

    @base64_encoded_logo.setter
    def base64_encoded_logo(self, base64_encoded_logo):
        """Sets the base64_encoded_logo of this DealerLogo.


        :param base64_encoded_logo: The base64_encoded_logo of this DealerLogo.  
        :type: str
        """
        if base64_encoded_logo is None:
            raise ValueError("Invalid value for `base64_encoded_logo`, must not be `None`")  

        self._base64_encoded_logo = base64_encoded_logo

    @property
    def file_name(self):
        """Gets the file_name of this DealerLogo.  


        :return: The file_name of this DealerLogo.  
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DealerLogo.


        :param file_name: The file_name of this DealerLogo.  
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
        if not isinstance(other, DealerLogo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
