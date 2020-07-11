.. create-library-from-scratch documentation master file, created by
   sphinx-quickstart on Sat Jul 11 14:22:22 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=======================================================
create-library-from-scratch's Documentation
=======================================================
.. image:: https://github.com/walkacross/create-library-from-scratch/workflows/hello-world/badge.svg


the create-library-from-scratch is to show how to create a production ready library from scratch.

.. note::

    this repo will walk throuth the full workflow of create a python library

feature
============================

=====================================    =====================================================================================
step 0.1: init setup                     create readme.md, lience and .gitignore in your empty repository
step 0.2: add CI                         add the continuous integration(CI) with github action by simplest case
step 0.3: add online docs                add professional documents by using `sphinx theme`_ and hosted in `readthedoc.com`_
step 0.4: make it be a library           add setup.py, requirements and your first function in your library
step 0.5: package and publication        package and make publication in PYPI
=====================================    =====================================================================================

Philosophy
============================

the create-library-from-scratch focuses on production ready library, viewing CI, documentation, test, type hint, tutorials and example, coding style as part of code. 


.. _sphinx theme: https://www.sphinx-doc.org/en/master/
.. _readthedoc.com: https://readthedocs.org/

.. toctree::
    :caption: basics
    :hidden:
    
    intro/overview
    intro/install


