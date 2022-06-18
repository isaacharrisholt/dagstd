from dagstd.constants import *


def test_numbers():
    assert Zero() == 0
    assert One() == 1
    assert Two() == 2
    assert Three() == 3
    assert Four() == 4
    assert Five() == 5
    assert Six() == 6
    assert Seven() == 7
    assert Eight() == 8
    assert Nine() == 9
    assert Ten() == 10
    assert Twenty() == 20
    assert Thirty() == 30
    assert Forty() == 40
    assert Fifty() == 50
    assert OneHundred() == 100
    assert OneThousand() == 1000


def test_constant():
    assert Constant('constants ') == 'constants '
    assert Constant('are great') == 'are great'

    some_dict = {'a': 1, 'b': 2}
    assert Constant(some_dict) == some_dict
