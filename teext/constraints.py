"""Types that express a constraint."""
from typing import NewType
from typing_extensions import TypeGuard

__all__ = [
    "Fraction",
    "NaturalNum",
    "Percentage",
    "PositiveInt",
    "Probability",
    "assert_fraction",
    "assert_natural_num",
    "assert_percentage",
    "assert_positive_int",
    "assert_prob",
    "is_fraction",
    "is_natural_num",
    "is_percentage",
    "is_positive_int",
    "is_prob",
]

# =================================== natural number ===================================
NaturalNum = NewType("NaturalNum", int)
"""A type for natural numbers (i.e., integers without the negative numbers)."""


def is_natural_num(num: int) -> TypeGuard[NaturalNum]:
    return num >= 0


def assert_natural_num(num: int) -> NaturalNum:
    assert is_natural_num(num), f"{num} is not a natural number"
    return num


# ================================== positive integer ==================================
PositiveInt = NewType("PositiveInt", int)
"""A type for positive integers."""


def is_positive_int(num: int) -> TypeGuard[PositiveInt]:
    return num > 0


def assert_positive_int(num: int) -> PositiveInt:
    assert is_positive_int(num), "{num} is not a positive integer"
    return num


# ====================================== fraction ======================================
Fraction = NewType("Fraction", float)
"""A type for fractions (i.e., floats between 0 and 1, inclusive)."""


def is_fraction(num: float) -> TypeGuard[Fraction]:
    return 0 <= num <= 1


def assert_fraction(num: float) -> Fraction:
    assert is_fraction(num), "{num} is not a fraction"
    return num


# ==================================== probability =====================================
Probability = NewType("Probability", float)
"""A type for probabilities (i.e., floats between 0 and 1, inclusive)."""


def is_prob(num: float) -> TypeGuard[Probability]:
    return 0 <= num <= 1


def assert_prob(num: float) -> Probability:
    assert is_prob(num), "{num} is not a probability"
    return num


# ===================================== percentage =====================================
Percentage = NewType("Percentage", float)
"""A type for percentages (i.e., floats between 0 and 1, inclusive)."""


def is_percentage(num: float) -> TypeGuard[Percentage]:
    return 0 <= num <= 1


def assert_percentage(num: float) -> Percentage:
    assert is_percentage(num), "{num} is not a percentage"
    return num
