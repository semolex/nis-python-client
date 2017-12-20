import requests


class Client:
    """
    Class that represents main API client.
    Make calls to NIS via related methods.
    For all required information, please follow:
    https://nemproject.github.io/
    All available methods documentation is also can be found there.
    """
    def __init__(self, endpoint='http://127.0.0.1:7890'):
        """
        Initialize client.

        :param endpoint: address of the NIS.
        """
        self.endpoint = endpoint

    def call(self, method, name, params=None, payload=None, **kwargs):
        """
        Make calls to the API via HTTP methods and passed params.
        Methods that uses this method returns response object.

        :param method: HTTP method of the request.
        :param name: name of the API endpoint method. Appends to base URL.
        :param params: GET method params, used when method is GET.
        :param payload: POST method data, used when method is POST.
        :param kwargs: any additional arguments.
        :return: response object
        """
        url = self.endpoint + '/' + name
        resp = requests.request(method, url, params=params, json=payload,
                                **kwargs)
        return resp

    def heartbeat(self):
        """
        Implements https://nemproject.github.io/#heart-beat-request
        Determines if NIS is up and responsive.
        If there is no response to this request, NIS is either not running or
        is in a state where it can't serve requests.
        """
        return self.call('GET', 'heartbeat')

    def status(self):
        """
        Implements https://nemproject.github.io/#status-request
        Determines the status of NIS.
        If there is no response to this request, NIS is either not running or
        is in a state where it can't serve requests
        """
        return self.call('GET', 'status')

    @property
    def account(self):
        """
        Represents account related requests from API.

        :return: Account instance for use with it's methods.
        """
        return Account(self)

    @property
    def blockchain(self):
        """
        Represents block chain related requests from API.

        :return: BlockChain instance for use with its methods.
        """
        return BlockChain(self)

    @property
    def node(self):
        """
        Represents node related requests from API.

        :return: Node instance for use with its methods.
        """
        return Node(self)

    @property
    def namespace(self):
        """
        Represents namespaces related requests from API.

        :return: Namespace instance for use with its methods.
        """
        return Namespace(self)

    @property
    def transaction(self):
        """
        Represents transaction related requests methods from API.

        :return: Transaction instance for use with its methods.
        """
        return Transaction(self)

    @property
    def debug(self):
        """
        Represents requests for additional information from NIS.

        :return: Transaction instance for use with its methods.
        """
        return Debug(self)


