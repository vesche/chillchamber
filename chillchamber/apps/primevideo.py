"""
chillchamber.apps.primevideo
"""

from chillchamber.common import App, run_command, fullscreen


class PrimeVideo(App):
    def __init__(self):
        super().__init__('PrimeVideo')

    def run(self):
        run_command('/usr/bin/firefox -new-window https://www.amazon.com/Amazon-Video/b/?ie=UTF8&node=2858778011')
        fullscreen()
