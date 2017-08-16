import os
from .base import BaseReport

class FileReport(BaseReport):

  def __init__(self, file, temp_dir):
    self.file = file
    # all files are valid until proven broken
    self.valid = True
    # starts with no reports
    self.reports = []
    self.images = []
    self.temp_dir= temp_dir

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
    self.logger.error("Calling default report render!")


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