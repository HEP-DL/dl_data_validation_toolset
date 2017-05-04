"""
  Tests classes in dl_data_validation_toolset.framework.base_test
"""

from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.framework import report_gen
from dl_data_validation_toolset.framework.configuration import Configuration

import os


class Test_ReportGenerator(base_unittest.BaseTestCase):

  def test_can_find_templates(self):
    """
      Ensures that invalid cases are handled appropriately
    """
    my_gen = report_gen.ReportGenerator(Configuration.default())
    assert(os.path.isdir(my_gen.template_directory))
    index_file = os.path.join(my_gen.template_directory, 'index.mako')
    assert(os.path.isfile(index_file))
