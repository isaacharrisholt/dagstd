"""
maths.py contains ops that perform common mathematical operations.
"""
from typing import List

from dagster import op


@op
def add(args: List):
    """
    Adds the given arguments.
    """

    try:
        return sum(args)
    except TypeError:
        start = args[0]
        for arg in args[1:]:
            start += arg
        return start


@op
def subtract(x, args: List):
    """
    Subtracts the given arguments from the first argument.
    """
    try:
        return x - sum(args)
    except TypeError:
        start = x
        for arg in args:
            start -= arg
        return start


@op
def multiply(args: List):
    """
    Multiplies the given arguments.
    """
    start = 1
    for arg in args:
        if arg == 0:
            return 0
        start *= arg
    return start


@op
def divide(x, args: List):
    """
    Divides the first argument by the given arguments.
    """
    start = x
    for arg in args:
        start /= arg
    return start
