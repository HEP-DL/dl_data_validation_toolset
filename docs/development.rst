Development
===========

This package is very much a work in progress.

Test Driven Development
-----------------------

Unit tests are kept in the `tests` directory. These are unit tests for developing code.
This is not to be confused with data tests, though the code pattern for both resemble each other.

These can be run with the command:

.. code-block:: bash

  make test


Bear in mind that flake8 is used to lint the code.


Documentation
-------------

Documentation can be built with:

.. code-block:: bash

  make docs

Inline documentation follows Sphinx guidelines. `An example can be found here`__.

__ sphinx_
.. _sphinx: https://pythonhosted.org/an_example_pypi_project/sphinx.html


Data Tests
----------

The data validation tests can be found in dl_data_validation_toolset/data_tests.

To create a new data validation test or series of tests, simply copy one of the examples (such as consistency). Once your test is ready, please modify `__test_names__` to match the filename of your new test, minus the file extension.


