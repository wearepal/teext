"""Tests for constraints."""
from pytest import raises

import teext as tx


def test_natural_num() -> None:
    x: tx.NaturalNum = tx.NaturalNum(0)
    assert isinstance(x, int)

    with raises(AssertionError):
        tx.NaturalNum(-2)


def test_natural_num_from_str() -> None:
    x: tx.NaturalNum = tx.NaturalNum("0")  # type: ignore[arg-type]
    assert isinstance(x, int)

    with raises(AssertionError):
        tx.NaturalNum("-2")  # type: ignore[arg-type]

    with raises(ValueError):
        tx.NaturalNum("asdf")  # type: ignore[arg-type]


def test_positive_int() -> None:
    x: tx.PositiveInt = tx.PositiveInt(5)
    assert isinstance(x, int)

    with raises(AssertionError):
        tx.PositiveInt(0)


def test_fraction() -> None:
    x: tx.Fraction = tx.Fraction(0.7)
    assert isinstance(x, float)

    with raises(AssertionError):
        tx.Fraction(1.2)


def test_percentage() -> None:
    x: tx.Percentage = tx.Percentage(1.0)
    assert isinstance(x, float)

    with raises(AssertionError):
        tx.Percentage(1.2)


def test_probability() -> None:
    x: tx.Probability = tx.Probability(0.0)
    assert isinstance(x, float)

    with raises(AssertionError):
        tx.Probability(10)
