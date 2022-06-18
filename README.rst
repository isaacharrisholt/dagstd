Dagstd
======

Dagstd is a Python package containing a set of helper modules for use with
the `Dagster <https://dagster.io>`_ data orchestration tool.

Dagster is a great tool, but there are occasions where you just need to pass in
a simple integer or string as input to a Dagster op, but in Dagster, inputs to
ops can only be outputs of other ops. This results in a lot of boilerplate
functions being written that just return a formatted string or even just an
integer. This is why Dagstd was created.

Features
--------

- Simple ops for common numbers
- Constant value ops
- Helper ops for mathematical and string operations
- Ops for retrieving environment variables

Usage
-----

Here's an example of a pure-Dagster graph that downloads a daily zip file and
extracts a known file name. Note: the ``download_large_file`` op has been
omitted for brevity.

.. code-block:: python
    :linenos:

    import zipfile

    from datetime import datetime

    from dagster import op, job


    @op
    def get_todays_date() -> str:
        return datetime.today().strftime()


    @op
    def five() -> int:
        return 5


    @op
    def get_download_file_url(date: str) -> str:
        return f'https://example.com/{date}.csv'


    @op
    def get_nth_file_name(n: int) -> str:
        return f'file_{n:02}.txt'


    @op
    def extract_file_from_zip(context, zip_path: str, file_name: str) -> str:
        with zipfile.ZipFile(zip_path) as zip_file:
            with(f'/tmp/{file_name}', 'wb') as f:
                f.write(zip_file.read(file_name))
            context.log.info(f'Extracted {file_name} from {zip_path}')
            return f'/tmp/{file_name}'


    @job
    def process_data():
        date = get_todays_date()
        url = get_download_file_url(date)
        zip_path = download_large_file(url)

        file_name = get_nth_file_name(five())
        file_path = extract_file_from_zip(zip_path, file_name)



And here's the same graph, but with Dagstd ops.

.. code-block:: python
    :linenos:

    import zipfile

    from datetime import datetime

    from dagster import op, job
    from dagstd.constants import Constant, Five
    from dagstd.operations import fmt


    @op
    def get_todays_date_string() -> str:
        return datetime.today().strftime("%Y-%m-%d")


    @op
    def extract_file_from_zip(context, zip_path: str, file_name: str) -> str:
        with zipfile.ZipFile(zip_path) as zip_file:
            with(f'/tmp/{file_name}', 'wb') as f:
                f.write(zip_file.read(file_name))
            context.log.info(f'Extracted {file_name} from {zip_path}')
            return f'/tmp/{file_name}'


    @job
    def process_data():
        date = get_todays_date_string()
        url = fmt(Constant('https://example.com/{}.csv'), [date])
        zip_path = download_large_file(url)

        file_name = fmt(Constant('file_{}.txt'), [Five()])
        file_path = extract_file_from_zip(zip_path, file_name)

This was just a small example, but it serves to show how much boilerplate can
be avoided when using Dagstd.

Documentation
-------------

Documentation can be found at
https://dagstd.readthedocs.io/en/latest/readme.html.

Installation
------------

Install Dagstd with pip:

.. code-block:: bash

    pip install dagstd

Dependencies
------------

- `dagster <https://pypi.org/project/dagster/>`_

Contribute
----------

I'm always looking for more ideas to add to Dagstd. If you have an idea, please
open an issue or pull request, or message me on GitHub.

- Issue Tracker: https://github.com/isaacharrisholt/dagstd/issues
- Source Code: https://github.com/isaacharrisholt/dagstd

Support
-------

If you are having issues, please let me know.

License
-------

The project is licensed under the GNU GPLv3 license.