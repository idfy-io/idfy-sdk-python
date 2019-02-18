import asyncio
import functools

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk import urls as urls
from idfy_sdk.services.IdfyBaseService import IdfyBaseService
from idfy_sdk import models as models

class ValidationService(IdfyBaseService):
    def __init__(self, client_id: str=None, client_secret: str=None, scopes: list=None):
        super().__init__(client_id, client_secret, scopes)

    def validate_sdo(self, validate_sdo_request: 'ValidateSDORequest', threaded=False):
    
        url = config.BaseUrl + urls.ValidationBankid + '/validate'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.ValidateSDOResponse, data=validate_sdo_request))
        return self.Post(url, model=models.ValidateSDOResponse, data=validate_sdo_request)
    
    def parse_and_validate_sdo(self, parse_sdo_request: 'ParseSDORequest', threaded=False):
    
        url = config.BaseUrl + urls.ValidationBankid + '/parse'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.ParseSDOResponse, data=parse_sdo_request))
        return self.Post(url, model=models.ParseSDOResponse, data=parse_sdo_request)