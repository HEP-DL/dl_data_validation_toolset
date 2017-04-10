from click.testing import CliRunner
from dl_data_validation_toolset import cli
from dl_data_validation_toolset.framework import base_unittest
from dl_data_validation_toolset.framework.base_test import BaseTest


class TestDl_CLI(base_unittest.BaseTestCase):
  """
    Tests the functionality in cli.py
  """

  def test_command_line_interface(self):
    """
      Tests that the CLI can construct tests and run on a fake file.

      :note: This test will fail if any of the other tests also fail.
    """
    runner = CliRunner()
    result = runner.invoke(cli.validate_single_dl_file,["myfile.h5"])
    assert result.exit_code == 0

  def test_cli_help(self):
    """
      Tests that the CLI is no blocking the existing help functionality
    """
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

  def test_subclass_register(self):
    """
      Tests that the CLI is able to successfully find the 
      validation tests.
    """
    assert(len(BaseTest.__subclasses__())>0)