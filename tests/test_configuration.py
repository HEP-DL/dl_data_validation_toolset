from dl_data_validation_toolset.framework.configuration import Configuration
from dl_data_validation_toolset.framework import base_unittest
from mock import patch
import unittest
import logging
import sys
import os


class TestConfiguration(base_unittest.BaseTestCase):
  """
    Tests :code:`dl_data_validation_toolset.framework.configuration.Configuration`.
  """

  def test_can_read_example(self):
    logging.info(os.getcwd())
    c = Configuration()
    c.configure('examples/example.json')
    assert('something_dl' in ''.join(c.scan_paths))
    assert('results' in c.results_path)
    assert(c.results_path == os.path.abspath(c.results_path))

  def test_defaults(self):
    c = Configuration()
    assert('data' in c.scan_paths[0])
    assert(len(c.scan_paths) == 1)
    assert('results' in c.results_path)

  @patch('os.listdir')
  def test_null_scan(self, os_patch):
    os_patch.return_value = []
    c = Configuration()
    c.scan()
    assert(len(c.groups)==0)

  @patch('os.listdir')
  def test_nonnull_scan(self, os_patch):
    os_patch.return_value = ['my_1.h5','something_2.h5','notafile']
    c = Configuration()
    c.scan()
    assert(len(c.groups)==2)
