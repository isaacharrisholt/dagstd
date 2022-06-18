"""
env.py contains ops for working with environment variables.
"""
import os
from typing import Optional

from dagster import op


@op
def or_none(key: str) -> Optional[str]:
    """
    Returns the value of the environment variable with the given key,
    or None if the variable is not set.
    """
    return os.environ.get(key)


@op
def or_empty(key: str) -> str:
    """
    Returns the value of the environment variable with the given key,
    or an empty string if the variable is not set.
    """
    return os.environ.get(key, '')


@op
def or_default(key: str, default: str) -> str:
    """
    Returns the value of the environment variable with the given key,
    or the given default if the variable is not set.
    """
    return os.environ.get(key, default)


@op
def or_raise(key: str) -> str:
    """
    Returns the value of the environment variable with the given key,
    or raises an error if the variable is not set.
    """
    return os.environ[key]
