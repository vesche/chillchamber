"""
chillchamber.apps.spotify
"""

from chillchamber.common import App, run_command, fullscreen


class Spotify(App):
    def __init__(self):
        super().__init__('Spotify')

    def run(self):
        run_command('/usr/bin/spotify')
        fullscreen()
