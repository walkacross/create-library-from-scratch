=====================
step2_create_doc
=====================

general operation
===================================

Assuming you have Python already, install Sphinx:

.. code-block:: bash

    $ pip install sphinx
    
Create a directory inside your project to hold your docs:

.. code-block:: bash

    $ cd /path/to/project
    $ mkdir docs

Run sphinx-quickstart in there:

.. code-block:: bash

    $ cd docs
    $ sphinx-quickstart

This quick start will walk you through creating the basic configuration; in most cases, you can just accept the defaults. When it’s done, you’ll have an index.rst, a conf.py and some other files. Add these to revision control.

Now, edit your index.rst and add some information about your project. Include as much detail as you like (refer to the reStructuredText syntax or this template if you need help). Build them to see how they look:

.. code-block:: bash

    $ sphinx-build -b html source build

you can see a file named index.html in the build folder, then open it.


appendix 1: use sphinx-rtd-theme
========================================

if you want to use the sphinx-rtd-theme theme, you need put a requirements.txt under the docs.

.. code-block:: python

    Sphinx==3.1.2
    sphinx-rtd-theme
    

and then in the conf.py, you need input some code like:

.. code-block:: python

    import sphinx_rtd_theme
    
    extensions = [ ...,
    "sphinx_rtd_theme",
    ]
    html_theme = 'sphinx_rtd_theme'


appendix 2: use language except for english
=================================================

if your docs written in other language like chinese, you need to put some keywords in conf.py, something like

.. code-block:: python

    language = 'zh'
    latex_engine = 'xelatex'
    latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'extraclassoptions': 'oneside',
    'preamble': r'''
    \usepackage[titles]{tocloft}
    \usepackage{ctex}
    \setmainfont{Noto Serif}
    \setsansfont{Noto Sans}
    \setmonofont{Noto Sans Mono}
    \setCJKmainfont{Noto Serif CJK SC}
    \setCJKsansfont{Noto Sans CJK SC}
    \setCJKmonofont{Noto Sans Mono CJK SC}
    '''
    }
    

appendix 3: use autodoc
=======================================

if you want some doc content dicrectly generated from the function's comments in library. you need use the
sphinx.ext.autodoc extention.


sphinx-build locally
-----------------------------------
.. code-block:: python

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.coverage',
        'sphinx.ext.viewcode',
        "sphinx_rtd_theme",
    ]
    add_module_names = False
    
    
if you sphinx-build locally, that's it.


sphinx-build remotely
---------------------------------

if you want to build it on cloud like readthedoc.com, you need to add additonal code to build it.


.. code-block:: python

    # add the library path to environment path
    import os
    import sys
    from os import path
    root_dir = path.dirname(path.dirname(path.dirname(__file__)))
    sys.path.insert(0, root_dir)

    #for autodoc
    #to make the library work remotely, you need install that dependency
    # == autodoc_mock_imports
    autodoc_dependency = os.path.join(root_dir, "requirements.txt")
    os.system("pip install -r {}".format(autodoc_dependency))







    

