"""
  Tests classes in dl_data_validation_toolset.framework.base_test
"""

from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.framework.base_test import BaseTest


class MyTestCase(BaseTest):
  """
    Dummy validation tests.
  """
  def test_true(self):
    """
      creates a passing test
    """
    assert(True)

  def test_false(self):
    """
      creates a failing test
    """
    assert(False)


class Test_BaseTest(base_unittest.BaseTestCase):

    def test_gather_tests(self):
      """
        Tests whether or not the class specific tests can be gathered
      """
      my_data_test = MyTestCase("whatever.h5")
      assert(len(my_data_test._tests_) == 2)
      assert("test_false" in my_data_test._tests_)
      assert("test_true" in my_data_test._tests_)

    def test_valid_result(self):
      """
        Tests if  passing unit test gets gathered and passed
      """
      my_data_test = MyTestCase("whatever.h5")
      results = my_data_test.get_results()
      assert('test_true' in results)
      assert(results['test_true']['passed'])

    def test_invalid_result(self):
      """
        Ensures that invalid cases are handled appropriately
      """
      my_data_test = MyTestCase("whatever.h5")
      results = my_data_test.get_results()
      assert('test_false' in results)
      assert(not results['test_false']['passed'])
      assert('assert' in results['test_false']['result'])
