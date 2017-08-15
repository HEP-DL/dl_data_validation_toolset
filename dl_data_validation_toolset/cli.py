# -*- coding: utf-8 -*-

import click
import logging
from dl_data_validation_toolset.framework.configuration import Configuration
from dl_data_validation_toolset.framework.report_gen import ReportGenerator
from dl_data_validation_toolset.framework.base_test import BaseTest
from dl_data_validation_toolset.framework.report import FileReport
from dl_data_validation_toolset.data_tests import initialize


@click.command()
@click.option('--config', default=None, type=click.Path())
def main(config):
  logging.basicConfig(level=logging.DEBUG)
  logging.info("Starting")
  initialize()
  logging.info("Tests to perform: {}".format(BaseTest.__subclasses__()))
  configuration = Configuration()
  if config is None:
    configuration.configure(config)

  """
  # Now that we've located the files and start a report, let's
  # create some tests
  file_reports = []
  for file in scan_results[0]:
    report = FileReport(file)
    for test_case in BaseTest.__subclasses__():
      logging.debug(test_case)
      test_case(file).validate(report)
      # create an image with this file
    file_reports.append(report)

  # TODO: make this more comprehensive
  group_reports = scan_results[1]

  rep_gen = ReportGenerator(configuration.results_path)
  rep_gen.generate(file_reports, group_reports)
  if configuration.tar:
    rep_gen.tarball()
  else:
    rep_gen.move_to_results()
  logging.info("Finished")
  """
