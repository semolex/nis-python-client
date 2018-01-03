__copyright__ = "2017 Oleksii Semeshchuk"
__license__ = "License: MIT, see LICENSE."
__version__ = "0.0.9"
__author__ = "Oleksii Semeshchuk"
__email__ = "semolex@live.com"

'''
    asyncio
    -------

    Module for the asynchronous NIS client.
'''

import aiohttp
import asyncio
from .core import AbstractClient, LOCALHOST_ENDPOINT

__all__ = [
    'loop',
    'run',
    'map',
    'AsyncioClient',
]


def loop():
    """
    Represents the global event loop.
    :return: Event loop for nemnis client.
    """
    return asyncio.get_event_loop()


def run(future):
    """
    Run future until complete.
    :return: Return future's result, or raise exception.
    """
    return loop().run_until_complete(future)


def map(futures):
    """
    Asynchronously map list of futures.
    :return: Return value of all futures, or raise exception.
    """
    return run(asyncio.gather(*futures))


class AsyncioClient(AbstractClient):
    """
    Asynchronous variant of the main API client.
    Uses a session for connection pooling.
    """

    def __init__(self, endpoint=LOCALHOST_ENDPOINT, max_concurrency=100):
        """
        Initialize client.
        :param endpoint: address of the NIS.
        """
        super(AsyncioClient, self).__init__(endpoint)
        self.session = aiohttp.ClientSession(loop=loop())
        self.semaphore = asyncio.Semaphore(max_concurrency)

    def __del__(self):
        self.session.close()

    async def call(self, method, name, params=None, payload=None, **kwds):
        """
        Make calls to the API via HTTP methods and passed params.
        :return: response object
        """
        url = self.endpoint + '/' + name
        async with self.semaphore:
            return await self.session.request(method, url, params=params,
                                              json=payload, **kwds)
