from dagster import op, job
from dagstd.operations import add
from dagstd.constants import Constant


@op
def my_print(context, value):
    context.log.info(value)


@job
def my_job():
    my_print(add([Constant('constants '), Constant('are great')]))
    my_print(Constant({'a': 1, 'b': 2}))
