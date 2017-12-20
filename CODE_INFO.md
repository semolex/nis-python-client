
## nis-python-client code guide
#### main module: nemnis

----------

### Requirements:

[requests](http://python-requests.org/en/master/)
[requests-mock](http://requests-mock.readthedocs.io/en/latest/)

----------


### Classes:

- #### [Account](#class-account)

- #### [BlockChain](#class-blockchain)

- #### [Client](#class-client)

- #### [Debug](#class-debug)

- #### [Namespace](#class-namespace)

- #### [Node](#class-node)

- #### [Transaction](#class-transaction)

----------
  
### class **Account**

_Implements [account](https://nemproject.github.io/#account-related-requests) related methods from API._


#### Methods:  

- #### **\_\_init\_\_**(self, client)
	Initialize self.  See `help(type(self))` for accurate signature.

	- **client**: Client instance
    

- #### **generate**(self)
	Implements [generating-new-account-data](https://nemproject.github.io/#generating-new-account-data).  
	Generates a [**KeyPairViewModel**](https://nemproject.github.io/#keyPairViewModel).

- #### **get**(self, address)
	Implements [requesting-the-account-data](https://nemproject.github.io/#requesting-the-account-data).  
	Gets an [**AccountMetaDataPair**](https://nemproject.github.io/#accountMetaDataPair) for an account.  
	If the address parameter is not valid, NIS returns an error.  
   
	- **address**: the address of the account.

- #### **get_forwarded**(self, address)
	Implements [requesting-the-original-account-data-for-a-delegate-account](https://nemproject.github.io/#requesting-the-original-account-data-for-a-delegate-account).  
	Given a delegate (formerly known as remote) account's address,  
	gets the [**AccountMetaDataPair**](https://nemproject.github.io/#accountMetaDataPair) for the account for which the given account	is the delegate account. If the given account address is not a delegate  
	account for any account, the request returns the [**AccountMetaDataPair**](https://nemproject.github.io/#accountMetaDataPair) for the given address.  
	If the address parameter is not valid, NIS returns an error.  
   
	- **address**: the address of the delegate account.

- #### **get\_forwarded\_from\_public\_key**(self, pub_key)

	Implements [requesting-the-original-account-data-for-a-delegate-account](https://nemproject.github.io/#requesting-the-original-account-data-for-a-delegate-account).  
	Alternative to ***get_forwarded*** method. You can retrieve the original  
	account data by providing the public key of the delegate account.  
	If the public key parameter is not valid, NIS returns an error.  
   
	- **pub_key**: the public key of the account as hex string.

- #### **get\_from\_public\_key**(self, pub_key)

	Implements [requesting-the-account-data](https://nemproject.github.io/#requesting-the-account-data).  
	Alternative to ***get*** method. You can retrieve the account data  
	by providing the public key for the account.  
	If the public key parameter is not valid, NIS returns an error  
   
	- **pub_key**: The public key of the account as hex string.

- #### **harvests**(self, address, _hash)

	Implements [requesting-harvest-info-data-for-an-account](https://nemproject.github.io/#requesting-harvest-info-data-for-an-account).  
	Gets an array of harvest info objects for an account.  
	If the address parameter is not valid or the hash cannot be found in  
	the database, NIS returns an error.  
   
	- **address**: the address of the account.  
	- **\_hash**: the 256 bit sha3 hash of the block up to which harvested blocks are returned.

- #### **historical_get**(self, address, start\_height, end\_height, inc)

    Implements [retrieving-historical-account-data](https://nemproject.github.io/#retrieving-historical-account-data). 
    Gets historical information for an account.  
    To turn on this feature for your NIS, you need to add  
    ***HISTORICAL\_ACCOUNT\_DATA*** to the list of optional features in the file  
    ***config.properties***.  
    If the address is invalid, the ***start_height*** is larger than the  
    ***end_height***, the increment is not a positive or the request results in  
    more than 1000 data points an error is returned.  

    - **address**: the address of the account.  
    
    - **start\_height**: the block height from which on the data should be supplied.  
    
    - **end\_height**: the block height up to which the data should be supplied. The end height must be greater than or equal to the start height.
    
    - **inc**: The value by which the height is incremented between each data point. The value must be greater than _0_. NIS can supply up to _1000_ data points with one request. Requesting more than _1000_ data points results in an error.

- #### **importances**(self)

	Implements [retrieving-account-importances-for-accounts](https://nemproject.github.io/#retrieving-account-importances-for-accounts).  
	Gets an array of account importance view model objects.

- #### **lock**(self, private_key)

	Implements [locking-and-unlocking-accounts](https://nemproject.github.io/#locking-and-unlocking-accounts)  
	Locks an account (stops harvesting).  
	Request return an error if the private key does not correspond to a  
	known account or the account is not allowed to harvest.  
   
	- **private_key**: A [**PrivateKey**](https://nemproject.github.io/#privateKey) JSON object
       

- #### **mosaic\_definition\_page**(self, address, parent, _id)

	Implements [retrieving-mosaic-definitions-that-an-account-has-created](https://nemproject.github.io/#retrieving-mosaic-definitions-that-an-account-has-created).  
	Gets an array of mosaic definition objects for a given account address.  
	If ***parent*** param is supplied, only mosaic definitions for the given  
    parent namespace are returned.  
    NIS returns an error if the address, the parent (if supplied)  
    or the id (if supplied) is invalid.  
   
	- **address**: the address of the account.  
	- **parent**: _(optional)_ parent namespace id.  
	- **\_id**: _(optional)_ mosaic definition database id up to which mosaic  
        definitions are returned.

- #### **mosaic_owned**(self, address)

    Implements [retrieving-mosaics-that-an-account-owns](https://nemproject.github.io/#retrieving-mosaics-that-an-account-owns).  
    Gets an array of mosaic objects for a given account address.  
    NIS returns an error if the address is invalid.  

    - **address**: the address of the account.

- #### **namespace_page**(self, address, parent, \_id, page\_size=None)

    Implements [retrieving-namespaces-that-an-account-owns](https://nemproject.github.io/#retrieving-namespaces-that-an-account-owns).  
    Gets an array of namespace objects for a given account address.  
    If **parent** param is supplied, only sub-namespaces of the parent  
    namespace are returned.  
    NIS returns an error if the address or the parent (if supplied)  
    is invalid.  
   
    - **address**: the address of the account.  
    - **parent**: _(optional)_ parent namespace id.  
    - **\_id**: _(optional)_ namespace database id up to which namespaces  are returned.  
    - **page_size:** _(optional)_ number of namespaces to be returned.

- #### **status**(self, address)

    Implements [requesting-the-account-status](https://nemproject.github.io/#requesting-the-account-status).  
    Gets the \`AccountMetaData\` from an account  
    (https://nemproject.github.io/#accountMetaData).  
    If the address parameter is not valid, NIS returns an error.  

    - **address**: the address of the account.

- #### **transfers_all**(self, address, \_hash, \_id=None)

	Implements [requesting-transaction-data-for-an-account](https://nemproject.github.io/#requesting-transaction-data-for-an-account)  
	Gets an array of transaction meta data pairs for which an account is  
	the sender or receiver. A maximum of _25_ transaction meta data pairs  
	is returned.  
	If the address parameter is not valid or the id cannot be found in the  
	database, NIS returns an error.  
   
	- **address**: the address of the account.  
	- **\_hash**: _(optional)_ the 256 bit sha3 hash of the transaction up to 			which transactions are returned.  
	- **\_id**: _(optional)_ the transaction id up to which transactions are  
returned.

- #### **transfers_incoming**(self, address, \_hash=None, \_id=None)

    Implements [requesting-transaction-data-for-an-account ](https://nemproject.github.io/#requesting-transaction-data-for-an-account).  
    Gets an array of [**TransactionMetaDataPair**](https://nemproject.github.io/#transactionMetaDataPair) objects.    
    Has the address given as parameter to the request. A maximum of _25_  
    transaction meta data pairs is returned. The returned transaction meta  
    data pairs are sorted in descending order in which they were written  
    to the database.  
    If the address parameter is not valid or the id cannot be found in the  
    database, NIS returns an error.  

    - **address**: the address of the account.  
    - **\_hash**: _(optional)_ the 256 bit sha3 hash of the transaction up to  
            which transactions are returned.  
    - **\_id**: _(optional)_ the transaction id up to which transactions are  
                returned.

- #### **transfers_outgoing**(self, address, \_hash=None, \_id=None)

    Implements [requesting-transaction-data-for-an-account](https://nemproject.github.io/#requesting-transaction-data-for-an-account).  
    Gets an array of transaction meta data pairs where the recipient has  
    the address given as parameter to the request.  
    A maximum of _25_ transaction meta data pairs is returned.  
    f the address parameter is not valid or the id cannot be found in the  
    database, NIS returns an error.  
   
	- **address**: the address of the account.  
	- **\_hash**: _(optional)_ the 256 bit sha3 hash of the transaction up to  
        which transactions are returned.  
	- **\_id**: _(optional)_ the transaction id up to which transactions are  
            returned.

- #### **unconfirmed_transactions**(self, address)

    Implements [requesting-transaction-data-for-an-account](https://nemproject.github.io/#requesting-transaction-data-for-an-account).  
    Gets the array of transactions for which an account is the sender or  
    receiver and which have not yet been included in a block. The returned  
    structure is [**UnconfirmedTransactionMetaDataPair**](https://nemproject.github.io/#unconfirmedTransactionMetaDataPair).     
    If the address parameter is not valid, NIS returns an error.  
   
	- **address**: the address of the account.

- #### **unlock**(self, private_key)

    Implements [locking-and-unlocking-accounts](https://nemproject.github.io/#locking-and-unlocking-accounts)  
    Unlocks an account (starts harvesting).  
    Request return an error if the private key does not correspond to a  
    known account or the account is not allowed to harvest.  
   
	- **private_key**: A [**PrivateKey**](https://nemproject.github.io/#privateKey) JSON object.  
       

- #### **unlocked_info**(self)

    Implements [retrieving-the-unlock-info](https://nemproject.github.io/#retrieving-the-unlock-info).  
    Gives information about the maximum number of allowed harvesters and  
    how many harvesters are already using the node.

   
### class **BlockChain**

_Implements [block chain](https://nemproject.github.io/#block-chain-related-requests  ) related methods from API._  

#### Methods:

- #### **\_\_init\_\_**(self, client)

    Initialize self.  See `help(type(self))` for accurate signature.
    
    - **client**: Client instance

- #### **at_public**(self, block_height)

    Gets a block from the chain that has the given height.  
    If the block with the specified height cannot be found in the database,  
    NIS will return a JSON error object.  
   
	- **block_height**: A [**BlockHeight**](https://nemproject.github.io/#blockHeight) JSON object.  
     
- #### **height**(self)

	Gets the current height of the block chain.

- #### **last_block**(self)

	Gets the current last block of the chain.

- #### **local\_chain\_blocks_after**(self, block_height)

    Gets up to _10_ blocks after given block height from the chain.  
    The returned data is an array of [**ExplorerBlockViewModel**](https://nemproject.github.io/#explorerBlockViewModel) JSON objects.     
    If the block height supplied is not positive, NIS will return a  
    JSON error object.  
   
	- **block_height**: A [**BlockHeight**](https://nemproject.github.io/#blockHeight) JSON object. 
      
- #### **score**(self)

	Gets the current score of the block chain.

   
### class **Client**

_Class that represents main API client.Make calls to NIS via related methods.  
For all required information, please follow:_  
[here](https://nemproject.github.io/).  
_All available methods documentation is also can be found there._  
 

#### Methods:  

- #### **\_\_init\_\_**(self, endpoint='http://127.0.0.1:7890')

	Initialize client. 
   
	- **endpoint**: address of the NIS.

- #### **call**(self, method, name, params=None, payload=None, \**kwargs)

    Make calls to the API via HTTP methods and passed params.  
    Methods that uses this method returns response object.
    
	- **method**: HTTP method of the request ('GET', 'POST').  
	- **name**: name of the API endpoint method. Appends to base URL.  
	- **params**: GET method params, used when method is GET.  
	- **payload**: POST method data, used when method is POST.  
	- **kwargs**: any additional arguments.  
	- ***return***: [response](http://docs.python-requests.org/en/master/api/#requests.Response) object.

- #### **heartbeat**(self)

    Implements [heart-beat-request](https://nemproject.github.io/#heart-beat-request).  
    Determines if NIS is up and responsive.  
    If there is no response to this request, NIS is either not running or  
    is in a state where it can't serve requests.

- #### **status**(self)

    Implements [status-request](https://nemproject.github.io/#status-request)  
    Determines the status of NIS.  
    If there is no response to this request, NIS is either not running or  
    is in a state where it can't serve requests


#### Properties:

- #### **account**

    Represents account related requests from API.  

    - ***return***: Account instance for use with it's methods.

- #### **blockchain**

    Represents block chain related requests from API.  

    - ***return***: BlockChain instance for use with it's methods.

- #### **debug**

    Represents requests for additional information from NIS.  

    - ***return***: Debug instance for use with its methods.

- #### **namespace**

    Represents namespaces related requests from API.  

    - ***return***: Namespace instance for use with its methods.

- #### **node**

    Represents node related requests from API.  

    - ***return***: Node instance for use with its methods.

- #### **transaction**

	Represents transaction related requests methods from API.  
   
	- ***return***: Transaction instance for use with its methods.

   
### class **Debug**

_Implements requests for [additional information](https://nemproject.github.io/#requests-for-additional-information-from-NIS) from NIS._
  

#### Methods:

- **\_\_init\_\_**(self, client)

	Initialize self.  See `help(type(self))` for accurate signature.
    
	- **client**: Client instance

- **connections_incoming**(self)

	Gets an audit collection of incoming calls.  
	You can monitor the outstanding and recent incoming requests with  
	this information.

- **connections_outgoing**(self)

	Gets an audit collection of outgoing calls.  
	You can monitor the outstanding and recent outgoing requests with  
	this information.

- **time_synchronization**(self)

	Gets an array of time synchronization results.  
	You can monitor the change in network time with this information.
    
    
- **timers**(self)

    Gets an array of task monitor structures.  
    You can monitor the statistics for periodic tasks with  
    this information.

   
### class **Namespace**

_Implements [namespace related](https://nemproject.github.io/#namespaces-and-mosaics  ) methods from API._  

#### Methods: 

- **\_\_init\_\_**(self, client)

	Initialize self.  See `help(type(self))` for accurate signature.
    
	- **client**: Client instance

- **mosaic\_definition\_page**(self, namespace, \_id=None, pagesize=25)

	Gets the mosaic definitions for a given namespace.  
   
	- **namespace**: the namespace id.  
	- **\_id**: _(optional)_ the topmost mosaic definition database id up to  
        which root mosaic definitions are returned.  
        The parameter is optional. If not supplied the most recent  
        mosaic definitiona are returned.  
	- **pagesize**: the number of mosaic definition objects to be returned  
       	for each request. The parameter is optional. The default value  
       	is _25_, the minimum value is _5_ and hte maximum value is _100_.

- **namespace**(self, namespace)

	Gets the namespace with given id.  
   
	- **namespace**: the namespace id.

- **root_page**(self, \_id=None, page\_size=25)

	Gets the root namespaces.  
   
	- **\_id**: _(optional)_ the topmost namespace database id up to which  
            root namespaces are returned  
	- **page_size**: _(optional )_the number of namespace objects to be  
       	returned for each request. The parameter is optional.  
       	The default value is _25_, the minimum value is _5_ and hte maximum  
       	value is _100_.

   
class **Node**

_Implements [node](https://nemproject.github.io/#block-chain-related-requests  ) related methods from API._  


#### Methods:

- **\_\_init\_\_**(self, client)

	Initialize self.  See help(type(self)) for accurate signature.
	- **client**: Client instance    

- **boot**(self, boot\_node\_request)

	Boots the local node and thus assign an account (the identity) to  
	the local node.  
	In case the node has already been booted, NIS will return a  
	JSON error object.  
   
	- **boot\_node\_request**: A [BootNodeRequest](https://nemproject.github.io/#bootNodeRequest) JSON object.

- **experiences**(self)

    Gets an array of node experiences from another node.  
    In case the node has not been booted yet, NIS will return a  
    JSON error object.

- **extended_info**(self)

	Gets extended information about a node.  
	In case the node has not been booted yet, NIS will return a  
	JSON error object.

- **info**(self)

	Gets basic information about a node.  
	In case the node has not been booted yet, NIS will return a  
	JSON error.

- **max\_chain\_height**(self)

	Requests the chain height from every node in the active node list  
	and returns the maximum height seen.  
	In case the node has not been booted yet, NIS will return a JSON  
	error object.

- **peer\_list\_active**(self)

    Gets an array of active nodes in the neighborhood that are selected for  
    broadcasts.  
    In case the node has not been booted yet, NIS will return a  
    JSON error object.

- **peer\_list\_all**(self)

	Gets an array of all known nodes in the neighborhood.  
	In case the node has not been booted yet, NIS will return a  
	JSON error object.

- **peer\_list\_reachable**(self)

	Gets an array of all nodes with status 'active' in the neighborhood.  
	In case the node has not been booted yet, NIS will return a  
	JSON error object.
    
   
### class **Transaction**

_Implements [transaction](https://nemproject.github.io/#initiating-transactions  ) related methods from API. _ 
_According to documentation, should be used with care!_  

#### Methods:

- **\_\_init\_\_**(self, client)

	Initialize self.  See `help(type(self))` for accurate signature.
    - **client**: Client instance 

- **announce**(self, request_announce)

	Creates and broadcasts a transaction. The private key is not involved.  
   
   	- **request_announce**: A [**RequestAnnounce**](https://nemproject.github.io/#requestAnnounce) JSON object.
       

- **prepare_announce**(self, request_announce)

    Creates and broadcasts a transaction. Since this request involves the private key of an account, it should only be sent to a local NIS. There are various errors that can occur due to failure of transaction validation.  
	- **request_announce**: A [**requestPrepareAnnounce**](https://nemproject.github.io/#requestPrepareAnnounce) JSON object.  

