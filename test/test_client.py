from unittest import TestCase

import requests
import requests_mock
from client import (Client, Account, BlockChain, Node, Namespace, Transaction,
                    Debug)


class TestClient(TestCase):

    def setUp(self):
        self.client = Client(endpoint='mock://127.0.0.1:7890')

    def test_call(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/test/api', text='ok')
            resp = self.client.call('GET', 'test/api')
            self.assertIsInstance(resp, requests.Response)

    def test_heartbeat(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/heartbeat', status_code=200)
            resp = self.client.heartbeat()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/heartbeat')
            self.assertEqual(resp.status_code, 200)

    def test_status(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/status', status_code=200)
            resp = self.client.status()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/status')
            self.assertEqual(resp.status_code, 200)

    def test_account(self):
        self.assertIsInstance(self.client.account, Account)

    def test_blockchain(self):
        self.assertIsInstance(self.client.blockchain, BlockChain)

    def test_node(self):
        self.assertIsInstance(self.client.node, Node)

    def test_namespace(self):
        self.assertIsInstance(self.client.namespace, Namespace)

    def test_transaction(self):
        self.assertIsInstance(self.client.transaction, Transaction)

    def test_debug(self):
        self.assertIsInstance(self.client.debug, Debug)
