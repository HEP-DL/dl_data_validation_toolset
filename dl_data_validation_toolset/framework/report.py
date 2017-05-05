import os


class TestReport(object):
  """
    2= Good
    1= Warning
    0= BAD
  """

  def __init__(self,name):
    self.name = name
    self.status=2

class FileReport(object):
  def __init__(self, file):
    self.file = file
    # all files are valid until proven broken
    self.valid = True
    # starts with no reports
    self.reports = []

  @property
  def filename(self):
    return self.file.split('/')[-1]

  @property
  def parent(self):
    return os.path.dirname(self.file)
