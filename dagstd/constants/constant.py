"""
constant.py contains a Constant function that acts as an op that returns
whatever value is passed to it.
"""
import re

from typing import Any

from dagster import op


# Although Constant is a function, it's more readable if it appears to be a
# class.
def Constant(value: Any) -> Any:
    """
    Acts as an op that returns whatever value is passed to it on creation.

    The name of the op is the value passed to it.
    """
    r = re.compile(r'\W')

    @op(
        name=r.sub('', repr(value).replace(' ', '_')),
        description=f'Returns {repr(value)}',
    )
    def constant_op():
        return value

    return constant_op()
