UberCalc
========

A simple, sample project to show off front-end testing.

First, make a virtual environment and install the required
software::

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Then, you can start the server with::

    python server.py

You can run the Jasmine-based unit tests by just looking
at the rendered page; they appear there.

You can run the Selenium-based functional tests with::

    python tests.py

Or you can run the equivalent Selenium-based functional
tests written as a Docfile with::

    python -m doctest tests.txt

Happy testing!
