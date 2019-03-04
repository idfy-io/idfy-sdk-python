import asyncio
import unittest
import unittest.mock

from test.base_test import BaseTest
from idfy_sdk.version import version

import idfy_sdk

class TestNotification(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.notification_service = idfy_sdk.services.NotificationService()

    def test_list_unhandled_events(self):
        data = self.notification_service.list_unhandled_events()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/notification/events'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'eventType': None, 'tags': None})


    def test_handle_event(self):
        data = self.notification_service.handle_event(event_id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/notification/events/1/handle'.format(self.base_url), auth=None, data='null', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_handle_multiple_events(self):
        data = self.notification_service.handle_multiple_events(event_ids="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/notification/events/handle'.format(self.base_url), auth=None, data='"1"', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_peek_events(self):
        data = self.notification_service.peek_events()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/notification/events/peek'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'eventType': None, 'tags': None})


    def test_clear_events(self):
        data = self.notification_service.clear_events()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/notification/events/clear'.format(self.base_url), auth=None, data='null', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_list_event_types(self):
        data = self.notification_service.list_event_types()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/notification/events/types'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_mock_event(self):
        data = self.notification_service.mock_event(mock_event_request=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/notification/events/mock'.format(self.base_url), auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_get_webhook(self):
        data = self.notification_service.get_webhook(id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/notification/webhooks/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_delete_webhook(self):
        data = self.notification_service.delete_webhook(id="1")

        self.assertIsNone(data)
        #self.AssertEqual()
        self.mock_http.delete.assert_called_once_with('{}/notification/webhooks/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})


    def test_update_webhook(self):
        data = self.notification_service.update_webhook(id="1", webhook_update_options=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.patch.assert_called_once_with('{}/notification/webhooks/1'.format(self.base_url), data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})


    def test_list_webhooks(self):
        data = self.notification_service.list_webhooks()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/notification/webhooks'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_create_webhook(self):
        data = self.notification_service.create_webhook(webhook_create_options=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/notification/webhooks'.format(self.base_url), auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_ping_webhook(self):
        data = self.notification_service.ping_webhook(id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/notification/webhooks/1/ping'.format(self.base_url), auth=None, data='null', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_list_webhook_deliveries(self):
        data = self.notification_service.list_webhook_deliveries(id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/notification/webhooks/1/deliveries'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

class TestNotificationAsync(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.notification_service = idfy_sdk.services.NotificationService()

    def setUp(self):
        super().setUp()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()

    def test_list_unhandled_events_async_async(self):
        async def func():
            return await self.notification_service.list_unhandled_events( threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('{}/notification/events'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'eventType': None, 'tags': None})
    
    def test_handle_event_async(self):
        async def func():
            return await self.notification_service.handle_event(event_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('{}/notification/events/1/handle'.format(self.base_url), auth=None, data='null', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_handle_multiple_events_async(self):
        async def func():
            return await self.notification_service.handle_multiple_events(event_ids="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('{}/notification/events/handle'.format(self.base_url), auth=None, data='"1"', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_peek_events_async(self):
        async def func():
            return await self.notification_service.peek_events(threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('{}/notification/events/peek'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'eventType': None, 'tags': None})
    
    def test_clear_events_async(self):
        async def func():
            return await self.notification_service.clear_events(threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('{}/notification/events/clear'.format(self.base_url), auth=None, data='null', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_list_event_types_async(self):
        async def func():
            return await self.notification_service.list_event_types(threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('{}/notification/events/types'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_mock_event_async(self):
        async def func():
            return await self.notification_service.mock_event(mock_event_request=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('{}/notification/events/mock'.format(self.base_url), auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_get_webhook_async(self):
        async def func():
            return await self.notification_service.get_webhook(id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('{}/notification/webhooks/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_delete_webhook_async(self):
        async def func():
            return await self.notification_service.delete_webhook(id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNone(data)
        self.mock_http.delete.assert_called_once_with('{}/notification/webhooks/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
    
    def test_update_webhook_async(self):
        async def func():
            return await self.notification_service.update_webhook(id="1", webhook_update_options=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.patch.assert_called_once_with('{}/notification/webhooks/1'.format(self.base_url), data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
    
    def test_list_webhooks_async(self):
        async def func():
            return await self.notification_service.list_webhooks(threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('{}/notification/webhooks'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_create_webhook_async(self):
        async def func():
            return await self.notification_service.create_webhook(webhook_create_options=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('{}/notification/webhooks'.format(self.base_url), auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_ping_webhook_async(self):
        async def func():
            return await self.notification_service.ping_webhook(id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('{}/notification/webhooks/1/ping'.format(self.base_url), auth=None, data='null', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_list_webhook_deliveries_async(self):
        async def func():
            return await self.notification_service.list_webhook_deliveries(id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('{}/notification/webhooks/1/deliveries'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
