# content of test_sample.py
import pytest


# Functions
def increase_by_one(x):
    return x + 1


def test_various_cases():
    assert increase_by_one(-1) == 0
    assert increase_by_one(0) == 1
    assert increase_by_one(10) == 11
    assert increase_by_one(-10) == -9


@pytest.mark.parametrize("number, result", [(-1, 0), (0, 1), (10, 11), (-10, -9)])
def test_various_cases_params(number, result):
    assert increase_by_one(number) == result
