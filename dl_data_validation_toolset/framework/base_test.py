import h5py
import abc


class BaseTest(object):

  __metaclass__ = abc.ABCMeta

  def __init__(self, filename):
    self._file = h5py.File(filename, 'r')


