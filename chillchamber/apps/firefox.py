"""
chillchamber.apps.firefox
"""

from chillchamber.common import App, run_command


class Firefox(App):
    def __init__(self):
        super().__init__('Firefox')

    def run(self):
        run_command(f'/usr/bin/firefox -new-window')
