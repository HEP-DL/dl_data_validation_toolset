from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.data_tests.consistency import ConsistencyTests
import logging


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
    results = label_test.get_results()
    logging.debug(results)
    assert(results['test_consistent_labels_wires'] is not None)

    assert(results['test_consistent_labels_wires']['passed'])
    assert(results['test_consistent_labels_rawdigits']['passed'])
    assert(results['test_consistent_digits_wires']['passed'])
