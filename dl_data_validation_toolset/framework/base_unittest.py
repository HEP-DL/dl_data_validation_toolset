import unittest
from mock import patch
import logging
import sys


class BaseTestCase(unittest.TestCase):

  def setUp(self):
    """
      Monkeypatches the file functionality out so that we don't 
      run on real files during unit tests.
    """
    logging.basicConfig( stream=sys.stderr, level=logging.DEBUG )
    self.patcher = patch('h5py.File')
    self.mock_file = self.patcher.start()

  def tearDown(self):
    self.patcher.stop()