class Account:
    """
    Implements account related methods from API.
    https://nemproject.github.io/#account-related-requests
    """
    def __init__(self, client):
        self.name = 'account/'
        self.client = client

    def generate(self):
        """
        Implements https://nemproject.github.io/#generating-new-account-data
        Generates a `KeyPairViewModel`
        (https://nemproject.github.io/#keyPairViewModel).
        """
        return self.client.call('GET', self.name + 'generate')

    def get(self, address):
        """
        Implements https://nemproject.github.io/#requesting-the-account-data
        Gets an `AccountMetaDataPair` for an account
        (https://nemproject.github.io/#accountMetaDataPair).
        If the address parameter is not valid, NIS returns an error.

        :param address: the address of the account.
        """
        return self.client.call('GET', self.name + 'get',
                                params={'address': address})

    def get_from_public_key(self, pub_key):
        """
        Implements https://nemproject.github.io/#requesting-the-account-data
        Alternative to `get` method. You can retrieve the account data
        by providing the public key for the account.
        If the public key parameter is not valid, NIS returns an error

        :param pub_key: The public key of the account as hex string.
        """
        return self.client.call('GET', self.name + 'get/from-public-key',
                                params={'publicKey': pub_key})

    def get_forwarded(self, address):
        """
        Implements https://nemproject.github.io/#requesting-the-original-account-data-for-a-delegate-account
        Given a delegate (formerly known as remote) account's address,
        gets the AccountMetaDataPair for the account for which the given account
        is the delegate account. If the given account address is not a delegate
        account for any account, the request returns the `AccountMetaDataPair `
        for the given address
        (https://nemproject.github.io/#accountMetaDataPair).
        If the address parameter is not valid, NIS returns an error.

        :param address: the address of the delegate account.

        """
        return self.client.call('GET', self.name + 'get/forwarded',
                                params={'address': address})

    def get_forwarded_from_public_key(self, pub_key):
        """
        Implements https://nemproject.github.io/#requesting-the-original-account-data-for-a-delegate-account
        Alternative to `get_forwarded` method. You can retrieve the original
        account data by providing the public key of the delegate account.
        If the public key parameter is not valid, NIS returns an error.

        :param pub_key: the public key of the account as hex string.
        """
        return self.client.call('GET',
                                self.name + 'get/forwarded/from-public-key',
                                params={'publicKey': pub_key})

    def status(self, address):
        """
        Implements https://nemproject.github.io/#requesting-the-account-status
        Gets the `AccountMetaData` from an account
        (https://nemproject.github.io/#accountMetaData).
        If the address parameter is not valid, NIS returns an error.

        :param address: the address of the account.
        """
        return self.client.call('GET', self.name + 'status',
                                params={'address': address})

    def transfers_incoming(self, address, _hash=None, _id=None):
        """
        Implements https://nemproject.github.io/#requesting-transaction-data-for-an-account
        Gets an array of `TransactionMetaDataPair` objects
        (https://nemproject.github.io/#transactionMetaDataPair)
        has the address given as parameter to the request. A maximum of 25
        transaction meta data pairs is returned. The returned transaction meta
        data pairs are sorted in descending order in which they were written
        to the database.
        If the address parameter is not valid or the id cannot be found in the
        database, NIS returns an error.

        :param address: the address of the account.
        :param _hash: (optional) the 256 bit sha3 hash of the transaction up to
                which transactions are returned.
        :param _id: (optional) the transaction id up to which transactions are
                    returned.
        """
        return self.client.call('GET', self.name + 'transfers/incoming',
                                params={'address': address,
                                        'hash': _hash,
                                        'id': _id})

    def transfers_outgoing(self, address, _hash=None, _id=None):
        """
        Implements https://nemproject.github.io/#requesting-transaction-data-for-an-account
        Gets an array of transaction meta data pairs where the recipient has
        the address given as parameter to the request.
        A maximum of 25 transaction meta data pairs is returned.
        f the address parameter is not valid or the id cannot be found in the
        database, NIS returns an error.

        :param address: the address of the account.
        :param _hash: (optional) the 256 bit sha3 hash of the transaction up to
                which transactions are returned.
        :param _id: (optional) the transaction id up to which transactions are
                    returned.
        """
        return self.client.call('GET', self.name + 'transfers/outgoing',
                                params={'address': address,
                                        'hash': _hash,
                                        'id': _id})

    def transfers_all(self, address, _hash, _id=None):
        """
        Implements https://nemproject.github.io/#requesting-transaction-data-for-an-account
        Gets an array of transaction meta data pairs for which an account is
        the sender or receiver. A maximum of 25 transaction meta data pairs
        is returned.
        If the address parameter is not valid or the id cannot be found in the
        database, NIS returns an error.

        :param address: the address of the account.
        :param _hash: (optional) the 256 bit sha3 hash of the transaction up to
                which transactions are returned.
        :param _id: (optional) the transaction id up to which transactions are
                    returned.
        """
        return self.client.call('GET', self.name + 'transfers/all',
                                params={'address': address,
                                        'hash': _hash,
                                        'id': _id})

    def unconfirmed_transactions(self, address):
        """
        Implements https://nemproject.github.io/#requesting-transaction-data-for-an-account
        Gets the array of transactions for which an account is the sender or
        receiver and which have not yet been included in a block. The returned
        structure is UnconfirmedTransactionMetaDataPair
        (https://nemproject.github.io/#unconfirmedTransactionMetaDataPair)
        If the address parameter is not valid, NIS returns an error.

        :param address: the address of the account.
        """
        return self.client.call('GET', self.name + 'unconfirmedTransactions',
                                params={'address': address})

    def _transfers_incoming(self, private_key, _hash=None, _id=None):
        """
        Implements https://nemproject.github.io/#transaction-data-with-decoded-messages
        The request returns outgoing transactions as described in the
        `transfers_incoming` method. The only difference is that if a
        transaction contains an encoded message, this message will be decoded
        before it is sent to the requester.
        If the private key is not supplied, NIS returns an error.

        :param private_key: the private key as hexadecimal string.
        :param (optional) hash value.
        :param (optional) transaction id.
        """
        return self.client.call('POST', 'local/transfers/incoming',
                                payload={'value': private_key,
                                         'hash': _hash,
                                         'id': _id})

    def _transfers_outgoing(self, private_key, _hash=None, _id=None):
        """
        Implements https://nemproject.github.io/#transaction-data-with-decoded-messages
        The request returns outgoing transactions as described in the
        `transfers_outgoing` method. The only difference is that if a
        transaction contains an encoded message, this message will be decoded
        before it is sent to the requester.
        If the private key is not supplied, NIS returns an error.

        :param private_key: the private key as hexadecimal string.
        :param (optional) hash value.
        :param (optional) transaction id.
        """
        return self.client.call('POST', 'local/transfers/outgoing',
                                payload={'value': private_key,
                                         'hash': _hash,
                                         'id': _id})

    def _transfers_all(self, private_key, _hash=None, _id=None):
        """
        Implements https://nemproject.github.io/#transaction-data-with-decoded-messages
        The request returns all transactions as described in the `transfers_all`
        method. The only difference is that if a transaction contains an
        encoded message, this message will be decoded before it is sent
        to the requester.
        If the private key is not supplied, NIS returns an error.

        :param private_key: the private key as hexadecimal string.
        :param (optional) hash value.
        :param (optional) transaction id.
        """
        return self.client.call('POST', 'local/transfers/all',
                                payload={'value': private_key,
                                         'hash': _hash,
                                         'id': _id})

    def harvests(self, address, _hash):
        """
        Implements https://nemproject.github.io/#requesting-harvest-info-data-for-an-account
        Gets an array of harvest info objects for an account.
        If the address parameter is not valid or the hash cannot be found in
        the database, NIS returns an error.

        :param address: the address of the account.
        :param _hash: the 256 bit sha3 hash of the block up to which harvested
               blocks are returned.
        """
        return self.client.call('GET', self.name + 'harvests',
                                params={'address': address, 'hash': _hash})

    def importances(self):
        """
        Implements https://nemproject.github.io/#retrieving-account-importances-for-accounts
        Gets an array of account importance view model objects.
        """
        return self.client.call('GET', self.name + 'importances')

    def namespace_page(self, address, parent, _id, page_size=None):
        """
        Implements https://nemproject.github.io/#retrieving-namespaces-that-an-account-owns
        Gets an array of namespace objects for a given account address.
        If `parent` param is supplied, only sub-namespaces of the parent
        namespace are returned.
        NIS returns an error if the address or the parent (if supplied)
        is invalid.

        :param address: the address of the account.
        :param parent: (optional) parent namespace id.
        :param _id: (optional) namespace database id up to which namespaces
                are returned.
        :param page_size: (optional) number of namespaces to be returned.
        """
        return self.client.call('GET', self.name + 'namespace/page',
                                params={'address': address,
                                        'parent': parent,
                                        'id': _id,
                                        'pageSize': page_size})

    def mosaic_definition_page(self, address, parent, _id):
        """
        Implements https://nemproject.github.io/#retrieving-mosaic-definitions-that-an-account-has-created
        Gets an array of mosaic definition objects for a given account address.
        If `parent` param is supplied, only mosaic definitions for the given
        parent namespace are returned.
        NIS returns an error if the address, the parent (if supplied)
        or the id (if supplied) is invalid.

        :param address: the address of the account.
        :param parent: (optional) parent namespace id.
        :param _id: (optional) mosaic definition database id up to which mosaic
               definitions are returned.
        """
        return self.client.call('GET', self.name + 'mosaic/definition/page',
                                params={'address': address,
                                        'parent': parent,
                                        'id': _id})

    def mosaic_owned(self, address):
        """
        Implements https://nemproject.github.io/#retrieving-mosaics-that-an-account-owns
        Gets an array of mosaic objects for a given account address.
        NIS returns an error if the address is invalid.

        :param address: the address of the account.
        """
        return self.client.call('GET', self.name + 'mosaic/owned',
                                params={'address': address})

    def unlock(self, private_key):
        """
        Implements https://nemproject.github.io/#locking-and-unlocking-accounts
        Unlocks an account (starts harvesting).
        Request return an error if the private key does not correspond to a
        known account or the account is not allowed to harvest.

        :param private_key: A PrivateKey JSON object:
               (https://nemproject.github.io/#privateKey)
        """
        return self.client.call('POST', self.name + 'unlock',
                                payload={'value': private_key})

    def lock(self, private_key):
        """
        Implements https://nemproject.github.io/#locking-and-unlocking-accounts
        Locks an account (stops harvesting).
        Request return an error if the private key does not correspond to a
        known account or the account is not allowed to harvest.

        :param private_key: A PrivateKey JSON object:
               (https://nemproject.github.io/#privateKey)
        """
        return self.client.call('POST', self.name + 'lock',
                                payload={'value': private_key})

    def unlocked_info(self):
        """
        Implements https://nemproject.github.io/#retrieving-the-unlock-info
        Gives information about the maximum number of allowed harvesters and
        how many harvesters are already using the node.
        """
        return self.client.call('POST', self.name + 'unlocked/info')

    def historical_get(self, address, start_height, end_height, inc):
        """
        Implements https://nemproject.github.io/#retrieving-historical-account-data
        Gets historical information for an account.
        To turn on this feature for your NIS, you need to add
        `HISTORICAL_ACCOUNT_DATA` to the list of optional features in the file
        `config.properties`.
        If the address is invalid, the `start_height` is larger than the
        `end_height`, the increment is not a positive or the request results in
        more than 1000 data points an error is returned.

        :param address: the address of the account.
        :param start_height: the block height from which on the data
               should be supplied.
        :param end_height: the block height up to which the data should be
               supplied. The end height must be greater than or equal to the
               start height.
        :param inc: The value by which the height is incremented between each
                    data point. The value must be greater than 0.
                    NIS can supply up to 1000 data points with one request.
                    Requesting more than 1000 data points results in an error.
        """
        return self.client.call('GET', self.name + 'historical/get',
                                params={'address': address,
                                        'startHeight': start_height,
                                        'endHeight': end_height,
                                        'increment': inc})


