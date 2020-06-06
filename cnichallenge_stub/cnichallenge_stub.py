#!/usr/bin/env python                                            
#
# cnichallenge_stub ds ChRIS plugin app
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
import sys
sys.path.append(os.path.dirname(__file__))

# import the Chris app superclass
from chrisapp.base import ChrisApp

# Import the example python function that performs random label assignments to data
from example_python.classification_test_code import classification_random

Gstr_title = """

 _____  _   _ _____   _____ _           _ _                       
/  __ \| \ | |_   _| /  __ \ |         | | |                      
| /  \/|  \| | | |   | /  \/ |__   __ _| | | ___ _ __   __ _  ___ 
| |    | . ` | | |   | |   | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \
| \__/\| |\  |_| |_  | \__/\ | | | (_| | | |  __/ | | | (_| |  __/
 \____/\_| \_/\___/   \____/_| |_|\__,_|_|_|\___|_| |_|\__, |\___|
                                                        __/ |     
                                                       |___/      

"""

Gstr_synopsis = """

    NAME

       cnichallenge_stub.py 

    SYNOPSIS

        python cnichallenge_stub.py                                         \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution of a python example to read in IDs from folders names 
	(assumes CNI Challenge data structure), perform a random task (assigning labels)
	and outputs to a text file ('classification.csv'):

            > mkdir inputDir outputDir && chmod 777 outputDir
            > python cnichallenge_stub.py inputDir outputDir
            
	N.B. Required data should be in 'inputDir' as provided by CNI Challenge
	(see https://fnndsc.childrens.harvard.edu/cnichallenge/
            Output will be outputdir/classification.txt and outputdir/scores.txt.


    DESCRIPTION

        `cnichallenge_stub.py` contains an example to randomly classify input data from the 
	CNI Challenge (www.brainconnectivity.net). The purpose is to demonstrate how this
	code can be converted into a ChRIS compatible Docker image to submit a trained
	classification model to the Challenge Evaluation Portal.

    ARGS

        <inputDir> 
        Mandatory. A directory which contains Challenge input files.
        
        <outputDir>
        Mandatory. A directory where output will be saved to. Must be universally writable to.

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 

"""


class Cnichalleng_stub(ChrisApp):
    """
    This stub allows users to populate with their trained model to be containerized via Docker Hub. The resulting Docker image can then be entered into the CNI Challenge Evaluation Portal to execute the user's classification model on hidden test data, and its performance evaluated.
    """
    AUTHORS                 = 'AWC (aiwern.chung@childrens.harvard.edu)'
    SELFPATH                = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC                = os.path.basename(__file__)
    EXECSHELL               = 'python3'
    TITLE                   = 'Example plugin to populate with trained model for CNI Challenge Evaluation Portal'
    CATEGORY                = ''
    TYPE                    = 'ds'
    DESCRIPTION             = 'This stub is for users to populate with their trained model to be containerized via Docker Hub. The resulting Docker image can then be entered into the CNI Challenge Evaluation Portal (https://fnndsc.childrens.harvard.edu/cnichallenge) to be executed on the hidden test data, and the model performance evaluated.'
    DOCUMENTATION           = 'http://wiki'
    VERSION                 = '0.1'
    ICON                    = '' # url of an icon image
    LICENSE                 = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())

        # ===============================================
        # Initialising variables
        # ===============================================
        inputdir_data = '%s' % (options.inputdir)
        outputpath = '%s' % (options.outputdir)

        # ===============================================
        # Call code - Invoke the training model here
        # ===============================================

        # Call python module
        print("\n")
        print("\tCalling python code to do some random task on input data...")
        classification_random(inputdir_data, outputpath)
        print ("\tOutput will be in %s/classification.csv" % outputpath)
        print("====================================================================================")

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


# ENTRYPOINT
if __name__ == "__main__":
    chris_app = Cnichalleng_stub()
    chris_app.launch()
