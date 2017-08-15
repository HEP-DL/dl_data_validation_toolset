"""
  Tests classes in dl_data_validation_toolset.framework.base_test
"""

from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.framework.base_test import BaseTest
from dl_data_validation_toolset.framework.report import FileReport


class MyTestCase(BaseTest):
  """
    Dummy validation tests. DO NOT ERASE.
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
      report = FileReport("test_report")
      my_data_test.validate(report)
      assert(not report.valid)
      assert(report.reports[0].status == 0)

    def test_invalid_result(self):
      """
        Ensures that invalid cases are handled appropriately
      """
      my_data_test = MyTestCase("whatever.h5")
      report = FileReport("test_report")
      my_data_test.validate(report)
      assert(not report.valid)
      assert(report.reports[1].status == 0)
