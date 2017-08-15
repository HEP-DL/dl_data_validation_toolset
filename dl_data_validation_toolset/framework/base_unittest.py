from mock import patch
import unittest
import logging
import sys


class BaseTestCase(unittest.TestCase):
  """
    Common definitions and actions for unit tests for this framework.

    An example:

    .. codeblock: python

      from dl_data_validation_toolset.framework import BaseTestCase
      class MyTestCase(BaseTestCase):
        def setUp(self):
          super().setupUp(self)
          # Do your setup here
        def tearDown(self):
          # Do your teardown here
          super().tearDown(self)
        def test_my_function(self):
          pass
          # Do more of your testing here.
  """

  def setUp(self):
    """
      Monkeypatches the file functionality out so that we don't
      run on real files during unit tests.
    """
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    self.patcher = patch('h5py.File')
    self.mock_file = self.patcher.start()

  def tearDown(self):
    """
      Releases the monkeypatch.
    """
    self.patcher.stop()
