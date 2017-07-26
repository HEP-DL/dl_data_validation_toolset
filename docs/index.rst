Welcome to DL Data Validation Toolset's documentation!
======================================================

The DL Data Validation Toolset is a framework built around a series of tools meant to help establish if a generated HDF5 file for the DL in HEP effort contains valid data. Each test is meant to be run as a unit test on a generated file and establish what the file contains along with problems that might arise due to using this file for deep learning.

Goal
====

The goal of this project is to create comprehensive reports on data produced external to the deep learning framework. Reports created should contain information on the validity of using these files in Deep Learning Frameworks as well as detailed information on the contents of the files and diagnostically relevant calculations.

Part of the diagnostic tools should be some visualization of the contents of the files.


.. toctree::
   :maxdepth: 3
   :caption: Contents:
   
   installation
   usage
   development
   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
