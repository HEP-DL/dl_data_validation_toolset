Usage
=====

Command Line Utility
--------------------

The primary interface is the command line interface.

By default, the command line utility can be called with 


  generate_report


This will look for data in the ``data`` subdirectory of the current working directory and place output in the ``results`` subdirectory of the current working directory.

The library can be configured with ``YAML`` by specifying the ``--config`` flag.

An example configuration YAML looks like:


  results_path: /home/my_user/results
  scan_paths: [/home/my_user/dl_data/, /data/]

Output
------

The command link util creates a tarball of the HTML output of the report generator. This is placed in the results path and is named by current time stamp.

If one untars the ball and opens the ``index.html`` file, the summary page contains links to file reports, etc...

Note that in order for the page to appear correctly, internet connectivity is required.


Python API
----------

Refer to the :modules: page.



