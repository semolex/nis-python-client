__name__ = 'nemnis'
__copyright__ = "2017 Oleksii Semeshchuk"
__license__ = "License: MIT, see LICENSE."
__version__ = "0.0.9"
__author__ = "Oleksii Semeshchuk"
__email__ = "semolex@live.com"

'''
    nis-python-client
    -----------------

    Python client bindings for the NEM NIS API.
'''

from .core import *
from .client import *
try:
    from .asyncio import *
except:
    pass
