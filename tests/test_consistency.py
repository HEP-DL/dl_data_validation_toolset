from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.data_tests.consistency import ConsistencyTests
from dl_data_validation_toolset.framework.report import FileReport


class TestDl_Consistency(base_unittest.BaseTestCase):

  def test_basic_consistency(self):
    label_test = ConsistencyTests('somefile.h5')

    def getitem(name):
      if 'label' in name:
        return [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
      elif 'wire' in name:
        return [[], [], []]
      else:
        return [[], [], []]

    label_test._file.__getitem__.side_effect = getitem
    report = FileReport("myfile")
    label_test.validate(report)
