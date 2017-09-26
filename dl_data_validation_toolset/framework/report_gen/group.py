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
    os.mkdir(self.temp_dir)
    file_gens = [FileGenerator(i) for i in self.meta.full_filenames]

    await asyncio.gather(*[i.generate(self) for i in file_gens])

    msg = "Finished with subtasks for group {}".format(self.meta.group)
    self.logger.info(msg)
    self.report = GroupReport(self.meta.group, self.temp_dir)
    self.report.file_reports = [i.report for i in file_gens]
    self.report.render(self.temp_dir)
