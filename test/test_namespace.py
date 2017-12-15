from unittest import TestCase

import requests
import requests_mock
from client import Client, Namespace


class TestNamespace(TestCase):
    def setUp(self):
        self.client = Client(endpoint='mock://127.0.0.1:7890')

    def test_client_is_used(self):
        node = Namespace(self.client)
        self.assertEqual(node.client, self.client)
        self.assertEqual(node.name, 'namespace/')

    def test_root_page(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/namespace/root/page', status_code=200)
            resp = self.client.namespace.root_page('id:0', 5)
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/namespace/root/page')
            self.assertEqual(resp.status_code, 200)

    def test_namespace(self):
        with requests_mock.Mocker() as m:
            m.get('mock://127.0.0.1:7890/namespace/', status_code=200)
            resp = self.client.namespace.namespace('test.namespace')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url, 'mock://127.0.0.1:7890/namespace/')
            self.assertEqual(resp.status_code, 200)

    def test_mosaic_definition_page(self):
        with requests_mock.Mocker() as m:
            part = 'definition/page'
            m.get('mock://127.0.0.1:7890/namespace/mosaic/definition/page',
                  status_code=200)
            resp = self.client.namespace.mosaic_definition_page(
                'test.namespace')
            self.assertIsInstance(resp, requests.Response)
            self.assertEqual(resp.url,
                             'mock://127.0.0.1:7890/namespace/mosaic/' + part)
            self.assertEqual(resp.status_code, 200)
