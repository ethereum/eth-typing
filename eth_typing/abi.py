from typing import (
    Any,
    Literal,
    Sequence,
    Tuple,
    TypedDict,
    Union,
)

from eth_typing.encoding import (
    HexStr,
)

TypeStr = str
Decodable = Union[bytes, bytearray]


class ABIEventParams(TypedDict, total=False):
    indexed: bool
    name: str
    type: str


class ABIEvent(TypedDict, total=False):
    anonymous: bool
    inputs: Sequence["ABIEventParams"]
    name: str
    type: Literal["event"]


class ABIFunctionComponents(TypedDict, total=False):
    components: Sequence["ABIFunctionComponents"]
    name: str
    type: str


class ABIFunctionParams(TypedDict, total=False):
    components: Sequence["ABIFunctionComponents"]
    name: str
    type: str


class ABIFunction(TypedDict, total=False):
    constant: bool
    inputs: Sequence["ABIFunctionParams"]
    name: str
    outputs: Sequence["ABIFunctionParams"]
    payable: bool
    stateMutability: Literal["pure", "view", "nonpayable", "payable"]
    type: Literal["function", "constructor", "fallback", "receive"]


class ABIFunctionInfo(TypedDict, total=False):
    abi: ABIFunction
    selector: HexStr
    arguments: Tuple[Any, ...]


ABIElement = Union[ABIFunction, ABIEvent]
ABI = Sequence[Union[ABIFunction, ABIEvent]]
