# -*- coding: utf-8 -*-

import click
import logging
from dl_data_validation_toolset.framework.configuration import Configuration
from dl_data_validation_toolset.framework.report_gen import ReportGenerator
from dl_data_validation_toolset.framework.scanner import Scanner
from dl_data_validation_toolset.framework.base_test import BaseTest
from dl_data_validation_toolset import data_tests
from dl_data_validation_toolset.framework.report import FileReport


@click.command()
@click.option('-n', default=1, type=click.INT)
@click.option('--scale', default=1, type=click.INT)
@click.option('--thresh', default=25, type=click.INT)
@click.argument('input_file', nargs=1)
def print_dl_images(n, scale, thresh, input_file):
  logging.basicConfig(level=logging.DEBUG)
  import h5py
  from scipy.misc import imsave
  from scipy.stats import threshold
  import numpy as np
  input_file = h5py.File(input_file, 'r')
  wires = input_file['image/wires']
  rawdigits = input_file['image/rawdigits']
  logging.info("""Producing {} images with
                  scale {} and threshold {}""".format(n, scale, thresh))
  for index in range(n):
    try:
      image = wires[index]
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
      imsave('wires_{}.png'.format(index), buff)
      logging.info('wires_{}.png created'.format(index))
    except Exception as e:
      logging.warning(e)
    return
    try:
      image = rawdigits[index]
      logging.info("Image: min: {}, max: {}".format(np.min(image),
                                                    np.max(image)))
      buff = np.ndarray(shape=(image.shape[1], image.shape[2],
                               image.shape[0]), dtype=np.uint8)
      for i in range(3):
        buff[:, :, i] = image[i, :, :]
      buff = buff * scale
      buff = threshold(buff, threshmin=thresh) + threshold(buff,
                                                           threshmax=-thresh)
      logging.info("Buffer: min: {}, max: {}".format(np.min(buff),
                                                     np.max(buff)))
      imsave('digits_{}.png'.format(index), buff)
      logging.info('digits_{}.png created'.format(index))
    except Exception as e:
      logging.warning(e)


@click.command()
@click.option('--config', default=None, type=click.Path())
def generate_report(config):
  logging.basicConfig(level=logging.DEBUG)
  logging.info("Starting")
  logging.info("Tests on file: {}".format(data_tests.__all__))
  configuration = None
  if config is None:
    configuration = Configuration.default()
  else:
    configuration = Configuration(config)
  scanner = Scanner(configuration.scan_paths)
  scan_results = scanner.scan()
  logging.debug(scan_results)

  # Now that we've located the files and start a report, let's
  # create some tests and
  file_reports = []
  for file in scan_results[0]:
    report = FileReport(file)
    for test_case in BaseTest.__subclasses__():
      logging.debug(test_case)
      test_case(file).validate(report)
    file_reports.append(report)

  # TODO: make this more comprehensive
  group_reports = scan_results[1]

  rep_gen = ReportGenerator(configuration.results_path)
  rep_gen.generate(file_reports, group_reports)

  logging.info("Finished")
