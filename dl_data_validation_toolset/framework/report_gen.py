from mako.lookup import TemplateLookup
import os
from dl_data_validation_toolset import templates
import tempfile
import logging


class ReportGenerator(object):
  logger = logging.getLogger('report_gen')

  def __init__(self, config):
    self.template_directory = os.path.dirname(templates.__file__)
    self.temp_dir = tempfile.mkdtemp()

  @property
  def lookup(self):
    return TemplateLookup(directories=[self.template_directory])

  @property
  def index_template(self):
    return self.lookup.get_template('index.mako')

  @property
  def file_template(self):
    return self.lookup.get_template('file.mako')

  @property
  def group_template(self):
    return self.lookup.get_template('group.mako')

  def generate(self, file_reports, group_reports):
    file_dir = os.path.join(self.temp_dir, 'files')
    self.logger.info("Creating file directory: {}".format(file_dir))
    os.mkdir(file_dir)
    group_dir = os.path.join(self.temp_dir, 'groups')
    self.logger.info("Creating group directory: {}".format(group_dir))
    os.mkdir(group_dir)
    for index, file_report in enumerate(file_reports):
      output_path = os.path.join(file_dir, '{}.html'.format(index))
      with open(output_path, 'w') as output:
        self.logger.info("Writing: {}".format(output_path))
        render = self.file_template.render(report=file_report,
                                           title=file_report.file)
        output.write(render)

    for index, group_report in enumerate(group_reports):
      output_path = os.path.join(group_dir, '{}.html'.format(index))
      with open(output_path, 'w') as output:
        self.logger.info("Writing: {}".format(output_path))
        render = self.group_template.render(report=group_report,
                                            title=group_report.group)
        output.write(render)

    with open(os.path.join(self.temp_dir, 'index.html'), 'w') as index_out:
      self.logger.info("Writing Index Page")
      index_out.write(self.index_template.render(files=file_reports,
                                                 groups=group_reports,
                                                 title="DL Data Report"))
