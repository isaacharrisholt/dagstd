import pytest

from dagstd.operations import *


def test_fmt():
    assert fmt('{}', ['format me']) == 'format me'
    assert fmt('{}', [1, 2, 3, 4]) == '1'
    assert fmt('{} {} {} {}', [1, 2, 3, 4]) == '1 2 3 4'

    assert fmt('', [1]) == ''
    assert fmt('', []) == ''

    with pytest.raises(IndexError):
        fmt('{}', [])


def test_add():
    assert add([1, 2, 3]) == 6
    assert add([1, 2, 3, 4]) == 10
    assert add([1, 2, 3, 4, 5]) == 15
    assert add([1, 2, 3, 4, 5, 6]) == 21
    assert add([1, 2, 3, 4, 5, 6, 7]) == 28
    assert add([1, 2, 3, 4, 5, 6, 7, 8]) == 36
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45


def test_subtract():
    assert subtract(10, [1, 2, 3]) == 4
    assert subtract(10, [1, 2, 3, 4]) == 0
    assert subtract(10, [1, 2, 3, 4, 5]) == -5
    assert subtract(10, [1, 2, 3, 4, 5, 6]) == -11
    assert subtract(10, [1, 2, 3, 4, 5, 6, 7]) == -18
    assert subtract(10, [1, 2, 3, 4, 5, 6, 7, 8]) == -26
    assert subtract(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -35


def test_multiply():
    assert multiply([1, 2, 3]) == 6
    assert multiply([1, 2, 3, 4]) == 24
    assert multiply([1, 2, 3, 4, 5]) == 120
    assert multiply([1, 2, 3, 4, 5, 6]) == 720
    assert multiply([1, 2, 3, 4, 5, 6, 7]) == 5040
    assert multiply([0, 1, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert multiply([-1, 2, 3, 4, 5, 6, 7, 8, 9]) == -362880


def test_divide():
    assert divide(10, [2]) == 5
    assert divide(10, [2, 2]) == 2.5
    assert divide(10, [2, 2, 5]) == 0.5
    assert divide(10, [2, 2, 5, 2]) == 0.25
    assert divide(10, [2, 2, 5, 2, 5]) == 0.05
