"""
  Tests classes in dl_data_validation_toolset.framework.base_test
"""

from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.framework.configuration import Configuration
from dl_data_validation_toolset.framework.report_gen import TopReportGenerator
from unittest.mock import patch
import logging
import os

from dl_data_validation_toolset.framework.report_gen.group import GroupGenerator
from dl_data_validation_toolset.framework.report import TopReport
import tarfile
import asyncio


async def generate_dummy(obj):
  logging.info("Calling generate dummy")


def render_dummy(obj, directory):
  logging.info("Calling render dummy")


def tarfileopen_dummy(tmp1,tmp2):
  class DummyTar:
    def add(self, item):
      pass
    def close(self):
      pass
  return DummyTar()

"""
class TestTopReportGen(base_unittest.BaseTestCase):

  @patch.object(tarfile, 'open', new=tarfileopen_dummy)
  @patch.object(TopReport, 'render', new=render_dummy)
  @patch.object(GroupGenerator, 'generate', new=generate_dummy)
  def test_generate(self):
    c = Configuration()
    top = TopReportGenerator()
    top.generate(c)
"""

from dl_data_validation_toolset.framework.report_gen.file import FileGenerator
from dl_data_validation_toolset.framework.report.group import GroupReport
from dl_data_validation_toolset.framework.configuration import Group


class TestGroupReportGen(base_unittest.BaseTestCase):

  @patch.object(GroupReport, 'render', new=render_dummy)
  @patch.object(FileGenerator, 'generate', new=generate_dummy)
  def test_generate(self):
    group = Group("myfile.h5", "./data","MyGroup")
    group.files.append("mysecondfile.h5")
    ggen = GroupGenerator(group)
