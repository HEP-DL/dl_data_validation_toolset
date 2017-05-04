import logging
import os


class Group:
  def __init__(self, file, base_dir, name):
    self.group = name
    self.files = [file, ]
    self.dir = base_dir


class Scanner(object):
  logger = logging.getLogger('scanner')

  def __init__(self, config):
    self.base_dirs = config

  def create_new_group(self, file, path, group):
    msg = "Creating new group: {} at {}".format(group,
                                                path)
    self.logger.debug(msg)
    return Group(file, path, group)

  def scan(self):
    """
      Returns a list of files to be validated/classified and
      a list of file groups
    """
    file_output = []
    group_output = []
    for base_dir in self.base_dirs:
      self.logger.info("Entering: {}".format(base_dir))
      files = os.listdir(base_dir)
      for file in files:
        if file.endswith('.h5'):
          file_output.append(os.path.join(base_dir, file))
          self.logger.debug("Adding file: {} to files".format(file))
          # get the group out
          file_parts = file.split('_')
          file_group = '_'.join(file_parts[:-1])
          group_exists = False
          for group in group_output:
            if group.group == file_group and group.dir == base_dir:
              group_exists = True
              group.files.append(file)
          if not group_exists:
            group_output.append(self.create_new_group(file, base_dir,
                                                      file_group))
    return (file_output, group_output)
