import yaml
import logging
import os

class Configuration(object):
  logger = logging.getLogger('config')

  def __init__(self, path):
    if path is not None:
      self.data = yaml.load(open(path, 'r'))
      self.scan_paths = [os.path.join(os.getcwd(), i) for i in self.data['scan_paths']]
      self.results_path = os.path.abspath(os.path.join(os.getcwd(), 
                                                       self.data['results_path']))
      self.logger.info("Loaded Config")
      self.logger.info(self.data)

  @staticmethod
  def default():
    c = Configuration(None)
    c.scan_paths = [os.path.join(os.getcwd(), 'data')]
    c.results_path = os.path.join(os.getcwd(), 'results')
    return c