Types
=====

The following types are available from the ``eth_typing`` module.

i.e.

.. code-block:: python

    from eth_typing import TypeStr

ABI
---

TypeStr
~~~~~~~

String representation of a data type.

.. code-block:: python

    TypeStr = str

Decodable
~~~~~~~~~

Binary data to be decoded.

.. code-block:: python

    Decodable = Union[bytes, bytearray]

Enumerables
-----------

ForkName
~~~~~~~~

Class that contains the different names used to represent hard forks on the Ethereum network.

.. code-block:: python

    class ForkName:
        Frontier = 'Frontier'
        Homestead = 'Homestead'
        EIP150 = 'EIP150'
        EIP158 = 'EIP158'
        Byzantium = 'Byzantium'
        Constantinople = 'Constantinople'
        Metropolis = 'Metropolis'


ChainId
~~~~~~~

`IntEnum` class defining EVM-compatible network name enums as their respective chain id `int` values.

To learn more about chain ids, see [CAIP-2](https://github.com/ChainAgnostic/CAIPs/blob/main/CAIPs/caip-2.md) for details.

The list of chain ids is available from the [ethereum-lists/chains](https://github.com/ethereum-lists/chains) repository.

.. code-block:: python

    class ChainId(IntEnum):
        # L1 networks
    	ETH = 1
    	EXP = 2
        ROP = 3
        RIN = 4
        GOR = 5
        # L2 networks
        OETH = 10
        GNO = 100


Discovery
---------

NodeID
~~~~~~

A 32-byte identifier for a node in the Discovery DHT

.. code-block:: python

    NodeID = NewType('NodeID', bytes)


EthPM
-----

ContractName
~~~~~~~~~~~~

Any string conforming to the regular expression ``[a-zA-Z][a-zA-Z0-9_]{0,255}``.

.. code-block:: python

    ContractName = NewType('ContractName', str)

URI
~~~

Any string that represents a URI.

.. code-block:: python

    URI = NewType('URI', str)

EVM
---

Address
~~~~~~~

Any bytestring representing a canonical address.

.. code-block:: python

    Address = NewType('Address', bytes)

HexAddress
~~~~~~~~~~

Any HexStr_ representing a hex encoded address.

.. code-block:: python

    HexAddress = NewType('HexAddress', HexStr)

ChecksumAddress
~~~~~~~~~~~~~~~

Any HexAddress_ that is formatted according to ERC55_.

.. _ERC55: https://github.com/ethereum/EIPs/issues/55

.. code-block:: python

    ChecksumAddress = NewType('ChecksumAddress', HexAddress)

AnyAddress
~~~~~~~~~~

Any of Address_, HexAddress_, ChecksumAddress_.

.. code-block:: python

    AnyAddress = TypeVar('AnyAddress', Address, HexAddress, ChecksumAddress)

Hash32
~~~~~~

Any 32 byte hash.

.. code-block:: python

    Hash32 = NewType('Hash32', bytes)

BlockNumber
~~~~~~~~~~~

Any integer that represents a valid block number on a chain.

.. code-block:: python

    BlockNumber = NewType('BlockNumber', int)

BlockIdentifier
~~~~~~~~~~~~~~~

Either a 32 byte hash or an integer block number

.. code-block:: python

    BlockIdentifier = Union[Hash32, BlockNumber]

Encodings
---------

HexStr
~~~~~~

Any string that is hex encoded.

.. code-block:: python

    HexStr = NewType('HexStr', str)

Primitives
~~~~~~~~~~

Any of `bytes`, `int`, or `bool` used as the `Primitive` arg for conversion utils in ETH-Utils_.

.. _ETH-Utils: https://github.com/ethereum/eth-utils/

.. code-block:: python

    Primitives = Union[bytes, int, bool]
