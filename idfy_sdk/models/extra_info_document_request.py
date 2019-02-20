# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  



from idfy_sdk.models.extra_info_signer_request_special_properties import ExtraInfoSignerRequestSpecialProperties  


class ExtraInfoDocumentRequest(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'types': 'list[str]',
        'special_properties': 'ExtraInfoSignerRequestSpecialProperties'
    }

    attribute_map = {
        'types': 'types',
        'special_properties': 'specialProperties'
    }

    def __init__(self, types=None, special_properties=None):  
        """ExtraInfoDocumentRequest"""  

        self._types = None
        self._special_properties = None
        self.discriminator = None

        if types is not None:
            self.types = types
        if special_properties is not None:
            self.special_properties = special_properties

    @property
    def types(self):
        """Gets the types of this ExtraInfoDocumentRequest.  

        A list of the extra information you want to order. Certain types require special properties, see documentation for more information. Additional cost will incur (with the exception of Difi company info).  

        :return: The types of this ExtraInfoDocumentRequest.  
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this ExtraInfoDocumentRequest.

        A list of the extra information you want to order. Certain types require special properties, see documentation for more information. Additional cost will incur (with the exception of Difi company info).  

        :param types: The types of this ExtraInfoDocumentRequest.  
        :type: list[str]
        """
        allowed_values = ["rightsAndProkura"]  
        if not set(types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `types` [{0}], must be a subset of [{1}]"  
                .format(", ".join(map(str, set(types) - set(allowed_values))),  
                        ", ".join(map(str, allowed_values)))
            )

        self._types = types

    @property
    def special_properties(self):
        """Gets the special_properties of this ExtraInfoDocumentRequest.  


        :return: The special_properties of this ExtraInfoDocumentRequest.  
        :rtype: ExtraInfoSignerRequestSpecialProperties
        """
        return self._special_properties

    @special_properties.setter
    def special_properties(self, special_properties):
        """Sets the special_properties of this ExtraInfoDocumentRequest.


        :param special_properties: The special_properties of this ExtraInfoDocumentRequest.  
        :type: ExtraInfoSignerRequestSpecialProperties
        """

        self._special_properties = special_properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.swagger_types.items():
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
        if not isinstance(other, ExtraInfoDocumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
