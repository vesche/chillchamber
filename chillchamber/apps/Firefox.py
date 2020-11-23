"""
chillchamber.apps.Firefox
"""

from chillchamber.common import App, run_command, fullscreen


class Firefox(App):
    def __init__(self):
        super().__init__('Firefox')

    def run(self):
        run_command(f'/usr/bin/firefox -new-window')
        fullscreen()
