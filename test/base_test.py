from unittest import TestCase
import unittest.mock

from idfy_sdk.infrastructure import http_requests as http, urls as urls

class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params = {'unit': 'test'}
        cls.base_url = urls.TestBaseUrl
        cls.api_headers = {'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}

    def setUp(self):
        self.patcher = unittest.mock.patch('idfy_sdk.infrastructure.http_requests.requests', wraps=http.requests)
        self.mock_http = self.patcher.start()
        #self.addCleanup(patcher.stop())

    def tearDown(self):
        self.patcher.stop()