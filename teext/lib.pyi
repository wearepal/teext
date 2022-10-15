from typing import Generic, TypeVar, final

T = TypeVar("T")
E = TypeVar("E", bound=Exception)

@final
class Some(Generic[T]):
    _content: T
    __match_args__ = ("_content",)
    def __init__(self, content: T, /) -> None: ...

@final
class Ok(Generic[T]):
    _value: T
    __match_args__ = ("_value",)
    def __init__(self, value: T, /) -> None: ...

@final
class Err(Generic[E]):
    _error: E
    __match_args__ = ("_error",)
    def __init__(self, error: E, /) -> None: ...
