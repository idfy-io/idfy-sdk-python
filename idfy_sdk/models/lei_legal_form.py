# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class LeiLegalForm(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'other_legal_form': 'str',
        'entity_legal_form_code': 'str'
    }

    attribute_map = {
        'other_legal_form': 'OtherLegalForm',
        'entity_legal_form_code': 'EntityLegalFormCode'
    }

    def __init__(self, other_legal_form=None, entity_legal_form_code=None):  
        """LeiLegalForm"""  

        self._other_legal_form = None
        self._entity_legal_form_code = None
        self.discriminator = None

        if other_legal_form is not None:
            self.other_legal_form = other_legal_form
        if entity_legal_form_code is not None:
            self.entity_legal_form_code = entity_legal_form_code

    @property
    def other_legal_form(self):
        """Gets the other_legal_form of this LeiLegalForm.  


        :return: The other_legal_form of this LeiLegalForm.  
        :rtype: str
        """
        return self._other_legal_form

    @other_legal_form.setter
    def other_legal_form(self, other_legal_form):
        """Sets the other_legal_form of this LeiLegalForm.


        :param other_legal_form: The other_legal_form of this LeiLegalForm.  
        :type: str
        """

        self._other_legal_form = other_legal_form

    @property
    def entity_legal_form_code(self):
        """Gets the entity_legal_form_code of this LeiLegalForm.  


        :return: The entity_legal_form_code of this LeiLegalForm.  
        :rtype: str
        """
        return self._entity_legal_form_code

    @entity_legal_form_code.setter
    def entity_legal_form_code(self, entity_legal_form_code):
        """Sets the entity_legal_form_code of this LeiLegalForm.


        :param entity_legal_form_code: The entity_legal_form_code of this LeiLegalForm.  
        :type: str
        """

        self._entity_legal_form_code = entity_legal_form_code

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
        if not isinstance(other, LeiLegalForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
