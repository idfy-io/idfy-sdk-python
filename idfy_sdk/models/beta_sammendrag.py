# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class BetaSammendrag(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'antall_inkasso_field': 'int',
        'ajour_dato_inkasso_field': 'datetime',
        'antall_panter_losore_field': 'int',
        'ajour_dato_losore_field': 'datetime',
        'antall_panter_eiendom_field': 'int',
        'ajour_dato_eiendom_field': 'datetime'
    }

    attribute_map = {
        'antall_inkasso_field': 'antallInkassoField',
        'ajour_dato_inkasso_field': 'ajourDatoInkassoField',
        'antall_panter_losore_field': 'antallPanterLosoreField',
        'ajour_dato_losore_field': 'ajourDatoLosoreField',
        'antall_panter_eiendom_field': 'antallPanterEiendomField',
        'ajour_dato_eiendom_field': 'ajourDatoEiendomField'
    }

    def __init__(self, antall_inkasso_field=None, ajour_dato_inkasso_field=None, antall_panter_losore_field=None, ajour_dato_losore_field=None, antall_panter_eiendom_field=None, ajour_dato_eiendom_field=None):  
        """BetaSammendrag"""  

        self._antall_inkasso_field = None
        self._ajour_dato_inkasso_field = None
        self._antall_panter_losore_field = None
        self._ajour_dato_losore_field = None
        self._antall_panter_eiendom_field = None
        self._ajour_dato_eiendom_field = None
        self.discriminator = None

        if antall_inkasso_field is not None:
            self.antall_inkasso_field = antall_inkasso_field
        if ajour_dato_inkasso_field is not None:
            self.ajour_dato_inkasso_field = ajour_dato_inkasso_field
        if antall_panter_losore_field is not None:
            self.antall_panter_losore_field = antall_panter_losore_field
        if ajour_dato_losore_field is not None:
            self.ajour_dato_losore_field = ajour_dato_losore_field
        if antall_panter_eiendom_field is not None:
            self.antall_panter_eiendom_field = antall_panter_eiendom_field
        if ajour_dato_eiendom_field is not None:
            self.ajour_dato_eiendom_field = ajour_dato_eiendom_field

    @property
    def antall_inkasso_field(self):
        """Gets the antall_inkasso_field of this BetaSammendrag.  


        :return: The antall_inkasso_field of this BetaSammendrag.  
        :rtype: int
        """
        return self._antall_inkasso_field

    @antall_inkasso_field.setter
    def antall_inkasso_field(self, antall_inkasso_field):
        """Sets the antall_inkasso_field of this BetaSammendrag.


        :param antall_inkasso_field: The antall_inkasso_field of this BetaSammendrag.  
        :type: int
        """

        self._antall_inkasso_field = antall_inkasso_field

    @property
    def ajour_dato_inkasso_field(self):
        """Gets the ajour_dato_inkasso_field of this BetaSammendrag.  


        :return: The ajour_dato_inkasso_field of this BetaSammendrag.  
        :rtype: datetime
        """
        return self._ajour_dato_inkasso_field

    @ajour_dato_inkasso_field.setter
    def ajour_dato_inkasso_field(self, ajour_dato_inkasso_field):
        """Sets the ajour_dato_inkasso_field of this BetaSammendrag.


        :param ajour_dato_inkasso_field: The ajour_dato_inkasso_field of this BetaSammendrag.  
        :type: datetime
        """

        self._ajour_dato_inkasso_field = ajour_dato_inkasso_field

    @property
    def antall_panter_losore_field(self):
        """Gets the antall_panter_losore_field of this BetaSammendrag.  


        :return: The antall_panter_losore_field of this BetaSammendrag.  
        :rtype: int
        """
        return self._antall_panter_losore_field

    @antall_panter_losore_field.setter
    def antall_panter_losore_field(self, antall_panter_losore_field):
        """Sets the antall_panter_losore_field of this BetaSammendrag.


        :param antall_panter_losore_field: The antall_panter_losore_field of this BetaSammendrag.  
        :type: int
        """

        self._antall_panter_losore_field = antall_panter_losore_field

    @property
    def ajour_dato_losore_field(self):
        """Gets the ajour_dato_losore_field of this BetaSammendrag.  


        :return: The ajour_dato_losore_field of this BetaSammendrag.  
        :rtype: datetime
        """
        return self._ajour_dato_losore_field

    @ajour_dato_losore_field.setter
    def ajour_dato_losore_field(self, ajour_dato_losore_field):
        """Sets the ajour_dato_losore_field of this BetaSammendrag.


        :param ajour_dato_losore_field: The ajour_dato_losore_field of this BetaSammendrag.  
        :type: datetime
        """

        self._ajour_dato_losore_field = ajour_dato_losore_field

    @property
    def antall_panter_eiendom_field(self):
        """Gets the antall_panter_eiendom_field of this BetaSammendrag.  


        :return: The antall_panter_eiendom_field of this BetaSammendrag.  
        :rtype: int
        """
        return self._antall_panter_eiendom_field

    @antall_panter_eiendom_field.setter
    def antall_panter_eiendom_field(self, antall_panter_eiendom_field):
        """Sets the antall_panter_eiendom_field of this BetaSammendrag.


        :param antall_panter_eiendom_field: The antall_panter_eiendom_field of this BetaSammendrag.  
        :type: int
        """

        self._antall_panter_eiendom_field = antall_panter_eiendom_field

    @property
    def ajour_dato_eiendom_field(self):
        """Gets the ajour_dato_eiendom_field of this BetaSammendrag.  


        :return: The ajour_dato_eiendom_field of this BetaSammendrag.  
        :rtype: datetime
        """
        return self._ajour_dato_eiendom_field

    @ajour_dato_eiendom_field.setter
    def ajour_dato_eiendom_field(self, ajour_dato_eiendom_field):
        """Sets the ajour_dato_eiendom_field of this BetaSammendrag.


        :param ajour_dato_eiendom_field: The ajour_dato_eiendom_field of this BetaSammendrag.  
        :type: datetime
        """

        self._ajour_dato_eiendom_field = ajour_dato_eiendom_field

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
        if not isinstance(other, BetaSammendrag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
