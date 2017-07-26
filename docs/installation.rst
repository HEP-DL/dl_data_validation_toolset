Installation
============

Prereqs
-------

This framework depends heavily on HDF5. Users should have the HDF5 libraries with compression back installed.

For instance, on Ubuntu, this can be accomplished with 

.. code-block:: bash

  sudo apt-get install libhdf5-serial-dev


Similarly, on RHEL, this is done with ``dev`` being replaced by ``devel``.


Installation with Pip
---------------------

For non-development usage, one may install with:

.. code-block:: bash

  pip install <options> git+https://github.com/HEP-DL/dl_data_validation_toolset


Where <options> typically contain ``--user``, ``--upgrade`` or both.


Installation with dist-utils
----------------------------

For development usage, one may install with:

.. code-block:: bash

  git clone https://github.com/HEP-DL/dl_data_validation_toolset
  cd dl_data_validation_toolset
  make install

