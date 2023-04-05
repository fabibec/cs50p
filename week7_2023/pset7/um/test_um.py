from um import count
import pytest

def test_um():
    assert(count("um") == 1)

def test_um_with_sep():
    assert(count("um?") == 1)

def test_um_in_sentence():
    assert(count("Um, thanks for the album.") == 1)

def test_um_multiple():
    assert(count("Um, thanks, um...") == 2)
