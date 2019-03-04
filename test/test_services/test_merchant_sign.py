import asyncio
import unittest
import unittest.mock

from test.base_test import BaseTest
from idfy_sdk.version import version

import idfy_sdk

class TestMerchantSign(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.merchant_sign_service = idfy_sdk.services.MerchantSignService()

    def test_create_merchant_signature(self):
        data = self.merchant_sign_service.create_merchant_signature(sign_request=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/merchant/signature'.format(self.base_url), auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_get_transaction(self):
        data = self.merchant_sign_service.get_transaction(transaction_id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/merchant/signature/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_list_transactions(self):
        data = self.merchant_sign_service.list_transactions()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/merchant/signature/list'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'oauthClientId': None, 'fromDate': None, 'to_date': None})
    #@unittest.skip("Mock server error")
    #def test_get_pades(self):
    #    data = self.merchant_sign_service.get_pades(signed_document_id="1")
#
    #    self.assertIsNotNone(data)
    #    #self.AssertEqual()
    #    self.mock_http.get.assert_called_once_with('{}/merchant/pades/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


class TestMerchantSignAsync(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.merchant_sign_service = idfy_sdk.services.MerchantSignService()

    def setUp(self):
        super().setUp()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()

    def test_create_merchant_signature_async(self):
        async def func():
            return await self.merchant_sign_service.create_merchant_signature(sign_request=self.params, threaded=True)
        data = self.loop.run_until_complete(func())

        
        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('{}/merchant/signature'.format(self.base_url), auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_get_transaction(self):
        async def func():
            return await self.merchant_sign_service.get_transaction(transaction_id="1", threaded=True)
        data = self.loop.run_until_complete(func())

        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('{}/merchant/signature/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_list_transactions(self):
        async def func():
            return await self.merchant_sign_service.list_transactions(threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('{}/merchant/signature/list'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'oauthClientId': None, 'fromDate': None, 'to_date': None})
    #@unittest.skip("Mock server error")
    #def test_get_pades(self):
    #    async def func():
    #        return await self.merchant_sign_service.get_pades(signed_document_id="1", threaded=True)
    #    data = self.loop.run_until_complete(func())
#
    #    
    #    self.assertIsNotNone(data)
    #    self.mock_http.get.assert_called_once_with('{}/merchant/pades/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
