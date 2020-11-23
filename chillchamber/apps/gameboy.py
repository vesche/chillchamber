"""
chillchamber.apps.gameboy
"""

from chillchamber.common import App, run_command, fullscreen


class GameBoy(App):
    def __init__(self):
        super().__init__('GameBoy')

    def run(self):
        run_command('/usr/bin/visualboyadvance-m')
        fullscreen()
