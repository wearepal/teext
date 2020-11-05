from typing import Generic, TypeVar, Union

__all__ = ["Err", "Ok", "Result"]


T = TypeVar("T")
E = TypeVar("E", bound=Exception)


class Ok(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    def ok(self) -> T:
        return self._value


class Err(Generic[E]):
    def __init__(self, e: E) -> None:
        self._e = e

    def err(self) -> E:
        return self._e


Result = Union[Ok[T], Err[E]]
