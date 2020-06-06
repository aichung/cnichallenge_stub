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

This stub was created for the Connectomics in NeuroImaging Challenge that was held at MICCAI: http://www.brainconnectivity.net/challenge.html

This stub is for you to populate with your trained model that is to be containerized via Docker Hub. The resulting Docker image can then be entered into the CNI Challenge Evaluation Portal (https://fnndsc.childrens.harvard.edu/cnichallenge/submit.html). This will run the classification model on our hidden test data, and the performance of the model will be automatically evaluated and printed to screen.

While ``cnichallenge_stub.py`` is coded in Python and contains a bare bones example that is also in Python, models in other languages are possible to include. Such programs need only be called via the os.system() Python function.

``pl-cnichallenge_stub`` is a ChRIS-based application: https://chrisproject.org, created using https://github.com/FNNDSC/cookiecutter-chrisapp.


Synopsis
--------

.. code::

    python cnichallenge_stub.py                                           \
        [-v <level>] [--verbosity <level>]                          \
        [--version]                                                 \
        [--man]                                                     \
        [--meta]                                                    \
        <inputDir>  [mandatory]
        <outputDir> [mandatory]

Installation Requirements and Quick Setup
----------------------------

1. Install ``Python`` (3.5+) and ``pip`` (which is usually installed with Python)
2. Create a GitHub account on https://github.com, and install on machine.
3. Create a DockerHub account on https://hub.docker.com .
4. Install latest ``Docker`` (17.04.0+) if you want to test your plugin's Docker image and containers on your local machine. 
   To install on Ubuntu 18.04:      
      
.. code:: bash

            apt-get remove docker docker-engine docker.io 
            apt install docker.io  
    
Otherwise, visit https://docs.docker.com/install/ for installation directions

5. Fork this pl-cnichallenge_stub repository to your GitHub.
6. Log onto your DockerHub account and create a new repository with automated build.
   In 'Account Settings' -> 'Linked Accounts', connect your GitHub account to DockerHub.

   Then back in your DockerHub home, click the ``Create Repository +``  button. The website page will walk you through setting up the automated build. When prompted for the GitHub repository that you’d like to use for the automated build select the pl-cnichallenge_stub repository that you just forked/cloned. Name the Docker repository ${cnichallenge_DockerRepo} and make it Public.

   **It is extremely important that you tag your automatically built docker image with an appropriate version number based on your GitHub tags**.
      Do not delete the default build rule that is already in place, this handles the 'latest' tag for pulling the most recent Docker image.
   Create a new build rule by clicking the ``BUILD RULES +``  button. A good rule would be **Source type:** ``Tag``,
   **Source:** ``/^[0-9.]+$/`` and **Docker Tag:** ``version-{sourceref}``.

   Click ``Create && Build``  button to finish the setup and trigger the automated build.

   After the build has completed, the ``cnichallenge_stub`` bare bones example is now available as a Docker image to be pulled from your DockerHub. The link to it will be ${your_Docker_account name}/${cnichallenge_DockerRepo}.
   
   ***${your_Docker_account name}/${cnichallenge_DockerRepo} is the link to copy in our Challenge Evaluation Portal***

Description
-----------

``cnichallenge_stub.py`` is a ChRIS-based application that contains an example to randomly classify input data from the 
	CNI Challenge (www.brainconnectivity.net). The purpose is to demonstrate how this
	code can be converted into a ChRIS compatible Docker image to submit a trained
	classification model to the Challenge Evaluation Portal.


Agruments
---------

.. code::

    <inputDir> 
    Mandatory. A directory which contains Challenge data files.
        
    <outputDir>
    Mandatory. A directory where output will be saved. Must be universally writable to.
    
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

This ``plugin`` can be run in two modes: natively as a python package or as a containerized Docker image.

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

***For the bare bones example, make sure to download and copy Challenge Training or Validation datasets to the input directory. For data: http://www.brainconnectivity.net/challenge_data.html***


Using ``docker run``
~~~~~~~~~~~~~~~~~~~~

Pull the latest ``cnichallenge_stub`` image to your machine and create input and output folders. *Make sure that the* ``$(pwd)/outputDir`` *directory is world writable!*

.. code:: bash

    docker pull ${your_Docker_account name}/${cnichallenge_DockerRepo}
    mkdir inputDir outputDir && chmod 777 outputDir

Copy Challenge Test or Validation data from http://www.brainconnectivity.net/challenge_data.html to the input folder.

To run using ``docker``, be sure to assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code:: bash

    sudo docker run --rm -v $(pwd)/inputDir:/incoming -v $(pwd)/outputDir:/outgoing \
    ${your_Docker_account name}/${cnichallenge_DockerRepo} cnichallenge_stub.py     \
    /incoming /outgoing

The output file ``classifications.txt``, will be in  ``outputdir``.

Our bare bones Docker image can be retrieved (from DockerHub 'aiwc') and executed (calling 'man') on your machine as follows (with directories 'inputDir' and 'outputDir' as specified above):

.. code:: bash

    docker pull aiwc/pl-cnichallenge_stub
    sudo docker run --rm -v $(pwd)/inputDir:/incoming -v $(pwd)/outputDir:/outgoing      \
                 aiwc/pl-cnichallenge_stub cnichallenge_stub.py                          \
                 --man                                                                   \
                 /incoming /outgoing


Classification Model Output Format
-------------------------------------
The results from your model should be output into a text file in the following format: 

	Classification labels should be 0 = Controls, 1 = Patient;
	Prediction probability or score for each subject is required;			
	The output file should contain comma-separated values and named "classification.csv";
	Each row must contain the subject ID, the classification label, and the prediction probability (one 			row per subject)
.. code:: bash	
	eg.
		sub-066,1,0.7269782399142388
		sub-090,0,0.8111361229380137
		.
		.
		.
		sub-111,0,0.60761617828937793
		sub-115,1,0.836589863164504


