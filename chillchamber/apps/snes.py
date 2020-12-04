"""
chillchamber.apps.snes
"""

from chillchamber.common import App, run_command


class Snes(App):
    def __init__(self):
        super().__init__('Snes')

    def run(self):
        run_command('/usr/bin/snes9x-gtk')
