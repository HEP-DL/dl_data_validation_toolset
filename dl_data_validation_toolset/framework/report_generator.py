from mako.template import Template
import os
from dl_data_validation_toolset import templates
import tempfile
import logging


class ReportGenerator(object):
  logger = logging.getLogger()

  def __init__(self):
    self.template_directory = os.path.dirname(templates.__file__)
    self.temp_dir = tempfile.mkdtemp()

  def make_index_page(self):
    index_template = Template(filename='index.mako',
                              module_directory=self.template_directory)
    return index_template

  def make_dataset_page(self):
    pass
