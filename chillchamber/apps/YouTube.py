"""
chillchamber.apps.YouTube
"""

from chillchamber.common import App, run_command


class YouTube(App):
    def __init__(self):
        super().__init__('YouTube')

    def run(self):
        run_command('/usr/bin/firefox -new-window https://www.youtube.com')
        # run_command('xdotool search --sync --onlyvisible --class "Firefox" windowactivate key F11')
