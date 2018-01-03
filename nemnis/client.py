__copyright__ = "2017 Oleksii Semeshchuk"
__license__ = "License: MIT, see LICENSE."
__version__ = "0.0.9"
__author__ = "Oleksii Semeshchuk"
__email__ = "semolex@live.com"

'''
    client
    ------

    Module for the synchronous NIS client.
'''

import requests
from .core import AbstractClient, LOCALHOST_ENDPOINT

__all__ = [
    'Client',
]


class Client(AbstractClient):
    """
    Synchronous variant of the main API client.
    Uses a session for connection pooling.
    """

    def __init__(self, endpoint=LOCALHOST_ENDPOINT):
        """
        Initialize client.
        :param endpoint: address of the NIS.
        """
        super(Client, self).__init__(endpoint)
        self.session = requests.Session()

    def call(self, method, name, params=None, payload=None, **kwds):
        """
        Make calls to the API via HTTP methods and passed params.
        :return: response object
        """
        url = self.endpoint + '/' + name
        return self.session.request(method, url, params=params,
                                    json=payload, **kwds)
