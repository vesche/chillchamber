"""
chillchamber.apps.google
"""

from chillchamber.common import App, run_command


class Google(App):
    def __init__(self):
        super().__init__('Google')

    def run(self):
        run_command('/usr/bin/firefox -new-window https://www.google.com/')
