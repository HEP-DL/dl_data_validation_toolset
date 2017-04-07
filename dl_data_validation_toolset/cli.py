# -*- coding: utf-8 -*-

import click
import logging
import sys


@click.command()
def main(files=None):
    logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    main()