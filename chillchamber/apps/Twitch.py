"""
chillchamber.apps.Locast
"""

from chillchamber.common import App, run_command


class Twitch(App):
    def __init__(self):
        super().__init__('Twitch')

    def run(self):
        run_command('/usr/bin/streamlink-twitch-gui')

