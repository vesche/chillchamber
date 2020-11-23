"""
chillchamber.apps.emby
"""

from chillchamber.common import App, run_command, fullscreen


class Emby(App):
    def __init__(self):
        super().__init__('Emby')

    def run(self):
        url = self.config['url']
        run_command(f'/usr/bin/firefox -new-window {url}')
        fullscreen()
