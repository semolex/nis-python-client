from unittest import TestCase

import requests
import requests_mock
from nis import Client, Transaction


class TestTransaction(TestCase):
    def setUp(self):
        self.client = Client(endpoint='mock://127.0.0.1:7890')

    def test_client_is_used(self):
        transaction = Transaction(self.client)
        self.assertEqual(transaction.client, self.client)
        self.assertEqual(transaction.name, 'transaction/')

    def test_prepare_announce(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/transaction/prepare-announce',
                   status_code=200)
            resp = self.client.transaction.prepare_announce(
                {'testtrasaction': 'data'})
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(
                 resp.url,
                 'mock://127.0.0.1:7890/transaction/prepare-announce'
                 )
            self.assertEqual(resp.status_code, 200)

    def test_announce(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/transaction/announce',
                   status_code=200)
            resp = self.client.transaction.announce({'testtrasaction': 'data'})
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/transaction/announce')
            self.assertEqual(resp.status_code, 200)
