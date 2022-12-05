"""This file is compiled with mypyc.

It has to be kept in sync with the type stub, lib.pyi.
"""
from typing import Generic, TypeVar

__all__ = ["Some", "Ok", "Err"]

T = TypeVar("T")


class Some(Generic[T]):
    __match_args__ = ("_content",)

    def __init__(self, content: T) -> None:
        self._content = content


class Ok(Generic[T]):
    __match_args__ = ("_value",)

    def __init__(self, value: T) -> None:
        self._value = value


class Err(Generic[T]):
    __match_args__ = ("_error",)

    def __init__(self, error: T) -> None:
        self._error = error
