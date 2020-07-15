import pytest


# Functions
def increase_by_one(x):
    return x + 1


def raises_exception():
    raise ValueError("Something went wrong")


# Tests
def test_simple_case():
    assert increase_by_one(3) == 4


def test_various_cases():
    assert increase_by_one(-1) == 0
    assert increase_by_one(0) == 1
    assert increase_by_one(10) == 11
    assert increase_by_one(-10) == -9


def test_expect_failure():
    with pytest.raises(ValueError):
        raises_exception()
