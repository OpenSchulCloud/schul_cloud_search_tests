Search Tests
============

These are the tests to run on every request.
We use PyTest_ to run the tests.

There are two phases to execute tests:

1. The client makes a request. The request needs to be tested.
   It is a `bottle.BaseRequest <https://bottlepy.org/docs/dev/api.html#bottle.BaseRequest>`_ object.
   Such a test can look like this:

   .. code:: Python

       import pytest
       
       @pytest.mark.request
       def test_TESTNAME(request):
           # ...

2. The requests pass and the client responded. In this case, all tests in this folder
   are executed if the have not been marked with `pytest.mark`_.request.


.. _PyTest: https://docs.pytest.org/en/latest/index.html
.. _pytest.mark: https://docs.pytest.org/en/latest/mark.html?highlight=mark#api-reference-for-mark-related-objects
