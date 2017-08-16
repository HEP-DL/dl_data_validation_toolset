from .base import BaseReport
import os

class GroupReport(BaseReport):

  def __init__(self, name, directory):
    self.name = name
    self.file_reports = []
    self.directory = directory

  def render(self, directory):
    if not os.path.isdir(directory):
      os.mkdir(directory)
    with open(os.path.join(directory, 'index.html'), 'w') as index_out:
      self.logger.info("Writing group Page for {}".format(self.name))
      index_out.write(self.group_template.render(title=self.name,group_report=self))

  @property
  def n_files(self):
    return len(self.file_reports)

  @property
  def n_valid_files(self):
    return len([i for i in self.file_reports if i.valid])