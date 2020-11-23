"""
chillchamber.apps.youtube
"""

from chillchamber.common import App, run_command, fullscreen


class YouTube(App):
    def __init__(self):
        super().__init__('YouTube')

    def run(self):
        run_command('/usr/bin/firefox -new-window https://www.youtube.com')
        fullscreen()
