"""Tests for constraints."""
import teext as tx


def test_natural_num() -> None:
    x: tx.NaturalNum
    y: int = 0
    assert tx.is_natural_num(y)
    x = y
    assert isinstance(x, int)
    assert not tx.is_natural_num(-2)


def test_positive_int() -> None:
    x: tx.PositiveInt
    y: int = 5
    assert tx.is_positive_int(y)
    x = y
    assert isinstance(x, int)
    assert not tx.is_positive_int(0)


def test_fraction() -> None:
    x: tx.Fraction
    y: float = 0.7
    assert tx.is_fraction(y)
    x = y
    assert isinstance(x, float)
    assert not tx.is_fraction(1.2)


def test_percentage() -> None:
    x: tx.Percentage
    y: float = 1.0
    assert tx.is_percentage(y)
    x = y
    assert isinstance(x, float)
    assert not tx.is_percentage(1.2)


def test_probability() -> None:
    x: tx.Probability
    y: float = 0.0
    assert tx.is_prob(y)
    x = y
    assert isinstance(x, float)
    assert not tx.is_prob(10)
