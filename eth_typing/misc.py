from typing import (
    NewType,
    TypeVar,
    Union,
)

Address = NewType('Address', bytes)
BlockNumber = NewType('BlockNumber', int)
ContractName = NewType('ContractName', str)
Hash32 = NewType('Hash32', bytes)
HexAddress = NewType('HexAddress', str)
HexStr = NewType('HexStr', str)
Primitives = Union[bytes, int, bool]
URI = NewType('URI', str)

ChecksumAddress = NewType('ChecksumAddress', HexAddress)

AnyAddress = TypeVar('AnyAddress', Address, HexAddress, ChecksumAddress)
