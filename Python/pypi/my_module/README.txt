# How to make a python module
## Directory Structure
   
    My_module/
        LICENSE.txt
        README.txt
        setup.py
        My_module/
            __init__.py
            
## The setup.py file
The setup.py file is the heart of any python module or library. It describes the module and lists some other useful info about the module like it lists any dependencies on which a module depends and it also tells distutils where to find the necessary scripts of this module. So lets describe our module with the help of our setup.py file.

## Making your first release
So how do we make our first release ? Just follow me. Your release should have a single archive file. It can be easily made with this command.
  
    $ python setup.py sdist
    
##Publishing your module
Now that archive file can be uploaded anywhere for distribution but we will focus on PyPI. In order to upload on PyPI you will first have to make an account on http://pypi.python.org/pypi . After that you will have to register your package on PyPI like this:

    $ cd path/to/My_module
    $ python setup.py register
    $ python setup.py sdist upload
