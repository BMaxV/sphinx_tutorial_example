make new copies the the project and creates a "docs folder"

use

	sphinx-quickstart

options different from default for the quickstart I used:

doc root : new_project/docs
separate source and build : y
projectname: test
author : test_author
version : 0.1
autodoc docstrings : y
windows cmd file : n

then go to new_project/docs

and execute

    make html
    
This produces a nearly empty index page that goes nowhere and does nothing.


