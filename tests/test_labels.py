from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.data_tests.labels import LabelTests
import logging


class TestDl_CLI(base_unittest.BaseTestCase):

  def test_label_existence(self):
    label_test = LabelTests('somefile.h5')

    def getitem(name):
      return [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

    label_test._file.__getitem__.side_effect = getitem
    results = label_test.get_results()
    logging.debug(results)
    assert(results['test_label_exists']['passed'])

  def test_zero_labels(self):
    label_test = LabelTests('somefile.h5')

    def getitem(name):
      return [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]]

    label_test._file.__getitem__.side_effect = getitem
    results = label_test.get_results()
    assert(results['test_nonzero_labels']['passed'])
    assert(results['test_nonzero_labels']['result']['null_vectors'] == 1)

  def test_nonzero_labels(self):
    label_test = LabelTests('somefile.h5')

    def getitem(name):
      return [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

    label_test._file.__getitem__.side_effect = getitem
    results = label_test.get_results()
    assert(results['test_nonzero_labels']['passed'])
    assert(results['test_nonzero_labels']['result']['null_vectors'] == 0)
