import os


class IndividualReport(object):
  """
    2+ Better than good
    2= Good
    1= Warning
    0= Invalidates
  """

  def __init__(self, name, status, fields):
    self.name = name
    self.status = status
    self.fields = fields


class FileReport(object):
  def __init__(self, file):
    self.file = file
    # all files are valid until proven broken
    self.valid = True
    # starts with no reports
    self.reports = []
    self.images = []

  @property
  def filename(self):
    return self.file.split('/')[-1]

  @property
  def parent(self):
    return os.path.dirname(self.file)
