import logging
import h5py
import abc


class BaseTest(object):
  """
    Abstract base class for tests to be run on data files.
  """

  __metaclass__ = abc.ABCMeta
  logger = logging.getLogger("test")

  def __init__(self, filename):
    self.logger.info("Scanning file: {}".format(filename))
    self._file = h5py.File(filename, 'r')

  @property
  def _tests_(self):
    return [att for att in dir(self) if att.startswith('test')]
