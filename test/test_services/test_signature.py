import asyncio
import unittest
import unittest.mock

import idfy_sdk as python
from test.base_test import BaseTest

class TestSignature(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.signature_service = python.SignatureService() #Probably don't need to import the whole python SDK
    #Documents
    def test_get_document(self):
        data = self.signature_service.get_document('123')

        self.assertIsNotNone(data)
        self.assertEqual(data.description, 'This is an important document')
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/123', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_create_document(self):
        data = self.signature_service.create_document(options=self.params)
        
        self.assertIsNotNone(data)
        self.assertEqual(data.document_id, "94865b6f-2aa9-436d-8b3c-a85e00efd034")
        self.mock_http.post.assert_called_with('http://localhost:5000/signature/documents', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.post.call_count, 1)

    def test_update_document(self):
        data = self.signature_service.update_document(document_id="123")
        
        self.assertIsNotNone(data)
        self.assertEqual(data.title, "Updated title")
        self.mock_http.patch.assert_called_once_with('http://localhost:5000/signature/documents/123', data='null', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})

    def test_cancel_document(self):
        data = self.signature_service.cancel_document(document_id="123", reason="test")
        
        self.assertIsNone(data)
        self.mock_http.post.assert_called_with('http://localhost:5000/signature/documents/123/cancel', auth=None, data='null', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params='test')
        self.assertEqual(self.mock_http.post.call_count, 1)

    def test_get_document_status(self):
        data = self.signature_service.get_document_status(document_id="123")
        
        self.assertIsNotNone(data)
        self.assertEqual(data.document_status, "signed")
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/123/status', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)

    def test_get_document_summary(self):
        data = self.signature_service.get_document_summary(document_id="123")
        
        self.assertIsNotNone(data)
        #self.assertEqual(data.account_id, "098f63e6-497f-4b42-b3f7-59015df7c762")
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/123/summary', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    
    def test_list_document_summaries(self):
        data = self.signature_service.list_document_summaries()
        
        self.assertIsNotNone(data)
        self.assertEqual(data.size, 45)
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/summary', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'externalId': None, 'signerId': None, 'externalSignerId': None, 'fromDate': None, 'toDate': None, 'lastUpdated': None, 'signedDate': None, 'nameOfSigner': None, 'title': None, 'status': None, 'tags': None, 'offset': None, 'limit': None})
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    #Signers
    def test_get_signer(self):
        data = self.signature_service.get_signer(document_id="123", signer_id="123")
        
        self.assertIsNotNone(data)
        self.assertEqual(data.url, "https://sign-test.idfy.io/init?jwt=...")
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/123/signers/123', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_create_signer(self):
        data = self.signature_service.create_signer(document_id="123", signer_options=self.params)
        
        self.assertIsNotNone(data)
        self.assertEqual(data.external_signer_id, "aoijfnmo032q223")
        self.mock_http.post.assert_called_once_with('http://localhost:5000/signature/documents/123/signers', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.post.call_count, 1)
    
    def test_update_signer(self):
        data = self.signature_service.update_signer(document_id="123", signer_id="456", signer_options=self.params)
        
        self.assertIsNotNone(data)
        self.assertEqual(data.signer_info.first_name, "Updated")
        self.mock_http.patch.assert_called_once_with('http://localhost:5000/signature/documents/123/signers/456', data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
        self.assertEqual(self.mock_http.patch.call_count, 1)
    
    def test_delete_signer(self):
        data = self.signature_service.delete_signer(document_id="123", signer_id="456")
    
        self.assertIsNone(data)
        #self.assertEqual()
        self.mock_http.delete.assert_called_once_with('http://localhost:5000/signature/documents/123/signers/456', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
        self.assertEqual(self.mock_http.delete.call_count, 1)
        
    
    def test_list_signers(self):
        data = self.signature_service.list_signers(document_id="123")
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/123/signers/', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)

    def test_get_attachment(self):
        data = self.signature_service.get_attachment(document_id="1", attachment_id="2")
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/attachments/2', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_create_attachment(self):
        data = self.signature_service.create_attachment(document_id="1", data=self.params)
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.post.assert_called_once_with('http://localhost:5000/signature/documents/1/attachments/', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.post.call_count, 1)
    
    def test_update_attachment(self):
        data = self.signature_service.update_attachment(document_id="1", attachment_id="2", data=self.params)
    
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.patch.assert_called_once_with('http://localhost:5000/signature/documents/1/attachments/2', data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
        self.assertEqual(self.mock_http.patch.call_count, 1)

    def test_delete_attachment(self): # Not "tested" yet.
        data = self.signature_service.delete_attachment(document_id="1", attachment_id="1")
        
        self.assertIsNone(data)
        #self.assertEqual()
        self.mock_http.delete.assert_called_once_with('http://localhost:5000/signature/documents/1/attachments/1', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
        self.assertEqual(self.mock_http.delete.call_count, 1)

    def test_list_attachments(self):
        data = self.signature_service.list_attachments(document_id="1")
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/attachments', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)

    def test_get_file(self):
        data = self.signature_service.get_file(document_id="1", file_format="2")
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/files', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params='2')
        self.assertEqual(self.mock_http.get.call_count, 1)

    def test_get_file_for_signer(self):
        data = self.signature_service.get_file_for_signer(document_id="1", signer_id="2", file_format="3")
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/files/signers/2', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params='3')
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_get_attachment_file(self):
        data = self.signature_service.get_attachment_file(document_id="1", attachment_id="2", file_format="3")
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/files/attachments/2', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params='3')
        self.assertEqual(self.mock_http.get.call_count, 1)
   
    def test_get_attachment_file_for_signer(self):
        data = self.signature_service.get_attachment_file_for_signer(document_id="1", attachment_id="2", signer_id="3", file_format="4")
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/files/attachments/2/signers/3', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params='4')
        self.assertEqual(self.mock_http.get.call_count, 1)

    def test_list_notifications(self):
        data = self.signature_service.list_notifications(document_id="1")
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/notifications', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)

    def test_send_reminders(self):
        data = self.signature_service.send_reminders(document_id="1", manual_reminder=self.params)
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.post.assert_called_once_with('http://localhost:5000/signature/documents/1/notifications/reminder', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.post.call_count, 1)
    
    def test_list_themes(self):
        data = self.signature_service.list_themes()
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/themes/list/themes', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_list_spinners(self):
        data = self.signature_service.list_spinners()
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/themes/list/spinners', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)

class TestSignatureAsync(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.signature_service = python.SignatureService()

    def setUp(self):
        super().setUp()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()
    
        #Documents

    def test_get_document_async(self):
        async def func():
            return await self.signature_service.get_document('123', threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        self.assertEqual(data.signers[0].external_signer_id, 'uoiahsd321982983jhrmnec2wsadm32')
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/123', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)

    def test_create_document_async(self):
        async def func():
            return await self.signature_service.create_document(options=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        self.assertEqual(data.document_id, "94865b6f-2aa9-436d-8b3c-a85e00efd034") 
        self.mock_http.post.assert_called_once_with('http://localhost:5000/signature/documents', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.post.call_count, 1)
 
    def test_update_document_async(self):
        async def func():
            return await self.signature_service.update_document(document_id="123", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        #self.assertEqual() 
        self.mock_http.patch.assert_called_once_with('http://localhost:5000/signature/documents/123', data='null', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
        self.assertEqual(self.mock_http.patch.call_count, 1)


    def test_cancel_document_async(self):
        async def func():
            return await self.signature_service.cancel_document(document_id="123", reason="test", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertEqual(data, '""')
        self.mock_http.post.assert_called_with('http://localhost:5000/signature/documents/123/cancel', auth=None, data='null', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params='test')
        self.assertEqual(self.mock_http.post.call_count, 1)
    
    def test_get_document_status_async(self):
        async def func():
            return await self.signature_service.get_document_status(document_id="123", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        self.assertEqual(data.document_status, "signed")
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/123/status', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_get_document_summary_async(self):
        async def func():
            return await self.signature_service.get_document_summary(document_id="123", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual(data.account_id, "098f63e6-497f-4b42-b3f7-59015df7c762")
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/123/summary', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_list_document_summaries_async(self):
        async def func():
            return await self.signature_service.list_document_summaries(threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        self.assertEqual(data.size, 45)
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/summary', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'externalId': None, 'signerId': None, 'externalSignerId': None, 'fromDate': None, 'toDate': None, 'lastUpdated': None, 'signedDate': None, 'nameOfSigner': None, 'title': None, 'status': None, 'tags': None, 'offset': None, 'limit': None})
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    #Signers
    def test_get_signer_async(self):
        async def func():
            return await self.signature_service.get_signer(document_id="123", signer_id="123", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        self.assertEqual(data.url, "https://sign-test.idfy.io/init?jwt=...")
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/123/signers/123', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_create_signer_async(self):
        async def func():
            return await self.signature_service.create_signer(document_id="123", signer_options=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        self.assertEqual(data.external_signer_id, "aoijfnmo032q223")
        self.mock_http.post.assert_called_once_with('http://localhost:5000/signature/documents/123/signers', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.post.call_count, 1)

    def test_update_signer_async(self):
        async def func():
            return await self.signature_service.update_signer(document_id="123", signer_id="456", signer_options=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        self.assertEqual(data.signer_info.first_name, "Updated")
        self.mock_http.patch.assert_called_once_with('http://localhost:5000/signature/documents/123/signers/456', data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
        self.assertEqual(self.mock_http.patch.call_count, 1)
    
    def test_delete_signer_async(self):
        async def func():
            return await self.signature_service.delete_signer(document_id="123", signer_id="456", threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNone(data)
        #self.assertEqual()
        self.mock_http.delete.assert_called_once_with('http://localhost:5000/signature/documents/123/signers/456', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
        self.assertEqual(self.mock_http.delete.call_count, 1)
    
    def test_list_signers_async(self):
        async def func():
            return await self.signature_service.list_signers(document_id="123", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/123/signers/', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_get_attachment_async(self):
        async def func():
            return await self.signature_service.get_attachment(document_id="1", attachment_id="2", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/attachments/2', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_create_attachment_async(self):
        async def func():
            return await self.signature_service.create_attachment(document_id="1", data=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.post.assert_called_once_with('http://localhost:5000/signature/documents/1/attachments/', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.post.call_count, 1)
    
    def test_update_attachment_async(self):
        async def func():
            return await self.signature_service.update_attachment(document_id="1", attachment_id="2", data=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
    
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.patch.assert_called_once_with('http://localhost:5000/signature/documents/1/attachments/2', data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
        self.assertEqual(self.mock_http.patch.call_count, 1)

    def test_delete_attachment_async(self): # Not "tested" yet.
        async def func():
            return await self.signature_service.delete_attachment(document_id="1", attachment_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNone(data)
        #self.assertEqual()
        self.mock_http.delete.assert_called_once_with('http://localhost:5000/signature/documents/1/attachments/1', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})
        self.assertEqual(self.mock_http.delete.call_count, 1)
    

    def test_list_attachments_async(self):
        async def func():
            return await self.signature_service.list_attachments(document_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/attachments', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_get_file_async(self):
        async def func():
            return await self.signature_service.get_file(document_id="1", file_format="2", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/files', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params='2')
        self.assertEqual(self.mock_http.get.call_count, 1)

    def test_get_file_for_signer_async(self):
        async def func():
            return await self.signature_service.get_file_for_signer(document_id="1", signer_id="2", file_format="3", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/files/signers/2', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params='3')
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_get_attachment_file_async(self):
        async def func():
            return await self.signature_service.get_attachment_file(document_id="1", attachment_id="2", file_format="3", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/files/attachments/2', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params='3')
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_get_attachment_file_for_signer_async(self):
        async def func():
            return await self.signature_service.get_attachment_file_for_signer(document_id="1", attachment_id="2", signer_id="3", file_format="4", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/files/attachments/2/signers/3', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params='4')
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_list_notifications_async(self):
        async def func():
            return await self.signature_service.list_notifications(document_id="1", threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/1/notifications', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)

    def test_send_reminders_async(self):
        async def func():
            return await self.signature_service.send_reminders(document_id="1", manual_reminder=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.post.assert_called_once_with('http://localhost:5000/signature/documents/1/notifications/reminder', auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.post.call_count, 1)
    
    def test_list_themes_async(self):
        async def func():
            return await self.signature_service.list_themes(threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/themes/list/themes', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)
    
    def test_list_spinners_async(self):
        async def func():
            return await self.signature_service.list_spinners(threaded=True)
        data = self.loop.run_until_complete(func())
        
        
        self.assertIsNotNone(data)
        #self.assertEqual()
        self.mock_http.get.assert_called_once_with('http://localhost:5000/signature/documents/themes/list/spinners', headers={'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        self.assertEqual(self.mock_http.get.call_count, 1)

#Provide CLI to the test script.
if __name__ == '__main__':
    unittest.main()