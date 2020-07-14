def func1(x, y):
    return x + y


def func2(x, y):
    return x * y


def test_sum():
    assert func1(10, 99) == 109


def test_product():
    assert func2(7, 9) == 63
