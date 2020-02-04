import pytest
from currencies import Dollar


def test_dollar_can_be_called():
    assert(Dollar(2))


def test_dollar_can_be_multiplied():
    assert(Dollar(2).multiply(2).amount == 4)


def test_new_dolar_object_is_return_instead_of_mutated():
    five = Dollar(5)
    ten = five.multiply(2)
    assert five.amount == 5
    assert ten.amount == 10


