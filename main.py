#!/usr/bin/env python
import argparse
import logging
import os
import re
import sys

import click

def valid_date(date_string):
    DATE_INPUT_FORMAT = '%d-%m-%Y'
    from datetime import datetime
    try:
        return datetime.strptime(date_string, DATE_INPUT_FORMAT)
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(date_string)
        raise argparse.ArgumentTypeError(msg)


@click.group()
def cli():
    pass

@cli.group()
def process():
    pass

@process.command()
def cbs():
    from anyway.parsers.cbs import main
    return main()

@process.command()
@click.argument("filename", type=str, default="data/segments/road_segments.xlsx")
def road_segments(filename):
    from anyway.parsers.road_segments import parse
    return parse(filename)

if __name__ == '__main__':
    cli(sys.argv[1:])  # pylint: disable=too-many-function-args
