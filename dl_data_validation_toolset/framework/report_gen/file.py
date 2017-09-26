from dl_data_validation_toolset.data_tests import initialize
from .individual import IndividualGenerator
from ..report.file import FileReport
from ..base_test import BaseTest
import logging
import asyncio
import os


class FileGenerator(object):
  logger = logging.getLogger("rep_gen.file")

  def __init__(self, filename):
    self.filename = filename

  async def generate(self, parent):
    initialize()
    self.logger.info("Generating file report for {}".format(self.filename))
    self.temp_dir = os.path.join(parent.temp_dir,
                                 self.filename.split(".h5")[0])
    self.mkdir(self.temp_dir)
    self.report = FileReport(self.filename, self.temp_dir)
    file_gens = [IndividualGenerator(i) for i in BaseTest.__subclasses__()]

    await asyncio.gather(*[i.generate(self) for i in file_gens])
    self.report.render(os.path.join(parent.temp_dir, self.report.slug))
