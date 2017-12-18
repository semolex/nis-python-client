from unittest import TestCase

import requests
import requests_mock
from nemnis import Client, Node


class TestNode(TestCase):
    def setUp(self):
        self.client = Client(endpoint='mock://127.0.0.1:7890')

    def test_client_is_used(self):
        node = Node(self.client)
        self.assertEqual(node.client, self.client)
        self.assertEqual(node.name, 'node/')

    def test_info(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/node/info', status_code=200)
            resp = self.client.node.info()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/node/info')
            self.assertEqual(resp.status_code, 200)

    def test_extended_info(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/node/extended-info', status_code=200)
            resp = self.client.node.extended_info()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/node/extended-info')
            self.assertEqual(resp.status_code, 200)

    def test_peer_list_all(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/node/peer-list/all', status_code=200)
            resp = self.client.node.peer_list_all()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/node/peer-list/all')
            self.assertEqual(resp.status_code, 200)

    def test_peer_list_reachable(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/node/peer-list/reachable',
                  status_code=200)
            resp = self.client.node.peer_list_reachable()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/node/peer-list/reachable')
            self.assertEqual(resp.status_code, 200)

    def test_peer_list_active(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/node/peer-list/active',
                  status_code=200)
            resp = self.client.node.peer_list_active()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/node/peer-list/active')
            self.assertEqual(resp.status_code, 200)

    def test_max_chain_height(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/node/active-peers/max-chain-height',
                  status_code=200)
            resp = self.client.node.max_chain_height()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(
                resp.url,
                'mock://127.0.0.1:7890/node/active-peers/max-chain-height'
            )
            self.assertEqual(resp.status_code, 200)

    def test_experiences(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/node/experiences', status_code=200)
            resp = self.client.node.experiences()
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/node/experiences')
            self.assertEqual(resp.status_code, 200)

    def test_boot(self):
        with requests_mock.Mocker() as m:
            m.post('mock://127.0.0.1:7890/node/boot', status_code=200)
            resp = self.client.node.boot({'testbootobject': 'data'})
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/node/boot')
            self.assertEqual(resp.status_code, 200)
