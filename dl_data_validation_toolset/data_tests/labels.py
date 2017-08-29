import numpy as np
import logging
from dl_data_validation_toolset.framework import base_test


class LabelTests(base_test.BaseTest):
    logger = logging.getLogger('data_tests.labels')

    def test_nonempty(self):
        labels = self._file['label/type']
        valid = len(labels) > 0
        return {'Is Non Empty': valid}, valid

    def test_label_exists(self):
        labels = self._file['label/type']
        logging.debug("Labels: {}".format(labels))
        valid = int(labels is not None)
        valid += int(len(labels))
        return {'N Labels': len(labels)}, valid

    def test_nonzero_labels(self):
        labels = self._file['label/type']
        null_vectors = 0
        valid = 2
        for labelvec in labels:
            if np.max(labelvec) == 0:
                self.logger.debug("Found null vector: {}".format(labelvec))
                valid = 1
                null_vectors += 1
        if null_vectors == len(labels):
            valid = 0
        return {'null_vectors': null_vectors}, valid

    def test_label_diversity(self):
        labels = self._file['label/type']
        label_accumulator = np.ndarray(shape=(len(labels[0])))
        for labelvec in labels:
            label_accumulator += labelvec
        result = {}
        result['valid'] = np.max(label_accumulator) == 0
        result['valid'] = result['valid'] or np.min(label_accumulator) == 0
        result['labels'] = label_accumulator
        return result, 2
