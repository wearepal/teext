from typing import Any

__all__ = ["unpack_first"]


def unpack_first(o: object) -> Any:
    return getattr(o, o.__match_args__[0])  # type: ignore[attr-defined]
