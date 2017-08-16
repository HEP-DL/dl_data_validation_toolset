from .group import GroupGenerator
from ..report import TopReport

from scipy.stats import threshold
from scipy.misc import imsave
import numpy as np
import tempfile
import asyncio
import tarfile
import logging
import shutil
import h5py
import time
import glob
import os


class TopReportGenerator(object):
  logger = logging.getLogger("topreport.gen")

  def __init__(self):
    self.temp_dir = tempfile.mkdtemp()

  async def execute_generate(self, config):
    if not config.tar:
      self.temp_dir = config.results_path
    gens = [GroupGenerator(i) for i in config.groups]
    tasks = [asyncio.ensure_future(i.generate(self)) for i in gens]
    asyncio.wait(tasks)
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

  def generate(self, config):
    loop = asyncio.get_event_loop()
    self.logger.debug("Entering concurrent state")
    loop.run_until_complete(self.execute_generate(config))
