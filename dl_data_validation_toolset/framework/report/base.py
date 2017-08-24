from dl_data_validation_toolset import templates
from mako.lookup import TemplateLookup
import logging
import os


class BaseReport(object):
  logger = logging.getLogger("frmwk.report.base")
  template_directory = os.path.dirname(templates.__file__)

  @property
  def lookup(self):
    return TemplateLookup(directories=[self.template_directory])

  @property
  def index_template(self):
    return self.lookup.get_template('index.mako')

  @property
  def file_template(self):
    return self.lookup.get_template('file.mako')

  @property
  def group_template(self):
    return self.lookup.get_template('group.mako')

  def render(self, directory):
    self.logger.error("Calling default report render!")
