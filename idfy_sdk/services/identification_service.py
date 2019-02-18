import asyncio
import functools

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.services.IdfyBaseService import IdfyBaseService
from idfy_sdk import urls as urls
from idfy_sdk import models as models

class IdentificationService(IdfyBaseService):
    def __init__(self, client_id: str=None, client_secret: str=None, scopes: list=None):
        super().__init__(client_id, client_secret, scopes)

    def get_session(self, request_id, meta_data=False, threaded=False):

        params = {
            'requestId': request_id,
            'metaData': meta_data
        }

        url = config.BaseUrl + urls.IdentificationSession

        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, models.IdentificationResponse, params = params))
        return self.Get(url, models.IdentificationResponse, params = params)

    def create_session(self, create_identification_request, threaded=False):

        url = config.BaseUrl + urls.IdentificationSession

        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.CreateIdentificationResponse, data=create_identification_request))
        return self.Post(url, model=models.CreateIdentificationResponse, data=create_identification_request)
    
    def get_session_status(self, request_id, threaded=False):

        params = {'requestId': request_id}
        
        url = config.BaseUrl + urls.IdentificationSessionStatus

        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, models.IdentificationCompleteResponse, params=params))
        return self.Get(url, models.IdentificationCompleteResponse, params=params)
    
    def invalidate_session(self, request_id, threaded=False):
        
        url = config.BaseUrl + urls.InvalidateSession

        data = {'RequestId': request_id}

        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Put, url, data=data))
        return self.Put(url, data=data)
    
    def get_log_entry(self, request_id, threaded=False):
        
        url = config.BaseUrl + urls.RetrieveLogEntry + '/' + request_id

        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.IdentificationLogItem))
        return self.Get(url, model=models.IdentificationLogItem)
    
    def list_log_entries(
        self,
        year,
        month = None,
        day = None,
        status = None,
        identity_provider_type = None,
        external_id = None,
        name = None,
        skip = None,
        page_size = None
        , threaded=False):

        params = {
            "month": month,
            "day": day,
            "status": status,
            "identityProviderType": identity_provider_type,
            "externalId": external_id,
            "name": name,
            "skip": skip,
            "pageSize": page_size
        }

        url = config.BaseUrl + urls.ListLogEntries + '/' + str(year)

        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.LogItemList, params=params))
        return self.Get(url, model=models.LogItemList, params=params)
    
    def create_bankId_mobile_session(self, request: 'CreateBankIdMobileRequest', threaded=False):
        url = config.BaseUrl + urls.CreateBankIdMobileSession

        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.CreateBankIDMobileResponse, data=request))
    
        return self.Post(url, model=models.CreateBankIDMobileResponse, data=request)