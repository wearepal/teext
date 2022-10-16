"""Utils for dealing with `Optional` types."""
from typing import Callable, Optional, TypeVar, Union

from .lib import Some

__all__ = ["Maybe", "Option", "Some", "maybe_apply", "unwrap"]

T = TypeVar("T")


def unwrap(value: Optional[T], default: T) -> T:
    """Return a value unchanged if it is not `None`; otherwise return the default value.

    Args:
        value: a value which might be `None`
        default: a value of the same type as `value`

    Returns:
        either `value` (if it isn't `None`) or `default`
    """
    return value if value is not None else default


def maybe_apply(value: Optional[T], func: Callable[[T], Optional[T]]) -> Optional[T]:
    """Apply a function to a value if the value is not `None`."""
    return func(value) if value is not None else None


Maybe = Union[Some[T], None]
Option = Union[Some[T], None]
