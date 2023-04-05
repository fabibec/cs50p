from hello import hello

def test_argument():
    assert hello("david") == "hello, david"

def test_hello():
    assert hello() == "hello, world"