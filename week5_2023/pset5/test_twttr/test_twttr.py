from twttr import shorten

def test_lower_case():
    assert(shorten("twitter")) == "twttr"

def test_upper_case():
    assert(shorten("TwitteR")) == "TwttR"

def test_number():
    assert(shorten("Hi21")) == "H21"

def test_capitalized():
    assert(shorten("End")) == "nd"

def test_numb():
    assert(shorten("1.st Place")) == "1.st Plc"

