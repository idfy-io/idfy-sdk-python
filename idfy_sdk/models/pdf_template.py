# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.create_pdf_template_details_page_html import CreatePdfTemplateDetailsPageHtml  
from idfy_sdk.models.create_pdf_template_labels import CreatePdfTemplateLabels  
from idfy_sdk.models.create_pdf_template_verified_template import CreatePdfTemplateVerifiedTemplate  


class PdfTemplate(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cover_page_setting': 'str',
        'add_list_of_signatures_on_last_page_of_existing_pdf': 'bool',
        'cover_page_html': 'str',
        'details_page_html': 'CreatePdfTemplateDetailsPageHtml',
        'verified_template': 'CreatePdfTemplateVerifiedTemplate',
        'labels': 'CreatePdfTemplateLabels',
        'include_logo': 'bool',
        'time_zone': 'str',
        'logo_source_url': 'str',
        'id': 'str',
        'name': 'str',
        'last_edited': 'datetime'
    }

    attribute_map = {
        'cover_page_setting': 'CoverPageSetting',
        'add_list_of_signatures_on_last_page_of_existing_pdf': 'AddListOfSignaturesOnLastPageOfExistingPDF',
        'cover_page_html': 'CoverPageHtml',
        'details_page_html': 'DetailsPageHtml',
        'verified_template': 'VerifiedTemplate',
        'labels': 'Labels',
        'include_logo': 'IncludeLogo',
        'time_zone': 'TimeZone',
        'logo_source_url': 'LogoSourceUrl',
        'id': 'Id',
        'name': 'Name',
        'last_edited': 'LastEdited'
    }

    def __init__(self, cover_page_setting=None, add_list_of_signatures_on_last_page_of_existing_pdf=None, cover_page_html=None, details_page_html=None, verified_template=None, labels=None, include_logo=None, time_zone=None, logo_source_url=None, id=None, name=None, last_edited=None):  
        """PdfTemplate"""  

        self._cover_page_setting = None
        self._add_list_of_signatures_on_last_page_of_existing_pdf = None
        self._cover_page_html = None
        self._details_page_html = None
        self._verified_template = None
        self._labels = None
        self._include_logo = None
        self._time_zone = None
        self._logo_source_url = None
        self._id = None
        self._name = None
        self._last_edited = None
        self.discriminator = None

        if cover_page_setting is not None:
            self.cover_page_setting = cover_page_setting
        if add_list_of_signatures_on_last_page_of_existing_pdf is not None:
            self.add_list_of_signatures_on_last_page_of_existing_pdf = add_list_of_signatures_on_last_page_of_existing_pdf
        if cover_page_html is not None:
            self.cover_page_html = cover_page_html
        if details_page_html is not None:
            self.details_page_html = details_page_html
        if verified_template is not None:
            self.verified_template = verified_template
        if labels is not None:
            self.labels = labels
        if include_logo is not None:
            self.include_logo = include_logo
        if time_zone is not None:
            self.time_zone = time_zone
        if logo_source_url is not None:
            self.logo_source_url = logo_source_url
        self.id = id
        self.name = name
        if last_edited is not None:
            self.last_edited = last_edited

    @property
    def cover_page_setting(self):
        """Gets the cover_page_setting of this PdfTemplate.  

        Coverpage is the page added to the document at the beginning or end that show a list of the signers. This settings hides that page or put it first or last. Default firstpage  

        :return: The cover_page_setting of this PdfTemplate.  
        :rtype: str
        """
        return self._cover_page_setting

    @cover_page_setting.setter
    def cover_page_setting(self, cover_page_setting):
        """Sets the cover_page_setting of this PdfTemplate.

        Coverpage is the page added to the document at the beginning or end that show a list of the signers. This settings hides that page or put it first or last. Default firstpage  

        :param cover_page_setting: The cover_page_setting of this PdfTemplate.  
        :type: str
        """
        allowed_values = ["FIRSTPAGE", "LASTPAGE", "HIDDEN"]  
        if cover_page_setting not in allowed_values:
            raise ValueError(
                "Invalid value for `cover_page_setting` ({0}), must be one of {1}"  
                .format(cover_page_setting, allowed_values)
            )

        self._cover_page_setting = cover_page_setting

    @property
    def add_list_of_signatures_on_last_page_of_existing_pdf(self):
        """Gets the add_list_of_signatures_on_last_page_of_existing_pdf of this PdfTemplate.  

        Coverpage is the page added to the document at the beginning or end that show a list of the signers. This settings hides that page or put it first or last. Default firstpage  

        :return: The add_list_of_signatures_on_last_page_of_existing_pdf of this PdfTemplate.  
        :rtype: bool
        """
        return self._add_list_of_signatures_on_last_page_of_existing_pdf

    @add_list_of_signatures_on_last_page_of_existing_pdf.setter
    def add_list_of_signatures_on_last_page_of_existing_pdf(self, add_list_of_signatures_on_last_page_of_existing_pdf):
        """Sets the add_list_of_signatures_on_last_page_of_existing_pdf of this PdfTemplate.

        Coverpage is the page added to the document at the beginning or end that show a list of the signers. This settings hides that page or put it first or last. Default firstpage  

        :param add_list_of_signatures_on_last_page_of_existing_pdf: The add_list_of_signatures_on_last_page_of_existing_pdf of this PdfTemplate.  
        :type: bool
        """

        self._add_list_of_signatures_on_last_page_of_existing_pdf = add_list_of_signatures_on_last_page_of_existing_pdf

    @property
    def cover_page_html(self):
        """Gets the cover_page_html of this PdfTemplate.  

        The html template for the coverpage, if this is set it will override the default template. See our documentation on more info on how to make your own custom template.  

        :return: The cover_page_html of this PdfTemplate.  
        :rtype: str
        """
        return self._cover_page_html

    @cover_page_html.setter
    def cover_page_html(self, cover_page_html):
        """Sets the cover_page_html of this PdfTemplate.

        The html template for the coverpage, if this is set it will override the default template. See our documentation on more info on how to make your own custom template.  

        :param cover_page_html: The cover_page_html of this PdfTemplate.  
        :type: str
        """

        self._cover_page_html = cover_page_html

    @property
    def details_page_html(self):
        """Gets the details_page_html of this PdfTemplate.  


        :return: The details_page_html of this PdfTemplate.  
        :rtype: CreatePdfTemplateDetailsPageHtml
        """
        return self._details_page_html

    @details_page_html.setter
    def details_page_html(self, details_page_html):
        """Sets the details_page_html of this PdfTemplate.


        :param details_page_html: The details_page_html of this PdfTemplate.  
        :type: CreatePdfTemplateDetailsPageHtml
        """

        self._details_page_html = details_page_html

    @property
    def verified_template(self):
        """Gets the verified_template of this PdfTemplate.  


        :return: The verified_template of this PdfTemplate.  
        :rtype: CreatePdfTemplateVerifiedTemplate
        """
        return self._verified_template

    @verified_template.setter
    def verified_template(self, verified_template):
        """Sets the verified_template of this PdfTemplate.


        :param verified_template: The verified_template of this PdfTemplate.  
        :type: CreatePdfTemplateVerifiedTemplate
        """

        self._verified_template = verified_template

    @property
    def labels(self):
        """Gets the labels of this PdfTemplate.  


        :return: The labels of this PdfTemplate.  
        :rtype: CreatePdfTemplateLabels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this PdfTemplate.


        :param labels: The labels of this PdfTemplate.  
        :type: CreatePdfTemplateLabels
        """

        self._labels = labels

    @property
    def include_logo(self):
        """Gets the include_logo of this PdfTemplate.  

        Include your logo in the Pdf template  

        :return: The include_logo of this PdfTemplate.  
        :rtype: bool
        """
        return self._include_logo

    @include_logo.setter
    def include_logo(self, include_logo):
        """Sets the include_logo of this PdfTemplate.

        Include your logo in the Pdf template  

        :param include_logo: The include_logo of this PdfTemplate.  
        :type: bool
        """

        self._include_logo = include_logo

    @property
    def time_zone(self):
        """Gets the time_zone of this PdfTemplate.  

        The time zone that is used for displaying signing time in the PADES (See: https://support.microsoft.com/en-us/help/973627/microsoft-time-zone-index-values for valid values) Defaults to W. Europe Standard Time  

        :return: The time_zone of this PdfTemplate.  
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this PdfTemplate.

        The time zone that is used for displaying signing time in the PADES (See: https://support.microsoft.com/en-us/help/973627/microsoft-time-zone-index-values for valid values) Defaults to W. Europe Standard Time  

        :param time_zone: The time_zone of this PdfTemplate.  
        :type: str
        """

        self._time_zone = time_zone

    @property
    def logo_source_url(self):
        """Gets the logo_source_url of this PdfTemplate.  

        Url to the logo that you want to use in your template  

        :return: The logo_source_url of this PdfTemplate.  
        :rtype: str
        """
        return self._logo_source_url

    @logo_source_url.setter
    def logo_source_url(self, logo_source_url):
        """Sets the logo_source_url of this PdfTemplate.

        Url to the logo that you want to use in your template  

        :param logo_source_url: The logo_source_url of this PdfTemplate.  
        :type: str
        """

        self._logo_source_url = logo_source_url

    @property
    def id(self):
        """Gets the id of this PdfTemplate.  


        :return: The id of this PdfTemplate.  
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PdfTemplate.


        :param id: The id of this PdfTemplate.  
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  

        self._id = id

    @property
    def name(self):
        """Gets the name of this PdfTemplate.  

        The name of the Pdf template  

        :return: The name of this PdfTemplate.  
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PdfTemplate.

        The name of the Pdf template  

        :param name: The name of this PdfTemplate.  
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  

        self._name = name

    @property
    def last_edited(self):
        """Gets the last_edited of this PdfTemplate.  

        Timestamp when the template is last edited  

        :return: The last_edited of this PdfTemplate.  
        :rtype: datetime
        """
        return self._last_edited

    @last_edited.setter
    def last_edited(self, last_edited):
        """Sets the last_edited of this PdfTemplate.

        Timestamp when the template is last edited  

        :param last_edited: The last_edited of this PdfTemplate.  
        :type: datetime
        """

        self._last_edited = last_edited

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
        if not isinstance(other, PdfTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
