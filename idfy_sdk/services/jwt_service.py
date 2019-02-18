import asyncio
import functools

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.services.IdfyBaseService import IdfyBaseService
from idfy_sdk import urls as urls
from idfy_sdk import models as models

class JwtService(IdfyBaseService):
    def __init__(self, client_id: str=None, client_secret: str=None, scopes: list=None):
        super().__init__(client_id, client_secret, scopes)

    def validate(self, jwt_validation_request: 'JwtValidationRequest', threaded=False):
    
        url = config.BaseUrl + urls.Jwt + '/validate'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.JwtValidationResponse, data=jwt_validation_request))
        return self.Post(url, model=models.JwtValidationResponse, data=jwt_validation_request)
    
    