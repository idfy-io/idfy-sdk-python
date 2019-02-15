# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class Styling(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'color_theme': 'str',
        'theme_mode': 'str',
        'spinner': 'str',
        'hide_top_bar': 'bool',
        'background_color': 'str'
    }

    attribute_map = {
        'color_theme': 'colorTheme',
        'theme_mode': 'themeMode',
        'spinner': 'spinner',
        'hide_top_bar': 'hideTopBar',
        'background_color': 'backgroundColor'
    }

    def __init__(self, color_theme=None, theme_mode=None, spinner=None, hide_top_bar=None, background_color=None):  
        """Styling"""  

        self._color_theme = None
        self._theme_mode = None
        self._spinner = None
        self._hide_top_bar = None
        self._background_color = None
        self.discriminator = None

        if color_theme is not None:
            self.color_theme = color_theme
        if theme_mode is not None:
            self.theme_mode = theme_mode
        if spinner is not None:
            self.spinner = spinner
        if hide_top_bar is not None:
            self.hide_top_bar = hide_top_bar
        if background_color is not None:
            self.background_color = background_color

    @property
    def color_theme(self):
        """Gets the color_theme of this Styling.  

        The color theme for the application.  

        :return: The color_theme of this Styling.  
        :rtype: str
        """
        return self._color_theme

    @color_theme.setter
    def color_theme(self, color_theme):
        """Sets the color_theme of this Styling.

        The color theme for the application.  

        :param color_theme: The color_theme of this Styling.  
        :type: str
        """
        allowed_values = ["Default", "Black", "Blue", "Cyan", "Dark", "Lime", "Neutral", "Pink", "Purple", "Red", "Teal", "Indigo", "LightBlue", "DeepPurple", "Green", "LightGreen", "Yellow", "Amber", "Orange", "DeepOrange", "Brown", "Gray", "BlueGray"]  
        if color_theme not in allowed_values:
            raise ValueError(
                "Invalid value for `color_theme` ({0}), must be one of {1}"  
                .format(color_theme, allowed_values)
            )

        self._color_theme = color_theme

    @property
    def theme_mode(self):
        """Gets the theme_mode of this Styling.  

        The theme color mode, specify if you want it dark or light themed. Defaults to light  

        :return: The theme_mode of this Styling.  
        :rtype: str
        """
        return self._theme_mode

    @theme_mode.setter
    def theme_mode(self, theme_mode):
        """Sets the theme_mode of this Styling.

        The theme color mode, specify if you want it dark or light themed. Defaults to light  

        :param theme_mode: The theme_mode of this Styling.  
        :type: str
        """
        allowed_values = ["Default", "Light", "Dark"]  
        if theme_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `theme_mode` ({0}), must be one of {1}"  
                .format(theme_mode, allowed_values)
            )

        self._theme_mode = theme_mode

    @property
    def spinner(self):
        """Gets the spinner of this Styling.  

        The type of spinner to show in loading screens.  

        :return: The spinner of this Styling.  
        :rtype: str
        """
        return self._spinner

    @spinner.setter
    def spinner(self, spinner):
        """Sets the spinner of this Styling.

        The type of spinner to show in loading screens.  

        :param spinner: The spinner of this Styling.  
        :type: str
        """
        allowed_values = ["Document", "Classic", "Cubes", "Bounce"]  
        if spinner not in allowed_values:
            raise ValueError(
                "Invalid value for `spinner` ({0}), must be one of {1}"  
                .format(spinner, allowed_values)
            )

        self._spinner = spinner

    @property
    def hide_top_bar(self):
        """Gets the hide_top_bar of this Styling.  

        If you want to hide the top bar, set this property to true (can be a good choice in iframe mode)  

        :return: The hide_top_bar of this Styling.  
        :rtype: bool
        """
        return self._hide_top_bar

    @hide_top_bar.setter
    def hide_top_bar(self, hide_top_bar):
        """Sets the hide_top_bar of this Styling.

        If you want to hide the top bar, set this property to true (can be a good choice in iframe mode)  

        :param hide_top_bar: The hide_top_bar of this Styling.  
        :type: bool
        """

        self._hide_top_bar = hide_top_bar

    @property
    def background_color(self):
        """Gets the background_color of this Styling.  

        Override the application background color (use hexadecimal value)  

        :return: The background_color of this Styling.  
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this Styling.

        Override the application background color (use hexadecimal value)  

        :param background_color: The background_color of this Styling.  
        :type: str
        """

        self._background_color = background_color

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
        if not isinstance(other, Styling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
