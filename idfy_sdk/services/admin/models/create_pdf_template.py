# coding: utf-8

"""
    Idfy.Admin

    In this API you can manage your account details, logo, styling or manage your openid / oauth api clients. If you are a dealer you can also manage the accounts registered to this dealer.   ## Last update   Last build date for this API: 14.01.2018  

"""


import pprint
import re
from typing import List, Dict
from datetime import datetime as datetime


from idfy_sdk.services.admin.models.create_pdf_template_details_page_html import CreatePdfTemplateDetailsPageHtml
from idfy_sdk.services.admin.models.create_pdf_template_labels import CreatePdfTemplateLabels
from idfy_sdk.services.admin.models.create_pdf_template_verified_template import CreatePdfTemplateVerifiedTemplate

class CreatePdfTemplate(object):
    """NOTE: This class is generated by Eivind.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': str,
        'cover_page_setting': str,
        'add_list_of_signatures_on_last_page_of_existing_pdf': bool,
        'cover_page_html': str,
        'details_page_html': CreatePdfTemplateDetailsPageHtml,
        'verified_template': CreatePdfTemplateVerifiedTemplate,
        'labels': CreatePdfTemplateLabels,
        'include_logo': bool
    }

    attribute_map = {
        'name': 'Name',
        'cover_page_setting': 'CoverPageSetting',
        'add_list_of_signatures_on_last_page_of_existing_pdf': 'AddListOfSignaturesOnLastPageOfExistingPDF',
        'cover_page_html': 'CoverPageHtml',
        'details_page_html': 'DetailsPageHtml',
        'verified_template': 'VerifiedTemplate',
        'labels': 'Labels',
        'include_logo': 'IncludeLogo'
    }

    def __init__(self, name=None, cover_page_setting=None, add_list_of_signatures_on_last_page_of_existing_pdf=None, cover_page_html=None, details_page_html=None, verified_template=None, labels=None, include_logo=None):

        self._name = None
        self._cover_page_setting = None
        self._add_list_of_signatures_on_last_page_of_existing_pdf = None
        self._cover_page_html = None
        self._details_page_html = None
        self._verified_template = None
        self._labels = None
        self._include_logo = None
        self.discriminator = None

        if name is not None:
            self.name = name
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

    @property
    def name(self):
        """Gets the name of this CreatePdfTemplate.

        The name of the Pdf template

        :return: The name of this CreatePdfTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePdfTemplate.

        The name of the Pdf template

        :param name: The name of this CreatePdfTemplate.
        :type: str
        """

        self._name = name

    @property
    def cover_page_setting(self):
        """Gets the cover_page_setting of this CreatePdfTemplate.

        Coverpage is the page added to the document at the beginning or end that show a list of the signers. This settings hides that page or put it first or last. Default firstpage

        :return: The cover_page_setting of this CreatePdfTemplate.
        :rtype: str
        """
        return self._cover_page_setting

    @cover_page_setting.setter
    def cover_page_setting(self, cover_page_setting):
        """Sets the cover_page_setting of this CreatePdfTemplate.

        Coverpage is the page added to the document at the beginning or end that show a list of the signers. This settings hides that page or put it first or last. Default firstpage

        :param cover_page_setting: The cover_page_setting of this CreatePdfTemplate.
        :type: str
        """

        self._cover_page_setting = cover_page_setting

    @property
    def add_list_of_signatures_on_last_page_of_existing_pdf(self):
        """Gets the add_list_of_signatures_on_last_page_of_existing_pdf of this CreatePdfTemplate.

        Adds a list of signer names on the last page of the PDF, only use this if you are sure that you have room for the signatures. Contact support for more information.

        :return: The add_list_of_signatures_on_last_page_of_existing_pdf of this CreatePdfTemplate.
        :rtype: bool
        """
        return self._add_list_of_signatures_on_last_page_of_existing_pdf

    @add_list_of_signatures_on_last_page_of_existing_pdf.setter
    def add_list_of_signatures_on_last_page_of_existing_pdf(self, add_list_of_signatures_on_last_page_of_existing_pdf):
        """Sets the add_list_of_signatures_on_last_page_of_existing_pdf of this CreatePdfTemplate.

        Adds a list of signer names on the last page of the PDF, only use this if you are sure that you have room for the signatures. Contact support for more information.

        :param add_list_of_signatures_on_last_page_of_existing_pdf: The add_list_of_signatures_on_last_page_of_existing_pdf of this CreatePdfTemplate.
        :type: bool
        """

        self._add_list_of_signatures_on_last_page_of_existing_pdf = add_list_of_signatures_on_last_page_of_existing_pdf

    @property
    def cover_page_html(self):
        """Gets the cover_page_html of this CreatePdfTemplate.

        The html template for the coverpage, if this is set it will override the default template. See our documentation on more info on how to make your own custom template.

        :return: The cover_page_html of this CreatePdfTemplate.
        :rtype: str
        """
        return self._cover_page_html

    @cover_page_html.setter
    def cover_page_html(self, cover_page_html):
        """Sets the cover_page_html of this CreatePdfTemplate.

        The html template for the coverpage, if this is set it will override the default template. See our documentation on more info on how to make your own custom template.

        :param cover_page_html: The cover_page_html of this CreatePdfTemplate.
        :type: str
        """

        self._cover_page_html = cover_page_html

    @property
    def details_page_html(self):
        """Gets the details_page_html of this CreatePdfTemplate.


        :return: The details_page_html of this CreatePdfTemplate.
        :rtype: CreatePdfTemplateDetailsPageHtml
        """
        return self._details_page_html

    @details_page_html.setter
    def details_page_html(self, details_page_html):
        """Sets the details_page_html of this CreatePdfTemplate.


        :param details_page_html: The details_page_html of this CreatePdfTemplate.
        :type: CreatePdfTemplateDetailsPageHtml
        """

        self._details_page_html = details_page_html

    @property
    def verified_template(self):
        """Gets the verified_template of this CreatePdfTemplate.


        :return: The verified_template of this CreatePdfTemplate.
        :rtype: CreatePdfTemplateVerifiedTemplate
        """
        return self._verified_template

    @verified_template.setter
    def verified_template(self, verified_template):
        """Sets the verified_template of this CreatePdfTemplate.


        :param verified_template: The verified_template of this CreatePdfTemplate.
        :type: CreatePdfTemplateVerifiedTemplate
        """

        self._verified_template = verified_template

    @property
    def labels(self):
        """Gets the labels of this CreatePdfTemplate.


        :return: The labels of this CreatePdfTemplate.
        :rtype: CreatePdfTemplateLabels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreatePdfTemplate.


        :param labels: The labels of this CreatePdfTemplate.
        :type: CreatePdfTemplateLabels
        """

        self._labels = labels

    @property
    def include_logo(self):
        """Gets the include_logo of this CreatePdfTemplate.

        Include your logo in the Pdf template

        :return: The include_logo of this CreatePdfTemplate.
        :rtype: bool
        """
        return self._include_logo

    @include_logo.setter
    def include_logo(self, include_logo):
        """Sets the include_logo of this CreatePdfTemplate.

        Include your logo in the Pdf template

        :param include_logo: The include_logo of this CreatePdfTemplate.
        :type: bool
        """

        self._include_logo = include_logo

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
        if not isinstance(other, CreatePdfTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
