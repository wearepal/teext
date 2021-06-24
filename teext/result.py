from dataclasses import dataclass
from typing import Generic, TypeVar, Union
from typing_extensions import final

__all__ = ["Err", "Ok", "Result"]


T = TypeVar("T")
E = TypeVar("E", bound=Exception)


@final
@dataclass(frozen=True)
class Ok(Generic[T]):
    value: T


@final
@dataclass(frozen=True)
class Err(Generic[E]):
    error: E


Result = Union[Ok[T], Err[E]]