class BlockChain:
    """
    Implements block chain related methods from API.
    https://nemproject.github.io/#block-chain-related-requests
    """
    def __init__(self, client):
        self.name = 'chain/'
        self.client = client

    def height(self):
        """
        Gets the current height of the block chain.
        """
        return self.client.call('GET', self.name + 'height')

    def score(self):
        """
        Gets the current score of the block chain.
        """
        return self.client.call('GET', self.name + 'score')

    def last_block(self):
        """
        Gets the current last block of the chain.

        """
        return self.client.call('GET', self.name + 'last-block')

    def at_public(self, block_height):
        """
        Gets a block from the chain that has the given height.
        If the block with the specified height cannot be found in the database,
        NIS will return a JSON error object.

        :param block_height: A `BlockHeight` JSON object
               (https://nemproject.github.io/#blockHeight).
        """
        return self.client.call('POST', 'block/at/public', payload={
            'height': block_height
        })

    def local_chain_blocks_after(self, block_height):
        """
        Gets up to 10 blocks after given block height from the chain.
        The returned data is an array of `ExplorerBlockViewModel` JSON objects
        (https://nemproject.github.io/#explorerBlockViewModel).
        If the block height supplied is not positive, NIS will return a
        JSON error object.

        :param block_height: A `BlockHeight` JSON object
               (https://nemproject.github.io/#blockHeight).
        """
        return self.client.call('POST', 'local/chain/blocks-after', payload={
            'height': block_height
        })


