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
]

# ========================================= natural number ========================================
NaturalNum = NewType("NaturalNum", int)
"""A type for natural numbers (i.e., integers without the negative numbers)."""


def assert_natural_num(num: int) -> TypeGuard[NaturalNum]:
    return num >= 0


# ======================================== positive integer =======================================
PositiveInt = NewType("PositiveInt", int)
"""A type for positive integers."""


def assert_positive_int(num: int) -> TypeGuard[PositiveInt]:
    return num > 0


# ============================================ fraction ===========================================
Fraction = NewType("Fraction", float)
"""A type for fractions (i.e., floats between 0 and 1, inclusive)."""


def assert_fraction(num: float) -> TypeGuard[Fraction]:
    return 0 <= num <= 1


# ========================================== probability ==========================================
Probability = NewType("Probability", float)
"""A type for probabilities (i.e., floats between 0 and 1, inclusive)."""


def assert_prob(num: float) -> TypeGuard[Probability]:
    return 0 <= num <= 1


# =========================================== percentage ==========================================
Percentage = NewType("Percentage", float)
"""A type for percentages (i.e., floats between 0 and 1, inclusive)."""


def assert_percentage(num: float) -> TypeGuard[Percentage]:
    return 0 <= num <= 1
