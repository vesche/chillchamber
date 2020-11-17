"""
chillchamber.apps.Locast
"""

from chillchamber.common import App, run_command


class Locast(App):
    def __init__(self):
        super().__init__('Locast')

    def run(self):
        print(self.config['username'])
        print(self.config['password'])
