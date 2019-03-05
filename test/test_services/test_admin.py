import asyncio
import functools
import unittest
import unittest.mock

from test.base_test import BaseTest
from idfy_sdk.version import version

import idfy_sdk

class TestAdmin(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.admin_service = idfy_sdk.services.AdminService()
    
    def test_get_account(self):
        data = self.admin_service.get_account()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/account'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_update_account(self):
        data = self.admin_service.update_account(account_update_options=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.put.assert_called_once_with('{}/admin/account'.format(self.base_url), data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        
    @unittest.skip("Mock server error")
    def test_create_account(self):
        data = self.admin_service.create_account(account_create_options=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with()

    @unittest.skip("Mock server error")
    def test_disable_account(self):
        data = self.admin_service.disable_account()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with()

    def test_list_accounts(self):
        data = self.admin_service.list_accounts()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/account/list'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'name': None, 'orgNo': None, 'uniCustomerNo': None, 'createdBefore': None, 'createdAfter': None, 'lastModifiedBefore': None,
'lastModifiedAfter': None, 'dealerName': None, 'dealerReference': None, 'tags': None, 'enable': None})

    def test_list_account_names(self):
        data = self.admin_service.list_account_names()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/account/list/names'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_get_dealer(self):
        data = self.admin_service.get_dealer(dealer_id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/dealer/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_update_dealer(self):
        data = self.admin_service.update_dealer(dealer_id="1", dealer=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/admin/dealer/1'.format(self.base_url), auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_list_accounts_for_dealer(self):
        data = self.admin_service.list_accounts_for_dealer(dealer_id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/dealer/1/accounts'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_list_transactions(self):
        data = self.admin_service.list_transactions()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/invoice'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'year': None, 'month': None, 'get_as_csv': None})

    def test_list_templates(self):
        data = self.admin_service.list_templates()

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/template'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_create_template(self):
        data = self.admin_service.create_template(pdf_template_options=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/admin/template'.format(self.base_url), auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_get_template(self):
        data = self.admin_service.get_template(id="1")

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/template/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_update_template(self):
        data = self.admin_service.update_template(id="1", pdf_template_options=self.params)

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.put.assert_called_once_with('{}/admin/template/1'.format(self.base_url), data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    def test_delete_template(self):
        data = self.admin_service.delete_template(id="1")

        self.assertIsNone(data)
        #self.AssertEqual()
        self.mock_http.delete.assert_called_once_with('{}/admin/template/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})

class TestAdminAsync(BaseTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.admin_service = idfy_sdk.services.AdminService()

    def setUp(self):
        super().setUp()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(None)
    
    def tearDown(self):
        self.loop.close()
    
    def test_get_account_async(self):
        async def func():
            return await self.admin_service.get_account(threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/account'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
    

    def test_update_account_async(self):
        async def func():
            return await self.admin_service.update_account(account_update_options=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
     
        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.put.assert_called_once_with('{}/admin/account'.format(self.base_url), data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
        
    @unittest.skip("Mock server error")
    def test_create_account_async(self):
        async def func():
            return await self.admin_service.create_account(account_create_options=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
       
        self.assertIsNotNone(data)
        #mock_service.create_account.assert_called_once_with(account_create_options=self.params, threaded=True)
    
    @unittest.skip("Mock server error")
    def test_disable_account_async(self):
        async def func():
            return await self.admin_service.disable_account(threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        #mock_service.disable_account.assert_called_once_with(threaded=True)
    
    def test_list_accounts_async(self):
        async def func():
            return await self.admin_service.list_accounts(threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/account/list'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'name': None, 'orgNo': None, 'uniCustomerNo': None, 'createdBefore': None, 'createdAfter': None, 'lastModifiedBefore': None,
'lastModifiedAfter': None, 'dealerName': None, 'dealerReference': None, 'tags': None, 'enable': None})

    
    def test_list_account_names_async(self):
        async def func():
            return await self.admin_service.list_account_names(threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/account/list/names'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    
    def test_get_dealer_async(self):
        async def func():
            return await self.admin_service.get_dealer(dealer_id="1", threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/dealer/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_update_dealer_async(self):
        async def func():
            return await self.admin_service.update_dealer(dealer_id="1", dealer=self.params, threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/admin/dealer/1'.format(self.base_url), auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_list_accounts_for_dealer_async(self):
        async def func():
            return await self.admin_service.list_accounts_for_dealer(dealer_id="1", threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/dealer/1/accounts'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)
            
    def test_list_transactions_async(self):
        async def func():
            return await self.admin_service.list_transactions(threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/invoice'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params={'year': None, 'month': None, 'get_as_csv': None})

        
    def test_list_templates_async(self):
        async def func():
            return await self.admin_service.list_templates(threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/template'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    
    def test_create_template_async(self):
        async def func():
            return await self.admin_service.create_template(pdf_template_options=self.params, threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.post.assert_called_once_with('{}/admin/template'.format(self.base_url), auth=None, data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)


    def test_get_template_async(self):
        async def func():
            return await self.admin_service.get_template(id="1", threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.get.assert_called_once_with('{}/admin/template/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    
    def test_update_template_async(self):
        async def func():
            return await self.admin_service.update_template(id="1", pdf_template_options=self.params, threaded=True)
        data = self.loop.run_until_complete(func())
        
        self.assertIsNotNone(data)
        #self.AssertEqual()
        self.mock_http.put.assert_called_once_with('{}/admin/template/1'.format(self.base_url), data='{"unit": "test"}', headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}, params=None)

    
    def test_delete_template_async(self):
        async def func():
            return await self.admin_service.delete_template(id="1", threaded=True)
        data = self.loop.run_until_complete(func())

        self.assertIsNone(data)
        #self.AssertEqual()
        self.mock_http.delete.assert_called_once_with('{}/admin/template/1'.format(self.base_url), headers={'X-Idfy-SDK': 'Python {}'.format(version), 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'})



#Provide CLI to the test script.
if __name__ == '__main__':
    unittest.main()
