from fuel import convert, gauge
import pytest

def test_convert_string():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_greater_1():
    with pytest.raises(ValueError):
        convert("7/3")

def test_convert_correct():
    assert(convert("3/4")) == 75

def test_gauge_F():
    assert(gauge(99)) == "F"

def test_gauge_percent():
    assert(gauge(50)) == "50%"

def test_gauge_E():
    assert(gauge(1)) == "E"
