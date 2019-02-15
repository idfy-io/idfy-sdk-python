# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.packaging import Packaging  


class DataToSign(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'base64_content': 'str',
        'base64_content_style_sheet': 'str',
        'file_name': 'str',
        'convert_to_pdf': 'bool',
        'packaging': 'Packaging'
    }

    attribute_map = {
        'base64_content': 'base64Content',
        'base64_content_style_sheet': 'base64ContentStyleSheet',
        'file_name': 'fileName',
        'convert_to_pdf': 'convertToPDF',
        'packaging': 'packaging'
    }

    def __init__(self, base64_content=None, base64_content_style_sheet=None, file_name=None, convert_to_pdf=None, packaging=None):  
        """DataToSign"""  

        self._base64_content = None
        self._base64_content_style_sheet = None
        self._file_name = None
        self._convert_to_pdf = None
        self._packaging = None
        self.discriminator = None

        if base64_content is not None:
            self.base64_content = base64_content
        if base64_content_style_sheet is not None:
            self.base64_content_style_sheet = base64_content_style_sheet
        self.file_name = file_name
        if convert_to_pdf is not None:
            self.convert_to_pdf = convert_to_pdf
        if packaging is not None:
            self.packaging = packaging

    @property
    def base64_content(self):
        """Gets the base64_content of this DataToSign.  

        Base64-encoded string of the document, UTF-8-encoded.  

        :return: The base64_content of this DataToSign.  
        :rtype: str
        """
        return self._base64_content

    @base64_content.setter
    def base64_content(self, base64_content):
        """Sets the base64_content of this DataToSign.

        Base64-encoded string of the document, UTF-8-encoded.  

        :param base64_content: The base64_content of this DataToSign.  
        :type: str
        """
        #if base64_content is None:
        #    raise ValueError("Invalid value for `base64_content`, must not be `None`")  

        self._base64_content = base64_content

    @property
    def base64_content_style_sheet(self):
        """Gets the base64_content_style_sheet of this DataToSign.  

        Stylesheet to be included if you are uploading XML.  

        :return: The base64_content_style_sheet of this DataToSign.  
        :rtype: str
        """
        return self._base64_content_style_sheet

    @base64_content_style_sheet.setter
    def base64_content_style_sheet(self, base64_content_style_sheet):
        """Sets the base64_content_style_sheet of this DataToSign.

        Stylesheet to be included if you are uploading XML.  

        :param base64_content_style_sheet: The base64_content_style_sheet of this DataToSign.  
        :type: str
        """

        self._base64_content_style_sheet = base64_content_style_sheet

    @property
    def file_name(self):
        """Gets the file_name of this DataToSign.  

        The document file name. Must include a valid file extension (.pdf, .xml, .txt, .doc, .docx, .rtf, .ott, odt).  

        :return: The file_name of this DataToSign.  
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this DataToSign.

        The document file name. Must include a valid file extension (.pdf, .xml, .txt, .doc, .docx, .rtf, .ott, odt).  

        :param file_name: The file_name of this DataToSign.  
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  
        if file_name is not None and len(file_name) > 100:
            raise ValueError("Invalid value for `file_name`, length must be less than or equal to `100`")  
        if file_name is not None and len(file_name) < 3:
            raise ValueError("Invalid value for `file_name`, length must be greater than or equal to `3`")  

        self._file_name = file_name

    @property
    def convert_to_pdf(self):
        """Gets the convert_to_pdf of this DataToSign.  

        Determines if the document should be converted to PDF. Supported formats are word documents, rich text format, and OpenOffice (.doc, .docx, .rtf, .odt, .ott).  Remark: When using this, the converted document (and not the original) is the one that will be signed.  

        :return: The convert_to_pdf of this DataToSign.  
        :rtype: bool
        """
        return self._convert_to_pdf

    @convert_to_pdf.setter
    def convert_to_pdf(self, convert_to_pdf):
        """Sets the convert_to_pdf of this DataToSign.

        Determines if the document should be converted to PDF. Supported formats are word documents, rich text format, and OpenOffice (.doc, .docx, .rtf, .odt, .ott).  Remark: When using this, the converted document (and not the original) is the one that will be signed.  

        :param convert_to_pdf: The convert_to_pdf of this DataToSign.  
        :type: bool
        """

        self._convert_to_pdf = convert_to_pdf

    @property
    def packaging(self):
        """Gets the packaging of this DataToSign.  


        :return: The packaging of this DataToSign.  
        :rtype: Packaging
        """
        return self._packaging

    @packaging.setter
    def packaging(self, packaging):
        """Sets the packaging of this DataToSign.


        :param packaging: The packaging of this DataToSign.  
        :type: Packaging
        """

        self._packaging = packaging

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
        if not isinstance(other, DataToSign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
