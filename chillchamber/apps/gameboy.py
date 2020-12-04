"""
chillchamber.apps.gameboy
"""

from chillchamber.common import App, run_command


class GameBoy(App):
    def __init__(self):
        super().__init__('GameBoy')

    def run(self):
        run_command('/usr/bin/visualboyadvance-m')
