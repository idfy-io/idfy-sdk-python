import asyncio
import functools
import sys
from typing import List, Dict

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk import urls as urls
from idfy_sdk.services.IdfyBaseService import IdfyBaseService
from idfy_sdk.services.notification import models as models

class NotificationService(IdfyBaseService):
    """Manage events that are raised when something happens in your account."""
    
    def __init__(self, client_id: str=None, client_secret: str=None, scopes: list=None):
        super().__init__(client_id, client_secret, scopes)

    #Events
    def list_unhandled_events(self, event_type=None, tags=None, threaded=False):

        params = {
            'eventType': event_type,
            'tags': tags
        }
    
        url = config.BaseUrl + urls.Notification + '/events'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=List[models.EventDto], params=params))
        return self.Get(url, model=List[models.EventDto], params=params)
    
    def handle_event(self, event_id, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/events/' + event_id + '/handle'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url))
        return self.Post(url)
    
    def handle_multiple_events(self, event_ids, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/events/handle'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, data=event_ids))
        return self.Post(url, data=event_ids)
    
    def peek_events(self, event_type=None, tags=None, threaded=False):

        params = {
            'eventType': event_type,
            'tags': tags
        }
    
        url = config.BaseUrl + urls.Notification + '/events/peek'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=List[models.EventDto], params=params))
        return self.Get(url, model=List[models.EventDto], params=params)
    
    def clear_events(self, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/events/clear'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url))
        return self.Post(url)

    def list_event_types(self, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/events/types'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=List[models.EventTypeInfo]))
        return self.Get(url, model=List[models.EventTypeInfo])
    
    def mock_event(self, mock_event_request: 'MockEventRequest', threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/events/mock'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.EventDto, data=mock_event_request))
        return self.Post(url, model=models.EventDto, data=mock_event_request)
    
    def get_webhook(self, id, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks/' + id
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.WebhookDto))
        return self.Get(url, model=models.WebhookDto)
    
    def delete_webhook(self, id, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks/' + str(id)
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Delete, url))
        return self.Delete(url)
    
    def update_webhook(self, id, webhook_update_options: 'WebhookUpdateOptions', threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks/' + str(id)
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Patch, url, model=models.WebhookDto, data=webhook_update_options))
        return self.Patch(url, model=models.WebhookDto, data=webhook_update_options)
    
    def list_webhooks(self, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=List[models.WebhookDto]))
        return self.Get(url, model=List[models.WebhookDto])

    def create_webhook(self, webhook_create_options: 'WebhookCreateOptions', threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.WebhookCreateDto, data=webhook_create_options))
        return self.Post(url, model=models.WebhookCreateDto, data=webhook_create_options)
    
    def ping_webhook(self, id, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks/' + id + '/ping'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Post, url))
        return self.Post(url)
    
    def list_webhook_deliveries(self, id, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks/' + id + '/deliveries'
    
        if threaded:
            if sys.version_info >= (3, 7):
                loop = asyncio.get_running_loop()
            else:
                loop = asyncio.get_event_loop()

            return loop.run_in_executor(None, functools.partial(self.Get, url, model=List[models.WebhookDeliveryDto]))
        return self.Get(url, model=List[models.WebhookDeliveryDto])
    
    