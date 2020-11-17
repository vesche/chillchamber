"""
chillchamber.cli
"""

import argparse

from chillchamber.gui import run_gui
from chillchamber.meta import VERSION
from chillchamber.install import run_install


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
