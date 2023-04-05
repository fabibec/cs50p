from working import convert
import pytest

def test_valid_long():
    assert(convert("9:00 AM to 7:30 PM") == "09:00 to 19:30")

def test_valid_short():
    assert(convert("9 AM to 7 PM") == "09:00 to 19:00")

def test_valid_invalid():
    with pytest.raises(ValueError) as e:
        convert("9:60 AM to 7:60PM")

def test_valid_wrong_format():
    with pytest.raises(ValueError) as e:
        convert("9 AM - 7PM")

def test_valid_out_of_range():
    with pytest.raises(ValueError) as e:
        convert("15:00 AM to 19:00 PM")

