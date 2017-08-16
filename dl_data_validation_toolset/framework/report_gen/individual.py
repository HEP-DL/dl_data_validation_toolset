import logging
from ..report.individual import IndividualReport


class IndividualGenerator(object):
  logger = logging.getLogger("ddvt.rep_gen.ind")

  def __init__(self, test):
    self.test = test

  async def generate(self, parent):
    test_group = self.test(parent.filename)
    for test in test_group._tests_:
      self.logger.info("Starting Test: {}".format(test))
      try:
        result, status = getattr(test_group, test)()
        parent.report.reports.append(IndividualReport(test, status, result))
        # TODO: Figure out what to do next
      except Exception as e:
        self.logger.warning("failed test")
        parent.report.reports.append(IndividualReport(test, 0,
                                                      {'error': str(e)}))
