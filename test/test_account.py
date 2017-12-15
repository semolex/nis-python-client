from unittest import TestCase

import requests
import requests_mock
from client import Client, Account


class TestAccount(TestCase):
    def setUp(self):
        self.client = Client(endpoint='mock://127.0.0.1:7890')

    def test_client_is_used(self):
        account = Account(self.client)
        self.assertEqual(account.client, self.client)
        self.assertEqual(account.name, 'account/')

    def test_generate(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/generate', status_code=200)
            resp = self.client.account.generate()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/account/generate')
            self.assertEqual(resp.status_code, 200)

    def test_get(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/get', status_code=200)
            resp = self.client.account.get('TESTADDRESS')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/account/get')
            self.assertEqual(resp.status_code, 200)

    def test_get_from_public_key(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/get/from-public-key',
                  status_code=200)
            resp = self.client.account.get_from_public_key('testpublickkey')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/get/from-public-key')
            self.assertEqual(resp.status_code, 200)

    def test_get_forwarded(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/get/forwarded',
                  status_code=200)
            resp = self.client.account.get_forwarded('TESTADDRESS')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/get/forwarded')
            self.assertEqual(resp.status_code, 200)

    def test_get_forwarded_from_public_key(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/get/forwarded/from-public-key',
                  status_code=200)
            resp = self.client.account.get_forwarded_from_public_key(
                'testpublickkey')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/get/forwarded/from-public-key')
            self.assertEqual(resp.status_code, 200)

    def test_status(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/status', status_code=200)
            resp = self.client.account.status('TESTADDRESS')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/account/status')
            self.assertEqual(resp.status_code, 200)

    def test_transfers_incoming(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/transfers/incoming',
                  status_code=200)
            resp = self.client.account.transfers_incoming('TESTADDRESS',
                                                          'testhash', 'id01')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/transfers/incoming')
            self.assertEqual(resp.status_code, 200)

    def test_transfers_outgoing(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/transfers/outgoing',
                  status_code=200)
            resp = self.client.account.transfers_outgoing('TESTADDRESS',
                                                          'testhash', 'id01')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/transfers/outgoing')
            self.assertEqual(resp.status_code, 200)

    def test_transfers_all(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/transfers/all',
                  status_code=200)
            resp = self.client.account.transfers_all('TESTADDRESS', 'testhash',
                                                     'id01')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/transfers/all')
            self.assertEqual(resp.status_code, 200)

    def test_unconfirmed_transactions(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/unconfirmedTransactions',
                  status_code=200)
            resp = self.client.account.unconfirmed_transactions('TESTADDRESS')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/unconfirmedTransactions')
            self.assertEqual(resp.status_code, 200)

    def test__transfers_incoming(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/local/transfers/incoming',
                   status_code=200)
            resp = self.client.account._transfers_incoming('testprivatekey',
                                                           'testhash', 'id01')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/local/transfers/incoming')
            self.assertEqual(resp.status_code, 200)

    def test__transfers_outgoing(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/local/transfers/outgoing',
                   status_code=200)
            resp = self.client.account._transfers_outgoing('testprivatekey',
                                                           'testhash', 'id01')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/local/transfers/outgoing')
            self.assertEqual(resp.status_code, 200)

    def test__transfers_all(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/local/transfers/all', status_code=200)
            resp = self.client.account._transfers_all('testprivatekey',
                                                      'testhash', 'id01')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/local/transfers/all')
            self.assertEqual(resp.status_code, 200)

    def test_harvests(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/harvests', status_code=200)
            resp = self.client.account.harvests('TESTADDRESS', 'testhash')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/account/harvests')
            self.assertEqual(resp.status_code, 200)

    def test_importances(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/importances', status_code=200)
            resp = self.client.account.importances()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/importances')
            self.assertEqual(resp.status_code, 200)

    def test_namespace_page(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/namespace/page',
                  status_code=200)
            resp = self.client.account.namespace_page('TESTADDRESS',
                                                      'some.parent', 'id:0')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/namespace/page')
            self.assertEqual(resp.status_code, 200)

    def test_mosaic_definition_page(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/mosaic/definition/page',
                  status_code=200)
            resp = self.client.account.mosaic_definition_page('TESTADDRESS',
                                                              'some.parent',
                                                              'id:0')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/mosaic/definition/page')
            self.assertEqual(resp.status_code, 200)

    def test_mosaic_owned(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/mosaic/owned', status_code=200)
            resp = self.client.account.mosaic_owned('TESTADDRESS')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/mosaic/owned')
            self.assertEqual(resp.status_code, 200)

    def test_unlock(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/account/unlock', status_code=200)
            resp = self.client.account.unlock('testprivatekey')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/account/unlock')
            self.assertEqual(resp.status_code, 200)

    def test_lock(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/account/lock', status_code=200)
            resp = self.client.account.lock('testprivatekey')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/account/lock')
            self.assertEqual(resp.status_code, 200)

    def test_unlocked_info(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/account/unlocked/info',
                   status_code=200)
            resp = self.client.account.unlocked_info()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/unlocked/info')
            self.assertEqual(resp.status_code, 200)

    def test_historical_get(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/account/historical/get',
                  status_code=200)
            resp = self.client.account.historical_get('TESTADDRESS', 1, 2, 1)
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/account/historical/get')
            self.assertEqual(resp.status_code, 200)
