"""
chillchamber.apps.twitch
"""

from chillchamber.common import App, run_command, fullscreen


class Twitch(App):
    def __init__(self):
        super().__init__('Twitch')

    def run(self):
        run_command('/usr/bin/streamlink-twitch-gui')
        fullscreen()
