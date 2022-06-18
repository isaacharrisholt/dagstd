"""
numbers.py contains ops that return common numbers. These ops are capitalised
to make them seem more like classes, which helps with readability.
"""
from dagster import op


@op
def Zero() -> int:
    return 0


@op
def One() -> int:
    return 1


@op
def Two() -> int:
    return 2


@op
def Three() -> int:
    return 3


@op
def Four() -> int:
    return 4


@op
def Five() -> int:
    return 5


@op
def Six() -> int:
    return 6


@op
def Seven() -> int:
    return 7


@op
def Eight() -> int:
    return 8


@op
def Nine() -> int:
    return 9


@op
def Ten() -> int:
    return 10


@op
def Twenty() -> int:
    return 20


@op
def Thirty() -> int:
    return 30


@op
def Forty() -> int:
    return 40


@op
def Fifty() -> int:
    return 50


@op
def OneHundred() -> int:
    return 100


@op
def FiveHundred() -> int:
    return 500


@op
def OneThousand() -> int:
    return 1000
