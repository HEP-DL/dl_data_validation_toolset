from .file import FileGenerator
from ..report.group import GroupReport
import logging
import asyncio
import os


class GroupGenerator(object):
  logger = logging.getLogger("ddvt.rep_gen.grp")

  def __init__(self, group):
    self.meta = group

  async def generate(self, parent):
    self.logger.info("Generating Group Report: {}".format(self.meta.group))
    self.temp_dir = os.path.join(parent.temp_dir, self.meta.group)
    file_gens = [FileGenerator(i) for i in self.meta.full_filenames]
    tasks = [asyncio.ensure_future(i.generate(self)) for i in file_gens]
    asyncio.wait(tasks)
    for i in tasks:
      await i
    self.logger.info("Finished with subtasks for group {}".format(self.meta.group))
    self.report = GroupReport(self.meta.group, self.temp_dir)
    self.report.file_reports = [i.report for i in file_gens]
    self.report.render(self.temp_dir)
