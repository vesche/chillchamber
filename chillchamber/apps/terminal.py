"""
chillchamber.apps.terminal
"""

from chillchamber.common import App, run_command


class Terminal(App):
    def __init__(self):
        super().__init__('Terminal')

    def run(self):
        run_command('/usr/bin/urxvt')
