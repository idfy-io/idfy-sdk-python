import asyncio
import functools
import sys
from typing import List, Dict

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk import urls as urls
from idfy_sdk.services.IdfyBaseService import IdfyBaseService
from idfy_sdk.services.signature import models as models

class SignatureService(IdfyBaseService):
    """Sign contracts, declarations, forms and other documents using digital signatures."""

    def __init__(self, client_id=None, client_secret=None, scopes=None):
        super().__init__(client_id=client_id, client_secret=client_secret, scopes=scopes)

    #Documents
    def get_document(self, documentId, threaded=False):
        base = config.BaseUrl
        url = base + urls.SignatureDocuments + '/' + documentId

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.CreateDocumentResponse))
        return self.Get(url, model=models.CreateDocumentResponse)

    def create_document(self, options: 'DocumentCreateOptions', threaded=False):
        url = config.BaseUrl + urls.SignatureDocuments

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.CreateDocumentResponse, data=options))
        return self.Post(url, model=models.CreateDocumentResponse, data=options)
    
    def update_document(self, document_id, options: 'DocumentUpdateOptions' = None, threaded=False):
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Patch, url, model=models.UpdateDocumentRequest, data=options))
        return self.Patch(url, model=models.UpdateDocumentRequest, data=options)
    
    def cancel_document(self, document_id, reason, threaded=False):
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/cancel'

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, params=reason))
        self.Post(url, params=reason)
    
    def get_document_status(self, document_id, threaded=False):
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/status'

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.Status))
        return self.Get(url, model=models.Status)
    
    def get_document_summary(self, document_id, threaded=False):
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/summary'

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.DocumentSummary))
        return self.Get(url, model=models.DocumentSummary)
    
    def list_document_summaries(
        self,
        external_id = None,
        signer_id = None,
        external_signer_id = None,
        from_date = None,
        to_date = None,
        last_updated = None,
        signed_date = None,
        name_of_signer = None,
        title = None,
        status = None,
        tags = None,
        offset = None,
        limit = None
        , threaded=False):

        params = {
            "externalId": external_id,
            "signerId": signer_id,
            "externalSignerId": external_signer_id,
            "fromDate": from_date,
            "toDate": to_date,
            "lastUpdated": last_updated,
            "signedDate": signed_date,
            "nameOfSigner": name_of_signer,
            "title": title,
            "status": status,
            "tags": tags,
            "offset": offset,
            "limit": limit
        }
        
        url = config.BaseUrl + urls.SignatureDocuments + '/summary'

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.CollectionWithPagingDocumentSummary, params=params))
        return self.Get(url, model=models.CollectionWithPagingDocumentSummary, params=params)
    
    #Signers
    def get_signer(self, document_id, signer_id, threaded=False):
        
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/signers/' + signer_id

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.SignerResponse))
        return self.Get(url, model=models.SignerResponse)
    
    def create_signer(self, document_id, signer_options: 'SignerWrapper', threaded=False):
        
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/signers'

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.SignerResponse, data=signer_options))
        return self.Post(url, model=models.SignerResponse, data=signer_options)
    
    def update_signer(self, document_id, signer_id, signer_options: 'SignerWrapper', threaded=False):
        
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/signers/' + signer_id

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Patch, url, model=models.SignerResponse, data=signer_options))
        return self.Patch(url, model=models.SignerResponse, data=signer_options)
    
    def delete_signer(self, document_id, signer_id, threaded=False):
        
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/signers/' + signer_id

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Delete, url))
        self.Delete(url)
    
    def list_signers(self, document_id, threaded=False):
        
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/signers/'

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=List[models.SignerResponse]))
        return self.Get(url, model=List[models.SignerResponse])

#Signature/status/ping?

    def get_attachment(self, document_id, attachment_id, threaded=False):
        
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/attachments/' + attachment_id

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.AttachmentResponse))
        return self.Get(url, model=models.AttachmentResponse)
    
    def create_attachment(self, document_id, data: 'AttachmentRequestWrapper', threaded=False):
        
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/attachments/'

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.AttachmentResponse, data=data))
        return self.Post(url, model=models.AttachmentResponse, data=data)
    
    def update_attachment(self, document_id, attachment_id, data: 'AttachmentOptions', threaded=False):
    
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/attachments/' + attachment_id
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Patch, url, model=models.AttachmentResponse, data=data))
        return self.Patch(url, model=models.AttachmentResponse, data=data)

    def delete_attachment(self, document_id, attachment_id, threaded=False): # Not "tested" yet.
    
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/attachments/' + attachment_id

        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Delete, url))
        return self.Delete(url)
    

    def list_attachments(self, document_id, threaded=False):
    
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/attachments'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=List[models.AttachmentListItem]))
        return self.Get(url, model=List[models.AttachmentListItem])
    
    def get_file(self, document_id, file_format, threaded=False):
    
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/files'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model='file', params=file_format))
        return self.Get(url, model='file', params=file_format)

    def get_file_for_signer(self, document_id, signer_id, file_format, threaded=False):
    
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/files/signers/' + signer_id
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model='file', params=file_format))
        return self.Get(url, model='file', params=file_format)
    
    def get_attachment_file(self, document_id, attachment_id, file_format, threaded=False):
    
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/files/attachments/' + attachment_id
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model='file', params=file_format))
        return self.Get(url, model='file', params=file_format)
    
    def get_attachment_file_for_signer(self, document_id, attachment_id, signer_id, file_format, threaded=False):
    
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/files/attachments/' + attachment_id + '/signers/' + signer_id
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model='file', params=file_format))
        return self.Get(url, model='file', params=file_format)
    
    def list_notifications(self, document_id, threaded=False):
    
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/notifications'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=List[models.NotificationLogItem]))
        return self.Get(url, model=List[models.NotificationLogItem])

    def send_reminders(self, document_id, manual_reminder: 'ManualReminder', threaded=False):
    
        url = config.BaseUrl + urls.SignatureDocuments + '/' + document_id + '/notifications/reminder'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.ManualReminder, data=manual_reminder))
        return self.Post(url, model=models.ManualReminder, data=manual_reminder)
    
    def list_themes(self, threaded=False):
    
        url = config.BaseUrl + urls.Signature + '/themes/list/themes'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=List[str]))
        return self.Get(url, model=List[str])
    
    def list_spinners(self, threaded=False):
    
        url = config.BaseUrl + urls.Signature + '/themes/list/spinners'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=List[str]))
        return self.Get(url, model=List[str])