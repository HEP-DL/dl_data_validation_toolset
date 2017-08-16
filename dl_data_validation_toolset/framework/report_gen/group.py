from .file import FileGenerator
from ..report.group import GroupReport
import asyncio
import os


class GroupGenerator(object):

  def __init__(self, group):
    self.meta = group

  async def generate(self, parent):
    self.temp_dir = os.path.join(parent.temp_dir, self.meta)
    file_gens = [FileGenerator(i) for i in self.meta.files]
    tasks = [asyncio.ensure_future(i.generate(self)) for i in gens]
    asyncio.wait(tasks)
    self.report = GroupReport(self.meta.name, self.temp_dir)
    self.report.files = [i.report for i in self.file_gens]
    self.report.render()
