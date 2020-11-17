"""
chillchamber.main
"""

import PySimpleGUI as sg

from chillchamber.apps import app_list
from chillchamber.common import get_image


def main():
    app_tiles = dict()
    for App in app_list:
        app = App()
        app_tiles[sg.Button(image_filename=app.icon_path())] = app

    layout = [
        [
            sg.Image(filename=get_image('logo_smoke2.png')),
            sg.Image(filename=get_image('logo_text.png')),
        ],
        app_tiles.keys()
    ]

    window = sg.Window(
        "chillchamber",
        layout,
    ).Finalize()
    window.Maximize()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    main()
