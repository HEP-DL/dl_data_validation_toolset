import os


class FileReport(object):
  def __init__(self, file):
    self.file = file
    # all files are valid until proven broken
    self.valid = True
    # starts with no reports
    self.reports=[]

  @property
  def parent(self):
    os.path.dirname(self.file)

