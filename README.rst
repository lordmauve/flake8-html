===========
flake8-html
===========


.. image:: https://img.shields.io/pypi/v/flake8_html.svg
        :target: https://pypi.python.org/pypi/flake8_html

.. image:: https://img.shields.io/travis/lordmauve/flake8_html.svg
        :target: https://travis-ci.org/lordmauve/flake8_html

.. image:: https://readthedocs.org/projects/flake8-html/badge/?version=latest
        :target: https://flake8-html.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/lordmauve/flake8_html/shield.svg
     :target: https://pyup.io/repos/github/lordmauve/flake8_html/
     :alt: Updates


A flake8 plugin to generate HTML reports of flake8 violations.

Simply

.. code-block:: bash

   $ pip install flake8-html

Then run flake8 passing the ``--format=html`` option and a ``--htmldir``:

.. code-block:: bash

   $ flake8 --format=html --htmldir=flake-report


License
-------

* Free software: Apache Software License 2.0

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

