import asyncio
import unittest
import unittest.mock

from test.base_test import BaseTest
from idfy_sdk.version import version

import idfy_sdk

class TestIdentification(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.identification_service = idfy_sdk.services.IdentificationService()
    
    def test_get_session(self):
        data = self.identification_service.get_session(request_id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/identification/session', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'requestId': '1', 'metaData': False})

    def test_create_session(self):
        data = self.identification_service.create_session(create_identification_request=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('http://localhost:5000/identification/session', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_get_session_status(self):
        data = self.identification_service.get_session_status(request_id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/identification/session/status', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'requestId': '1'})

    def test_invalidate_session(self):
        data = self.identification_service.invalidate_session(request_id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.put.assert_called_once_with('http://localhost:5000/identification/session/invalidate', data='{"RequestId": "1"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_get_log_entry(self):
        data = self.identification_service.get_log_entry(request_id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/identification/log/requestId/1', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_list_log_entries(self):
        data = self.identification_service.list_log_entries(year="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/identification/log/filter/1', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'month': None, 'day': None, 'status': None, 'identityProviderType': None, 'externalId': None, 'name': None, 'skip': None, 'pageSize': None})

    def test_create_bankId_mobile_session(self):
        data = self.identification_service.create_bankId_mobile_session(request="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('http://localhost:5000/identification/no/bankid/mobile', auth=None, data='"1"', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

class TestIdentificationAsync(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.identification_service = idfy_sdk.services.IdentificationService()

    def setUp(self):
        super().setUp()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()
    
    def test_get_session_async(self):
        async def func():
            return await self.identification_service.get_session(request_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('http://localhost:5000/identification/session', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'requestId': '1', 'metaData': False})

    def test_create_session_async(self):
        async def func():
            return await self.identification_service.create_session(create_identification_request=self.params, threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('http://localhost:5000/identification/session', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_get_session_status_async(self):
        async def func():
            return await self.identification_service.get_session_status(request_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('http://localhost:5000/identification/session/status', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'requestId': '1'})
    
    def test_invalidate_session_async(self):
        async def func():
            return await self.identification_service.invalidate_session(request_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.put.assert_called_once_with('http://localhost:5000/identification/session/invalidate', data='{"RequestId": "1"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_get_log_entry_async(self):
        async def func():
            return await self.identification_service.get_log_entry(request_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('http://localhost:5000/identification/log/requestId/1', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    
    def test_list_log_entries_async(self):
        async def func():
            return await self.identification_service.list_log_entries(year="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.get.assert_called_once_with('http://localhost:5000/identification/log/filter/1', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'month': None, 'day': None, 'status': None, 'identityProviderType': None, 'externalId': None, 'name': None, 'skip': None, 'pageSize': None})
    
    def test_create_bankId_mobile_session_async(self):
        async def func():
            return await self.identification_service.create_bankId_mobile_session(request="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.mock_http.post.assert_called_once_with('http://localhost:5000/identification/no/bankid/mobile', auth=None, data='"1"', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
