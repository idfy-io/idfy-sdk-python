import asyncio 
import functools
import sys

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.services.IdfyBaseService import IdfyBaseService
from idfy_sdk import urls as urls
from idfy_sdk import models as models

class AdminService(IdfyBaseService):    #TODO: add comments to delimit the different sections
    def __init__(self, client_id: str=None, client_secret: str=None, scopes: list=None):
        super().__init__(client_id, client_secret, scopes)

    # Account
    def get_account(self, threaded=False):
    
        url = config.BaseUrl + urls.Account
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.Account))
        return self.Get(url, model=models.Account)
    

    def update_account(self, account_update_options, threaded=False):
    
        url = config.BaseUrl + urls.Account
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Put, url, model=models.Account, data=account_update_options))
        return self.Put(url, model=models.Account, data=account_update_options)
    
    def create_account(self, account_create_options: 'AccountCreateOpions', threaded=False):
    
        url = config.BaseUrl + urls.Account
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.Account, data=account_create_options))
        return self.Post(url, model=models.Account, data=account_create_options)
    
    def disable_account(self, threaded=False):
    
        url = config.BaseUrl + urls.Account + "/disable"
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url))
        return self.Post(url)
    
    def list_accounts(self,
        name=None,
        org_no=None,
        uni_customer_no=None,
        created_before=None,
        created_after=None,
        last_modified_before=None,
        last_modified_after=None,
        dealer_name=None,
        dealer_reference=None,
        tags=None,
        enable=None
        , threaded=False):

        params = {
            'name': name,
            'orgNo': org_no,
            'uniCustomerNo': uni_customer_no,
            'createdBefore': created_before,
            'createdAfter': created_after,
            'lastModifiedBefore': last_modified_before,
            'lastModifiedAfter': last_modified_after,
            'dealerName': dealer_name,
            'dealerReference': dealer_reference,
            'tags': tags,
            'enable': enable
        }
    
        url = config.BaseUrl + urls.Account + "/list"
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[AccountListItem]', params=params))
        return self.Get(url, model='list[AccountListItem]', params=params)
    
    def list_account_names(self, threaded=False):
    
        url = config.BaseUrl + urls.Account + '/list/names'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[AccountNameItem]'))
        return self.Get(url, model='list[AccountNameItem]')
    
    def get_dealer(self, dealer_id, threaded=False):
    
        url = config.BaseUrl + urls.Dealer + '/' + dealer_id
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.Dealer))
        return self.Get(url, model=models.Dealer)

    def update_dealer(self, dealer_id, dealer: 'Dealer', threaded=False):
    
        url = config.BaseUrl + urls.Dealer + '/' + dealer_id
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.Dealer, data=dealer))
        return self.Post(url, model=models.Dealer, data=dealer)

    def list_accounts_for_dealer(self, dealer_id, threaded=False):
    
        url = config.BaseUrl + urls.Dealer + '/' + dealer_id + '/accounts'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[AccountListItem]'))
        return self.Get(url, model='list[AccountListItem]')
            
    def list_transactions(self,
        year=None,
        month=None,
        get_as_csv=None
        , threaded=False):
        
        params = {
            'year': year,
            'month': month,
            'get_as_csv': get_as_csv
        }

        url = config.BaseUrl + urls.Admin + "/invoice"
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[Transaction]', params=params))
        return self.Get(url, model='list[Transaction]', params=params)
        
    def list_templates(self, threaded=False):
    
        url = config.BaseUrl + urls.Template
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[PdfTemplateListItem]'))
        return self.Get(url, model='list[PdfTemplateListItem]')
    
    def create_template(self, pdf_template_options: 'PdfTemplateOptions', threaded=False):
    
        url = config.BaseUrl + urls.Template
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.PdfTemplate, data=pdf_template_options))
        return self.Post(url, model=models.PdfTemplate, data=pdf_template_options)
    

    def get_template(self, id, threaded=False):
    
        url = config.BaseUrl + urls.Template + '/' + id
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.PdfTemplate))
        return self.Get(url, model=models.PdfTemplate)
    
    def update_template(self, id, pdf_template_options: 'PdfTemplateOptions', threaded=False):
    
        url = config.BaseUrl + urls.Template + '/' + id
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Put, url, model=models.PdfTemplate, data=pdf_template_options))
        return self.Put(url, model=models.PdfTemplate, data=pdf_template_options)
    
    def delete_template(self, id, threaded=False):
    
        url = config.BaseUrl + urls.Template + '/' + id
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Delete, url))
        return self.Delete(url)
    
    
    



# signature/status/ping?