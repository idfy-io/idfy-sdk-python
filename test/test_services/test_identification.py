import idfy_sdk as python
from test.base_test import BaseTest

import asyncio
#import pdb
import unittest
import unittest.mock

"""
class TestIdentification(BaseTest):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        #self.service = SignatureService()    #Read the "Organizing test code" part of the unittest docs
        pass
    
    def test_get_session(self, mock_service):

        data = mock_service.get_session(request_id="1")
        
        self.assertIsNotNone(data)
        mock_service.get_session.assert_called_once_with(request_id="1")

    def test_create_session(self, mock_service):

        data = mock_service.create_session(create_identification_request=params)
        
        self.assertIsNotNone(data)
        mock_service.create_session.assert_called_once_with(create_identification_request=params)
    
    def test_get_session_status(self, mock_service):
        
        data = mock_service.get_session_status(request_id="1")
        
        self.assertIsNotNone(data)
        mock_service.get_session_status.assert_called_once_with(request_id="1")
    
    def test_invalidate_session(self, mock_service):
        
        data = mock_service.invalidate_session(request_id="1")
        
        self.assertIsNotNone(data)
        mock_service.invalidate_session.assert_called_once_with(request_id="1")
    
    def test_get_log_entry(self, mock_service):
        
        data = mock_service.get_log_entry(request_id="1")
        
        self.assertIsNotNone(data)
        mock_service.get_log_entry.assert_called_once_with(request_id="1")
    
    def test_list_log_entries(self, mock_service):

        data = mock_service.list_log_entries(year="1")
        
        self.assertIsNotNone(data)
        mock_service.list_log_entries.assert_called_once_with(year="1")
    
    def test_create_bankId_mobile_session(self, mock_service):
        
        data = mock_service.create_bankId_mobile_session(request="1")
        
        self.assertIsNotNone(data)
        mock_service.create_bankId_mobile_session.assert_called_once_with(request="1")


@unittest.mock.patch('idfy_sdk.services.identification_service.IdentificationService', autospec=True, wrap=python.IdentificationService)
class TestIdentificationAsync(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()
    
    def test_get_session_async(self, mock_service):
        async def func():
            return mock_service.get_session(request_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.get_session.assert_called_once_with(request_id="1", threaded=True)

    def test_create_session_async(self, mock_service):
        async def func():
            return mock_service.create_session(create_identification_request=params, threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        mock_service.create_session.assert_called_once_with(create_identification_request=params, threaded=True)
    
    def test_get_session_status_async(self, mock_service):
        async def func():
            return mock_service.get_session_status(request_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.get_session_status.assert_called_once_with(request_id="1", threaded=True)
    
    def test_invalidate_session_async(self, mock_service):
        async def func():
            return mock_service.invalidate_session(request_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.invalidate_session.assert_called_once_with(request_id="1", threaded=True)
    
    def test_get_log_entry_async(self, mock_service):
        async def func():
            return mock_service.get_log_entry(request_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.get_log_entry.assert_called_once_with(request_id="1", threaded=True)
    
    def test_list_log_entries_async(self, mock_service):
        async def func():
            return mock_service.list_log_entries(year="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.list_log_entries.assert_called_once_with(year="1", threaded=True)
    
    def test_create_bankId_mobile_session_async(self, mock_service):
        async def func():
            return mock_service.create_bankId_mobile_session(request="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.create_bankId_mobile_session.assert_called_once_with(request="1", threaded=True)
"""