class Node:
    """
    Implements node related methods from API.
    https://nemproject.github.io/#node-related-requests
    """
    def __init__(self, client):
        self.name = 'node/'
        self.client = client

    def info(self):
        """
        Gets basic information about a node.
        In case the node has not been booted yet, NIS will return a
        JSON error object.
        """
        return self.client.call('GET', self.name + 'info')

    def extended_info(self):
        """
        Gets extended information about a node.
        In case the node has not been booted yet, NIS will return a
        JSON error object.
        """
        return self.client.call('GET', self.name + 'extended-info')

    def peer_list_all(self):
        """
        Gets an array of all known nodes in the neighborhood.
        n case the node has not been booted yet, NIS will return a
        JSON error object.
        """
        return self.client.call('GET', self.name + 'peer-list/all')

    def peer_list_reachable(self):
        """
        Gets an array of all nodes with status 'active' in the neighborhood.
        In case the node has not been booted yet, NIS will return a
        JSON error object.
        """
        return self.client.call('GET', self.name + 'peer-list/reachable')

    def peer_list_active(self):
        """
        Gets an array of active nodes in the neighborhood that are selected for
        broadcasts.
        In case the node has not been booted yet, NIS will return a
        JSON error object.
        """
        return self.client.call('GET', self.name + 'peer-list/active')

    def max_chain_height(self):
        """
        Requests the chain height from every node in the active node list
        and returns the maximum height seen.
        In case the node has not been booted yet, NIS will return a JSON
        error object.
        """
        return self.client.call('GET',
                                self.name + 'active-peers/max-chain-height')

    def experiences(self):
        """
        Gets an array of node experiences from another node.
        In case the node has not been booted yet, NIS will return a
        JSON error object.
        """
        return self.client.call('GET',
                                self.name + 'experiences')

    def boot(self, boot_node_request):
        """
        Boots the local node and thus assign an account (the identity) to
        the local node.
        In case the node has already been booted, NIS will return a
        JSON error object.

        :param boot_node_request: A `BootNodeRequest` JSON object
               (https://nemproject.github.io/#bootNodeRequest)
        """
        return self.client.call('POST',
                                self.name + 'boot', payload=boot_node_request)


