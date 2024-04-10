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
"""String representation of a data type."""
Decodable = Union[bytes, bytearray]
"""Binary data to be decoded."""


class ABIEventParam(TypedDict, total=False):
    """
    TypedDict to represent the `ABI` for event parameters.
    """

    indexed: bool
    """If True, event parameter can be used as a topic filter."""
    name: str
    """Name of the event parameter."""
    type: str
    """Type of the event parameter."""


class ABIEvent(TypedDict, total=False):
    """
    TypedDict to represent the `ABI` for an event.
    """

    anonymous: bool
    """If True, event is anonymous. Cannot filter the event by name."""
    inputs: Sequence["ABIEventParam"]
    """Input parameters for the event."""
    name: str
    """Event name identifier."""
    type: Literal["event"]
    """Event ABI type."""


class ABIFunctionComponent(TypedDict, total=False):
    """
    TypedDict representing the `ABI` for nested function parameters.

    Used as a component of `ABIFunctionParams`.
    """

    components: Sequence["ABIFunctionComponent"]
    """List of nested function parameters"""
    name: str
    """Name of the function parameter."""
    type: str
    """Type of the function parameter."""


class ABIFunctionParam(TypedDict, total=False):
    """
    TypedDict representing the `ABI` for function parameters.
    """

    components: Sequence["ABIFunctionComponent"]
    """List of function parameters"""
    name: str
    """Name of the function parameter."""
    type: str
    """Type of the function parameter."""


class ABIFunction(TypedDict, total=False):
    """
    TypedDict representing the `ABI` for a function.
    """

    constant: bool
    """Function is constant and does not change state."""
    inputs: Sequence["ABIFunctionParam"]
    """Function input parameters."""
    name: str
    """Name of the function."""
    outputs: Sequence["ABIFunctionParam"]
    """Function return values."""
    payable: bool
    """Contract is payable to receive ether on deployment."""
    stateMutability: Literal["pure", "view", "nonpayable", "payable"]
    """State mutability of the constructor."""
    type: Literal["function", "constructor", "fallback", "receive"]
    """Type of the function."""


class ABIFunctionInfo(TypedDict, total=False):
    """
    TypedDict to represent an `ABIFunction` with the function selector and
    corresponding arguments.
    """

    abi: ABIFunction
    """ABI for the function interface."""
    selector: HexStr
    """Solidity Function selector sighash."""
    arguments: Tuple[Any, ...]
    """Function input parameters."""


ABIElement = Union[ABIFunction, ABIEvent]
"""Base type for `ABIFunction` and `ABIEvent` types."""
ABI = Sequence[Union[ABIFunction, ABIEvent]]
"""
List of components representing function and event interfaces
(elements of an ABI).
"""
