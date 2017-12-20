# nis-python-client
##### Python client for [NEM NIS API](https://nemproject.github.io). 

### Prerequisites

Install all required dependencies into your `virtualenv` (if you want to use it):

`pip install git+https://github.com/semolex/nis-python-client`


### Description
Client implements methods from NEM API by calling appropriate method. 
Method names are consist of API parent parts and related resources (where hyphens and slashes replaced with underscore).
Its mean, that following API resource - `namespace/root/page` is implemented as `client.namespace.root_page` and `node/info` is `client.node.info`, etc.

Almost all methods are implemented this way, except few that has either super-long names or duplicate names. Simply discover all methods to see exact namings.
There is 6 API parent resource entities for usage:
* Account
* BlockChain
* Node
* Namespace
* Transaction
* Debug

Extended code guide for available classes can be found [here](https://github.com/semolex/nis-python-client/blob/master/CODE_INFO.md).

Few call can be used directly from `Client` instance.
To perform calls to the NEM NIS API, ensure you have access to running NIS instance.
By default NIS uses `7890` port, you can initialize NIS client with other address.


### Usage

Examples of usage:
```python
from nemnis import Client

nis = Client()

hb = nis.heartbeat()

print(hb.status_code)

print(hb.json())

acc = nis.account.get('NCKMNCU3STBWBR7E3XD2LR7WSIXF5IVJIDBHBZQT')

print(acc.status_code)

print(acc.json())

new_client =  Client('http://myaddress.com:8080')

new_hb = new_client.heartbeat()

print(new_hb.status_code)

print(new_hb.json())
```
All responses are `requests.Response` objects from [requests](http://docs.python-requests.org/en/master/) library.
You can perform all required manipulations after receiving them: convert to 
JSON, check status code etc.

You also can perform call via `call` method from Client:

```python
from nemnis import Client

nis = Client()
nis.call('GET', 'heartbeat')
nis.call('GET', 'account/get', params={'address':'SOMEADDRESS'})
nis.call('POST', 'local/chain/blocks-after', payload={'height': 100})
```
Also, each parent resource can be initialized separately by passing client instance as parameter:

```python
from nemnis import Client, Node

nis = Client()

node = Node(nis)

node_info = node.info()

print(node_info.status_code)

print(node_info.json())
```

If you are looking for async stuff, please, read this:
[asynchronous-requests](http://docs.python-requests.org/en/v0.10.6/user/advanced/#asynchronous-requests).

Have fun!