class Namespace:
    """
    Implements namespace related methods from API.
    https://nemproject.github.io/#namespaces-and-mosaics
    """
    def __init__(self, client):
        self.name = 'namespace/'
        self.client = client

    def root_page(self, _id=None, page_size=25):
        """
        Gets the root namespaces.

        :param _id: (optional) the topmost namespace database id up to which
                    root namespaces are returned
        :param page_size: (optional )the number of namespace objects to be
               returned for each request. The parameter is optional.
               The default value is 25, the minimum value is 5 and hte maximum
               value is 100.
        """
        return self.client.call('GET',
                                self.name + 'root/page',
                                params={'id': _id, 'pageSize': page_size})

    def namespace(self, namespace):
        """
        Gets the namespace with given id.

        :param namespace: the namespace id.
        """
        return self.client.call('GET',
                                self.name, params={'namespace': namespace})

    def mosaic_definition_page(self, namespace, _id=None, pagesize=25):
        """
        Gets the mosaic definitions for a given namespace.

        :param namespace: the namespace id.
        :param _id: (optional) the topmost mosaic definition database id up to
                which root mosaic definitions are returned.
                The parameter is optional. If not supplied the most recent
                mosaic definitiona are returned.
        :param pagesize: he number of mosaic definition objects to be returned
               for each request. The parameter is optional. The default value
               is 25, the minimum value is 5 and hte maximum value is 100.
        """
        return self.client.call('GET',
                                self.name + 'mosaic/definition/page',
                                params={'namespace': namespace, 'id': _id,
                                        'pagesize': pagesize})


class Transaction:
    """
    Implements transaction related methods from API.
    According to documentation, should be used with care!
    https://nemproject.github.io/#initiating-transactions
    """
    def __init__(self, client):
        self.name = 'transaction/'
        self.client = client

    def prepare_announce(self, request_announce):
        """
        Creates and broadcasts a transaction. Since this request involves t
        he private key of an account, it should only be sent to a local NIS.
        There are various errors that can occur due to failure of transaction
        validation.
        :param request_announce: `requestPrepareAnnounce` JSON object
               (https://nemproject.github.io/#requestPrepareAnnounce)
        """
        return self.client.call('POST',
                                self.name + 'prepare-announce',
                                payload=request_announce)

    def announce(self, request_announce):
        """
        Creates and broadcasts a transaction. The private key is not involved.

        :param request_announce: A `RequestAnnounce` JSON object
               (https://nemproject.github.io/#requestAnnounce)
        """
        return self.client.call('POST',
                                self.name + 'announce',
                                payload=request_announce)


class Debug:
    """
    Implements requests for additional information from NIS.
    https://nemproject.github.io/#requests-for-additional-information-from-NIS
    """
    def __init__(self, client):
        self.name = 'debug/'
        self.client = client

    def time_synchronization(self):
        """
        Gets an array of time synchronization results.
        You can monitor the change in network time with this information.
        """
        return self.client.call('GET', self.name + 'time-synchronization')

    def connections_incoming(self):
        """
        Gets an audit collection of incoming calls.
        You can monitor the outstanding and recent incoming requests with
        this information.
        """
        return self.client.call('GET', self.name + 'connections/incoming')

    def connections_outgoing(self):
        """
        Gets an audit collection of outgoing calls.
        You can monitor the outstanding and recent outgoing requests with
        this information.
        """
        return self.client.call('GET', self.name + 'connections/outgoing')

    def timers(self):
        """
        Gets an array of task monitor structures.
        You can monitor the statistics for periodic tasks with
        this information.
        """
        return self.client.call('GET', self.name + '/timers')

