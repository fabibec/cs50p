from bank import value

def test_hello_upper():
    assert(value("HELLO")) == 0

def test_hello_lower():
    assert(value("hello")) == 0

def test_hello_inside():
    assert(value("Hello, Newman")) == 0

def test_h_inside():
    assert(value("How you doing?")) == 20

def test_without_h():
    assert(value("What's happening")) == 100
