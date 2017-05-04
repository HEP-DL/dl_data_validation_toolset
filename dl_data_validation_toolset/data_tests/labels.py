import numpy as np
import logging
from dl_data_validation_toolset.framework import base_test


class LabelTests(base_test.BaseTest):
    logger = logging.getLogger('data_tests.labels')

    def test_label_exists(self):
        labels = self._file['label/type']
        logging.debug("Labels: {}".format(labels))
        assert(labels is not None)
        assert(len(labels) > 0)
        logging.debug("Number of label vectors: {}".format(len(labels)))
        return labels

    def test_nonzero_labels(self):
        labels = self._file['label/type']
        null_vectors = 0
        for labelvec in labels:
            self.logger.debug(labelvec)
            if np.max(labelvec) == 0:
                self.logger.debug("Found null vector: {}".format(labelvec))
                null_vectors += 1
        return {'null_vectors': null_vectors}

    def test_label_diversity(self):
        labels = self._file['label/type']
        label_accumulator = np.ndarray(shape=(len(labels[0])))
        for labelvec in labels:
            label_accumulator += labelvec
        result = {}
        result['valid'] = np.max(label_accumulator) == 0
        result['valid'] = result['valid'] or np.min(label_accumulator) == 0
        result['labels'] = label_accumulator
        return result
