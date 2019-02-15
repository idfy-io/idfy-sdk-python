import idfy_sdk as python

import asyncio
import functools

import unittest
import unittest.mock

params = {'unit': 'test'}

@unittest.mock.patch('idfy_sdk.services.jwt_service.JwtService', autospec=True, wrap=python.JwtService)
class TestJwt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        #self.service = SignatureService()
        pass
    
    def test_validate(self, mock_service):
    
        data = mock_service.validate(jwt_validation_request=params)
        
        self.assertIsNotNone(data)
        mock_service.validate.assert_called_once_with(jwt_validation_request=params)
    
@unittest.mock.patch('idfy_sdk.services.jwt_service.JwtService', autospec=True, wrap=python.JwtService)
class TestJwtAsync(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        #self.service = SignatureService() 
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()
    
    def test_validate_async(self, mock_service):
        async def func():
            return mock_service.validate(jwt_validation_request=params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        mock_service.validate.assert_called_once_with(jwt_validation_request=params, threaded=True)