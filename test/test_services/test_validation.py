import asyncio
import functools

import unittest
import unittest.mock

import idfy_sdk

params = {'unit': 'test'}

@unittest.mock.patch('idfy_sdk.services.validation_service.ValidationService', autospec=True, wrap=idfy_sdk.services.ValidationService)
class TestValidation(unittest.TestCase):
    def test_validate_sdo(self, mock_service):
    
        data = mock_service.validate_sdo(validate_sdo_request=params)
        
        self.assertIsNotNone(data)
        mock_service.validate_sdo.assert_called_once_with(validate_sdo_request=params)
    
    def test_parse_and_validate_sdo(self, mock_service):
    
        data = mock_service.parse_and_validate_sdo(parse_sdo_request=params)
        
        self.assertIsNotNone(data)
        mock_service.parse_and_validate_sdo.assert_called_once_with(parse_sdo_request=params)

@unittest.mock.patch('idfy_sdk.services.validation_service.ValidationService', autospec=True, wrap=idfy_sdk.services.ValidationService)
class TestValidationAsync(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()

    def test_validate_sdo_async(self, mock_service):
        async def func():
            return mock_service.validate_sdo(validate_sdo_request=params, threaded=True)
        data = self.loop.run_until_complete(func())
            
        self.assertIsNotNone(data)
        mock_service.validate_sdo.assert_called_once_with(validate_sdo_request=params, threaded=True)
    
    def test_parse_and_validate_sdo_async(self, mock_service):
        async def func():
            return mock_service.parse_and_validate_sdo(parse_sdo_request=params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.parse_and_validate_sdo.assert_called_once_with(parse_sdo_request=params, threaded=True)