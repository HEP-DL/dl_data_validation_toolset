#import h5py
#import os
import numpy as np
import logging
from dl_data_validation_toolset.framework import base_test

class DigitsTests(base_test.BaseTest):
    logger = logging.getLogger('data_tests.digits')

    def test_digits_exist(self):
        labels = self._file['label/type']
        logging.debug("Labels: {}".format(labels))
        assert(labels is not None)
        assert(len(labels)>0)
        logging.debug("Number of label vectors: {}".format(len(labels)))
        return labels

