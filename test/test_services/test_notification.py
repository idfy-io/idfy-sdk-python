import asyncio
import functools

import idfy_sdk as python
import unittest
import unittest.mock
"""
@unittest.mock.patch('idfy_sdk.services.notification_service.NotificationService', autospec=True, wrap=python.NotificationService)
class TestNotification(unittest.TestCase):
    def test_list_unhandled_events(self, mock_service):

        data = mock_service.list_unhandled_events()
        
        self.assertIsNotNone(data)
        mock_service.list_unhandled_events.assert_called_once_with()
    
    def test_handle_event(self, mock_service):
    
        data = mock_service.handle_event(event_id="1")
        
        self.assertIsNotNone(data)
        mock_service.handle_event.assert_called_once_with(event_id="1")
    
    def test_handle_multiple_events(self, mock_service):
    
        data = mock_service.handle_multiple_events(event_ids="1")
        
        self.assertIsNotNone(data)
        mock_service.handle_multiple_events.assert_called_once_with(event_ids="1")
    
    def test_peek_events(self, mock_service):

        data = mock_service.peek_events()
        
        self.assertIsNotNone(data)
        mock_service.peek_events.assert_called_once_with()
    
    def test_clear_events(self, mock_service):
    
        data = mock_service.clear_events()
        
        self.assertIsNotNone(data)
        mock_service.clear_events.assert_called_once_with()

    def test_list_event_types(self, mock_service):
    
        data = mock_service.list_event_types()
        
        self.assertIsNotNone(data)
        mock_service.list_event_types.assert_called_once_with()
    
    def test_mock_event(self, mock_service):
    
        data = mock_service.mock_event(mock_event_request=params)
        
        self.assertIsNotNone(data)
        mock_service.mock_event.assert_called_once_with(mock_event_request=params)
    
    def test_get_webhook(self, mock_service):
    
        data = mock_service.get_webhook(id="1")
        
        self.assertIsNotNone(data)
        mock_service.get_webhook.assert_called_once_with(id="1")
    
    def test_delete_webhook(self, mock_service):
    
        data = mock_service.delete_webhook(id="1")
        
        self.assertIsNotNone(data)
        mock_service.delete_webhook.assert_called_once_with(id="1")
    
    def test_update_webhook(self, mock_service):
    
        data = mock_service.update_webhook(id="1", webhook_update_options=params)
        
        self.assertIsNotNone(data)
        mock_service.update_webhook.assert_called_once_with(id="1", webhook_update_options=params)
    
    def test_list_webhooks(self, mock_service):
    
        data = mock_service.list_webhooks()
        
        self.assertIsNotNone(data)
        mock_service.list_webhooks.assert_called_once_with()

    def test_create_webhook(self, mock_service):
    
        data = mock_service.create_webhook(webhook_create_options=params)
        
        self.assertIsNotNone(data)
        mock_service.create_webhook.assert_called_once_with(webhook_create_options=params)
    
    def test_ping_webhook(self, mock_service):
    
        data = mock_service.ping_webhook(id="1")
        
        self.assertIsNotNone(data)
        mock_service.ping_webhook.assert_called_once_with(id="1")
    
    def test_list_webhook_deliveries(self, mock_service):
    
        data = mock_service.list_webhook_deliveries(id="1")
        
        self.assertIsNotNone(data)
        mock_service.list_webhook_deliveries.assert_called_once_with(id="1")

@unittest.mock.patch('idfy_sdk.services.notification_service.NotificationService', autospec=True, wrap=python.NotificationService)
class TestNotificationAsync(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()

    def test_list_unhandled_events_async_async(self, mock_service):
        async def func():
            return mock_service.list_unhandled_events( threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.list_unhandled_events.assert_called_once_with(threaded=True)
    
    def test_handle_event_async(self, mock_service):
        async def func():
            return mock_service.handle_event(event_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.handle_event.assert_called_once_with(event_id="1", threaded=True)
    
    def test_handle_multiple_events_async(self, mock_service):
        async def func():
            return mock_service.handle_multiple_events(event_ids="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.handle_multiple_events.assert_called_once_with(event_ids="1", threaded=True)
    
    def test_peek_events_async(self, mock_service):
        async def func():
            return mock_service.peek_events(threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.peek_events.assert_called_once_with(threaded=True)
    
    def test_clear_events_async(self, mock_service):
        async def func():
            return mock_service.clear_events(threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.clear_events.assert_called_once_with(threaded=True)

    def test_list_event_types_async(self, mock_service):
        async def func():
            return mock_service.list_event_types(threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.list_event_types.assert_called_once_with(threaded=True)
    
    def test_mock_event_async(self, mock_service):
        async def func():
            return mock_service.mock_event(mock_event_request=params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.mock_event.assert_called_once_with(mock_event_request=params, threaded=True)
    
    def test_get_webhook_async(self, mock_service):
        async def func():
            return mock_service.get_webhook(id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.get_webhook.assert_called_once_with(id="1", threaded=True)
    
    def test_delete_webhook_async(self, mock_service):
        async def func():
            return mock_service.delete_webhook(id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.delete_webhook.assert_called_once_with(id="1", threaded=True)
    
    def test_update_webhook_async(self, mock_service):
        async def func():
            return mock_service.update_webhook(id="1", webhook_update_options=params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.update_webhook.assert_called_once_with(id="1", webhook_update_options=params, threaded=True)
    
    def test_list_webhooks_async(self, mock_service):
        async def func():
            return mock_service.list_webhooks(threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.list_webhooks.assert_called_once_with(threaded=True)

    def test_create_webhook_async(self, mock_service):
        async def func():
            return mock_service.create_webhook(webhook_create_options=params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.create_webhook.assert_called_once_with(webhook_create_options=params, threaded=True)
    
    def test_ping_webhook_async(self, mock_service):
        async def func():
            return mock_service.ping_webhook(id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.ping_webhook.assert_called_once_with(id="1", threaded=True)
    
    def test_list_webhook_deliveries_async(self, mock_service):
        async def func():
            return mock_service.list_webhook_deliveries(id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.list_webhook_deliveries.assert_called_once_with(id="1", threaded=True)
"""