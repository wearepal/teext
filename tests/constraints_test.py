"""Tests for constraints."""
from pytest import raises

from teext import Fraction, NaturalNum, Percentage, PositiveInt, Probability


def test_natural_num() -> None:
    x: NaturalNum = NaturalNum(0)
    assert isinstance(x, int)

    with raises(AssertionError):
        NaturalNum(-2)


def test_positive_int() -> None:
    x: PositiveInt = PositiveInt(5)
    assert isinstance(x, int)

    with raises(AssertionError):
        PositiveInt(0)


def test_fraction() -> None:
    x: Fraction = Fraction(0.7)
    assert isinstance(x, float)

    with raises(AssertionError):
        Fraction(1.2)


def test_percentage() -> None:
    x: Percentage = Percentage(1.0)
    assert isinstance(x, float)

    with raises(AssertionError):
        Percentage(1.2)


def test_probability() -> None:
    x: Probability = Probability(0.0)
    assert isinstance(x, float)

    with raises(AssertionError):
        Probability(10)
