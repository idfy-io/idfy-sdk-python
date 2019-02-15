# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class CreatePdfTemplateLabels(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'en': 'dict(str, str)',
        'no': 'dict(str, str)',
        'sv': 'dict(str, str)',
        'da': 'dict(str, str)',
        'fi': 'dict(str, str)'
    }

    attribute_map = {
        'en': 'en',
        'no': 'no',
        'sv': 'sv',
        'da': 'da',
        'fi': 'fi'
    }

    def __init__(self, en=None, no=None, sv=None, da=None, fi=None):  
        """CreatePdfTemplateLabels"""  

        self._en = None
        self._no = None
        self._sv = None
        self._da = None
        self._fi = None
        self.discriminator = None

        if en is not None:
            self.en = en
        if no is not None:
            self.no = no
        if sv is not None:
            self.sv = sv
        if da is not None:
            self.da = da
        if fi is not None:
            self.fi = fi

    @property
    def en(self):
        """Gets the en of this CreatePdfTemplateLabels.  


        :return: The en of this CreatePdfTemplateLabels.  
        :rtype: dict(str, str)
        """
        return self._en

    @en.setter
    def en(self, en):
        """Sets the en of this CreatePdfTemplateLabels.


        :param en: The en of this CreatePdfTemplateLabels.  
        :type: dict(str, str)
        """

        self._en = en

    @property
    def no(self):
        """Gets the no of this CreatePdfTemplateLabels.  


        :return: The no of this CreatePdfTemplateLabels.  
        :rtype: dict(str, str)
        """
        return self._no

    @no.setter
    def no(self, no):
        """Sets the no of this CreatePdfTemplateLabels.


        :param no: The no of this CreatePdfTemplateLabels.  
        :type: dict(str, str)
        """

        self._no = no

    @property
    def sv(self):
        """Gets the sv of this CreatePdfTemplateLabels.  


        :return: The sv of this CreatePdfTemplateLabels.  
        :rtype: dict(str, str)
        """
        return self._sv

    @sv.setter
    def sv(self, sv):
        """Sets the sv of this CreatePdfTemplateLabels.


        :param sv: The sv of this CreatePdfTemplateLabels.  
        :type: dict(str, str)
        """

        self._sv = sv

    @property
    def da(self):
        """Gets the da of this CreatePdfTemplateLabels.  


        :return: The da of this CreatePdfTemplateLabels.  
        :rtype: dict(str, str)
        """
        return self._da

    @da.setter
    def da(self, da):
        """Sets the da of this CreatePdfTemplateLabels.


        :param da: The da of this CreatePdfTemplateLabels.  
        :type: dict(str, str)
        """

        self._da = da

    @property
    def fi(self):
        """Gets the fi of this CreatePdfTemplateLabels.  


        :return: The fi of this CreatePdfTemplateLabels.  
        :rtype: dict(str, str)
        """
        return self._fi

    @fi.setter
    def fi(self, fi):
        """Sets the fi of this CreatePdfTemplateLabels.


        :param fi: The fi of this CreatePdfTemplateLabels.  
        :type: dict(str, str)
        """

        self._fi = fi

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
        if not isinstance(other, CreatePdfTemplateLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other