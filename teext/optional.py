"""Utils for dealing with `Optional` types."""
from typing import Optional, TypeVar

__all__ = ["unwrap"]

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
