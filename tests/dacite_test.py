from dataclasses import dataclass

import dacite
from pytest import raises

from teext import Fraction, NaturalNum, Percentage, PositiveInt, Probability, TYPE_HOOKS


@dataclass
class Config:
    fraction: Fraction
    natural_num: NaturalNum
    percentage: Percentage = Percentage(1.0)
    positive_int: PositiveInt = PositiveInt(56)
    probability: Probability = Probability(0.01)


def test_load_all() -> None:
    data = {
        "fraction": 0.1,
        "natural_num": 0,
        "percentage": 0.75,
        "positive_int": 10,
        "probability": 0.5,
    }
    config = dacite.from_dict(Config, data, config=dacite.Config(type_hooks=TYPE_HOOKS))
    assert config.fraction == data["fraction"]


def test_load_partial() -> None:
    data = {
        "fraction": 0.9,
        "natural_num": 0,
    }
    config = dacite.from_dict(Config, data, config=dacite.Config(type_hooks=TYPE_HOOKS))
    assert config.fraction == data["fraction"]
    assert config.percentage == 1.0


def test_load_fail() -> None:
    data = {
        "fraction": 1.9,
        "natural_num": 0,
    }
    with raises(AssertionError, match=f"{data['fraction']} is not a fraction"):
        dacite.from_dict(Config, data, config=dacite.Config(type_hooks=TYPE_HOOKS))
