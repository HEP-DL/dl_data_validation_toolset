from mako.lookup import TemplateLookup
import os
from dl_data_validation_toolset import templates
import tempfile
import logging
import h5py
from scipy.misc import imsave
from scipy.stats import threshold
import numpy as np
import tarfile
import time


class ReportGenerator(object):
  logger = logging.getLogger('report_gen')

  def __init__(self, config):
    self.template_directory = os.path.dirname(templates.__file__)
    self.temp_dir = tempfile.mkdtemp()
    self.image_dir = None
    self.n_images = 0
    self.results_path = config

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
      if file_report.valid:
        self.add_image_to_manifest(file_report)
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

  def add_image_to_manifest(self, file_report):
    if self.image_dir is None:
      self.image_dir = os.path.join(self.temp_dir, 'files/images')
      os.mkdir(self.image_dir)
    input_file = h5py.File(file_report.file, 'r')
    wires = input_file['image/wires']
    n = 1
    scale = 100
    thresh = 25
    self.logger.info("""Producing {} images with
                     scale {} and threshold {}""".format(n, scale, thresh))
    try:
      image = wires[0]
      logging.info("Image: min: {}, max: {}".format(np.min(image),
                                                    np.max(image)))
      buff = np.ndarray(shape=(image.shape[1], image.shape[2],
                               image.shape[0]),
                        dtype=np.uint8)
      for i in range(3):
        buff[:, :, i] = image[i, :, :]
      buff = buff * scale
      buff = threshold(buff, threshmin=thresh) + threshold(buff,
                                                           threshmax=-thresh)
      logging.info("Buffer: min: {}, max: {}".format(np.min(buff),
                                                     np.max(buff)))
      output_file = os.path.join(self.image_dir,
                                 'wires_{}.png'.format(self.n_images))
      imsave(output_file, buff)
      logging.info('wires_{}.png created'.format(self.n_images))
      file_report.images.append('images/wires_{}.png'.format(self.n_images))
    except Exception as e:
      logging.warning(e)
    self.n_images += 1

  def tarball(self):
    self.logger.info("Tarballing")
    output_name = self.results_path
    output_name = os.path.join(self.results_path, "{}.tar".format(time.time()))
    self.logger.info("Output Directory: {}".format(output_name))
    tar = tarfile.open(output_name, "w")
    tar.add(self.temp_dir)
    tar.close()
