from dagstd.operations import *

import pytest


def test_fmt():
    assert fmt('{}', ['format me']) == 'format me'
    assert fmt('{}', [1, 2, 3, 4]) == '1'
    assert fmt('{} {} {} {}', [1, 2, 3, 4]) == '1 2 3 4'

    assert fmt('', [1]) == ''
    assert fmt('', []) == ''

    with pytest.raises(IndexError):
        fmt('{}', [])
