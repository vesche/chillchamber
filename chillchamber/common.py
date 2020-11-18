"""
chillchamber.common
"""

import os
import json
import subprocess


def run_command(string):
    subprocess.Popen(string.split())


def get_root_pwd():
    return os.path.abspath(os.path.dirname(__file__))


def get_image(file_name):
    return os.path.join(get_root_pwd(), f'images/{file_name}.png')


def shift_workspace(n):
    run_command(f"/usr/bin/bspc desktop -f ^{n}")


def fullscreen():
    os.system('sleep 1 && bspc node -t fullscreen')


class App():
    def __init__(self, name):
        self.name = name
        self.config = self.load_config()
        self.workspace = None

    def icon_path(self):
        return get_image(self.name)

    def load_config(self):
        with open(f'/opt/chillchamber/apps/{self.name}.json') as f:
            return json.loads(f.read())
