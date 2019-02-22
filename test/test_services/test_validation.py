import asyncio
import unittest
import unittest.mock

from test.base_test import BaseTest
from idfy_sdk.version import version

import idfy_sdk

class TestValidation(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.validation_service = idfy_sdk.services.ValidationService()

    def test_validate_sdo(self):
        data = self.validation_service.validate_sdo(validate_sdo_request=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('http://localhost:5000/validation/no/bankid/validate', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_parse_and_validate_sdo(self):
        data = self.validation_service.parse_and_validate_sdo(parse_sdo_request=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('http://localhost:5000/validation/no/bankid/parse', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


class TestValidationAsync(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.validation_service = idfy_sdk.services.ValidationService()

    def setUp(self):
        super().setUp()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()
    
    def test_validate_sdo_async(self):
        async def func():
            return await self.validation_service.validate_sdo(validate_sdo_request=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
            
        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('http://localhost:5000/validation/no/bankid/validate', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_parse_and_validate_sdo_async(self):
        async def func():
            return await self.validation_service.parse_and_validate_sdo(parse_sdo_request=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('http://localhost:5000/validation/no/bankid/parse', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
