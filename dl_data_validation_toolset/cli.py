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

if __name__ == "__main__":
    main()