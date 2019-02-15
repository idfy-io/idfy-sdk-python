# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.company_info_difi_response import CompanyInfoDifiResponse  


class DifiResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'organizations': 'list[CompanyInfoDifiResponse]',
        'raw_data': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'organizations': 'Organizations',
        'raw_data': 'RawData',
        'request_id': 'RequestId'
    }

    def __init__(self, organizations=None, raw_data=None, request_id=None):  
        """DifiResponse"""  

        self._organizations = None
        self._raw_data = None
        self._request_id = None
        self.discriminator = None

        if organizations is not None:
            self.organizations = organizations
        if raw_data is not None:
            self.raw_data = raw_data
        if request_id is not None:
            self.request_id = request_id

    @property
    def organizations(self):
        """Gets the organizations of this DifiResponse.  


        :return: The organizations of this DifiResponse.  
        :rtype: list[CompanyInfoDifiResponse]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this DifiResponse.


        :param organizations: The organizations of this DifiResponse.  
        :type: list[CompanyInfoDifiResponse]
        """

        self._organizations = organizations

    @property
    def raw_data(self):
        """Gets the raw_data of this DifiResponse.  


        :return: The raw_data of this DifiResponse.  
        :rtype: str
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this DifiResponse.


        :param raw_data: The raw_data of this DifiResponse.  
        :type: str
        """

        self._raw_data = raw_data

    @property
    def request_id(self):
        """Gets the request_id of this DifiResponse.  


        :return: The request_id of this DifiResponse.  
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DifiResponse.


        :param request_id: The request_id of this DifiResponse.  
        :type: str
        """

        self._request_id = request_id

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
        if not isinstance(other, DifiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
