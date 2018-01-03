# python-nis-client

Python client for [NEM NIS API](https://nemproject.github.io). 

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
from nemnis import Client, explain_status

nis = Client()

hb = nis.heartbeat()

status = nis.status()

print(status.json())

# you can use following function to get verbose message for status
print(explain_status(status.json()))  

print(hb.status_code)

print(hb.json())

acc = nis.account.get('NCKMNCU3STBWBR7E3XD2LR7WSIXF5IVJIDBHBZQT')

print(acc.status_code)

print(acc.json())

### You can connect to other nodes just by passing it address:
new_client =  Client('http://157.7.223.222:7890')

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

### Asynchronous Usage

On Python 3.4.2 and above, the python-nis-client supports asynchronous requests using the `aiohttp` library. Each method returns an asyncio coroutine returning a response object; otherwise, the API is identical to the standard client.

Three helper functions are also provided for the asynchronous API:
    - `loop()`          Returns the asyncio event loop.
    - `run(future)`     Evaluate a single asyncio coroutine or future.
    - `map(futures)`    Evaluate a sequence of asyncio coroutines or futures.

Examples of usage:
```python
import nemnis

# get our client
nis = nemnis.AsyncioClient()

# request a single NIS resource
hb = nis.run(nis.heartbeat())
print(nis.run(hb.json()))

# request many NIS resources asynchronously
hb = nis.heartbeat()
status = nis.status()
responses = nemnis.map([hb, status])
print(nis.map([i.json() for i in responses]))
```

Have fun!
