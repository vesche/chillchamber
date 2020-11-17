"""
chillchamber.common
"""

import os


def run_command(string):
    subprocess.run(string.split())


def get_image(file_name):
    pwd = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(pwd, f'images/{file_name}')


def get_root_pwd():
    return os.path.abspath(os.path.dirname(__file__))


def shift_workspace(n):
    run_command(f"/usr/bin/bspc desktop -f '^{n}'")


class App():
    def __init__(self, name):
        self.name = name

    def icon_path(self):
        return os.path.join(get_root_pwd(), f'images/{self.name}.png')
