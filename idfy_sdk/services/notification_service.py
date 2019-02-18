import asyncio
import functools

from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk import urls as urls
from idfy_sdk.services.IdfyBaseService import IdfyBaseService
from idfy_sdk import models as models

class NotificationService(IdfyBaseService):
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
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[event]', params=params))
        return self.Get(url, model='list[event]', params=params)
    
    def handle_event(self, event_id, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/events/' + event_id + '/handle'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url))
        return self.Post(url)
    
    def handle_multiple_events(self, event_ids, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/events/handle'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url, data=event_ids))
        return self.Post(url, data=event_ids)
    
    def peek_events(self, event_type=None, tags=None, threaded=False):

        params = {
            'eventType': event_type,
            'tags': tags
        }
    
        url = config.BaseUrl + urls.Notification + '/events/peek'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[Event]', params=params))
        return self.Get(url, model='list[Event]', params=params)
    
    def clear_events(self, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/events/clear'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url))
        return self.Post(url)

    def list_event_types(self, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/events/types'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[EventTypeInfo]'))
        return self.Get(url, model='list[EventTypeInfo]')
    
    def mock_event(self, mock_event_request: 'MockEventRequest', threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/events/mock'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.Event, data=mock_event_request))
        return self.Post(url, model=models.Event, data=mock_event_request)
    
    def get_webhook(self, id, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks/' + id
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model=models.Webhook))
        return self.Get(url, model=models.Webhook)
    
    def delete_webhook(self, id, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks/' + str(id)
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Delete, url))
        return self.Delete(url)
    
    def update_webhook(self, id, webhook_update_options: 'WebhookUpdateOptions', threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks/' + str(id)
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Patch, url, model=models.Webhook, data=webhook_update_options))
        return self.Patch(url, model=models.Webhook, data=webhook_update_options)
    
    def list_webhooks(self, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[Webhook]'))
        return self.Get(url, model='list[Webhook]')

    def create_webhook(self, webhook_create_options: 'WebhookCreateOptions', threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url, model=models.Webhook, data=webhook_create_options))
        return self.Post(url, model=models.Webhook, data=webhook_create_options)
    
    def ping_webhook(self, id, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks/' + id + '/ping'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Post, url))
        return self.Post(url)
    
    def list_webhook_deliveries(self, id, threaded=False):
    
        url = config.BaseUrl + urls.Notification + '/webhooks/' + id + '/deliveries'
    
        if threaded:
            loop = asyncio.get_running_loop()
            return loop.run_in_executor(None, functools.partial(self.Get, url, model='list[WebhookDelivery]'))
        return self.Get(url, model='list[WebhookDelivery]')
    
    