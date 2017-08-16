from .base import BaseReport


class GroupReport(BaseReport):

  def __init__(self, name):
    self.name = name
    self.file_reports = []

  def render(self, directory):
    pass
