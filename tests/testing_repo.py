"""
testing_repo.py contains a test Dagster repo for testing the dagstd package.

These tests are not automated, but feel free to use this as a starting point
for having a play with the package!

Just make sure the requirements are installed and run `dagit -f
testing_repo.py`
"""
from dagster import op, job

from dagstd.constants import Constant
from dagstd.operations import add


@op
def my_print(context, value):
    context.log.info(value)


@job
def my_job():
    my_print(add([Constant('constants '), Constant('are great')]))
    my_print(Constant({'a': 1, 'b': 2}))
