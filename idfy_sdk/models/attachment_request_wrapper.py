# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class AttachmentRequestWrapper(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_name': 'str',
        'title': 'str',
        'data': 'str',
        'convert_to_pdf': 'bool',
        'signers': 'list[str]',
        'description': 'str',
        'type': 'str'
    }

    attribute_map = {
        'file_name': 'fileName',
        'title': 'title',
        'data': 'data',
        'convert_to_pdf': 'convertToPdf',
        'signers': 'signers',
        'description': 'description',
        'type': 'type'
    }

    def __init__(self, file_name=None, title=None, data=None, convert_to_pdf=None, signers=None, description=None, type=None):  
        """AttachmentRequestWrapper"""  

        self._file_name = None
        self._title = None
        self._data = None
        self._convert_to_pdf = None
        self._signers = None
        self._description = None
        self._type = None
        self.discriminator = None

        self.file_name = file_name
        self.title = title
        self.data = data
        if convert_to_pdf is not None:
            self.convert_to_pdf = convert_to_pdf
        if signers is not None:
            self.signers = signers
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type

    @property
    def file_name(self):
        """Gets the file_name of this AttachmentRequestWrapper.  

        Filename with file extension. <span style=\"color:red;\">We only support PDF for attachments, set `convertToPdf` to `true` if you have a convertible file type.</span>  

        :return: The file_name of this AttachmentRequestWrapper.  
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this AttachmentRequestWrapper.

        Filename with file extension. <span style=\"color:red;\">We only support PDF for attachments, set `convertToPdf` to `true` if you have a convertible file type.</span>  

        :param file_name: The file_name of this AttachmentRequestWrapper.  
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  

        self._file_name = file_name

    @property
    def title(self):
        """Gets the title of this AttachmentRequestWrapper.  

        The title of the attachment which will be presented to the user.  

        :return: The title of this AttachmentRequestWrapper.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AttachmentRequestWrapper.

        The title of the attachment which will be presented to the user.  

        :param title: The title of this AttachmentRequestWrapper.  
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  

        self._title = title

    @property
    def data(self):
        """Gets the data of this AttachmentRequestWrapper.  

        Base64-encoded attachment (UTF-8-encoded)  

        :return: The data of this AttachmentRequestWrapper.  
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AttachmentRequestWrapper.

        Base64-encoded attachment (UTF-8-encoded)  

        :param data: The data of this AttachmentRequestWrapper.  
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  

        self._data = data

    @property
    def convert_to_pdf(self):
        """Gets the convert_to_pdf of this AttachmentRequestWrapper.  

        Determines if the attachment should be converted to PDF. See our documentation for supported file types.  

        :return: The convert_to_pdf of this AttachmentRequestWrapper.  
        :rtype: bool
        """
        return self._convert_to_pdf

    @convert_to_pdf.setter
    def convert_to_pdf(self, convert_to_pdf):
        """Sets the convert_to_pdf of this AttachmentRequestWrapper.

        Determines if the attachment should be converted to PDF. See our documentation for supported file types.  

        :param convert_to_pdf: The convert_to_pdf of this AttachmentRequestWrapper.  
        :type: bool
        """

        self._convert_to_pdf = convert_to_pdf

    @property
    def signers(self):
        """Gets the signers of this AttachmentRequestWrapper.  

        An optional list of signers that should be able to see / sign the attachment.  

        :return: The signers of this AttachmentRequestWrapper.  
        :rtype: list[str]
        """
        return self._signers

    @signers.setter
    def signers(self, signers):
        """Sets the signers of this AttachmentRequestWrapper.

        An optional list of signers that should be able to see / sign the attachment.  

        :param signers: The signers of this AttachmentRequestWrapper.  
        :type: list[str]
        """

        self._signers = signers

    @property
    def description(self):
        """Gets the description of this AttachmentRequestWrapper.  

        An optional description of the attachment.  

        :return: The description of this AttachmentRequestWrapper.  
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AttachmentRequestWrapper.

        An optional description of the attachment.  

        :param description: The description of this AttachmentRequestWrapper.  
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this AttachmentRequestWrapper.  

        The type of attachment. Choose between the following:  * <b>show_accept:</b> The signer will see the attachment before signing the main document (is default now)  * <b>read_accept:</b> The signer have to see the entire document before they can continue,   * <b>sign:</b> The signer has to sign the attachment (extra cost per signature)  

        :return: The type of this AttachmentRequestWrapper.  
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AttachmentRequestWrapper.

        The type of attachment. Choose between the following:  * <b>show_accept:</b> The signer will see the attachment before signing the main document (is default now)  * <b>read_accept:</b> The signer have to see the entire document before they can continue,   * <b>sign:</b> The signer has to sign the attachment (extra cost per signature)  

        :param type: The type of this AttachmentRequestWrapper.  
        :type: str
        """
        allowed_values = ["show_accept", "read_accept", "sign"]  
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, AttachmentRequestWrapper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
