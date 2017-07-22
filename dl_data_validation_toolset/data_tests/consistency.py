import logging
from dl_data_validation_toolset.framework import base_test


class ConsistencyTests(base_test.BaseTest):
  logger = logging.getLogger('data_tests.labels')

  def test_consistent_labels_wires(self):
    labels = self._file['label/type']
    wires = self._file['image/wires']
    valid = int(len(labels) == len(wires)) + 1
    return {'wires': len(wires), 'labels': len(labels)}, valid
