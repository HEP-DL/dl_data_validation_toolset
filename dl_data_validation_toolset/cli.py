# -*- coding: utf-8 -*-

import click
import logging
import sys
from dl_data_validation_toolset import data_tests
from dl_data_validation_toolset.framework.base_test import BaseTest


@click.command()
def main(files=None):
    logging.basicConfig(level=logging.INFO)

@click.command()
@click.argument('input_file', nargs=1)
def validate_single_dl_file(input_file):
  logging.basicConfig(level=logging.DEBUG)
  for test_case in BaseTest.__subclasses__():
    logging.info("Testing: {}".format(test_case))
    logging.info(test_case)
    test_case(input_file).get_results()


@click.command()
@click.option('--config',default=None, type=click.Path())
def validate_dl_data(config):
  """
    get the config and 
  """

  logging.basicConfig(level=logging.DEBUG)
  if config is None:
    pass
  else:
    pass

@click.command()
@click.option('-n', default=1, type=click.INT)
@click.option('--scale', default=1, type=click.INT)
@click.option('--thresh', default=25, type=click.INT)
@click.argument('input_file', nargs=1)
def print_dl_images(n,scale,thresh, input_file):
  logging.basicConfig(level = logging.DEBUG)
  import h5py
  from scipy.misc import imsave
  from scipy.stats import threshold
  import numpy as np
  input_file = h5py.File(input_file, 'r')
  wires = input_file['image/wires']
  rawdigits = input_file['image/rawdigits']
  logging.info("Producing {} images with scale {} and threshold {}".format(n, scale, thresh))
  for index in range(n):
    try:
      image = wires[index]
      logging.info("Image: min: {}, max: {}".format(np.min(image), np.max(image)))
      buff = np.ndarray(shape=(image.shape[1], image.shape[2], image.shape[0]), dtype=np.uint8)
      for i in range(3): buff[:,:,i]=image[i,:,:]
      buff = buff*scale
      buff = threshold(buff, threshmin=thresh)+threshold(buff, threshmax=-thresh)
      logging.info("Buffer: min: {}, max: {}".format(np.min(buff), np.max(buff)))
      imsave('wires_{}.png'.format(index), buff)
      logging.info('wires_{}.png created'.format(index))
    except Exception as e:
      logging.warning(e)
    return
    try:
      image = rawdigits[index]
      logging.info("Image: min: {}, max: {}".format(np.min(image), np.max(image)))
      buff = np.ndarray(shape=(image.shape[1], image.shape[2], image.shape[0]), dtype=np.uint8)
      for i in range(3): buff[:,:,i]=image[i,:,:]
      buff = buff*scale
      buff = threshold(buff, threshmin=thresh)+threshold(buff, threshmax=-thresh)
      logging.info("Buffer: min: {}, max: {}".format(np.min(buff), np.max(buff)))
      imsave('digits_{}.png'.format(index), buff)
      logging.info('digits_{}.png created'.format(index))
    except Exception as e:
      logging.warning(e)


if __name__ == "__main__":
    main()
