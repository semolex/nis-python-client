# nis-python-client #
##### Python client for [NEM NIS API](https://nemproject.github.io). #####

### Prerequisites ###
Install all required dependencies into your `virtualenv` (if you wish to use it):
```pip install -r requirements.txt```
### Description ###
Client implements methods from NEM API by calling appropriate method. 
Method names are consist of API`s parent parts and related resources (where hyphens and slashes replced with underscore).
Its mean, that following API resource - `namespace/root/page` is implemented as `client.namespace.root_page` and `node/info` is `client.node.info`, etc.
Almost all methods are implemented this way, except few that has either super-long names or duplicate names. Simply discover all methods to see exact namings.
There is 6 API parent entities for usage:
* Account
* BlockChain
* Node
* Namespace
* Transaction
* Debug

To perform calls to the NEM NIS API, ensure you have working NIS instance.
By default NIS uses `7890` port, you can initialize NIS client with other address.

### Usage ###

Examples of usage:
```python
from client import Client

nis = Client()
hb = nis.heartbeat()
print(hb.status_code)
print(hb.json())
acc = nis.account.get('NCKMNCU3STBWBR7E3XD2LR7WSIXF5IVJIDBHBZQT')
print(acc.status_code)
print(acc.json())

```
All responses are `requests.Response` objects from `requests` lib.
You can perform all required manipulations after receiving them: convert to 
JSON, check status code etc.

Yiu also can perform call via `call` method from Client:

```python
from client import Client

nis = Client()
nis.call('GET', 'heartbeat')
nis.call('GET', 'account/get', params={'address':'SOMEADDRESS'})
nis.call('POST', 'chain/local/chain/blocks-after', payload={'height': 100})
```

Have fun!



