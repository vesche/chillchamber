"""
chillchamber.cli
"""

import argparse

from chillchamber.menu import run_menu
from chillchamber.meta import VERSION


def get_parser():
    parser = argparse.ArgumentParser(
        description='chillchamber'
    )
    parser.add_argument(
        '-v', '--version',
        help='display the current version',
        action='version',
        version=VERSION
    )
    return parser


def run_cli():
    parser = get_parser()
    args = vars(parser.parse_args())
    run_gui()
