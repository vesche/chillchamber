"""
chillchamber.apps.Terminal
"""

from chillchamber.common import App, run_command, fullscreen


class Terminal(App):
    def __init__(self):
        super().__init__('Terminal')

    def run(self):
        run_command('/usr/bin/urxvt')
        fullscreen()
