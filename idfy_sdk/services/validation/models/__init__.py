# coding: utf-8

# flake8: noqa
"""
    Idfy.Validation

    In this API you can validate signatures from the following electronic IDs (e-ID)<br/><br/>  &bull; Norwegian BankId (SDO)<br/>  ## Last update [LastUpdate] ## Last update   Last build date for this endpoint: 12.03.2018  # noqa: E501

"""


from __future__ import absolute_import

# import models into model package
from idfy_sdk.services.validation.models.certificate import Certificate
from idfy_sdk.services.validation.models.parse_sdo_request import ParseSDORequest
from idfy_sdk.services.validation.models.parse_sdo_response import ParseSDOResponse
from idfy_sdk.services.validation.models.sdo_signers import SDOSigners
from idfy_sdk.services.validation.models.seal import Seal
from idfy_sdk.services.validation.models.signers import Signers
from idfy_sdk.services.validation.models.validate_sdo_request import ValidateSDORequest
from idfy_sdk.services.validation.models.validate_sdo_response import ValidateSDOResponse
from idfy_sdk.services.validation.models.validated_signers import ValidatedSigners
from idfy_sdk.services.validation.models.validation_error import ValidationError
from idfy_sdk.services.validation.models.x509_certificate import X509Certificate
