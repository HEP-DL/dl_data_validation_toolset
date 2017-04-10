# -*- coding: utf-8 -*-

import click
import logging
import sys
from dl_data_validation_toolset import data_tests
from framework.base_test import BaseTest


@click.command()
def main(files=None):
    logging.basicConfig(level=logging.INFO)

@click.command()
@click.argument('input_file', nargs=1)
def validate_single_dl_file(input_file):
  for test_case in BaseTest.__subclasses__():
    logging.info(test_case)
    test_case(input_file).go()

if __name__ == "__main__":
    main()
