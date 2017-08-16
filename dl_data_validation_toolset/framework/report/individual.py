from .base import BaseReport


class IndividualReport(BaseReport):
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
