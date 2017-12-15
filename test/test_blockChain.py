from unittest import TestCase

import requests
import requests_mock
from client import Client, BlockChain


class TestBlockChain(TestCase):
    def setUp(self):
        self.client = Client(endpoint='mock://127.0.0.1:7890')

    def test_client_is_used(self):
        blockchain = BlockChain(self.client)
        self.assertEqual(blockchain.client, self.client)
        self.assertEqual(blockchain.name, 'chain/')

    def test_height(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/chain/height', status_code=200)
            resp = self.client.blockchain.height()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/chain/height')
            self.assertEqual(resp.status_code, 200)

    def test_score(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/chain/score', status_code=200)
            resp = self.client.blockchain.score()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/chain/score')
            self.assertEqual(resp.status_code, 200)

    def test_last_block(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/chain/last-block', status_code=200)
            resp = self.client.blockchain.last_block()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/chain/last-block')
            self.assertEqual(resp.status_code, 200)

    def test_at_public(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/block/at/public', status_code=200)
            resp = self.client.blockchain.at_public(100)
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/block/at/public')
            self.assertEqual(resp.status_code, 200)

    def test_local_chain_blocks_after(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/local/chain/blocks-after',
                   status_code=200)
            resp = self.client.blockchain.local_chain_blocks_after(100)
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/local/chain/blocks-after')
            self.assertEqual(resp.status_code, 200)
