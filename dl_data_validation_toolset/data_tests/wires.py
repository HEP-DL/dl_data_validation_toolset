import logging
from dl_data_validation_toolset.framework import base_test


class WiresTests(base_test.BaseTest):
    logger = logging.getLogger('data_tests.wires')

    def test_nonempty(self):
        data = self._file['image/wires']
        valid = len(data) > 0
        return {'Is Non Empty': valid}, valid

    def test_digits_exist(self):
        wiers = self._file['image/wires']
        valid = int(wiers is not None)
        valid += int(len(wiers) > 0)
        return {'N Wires': len(wiers)}, valid
