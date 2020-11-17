"""
chillchamber.gui
"""

import PySimpleGUI as sg

from chillchamber.apps import app_list
from chillchamber.common import get_image, shift_workspace


def run_gui():
    shift_workspace(1)

    layout = [
        [
            sg.Image(filename=get_image('logo_smoke')),
            sg.Image(filename=get_image('logo_text')),
        ],
        []
    ]

    app_tiles = dict()
    for App in app_list:
        app = App()
        app_tiles[app.name] = app
        layout[-1].append(sg.Button(app.name, image_filename=app.icon_path()))

    window = sg.Window(
        'chillchamber',
        layout,
    ).Finalize()
    window.Maximize()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event in app_tiles:
            app_tiles[event].run()

    window.close()
