"""Types that express a constraint."""
from typing import NewType, cast

__all__ = ["NaturalNum", "PositiveInt", "Fraction"]

NaturalNum = NewType("NaturalNum", int)


def _assert_natural_number(num: int) -> NaturalNum:
    assert num >= 0, f"{num} is not a natural number"
    return cast(NaturalNum, num)


NaturalNum = _assert_natural_number  # type: ignore[misc,assignment]

PositiveInt = NewType("PositiveInt", int)


def _assert_positive_int(num: int) -> PositiveInt:
    assert num > 0, f"{num} is not a positive integer"
    return cast(PositiveInt, num)


PositiveInt = _assert_positive_int  # type: ignore[misc,assignment]

Fraction = NewType("Fraction", float)


def _assert_fraction(num: float) -> Fraction:
    assert 0 <= num <= 1, f"{num} is not a fraction"
    return cast(Fraction, num)


Fraction = _assert_fraction  # type: ignore[misc,assignment]
