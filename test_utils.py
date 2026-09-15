import pytest
from util import utils


def test_reversed_with_int():
    assert utils.reversed(123) == 321


def test_reversed_with_negative_int():
    assert utils.reversed(-120) == -21


def test_reversed_with_str():
    assert utils.reversed("456") == 654


def test_reversed_with_float():
    # float will be truncated to int before reversing
    assert utils.reversed(78.9) == 87


def test_formatter_with_int():
    assert utils.formatter(10) == ("1010", "12")


def test_formatter_with_str():
    assert utils.formatter("8") == ("1000", "10")


def test_formatter_with_float():
    # float truncated to int
    assert utils.formatter(7.9) == ("111", "7")
