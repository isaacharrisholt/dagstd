"""
utils.py contains useful helper ops that are not specific to any part of the
Dagstd library.
"""
from typing import Any

from dagster import op


@op(description='Does nothing. Allows unlinked dependencies for graphs.')
def no_op(value: Any) -> Any:
    """
    Does nothing. Allows unlinked dependencies for graphs.

    Examples
    --------
    In this example, even though graph_2 has no data dependencies on graph_1,
    it will still wait for graph_1 to complete before starting due to the use
    of the `no_op` operation.

    This is useful when you have graphs that need to activate in sequence, but
    the earlier graphs don't pass data. For example, you might run a data sync
    with Airbyte, and then run a dbt project to transform that data in your
    warehouse.

    .. code-block:: python

        from dagster import graph, job, In

        from dagstd.constants import Constant, One, Two
        from dagstd.operations import add, fmt
        from dagstd.utils import no_op

        @graph
        def graph_1():
             name = Constant('Isaac')
             age = Constant(20)
             return fmt(Constant('{} is {} years old'), name, age)


        @graph(ins={'arg_1': In(int), 'arg_2': In(int), 'deps': In(Any)})
        def graph_2(arg_1, arg_2, deps):
             no_op(deps)
             return add([arg_1, arg_2])


        @job
        def my_job():
            string = graph_1()
            num = graph_2(One(), Two(), deps=string)
    """
    return value
