from dagstd import utils


def test_no_op():
    assert utils.no_op('some_arg') == 'some_arg'
    assert utils.no_op(['mutable', 'arg']) == ['mutable', 'arg']
