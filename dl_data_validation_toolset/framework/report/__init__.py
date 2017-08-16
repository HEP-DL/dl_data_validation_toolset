from .base import BaseReport
import os

class TopReport(BaseReport):
  def __init__(self, name):
    self.name = name
    self.groups = []

  def render(self, directory):
    with open(os.path.join(directory, 'index.html'), 'w') as index_out:
      self.logger.info("Writing Index Page")
      index_out.write(self.index_template.render(title="DL Data Report"))    
      #files=file_reports,groups=group_reports,
