import logging


class IndividualGenerator(object):
  logger = logging.getLogger("ddvt.rep_gen.ind")

  def __init__(self, test):
    self.test = test

  async def generate(self, parent):
    result = self.test(parent.filename)
    for test in self.test:
      self.logger.info("Starting Test: {}".format(test))
      try:
        result, status = getattr(self.test, test)()
        # TODO: Figure out what to do next
      except Exception as e:
        self.logger.error(e)