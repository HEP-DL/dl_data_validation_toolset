import logging
import json
import os

class Group:
  """
    Defines a named group of files.

    example instantiation:

    .. code_block: python

      g= Group("myfile.h5",'/points/to/your/dir/','my_group')

  """
  def __init__(self, file, base_dir, name):
    self.group = name
    self.files = [file, ]
    self.dir = base_dir


class Configuration(object):
  """
    De-serializes configuration into a useable object by other 
    objects.
  """
  logger = logging.getLogger('config')

  def __init__(self):
    self.data={}
    self.scan_paths = [os.path.join(os.getcwd(), 'data')]
    self.results_path = os.path.join(os.getcwd(), 'results')
    self.groups=[]
    self.tar = True  
    self.name="DL Data Validation Report"  

  def configure(self, path):
    self.logger.debug("Opening file: {}".format(path))
    with open(path, 'r') as input_file:

      self.data = json.load(input_file)
      self.scan_paths = [os.path.join(os.getcwd(),
                                      i) for i in self.data['scan_paths']]
      self.results_path = os.path.join(os.getcwd(),
                                       self.data['results_path'])
      self.results_path = os.path.abspath(self.results_path)
      self.tar = bool(self.data['tar'])
      self.logger.info("Loaded Config")
      self.logger.info(self.data)

  def create_new_group(self, file, path, group):
    msg = "Creating new group: {} at {}".format(group,
                                                path)
    self.logger.debug(msg)
    return Group(file, path, group)

  def scan(self):
    """
      Creates groups of files to be used in the parallelized framework.
    """
    self.groups = []
    for base_dir in self.scan_paths:
      self.logger.info("Entering: {}".format(base_dir))
      files = os.listdir(base_dir)
      for file in files:
        if file.endswith('.h5'):
          self.logger.debug("Adding file: {} to files".format(file))
          # get the group out
          file_parts = file.split('_')
          file_group = '_'.join(file_parts[:-1])
          group_exists = False
          for group in self.groups:
            if group.group == file_group and group.dir == base_dir:
              group_exists = True
              group.files.append(file)
          if not group_exists:
            self.groups.append(self.create_new_group(file, base_dir,
                                                     file_group))
