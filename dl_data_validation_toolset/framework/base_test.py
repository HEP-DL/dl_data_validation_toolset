import h5py
import abc
from dl_data_validation_toolset.framework.report import IndividualReport
import logging


class BaseTest(object):

  __metaclass__ = abc.ABCMeta
  logger = logging.getLogger("test")

  def __init__(self, filename):
    self.logger.info("Scanning file: {}".format(filename))
    self._file = h5py.File(filename, 'r')

  @property
  def _tests_(self):
    return [att for att in dir(self) if att.startswith('test')]

  def validate(self, report):
    for test in self._tests_:
      self.logger.debug("Starting Test: {}".format(test))
      try:
        test_result, status = getattr(self, test)()
        self.logger.debug(test_result)
        self.logger.debug(status)
        report.reports.append(IndividualReport(test, status, test_result))
      except Exception as e:
        report.valid = False
        self.logger.warning("Critically failed test: {} with {}".format(test,
                                                                        e))
        report.reports.append(IndividualReport(test, 0, {'failure': str(e)}))
