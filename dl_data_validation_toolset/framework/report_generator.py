import mako
import os
from dl_data_validation_toolset import templates

class ReportGenerator(object):
  def __init__(self):
    self.template_directory = os.path.dirname(templates.__file__)

  def make_index_page(self):
    pass

  def make_dataset_page(self):
    pass
