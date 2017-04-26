#import h5py
#import os
import numpy as np
import logging
from dl_data_validation_toolset.framework import base_test

class WiresTests(base_test.BaseTest):
    logger = logging.getLogger('data_tests.wires')

    def test_digits_exist(self):
        wiers = self._file['images/wires']
        logging.debug("Labels: {}".format(labels))
        assert(labels is not None)
        assert(len(labels)>0)
        logging.debug("Number of label vectors: {}".format(len(labels)))
        return labels
