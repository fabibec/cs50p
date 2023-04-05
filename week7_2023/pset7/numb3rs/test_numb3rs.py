from numb3rs import validate

def test_text():
    assert(validate("cat") == False)

def test_to_short():
    assert(validate("127.0") == False)

def test_to_long():
    assert(validate("1.1.1.1.1") == False)

def test_to_large_value():
    assert(validate("25.276.2.4") == False)

def test_missformatted():
    assert(validate("....1") == False)

def test_correct():
    assert(validate("255.255.255.255") == True)
