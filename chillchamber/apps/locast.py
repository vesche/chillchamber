"""
chillchamber.apps.Locast
"""

from chillchamber.common import App, run_command


class Locast(App):
    def __init__(self):
        App.__init__(self, 'Locast')

    def run(self):
        # run_command("/usr/bin/urxvt")
        pass
