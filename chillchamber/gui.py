"""
chillchamber.gui
"""

import PySimpleGUI as sg

from chillchamber.apps import app_list
from chillchamber.common import get_image, shift_workspace

sg.LOOK_AND_FEEL_TABLE['ChillChamber'] = {
    'BACKGROUND': '#000000',
    'TEXT': '#faebd7',
    'INPUT': '#000000',
    'TEXT_INPUT': '#000000',
    'SCROLL': '#000000',
    'BUTTON': ('#faebd7', '#000000'),
    'PROGRESS': ('#faebd7', '#000000'),
    'BORDER': 0,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0,
    'COLOR_LIST': ['#faebd7', '#000000'],
    'DESCRIPTION': ['Black']
}
sg.change_look_and_feel('ChillChamber')


def run_gui():
    shift_workspace(1)

    layout = [
        [
            sg.Image(filename=get_image('logo_smoke')),
            sg.Image(filename=get_image('logo_text')),
        ],
    ]

    workspace = 2
    app_tiles = dict()
    for App in app_list:
        app = App()
        app.workspace = workspace
        workspace += 1
        app_tiles[app.name] = app

    ### shitty way of doing a 4x4 grid menu
    i = 0
    row = list()
    for app_name, app in app_tiles.items():
        row.append(sg.Button(app_name, image_filename=app.icon_path()))
        i += 1
        if i == 4:
            i = 0
            layout.append(row)
            row = list()
    if row:
        layout.append(row)
    ###

    window = sg.Window(
        'chillchamber',
        layout,
        element_justification='center',
    ).Finalize()
    window.Maximize()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event in app_tiles:
            shift_workspace(app_tiles[event].workspace)
            app_tiles[event].run()

    window.close()
