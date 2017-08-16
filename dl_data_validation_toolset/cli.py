import click
import logging
from dl_data_validation_toolset.framework.configuration import Configuration
from dl_data_validation_toolset.framework.report_gen import TopReportGenerator


@click.command()
@click.option('--config', default=None, type=click.Path())
def main(config):
  logging.basicConfig(level=logging.DEBUG)
  logging.info("Starting")
  configuration = Configuration()
  if config is not None:
    configuration.configure(config)
  configuration.scan()
  top = TopReportGenerator()
  top.generate(configuration)
