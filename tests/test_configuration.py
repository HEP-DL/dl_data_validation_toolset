import unittest
from dl_data_validation_toolset.framework.configuration import Configuration
import logging
import sys
import os

class ConfigurationTests(unittest.TestCase):

  def setUp(self):
    """
      Monkeypatches the file functionality out so that we don't 
      run on real files during unit tests.
    """
    logging.basicConfig( stream=sys.stderr, level=logging.DEBUG )

  def test_can_read_example(self):
    logging.info(os.getcwd())
    c = Configuration('examples/example.yaml')
    assert('something_dl' in ''.join(c.scan_paths))
    assert('results' in c.results_path)
    assert(c.results_path == os.path.abspath(c.results_path))

  def test_defaults(self):
    c = Configuration.default()
    assert('data' in c.scan_paths[0])
    assert(len(c.scan_paths)==1)
    assert('results' in c.results_path)