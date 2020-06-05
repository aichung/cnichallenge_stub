
import sys
import os


# Make sure we are running python3.5+
if 10 * sys.version_info[0] + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")


from setuptools import setup


def readme():
    print("Current dir = %s" % os.getcwd())
    print(os.listdir())
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   'cnichallenge_stub',
      # for best practices make this version the same as the VERSION class variable
      # defined in your ChrisApp-derived Python class
      version          =   '0.1',
      description      =   'This stub allows users to populate with their trained model to be containerized via Docker Hub. The resulting Docker image can then be entered into the CNI Challenge Evaluation Portal to execute the classification model on hidden test data, and its performance evaluated.',
      long_description =   readme(),
      author           =   'AWC',
      author_email     =   'aiwern.chung@childrens.harvard.edu',
      url              =   'http://wiki',
      packages         =   ['cnichallenge_stub'],
      install_requires =   ['chrisapp', 'pudb'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['cnichallenge_stub/cnichallenge_stub.py'],
      license          =   'MIT',
      zip_safe         =   False
     )
