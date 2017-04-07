# -*- coding: utf-8 -*-

import click
import logging
import sys
from stevedore import driver


@click.command()
def main(files=None):
    logging.basicConfig(level=logging.INFO)

@click.command()
def validate_single_dl_file(input_file)
  mgr = driver.ExtensionManager(
    namespace='dl_data_validation_toolset.validation_tests',
    invoke_on_load=False,
  )
  for ext in mgr:
    ext.process(input_file)
    logging.info(ext.result)

if __name__ == "__main__":
    main()
