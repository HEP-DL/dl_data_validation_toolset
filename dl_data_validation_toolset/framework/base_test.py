import h5py
import abc


class BaseTest(object):

  __metaclass__ = abc.ABCMeta

  def __init__(self, filename):
    self._file = h5py.File(filename, 'r')

  @property
  def _tests_(self):
    return [att for att in dir(self) if att.startswith('test')]

  def get_results(self):
    results = {}
    for test in self._tests_:
      test_result = {}
      try:
        test_result['result'] = getattr(self, test)()
        test_result['passed'] = True
      except Exception as e:
        test_result['passed'] = False
        test_result['result'] = str(e)
      results[test] = test_result
    return results
