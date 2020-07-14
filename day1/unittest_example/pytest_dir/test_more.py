# content of test_sample.py
import pytest
import sys


# Functions
def func(x):
    return x + 1


def f():
    raise SystemExit(1)


def my_sum(x, y):
    return x + y


# Tests
def test_answer():
    assert func(3) == 4


@pytest.mark.parametrize("x, y, result", [(30, 10, 40), (20, 2, 22), (99, 101, 200)])
def test_my_sum2(x, y, result):
    assert my_sum(x, y) == result


def test_my_sum():
    assert my_sum(7, 3) == 10


def test_mytest():
    with pytest.raises(SystemExit):
        f()


class TestClass(object):
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x == "hello"


@pytest.mark.skipif(sys.version_info > (3, 3), reason="requires python3.3")
def test_function():
    print(sys.version_info)
    assert True
