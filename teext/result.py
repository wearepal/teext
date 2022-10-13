from typing import TypeVar, Union

from .lib import Err, Ok

__all__ = ["Err", "Ok", "Result"]


T = TypeVar("T")
E = TypeVar("E", bound=Exception)


Result = Union[Ok[T], Err[E]]
