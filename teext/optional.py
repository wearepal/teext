"""Utils for dealing with `Optional` types."""
from typing import Callable, Generic, Optional, TypeVar, Union

__all__ = ["Maybe", "Some", "maybe_apply", "unwrap"]

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


class Some(Generic[T]):
    __slots__ = ("_content",)
    __match_args__ = ("_content",)

    def __init__(self, content: T, /):
        self._content = content


Maybe = Union[Some[T], None]
