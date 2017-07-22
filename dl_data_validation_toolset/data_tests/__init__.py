"""
  Definitions of the unit tests to perform on data
"""
__test_names__ = ['consistency', 'labels', 'wires']


def initialize():
  global __test_names__
  for i in __test_names__:
    __import__('dl_data_validation_toolset.data_tests.' + i)
