import asyncio
import functools
import sys
from typing import List, Dict

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.services.IdfyBaseService import IdfyBaseService
from idfy_sdk import urls as urls
from idfy_sdk.services.jwt import models as models

class JwtService(IdfyBaseService):
    """Validate JSON Web Tokens from Idfy."""
    def __init__(self, client_id: str=None, client_secret: str=None, scopes: list=None):
        super().__init__(client_id, client_secret, scopes)

    def validate(self, jwt_validation_request: 'ValidateJwtDto', threaded=False):
    
        url = config.BaseUrl + urls.Jwt + '/validate'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.JwtValidationResultDto, data=jwt_validation_request))
        return self.Post(url, model=models.JwtValidationResultDto, data=jwt_validation_request)
    
    