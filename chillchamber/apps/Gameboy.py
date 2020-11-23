"""
chillchamber.apps.Gameboy
"""

from chillchamber.common import App, run_command, fullscreen


class Gameboy(App):
    def __init__(self):
        super().__init__('Gameboy')

    def run(self):
        run_command('/usr/bin/visualboyadvance-m')
        fullscreen()
