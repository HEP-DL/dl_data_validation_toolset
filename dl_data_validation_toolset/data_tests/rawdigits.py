import logging
from dl_data_validation_toolset.framework import base_test


class DigitsTests(base_test.BaseTest):
    logger = logging.getLogger('data_tests.digits')

    def test_digits_exist(self):
        digits = self._file['image/rawdigits']
        valid = int(digits is not None)
        valid += int(len(digits) > 0)
        return {'N Digits': len(digits)}, valid
