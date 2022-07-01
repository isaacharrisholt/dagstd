"""
constant.py contains a Constant function that acts as an op that returns
whatever value is passed to it.
"""
import re
import uuid

from typing import Any

from dagster import op


# Although Constant is a function, it's more readable if it appears to be a
# class.
def Constant(value: Any, suffix: str = None, make_unique: bool = True) -> Any:
    """
    Acts as an op that returns whatever value is passed to it on creation.

    Parameters
    ----------
    value : Any
        The value to return.
    suffix : str, default=None
        A suffix to append to the op name.
    make_unique : bool, default=True
        If True, the op name will be suffixed with a UUID. Is overridden if the
        suffix argument is provided.

    The name of the op is the value passed to it plus a unique ID to allow
    having multiple constants with the same value. Alternatively, you can
    pass a suffix to the Constant function to be used instead of the unique ID.
    """
    r = re.compile(r'\W')

    if suffix is not None:
        name = (
            f'{r.sub("", repr(value).replace(" ", "_"))}_{r.sub("", suffix)}'
        )
    elif make_unique:
        name = (
            f'{r.sub("", repr(value).replace(" ", "_"))}_'
            f'{str(uuid.uuid1()).replace("-", "_")}'
        )
    else:
        name = r.sub("", repr(value).replace(" ", "_"))

    @op(
        name=name,
        description=f'Returns {repr(value)}',
    )
    def constant_op():
        return value

    return constant_op()
