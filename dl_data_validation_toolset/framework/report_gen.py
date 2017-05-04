from mako.template import Template
import os
from dl_data_validation_toolset import templates
import tempfile
import logging


class ReportGenerator(object):
  logger = logging.getLogger('report_gen')

  def __init__(self, config):
    self.template_directory = os.path.dirname(templates.__file__)
    self.temp_dir = tempfile.mkdtemp()

  def generate(self, file_reports):
    pass

  def make_index_page(self):
    index_path = os.path.join(self.template_directory, 'index.mako')
    index_template = Template(filename=index_path,
                              module_directory=self.template_directory)
    return index_template
