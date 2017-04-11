import numpy as np
import logging
from dl_data_validation_toolset.framework import base_test

class ConsistencyTests(base_test.BaseTest):
  logger = logging.getLogger('data_tests.labels')

  def test_consistent_labels_wires(self):
    labels = self._file['label/type']
    wires = self._file['image/wires']
    assert(len(labels) == len(wires))
    return {'wires':wires, 'labels':labels}

  def test_consistent_labels_rawdigits(self):
    labels = self._file['label/type']
    rawdigits = self._file['image/rawdigits']
    assert(len(labels) == len(rawdigits))
    return {'rawdigits':rawdigits, 'labels':labels}

  def test_consistent_digits_wires(self):
    digits = self._file['image/rawdigits']
    wires = self._file['image/wires']
    assert(len(digits) == len(wires))
    return {'wires':wires, 'rawdigits':digits}