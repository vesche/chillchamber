"""
chillchamber.apps.Terminal
"""

from chillchamber.common import App, run_command


class Terminal(App):
    def __init__(self):
        App.__init__(self, 'Terminal')

    def run(self):
        run_command('/usr/bin/urxvt')
