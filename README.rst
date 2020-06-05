pl-cnichallenge_stub
================================

.. image:: https://badge.fury.io/py/cnichallenge_stub.svg
    :target: https://badge.fury.io/py/cnichallenge_stub

.. image:: https://travis-ci.org/FNNDSC/cnichallenge_stub.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/cnichallenge_stub

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg
    :target: https://badge.fury.io/py/pl-cnichallenge_stub

.. contents:: Table of Contents


Abstract
--------

This stub allows users to populate with their trained model to be containerized via Docker Hub. The resulting Docker image can then be entered into the CNI Challenge Evaluation Portal to execute the classification model on hidden test data, and its performance evaluated.


Synopsis
--------

.. code::

    python cnichallenge_stub.py                                           \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        <inputDir>
        <outputDir> 

Description
-----------

``cnichallenge_stub.py`` is a ChRIS-based application that...

Agruments
---------

.. code::

    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.

    [--version]
    If specified, print version number. 
    
    [--man]
    If specified, print (this) man page.

    [--meta]
    If specified, print plugin meta data.


Run
----

This ``plugin`` can be run in two modes: natively as a python package or as a containerized docker image.

Using PyPI
~~~~~~~~~~

To run from PyPI, simply do a 

.. code:: bash

    pip install cnichallenge_stub

and run with

.. code:: bash

    cnichallenge_stub.py --man /tmp /tmp

to get inline help. The app should also understand being called with only two positional arguments

.. code:: bash

    cnichallenge_stub.py /some/input/directory /destination/directory


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``. *Make sure that the* ``$(pwd)/out`` *directory is world writable!*

Now, prefix all calls with 

.. code:: bash

    docker run --rm -v $(pwd)/out:/outgoing                             \
            fnndsc/pl-cnichallenge_stub cnichallenge_stub.py                        \

Thus, getting inline help is:

.. code:: bash

    mkdir in out && chmod 777 out
    docker run --rm -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
            fnndsc/pl-cnichallenge_stub cnichallenge_stub.py                        \
            --man                                                       \
            /incoming /outgoing

Examples
--------





