"""
chillchamber.apps.Spotify
"""

from chillchamber.common import App, run_command


class Spotify(App):
    def __init__(self):
        super().__init__('Spotify')

    def run(self):
        print(self.config['username'])
        print(self.config['password'])
        run_command('/usr/bin/spotify')
