from jar import Jar
import pytest

def test_init():
    jar = Jar(14)
    assert(jar.capacity) == 14
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(7)
    jar2 = Jar()
    jar2.deposit(5)
    jar2.withdraw(2)
    assert(jar2.size) == 3