from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.framework.base_test import BaseTest


class TestDl_CLI(base_unittest.BaseTestCase):
  """
    Tests the functionality in cli.py
  """

  def test_subclass_register(self):
    """
      Tests that the CLI is able to successfully find the
      validation tests.
    """
    assert(len(BaseTest.__subclasses__()) > 0)
