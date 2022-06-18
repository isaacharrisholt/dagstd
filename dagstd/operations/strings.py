"""
strings.py contains helper ops for working with strings.
"""
from typing import List

from dagster import op


@op
def fmt(string: str, args: List) -> str:
    """
    Formats a string with the given arguments.

    Parameters
    ----------
    string : str
        The string to format.
    args : List
        The arguments to format into the string.

    Returns
    -------
    str
        The formatted string.
    """
    return string.format(*args)
