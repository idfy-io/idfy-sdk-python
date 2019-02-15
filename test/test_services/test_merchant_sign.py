import asyncio
import functools

import idfy_sdk as python
import unittest
import unittest.mock

params = {'unit': 'test'}

@unittest.mock.patch('idfy_sdk.services.merchant_sign_service.MerchantSignService', autospec=True, wrap=python.MerchantSignService)
class TestMerchantSign(unittest.TestCase):
    def test_create_merchant_signature(self, mock_service):
    
        data = mock_service.create_merchant_signature(sign_request=params)
        
        self.assertIsNotNone(data)
        mock_service.create_merchant_signature.assert_called_once_with(sign_request=params)
    
    def test_get_transaction(self, mock_service):
    
        data = mock_service.get_transaction(transaction_id="1")
        
        self.assertIsNotNone(data)
        mock_service.get_transaction.assert_called_once_with(transaction_id="1")
    
    def test_list_transactions(self, mock_service):

        data = mock_service.list_transactions()
        
        self.assertIsNotNone(data)
        mock_service.list_transactions.assert_called_once_with()
    
    def test_get_pades(self, mock_service):
    
        data = mock_service.get_pades(signed_document_id="1")
        
        self.assertIsNotNone(data)
        mock_service.get_pades.assert_called_once_with(signed_document_id="1")

@unittest.mock.patch('idfy_sdk.services.merchant_sign_service.MerchantSignService', autospec=True, wrap=python.MerchantSignService)
class TestMerchantSignAsync(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()

    def test_create_merchant_signature_async(self, mock_service):
        async def func():
            return mock_service.create_merchant_signature(sign_request=params, threaded=True)
        data = self.loop.run_until_complete(func())

        
        self.assertIsNotNone(data)
        mock_service.create_merchant_signature.assert_called_once_with(sign_request=params, threaded=True)
    
    def test_get_transaction(self, mock_service):
        async def func():
            return mock_service.get_transaction(transaction_id="1", threaded=True)
        data = self.loop.run_until_complete(func())

        
        self.assertIsNotNone(data)
        mock_service.get_transaction.assert_called_once_with(transaction_id="1", threaded=True)
    
    def test_list_transactions(self, mock_service):
        async def func():
            return mock_service.list_transactions(threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        mock_service.list_transactions.assert_called_once_with(threaded=True)
    
    def test_get_pades(self, mock_service):
        async def func():
            return mock_service.get_pades(signed_document_id="1", threaded=True)
        data = self.loop.run_until_complete(func())

        
        self.assertIsNotNone(data)
        mock_service.get_pades.assert_called_once_with(signed_document_id="1", threaded=True)
