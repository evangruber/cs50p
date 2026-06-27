from fuel import convert, gauge
import pytest


def test_convert_invalid_format():
    assert convert("1/4") == 25

    with pytest.raises(ValueError):
        convert("1//4")


def test_convert_valid_fractions():
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ValueError):
        convert("5/4")


def test_convert_negative_fractions():
    with pytest.raises(ValueError):
        convert("-1/4")

    with pytest.raises(ValueError):
        convert("1/-4")

    with pytest.raises(ValueError):
        convert("-1/-4")


def test_convert_words():
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("1/dog")

    with pytest.raises(ValueError):
        convert("cat/4")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
