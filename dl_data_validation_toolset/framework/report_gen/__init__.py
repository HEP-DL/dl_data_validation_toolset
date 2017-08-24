from .group import GroupGenerator
from ..report import TopReport

import tempfile
import asyncio
import tarfile
import logging
import time
import os


class TopReportGenerator(object):
  logger = logging.getLogger("ddvt.rep_gen.top")

  def __init__(self):
    self.temp_dir = tempfile.mkdtemp()

  async def execute_generate(self, config):
    if not config.tar:
      self.temp_dir = config.results_path

    gens = [GroupGenerator(i) for i in config.groups]
    if len(gens) > 0:
      futures = [asyncio.ensure_future(i.generate(self)) for i in gens]
      await asyncio.wait(futures)

    self.logger.info("finished with subtasks")
    self.report = TopReport(config.name)
    self.report.groups = [i.report for i in gens]
    self.logger.info("Rendering")
    self.report.render(self.temp_dir)
    if config.tar:
      self.logger.info("Tarballing")
      output_name = config.results_path
      output_name = os.path.join(config.results_path,
                                 "{}.tar".format(time.time()))
      old_cwd = os.getcwd()
      os.chdir(self.temp_dir)
      tar = tarfile.open(output_name, "w")
      for i in os.listdir('.'):
        tar.add(i)
      tar.close()
      os.chdir(old_cwd)

  def generate(self, config):
    loop = asyncio.get_event_loop()
    self.logger.debug("Entering concurrent state")
    loop.run_until_complete(self.execute_generate(config))
