from plates import is_valid

def test_CS50():
    assert(is_valid("CS50")) == True

def test_CS05():
    assert(is_valid("CS05")) == False

def test_CS50P():
    assert(is_valid("CS50P")) == False

def test_PI():
    assert(is_valid("PI3.14")) == False

def test_single_letter():
    assert(is_valid("A")) == False

def test_long_string():
    assert(is_valid("OUTATIME")) == False

def test_only_number():
    assert(is_valid("1234")) == False



