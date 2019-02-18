import asyncio
import functools

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.services.IdfyBaseService import IdfyBaseService
from idfy_sdk import urls as urls
from idfy_sdk import models as models

class MerchantSignService(IdfyBaseService):
    def __init__(self, client_id: str=None, client_secret: str=None, scopes: list=None):
        super().__init__(client_id, client_secret, scopes)

    def create_merchant_signature(self, sign_request: 'MerchantSignRequest', threaded=False):
    
        url = config.BaseUrl + urls.MerchantSignature
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.SignResponse, data=sign_request))
        return self.Post(url, model=models.SignResponse, data=sign_request)
    
    def get_transaction(self, transaction_id, threaded=False):
    
        url = config.BaseUrl + urls.MerchantSignature + '/' + transaction_id
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.MerchantSignTransaction))
        return self.Get(url, model=models.MerchantSignTransaction)
    
    def list_transactions(self, 
        oauth_client_id = None,
        from_date = None,
        to_date = None
        , threaded=False):

        params = {
            'oauthClientId': oauth_client_id,
            'fromDate': from_date,
            'to_date': to_date
        }
    
        url = config.BaseUrl + urls.MerchantSignature + '/list'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[MerchantSignTransaction]', params=params))
        return self.Get(url, model='list[MerchantSignTransaction]', params=params)
    
    def get_pades(self, signed_document_id, threaded=False):
    
        url = config.BaseUrl + urls.Merchant + '/pades/' + signed_document_id
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model='file'))
        return self.Get(url, model='file')
    

    