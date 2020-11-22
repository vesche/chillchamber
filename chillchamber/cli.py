"""
chillchamber.cli
"""

import argparse

from chillchamber.tiles import run_tiles
from chillchamber.meta import VERSION


def get_parser():
    parser = argparse.ArgumentParser(
        description='chillchamber'
    )
    parser.add_argument(
        '-d', '--debug',
        help='enable debug mode',
        action='store_true',
        default=False
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
    run_tiles(debug=args['debug'])
