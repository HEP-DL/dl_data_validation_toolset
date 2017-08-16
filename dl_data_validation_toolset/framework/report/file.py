import os
import logging
from .base import BaseReport
import numpy as np
import h5py
from scipy.stats import threshold
from scipy.misc import imsave


class FileReport(BaseReport):
  logger = logging.getLogger("ddvt.rep.file")

  def __init__(self, file, temp_dir):
    self.file = file
    # all files are valid until proven broken
    self.valid = True
    # starts with no reports
    self.reports = []
    self.images = []
    self.temp_dir = temp_dir

  @property
  def filename(self):
    return self.file.split('/')[-1]

  @property
  def path(self):
    return os.path.dirname(self.file)

  @property
  def slug(self):
    return self.file.split('_')[-1].strip('.h5')

  def render(self, directory):
    if not os.path.isdir(directory):
      os.mkdir(directory)
    self.render_image(directory)
    with open(os.path.join(directory, 'index.html'), 'w') as index_out:
      self.logger.info("Writing file Page for {}".format(self.file))
      index_out.write(self.file_template.render(title=self.file,
                                                file_report=self))

  def render_image(self, dir):
    input_file = h5py.File(self.file, 'r')
    wires = input_file['image/wires']
    n = 1
    scale = 100
    thresh = 25
    self.logger.info("""Producing {} images with
                     scale {} and threshold {}""".format(n, scale, thresh))
    try:
      image = wires[0]
      self.logger.info("Image: min: {}, max: {}".format(np.min(image),
                                                        np.max(image)))
      buff = np.ndarray(shape=(image.shape[1], image.shape[2],
                               image.shape[0]),
                        dtype=np.uint8)
      for i in range(3):
        buff[:, :, i] = image[i, :, :]
      buff = buff * scale
      buff = threshold(buff, threshmin=thresh) + threshold(buff,
                                                           threshmax=-thresh)
      self.logger.info("Buffer: min: {}, max: {}".format(np.min(buff),
                                                         np.max(buff)))
      output_file = os.path.join(dir,
                                 'wires.png')
      imsave(output_file, buff)
    except Exception as e:
      self.logger.warning("problem creating image")
      self.logger.warning(e)
