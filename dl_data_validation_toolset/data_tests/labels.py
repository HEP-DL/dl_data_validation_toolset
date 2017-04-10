#import h5py
#import os
#import numpy as np
import logging
from dl_data_validation_toolset.framework import base_test

class LabelTests(base_test.BaseTest):
    logger = logging.getLogger('data_tests.labels')

    def go(self):
        return
        labels = _f['label/type']
        #print "  rawdigits  wires  type  consistent"
        #print "  {}        {}    {}   {}".format(len(rawdigits), len(wires), len(labels), len(rawdigits)== len(wires) and len(wires)==len(labels))
        # now check on the labels                                               
        label_accumulator = np.ndarray(shape = (len(labels[0])))
        for labelvec in labels:
            if np.max(labelvec)==0:
                print "  WARNING: Found null vector"
            label_accumulator+=labelvec
        if np.max(label_accumulator) == 0 or np.min(label_accumulator) == 0:
            print "Warning: zeroed columns in label vector"
        #print label_accumulato
