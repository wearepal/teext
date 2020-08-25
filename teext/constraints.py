"""Types that express a constraint."""
from typing import Any, Callable, Dict, NewType, cast

__all__ = ["Fraction", "NaturalNum", "Percentage", "PositiveInt", "Probability", "TYPE_HOOKS"]

# ========================================= natural number ========================================
NaturalNum = NewType("NaturalNum", int)
"""A type for natural numbers (i.e., integers without the negative numbers)."""


def _assert_natural_number(num: int) -> NaturalNum:
    num = int(num)  # if it can be converted to a natural number, it's also fine
    assert num >= 0, f"{num} is not a natural number"
    return cast(NaturalNum, num)


_assert_natural_number.__supertype__ = NaturalNum.__supertype__  # type: ignore[attr-defined]
NaturalNum = _assert_natural_number  # type: ignore[misc,assignment]

# ======================================== positive integer =======================================
PositiveInt = NewType("PositiveInt", int)
"""A type for positive integers."""


def _assert_positive_int(num: int) -> PositiveInt:
    num = int(num)  # if it can be converted to a positive int, it's also fine
    assert num > 0, f"{num} is not a positive integer"
    return cast(PositiveInt, num)


_assert_positive_int.__supertype__ = PositiveInt.__supertype__  # type: ignore[attr-defined]
PositiveInt = _assert_positive_int  # type: ignore[misc,assignment]

# ============================================ fraction ===========================================
Fraction = NewType("Fraction", float)
"""A type for fractions (i.e., floats between 0 and 1, inclusive)."""


def _assert_fraction(num: float) -> Fraction:
    num = float(num)  # if it can be converted to a fraction, it's also fine
    assert 0 <= num <= 1, f"{num} is not a fraction"
    return cast(Fraction, num)


_assert_fraction.__supertype__ = Fraction.__supertype__  # type: ignore[attr-defined]
Fraction = _assert_fraction  # type: ignore[misc,assignment]

# ========================================== probability ==========================================
Probability = NewType("Probability", float)
"""A type for probabilities (i.e., floats between 0 and 1, inclusive)."""


def _assert_prob(num: float) -> Probability:
    num = float(num)  # if it can be converted to a probability, it's also fine
    assert 0 <= num <= 1, f"{num} is not a probability"
    return cast(Probability, num)


_assert_prob.__supertype__ = Probability.__supertype__  # type: ignore[attr-defined]
Probability = _assert_prob  # type: ignore[misc,assignment]

# =========================================== percentage ==========================================
Percentage = NewType("Percentage", float)
"""A type for percentages (i.e., floats between 0 and 1, inclusive)."""


def _assert_percentage(num: float) -> Percentage:
    num = float(num)  # if it can be converted to a percentage, it's also fine
    assert 0 <= num <= 1, f"{num} is not a percentage"
    return cast(Percentage, num)


_assert_percentage.__supertype__ = Percentage.__supertype__  # type: ignore[attr-defined]
Percentage = _assert_percentage  # type: ignore[misc,assignment]


TYPE_HOOKS: Dict[type, Callable[[Any], Any]] = {
    Fraction: _assert_fraction,
    NaturalNum: _assert_natural_number,
    Percentage: _assert_percentage,
    PositiveInt: _assert_positive_int,
    Probability: _assert_prob,
}
