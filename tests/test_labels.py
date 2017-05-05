from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.data_tests.labels import LabelTests
from dl_data_validation_toolset.framework.report import FileReport


class TestDl_CLI(base_unittest.BaseTestCase):

  def test_label_existence(self):
    label_test = LabelTests('somefile.h5')

    def getitem(name):
      return [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

    label_test._file.__getitem__.side_effect = getitem
    report = FileReport("my report")
    label_test.validate(report)
    for i in report.reports:
      if i.name == 'test_label_exists':
        assert(i.status > 0)

  def test_zero_labels(self):
    label_test = LabelTests('somefile.h5')

    def getitem(name):
      return [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1]]

    label_test._file.__getitem__.side_effect = getitem
    report = FileReport("my report")
    label_test.validate(report)
    for i in report.reports:
      if i.name == 'test_nonzero_labels':
        assert(i.status > 0)
        assert(i.fields['null_vectors'] == 1)

  def test_nonzero_labels(self):
    label_test = LabelTests('somefile.h5')

    def getitem(name):
      return [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

    label_test._file.__getitem__.side_effect = getitem
    report = FileReport("my report")
    label_test.validate(report)
    for i in report.reports:
      if i.name == 'test_nonzero_labels':
        assert(i.status > 0)
        assert(i.fields['null_vectors'] == 0)
