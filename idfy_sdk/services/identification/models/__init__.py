# coding: utf-8

# flake8: noqa
"""
    Idfy Identification

    This endpoint enables authentication/identification through multiple identity providers such as Norwegian BankID, Swedish BankID and NemID. ## Last update   Last build date for this endpoint: 02.04.2019  # noqa: E501

"""


from __future__ import absolute_import

# import models into model package
from idfy_sdk.services.identification.models.create_bank_id_mobile_request import CreateBankIDMobileRequest
from idfy_sdk.services.identification.models.create_bank_id_mobile_response import CreateBankIDMobileResponse
from idfy_sdk.services.identification.models.create_identification_request import CreateIdentificationRequest
from idfy_sdk.services.identification.models.create_identification_response import CreateIdentificationResponse
from idfy_sdk.services.identification.models.environment_info import EnvironmentInfo
from idfy_sdk.services.identification.models.error import Error
from idfy_sdk.services.identification.models.i_frame_settings import IFrameSettings
from idfy_sdk.services.identification.models.identification_complete_response import IdentificationCompleteResponse
from idfy_sdk.services.identification.models.identification_log_item import IdentificationLogItem
from idfy_sdk.services.identification.models.identification_response import IdentificationResponse
from idfy_sdk.services.identification.models.invalidate_identification_request import InvalidateIdentificationRequest
from idfy_sdk.services.identification.models.list_result_identification_log_item import ListResultIdentificationLogItem
from idfy_sdk.services.identification.models.return_urls import ReturnUrls
