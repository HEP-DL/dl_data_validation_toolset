from dl_data_validation_toolset.data_tests import initialize
from .individual import IndividualGenerator
from ..report.file import FileReport
from ..base_test import BaseTest
import asyncio
import os


class FileGenerator(object):

  def __init__(self, filename):
    self.filename = filename

  async def generate(self, parent):
    initialize()
    self.temp_dir = os.path.join(parent.temp_dir, self.filename.strip(".h5"))
    file_gens = [IndividualGenerator(i) for i in BaseTest.__subclasses__()]
    tasks = [asyncio.ensure_future(i.generate(self)) for i in gens]
    asyncio.wait(tasks)
    self.report = FileReport(self.meta.name, self.temp_dir)
    self.report.files = [i.report for i in self.file_gens]
    self.reports.render()