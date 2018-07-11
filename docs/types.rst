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

Miscellaneous
-------------

Address
~~~~~~~

Any bytestring representing a canonical address.

.. code-block:: python

    Address = NewType('Address', bytes)

AnyAddress
~~~~~~~~~~

Any of Address_, HexAddress_, ChecksumAddress_.

.. code-block:: python

    AnyAddress = TypeVar('AnyAddress', Address, HexAddress, ChecksumAddress)

BlockNumber
~~~~~~~~~~~

Any integer that represents a valid block number on a chain.

.. code-block:: python

    BlockNumber = NewType('BlockNumber', int)

ContractName
~~~~~~~~~~~~

Any string conforming to the regular expression ``[a-zA-Z][a-zA-Z0-9_]{0,255}``.

.. code-block:: python

    ContractName = NewType('ContractName', str)

ChecksumAddress
~~~~~~~~~~~~~~~

Any HexAddress_ that is formatted according to ERC55_.

.. _ERC55: https://github.com/ethereum/EIPs/issues/55

.. code-block:: python

    ChecksumAddress = NewType('ChecksumAddress', HexAddress)

Hash32
~~~~~~

Any 32 byte hash.

.. code-block:: python

    Hash32 = NewType('Hash32', bytes)

HexAddress
~~~~~~~~~~

Any string representing a hex encoded address.

.. code-block:: python

    HexAddress = NewType('HexAddress', str)

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

URI
~~~

Any string that represents a URI.

.. code-block:: python

    URI = NewType('URI', str)
