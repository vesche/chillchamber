"""
chillchamber.tiles
"""

from chillchamber.gui import sg
from chillchamber.apps import app_list
from chillchamber.common import get_image, shift_workspace


def run_tiles(debug=False):
    shift_workspace(1)

    workspace = 1
    app_tiles = dict()
    for App in app_list:
        app = App()
        workspace += 1
        app.workspace = workspace
        app_tiles[app.name] = app

    ### shitty way of doing a 4x4 grid menu
    tile_layout = list()
    i = 0
    row = list()
    for app_name, app in app_tiles.items():
        row.append(sg.Button(key=app_name, image_filename=app.icon_path()))
        i += 1
        if i == 4:
            i = 0
            tile_layout.append(row)
            row = list()
    if row:
        tile_layout.append(row)
    ###

    layout = [
        [
            sg.Image(filename=get_image('logo_smoke')),
            sg.Image(filename=get_image('logo_text')),
        ],
        [
            sg.Column(
                tile_layout,
                size=(1920, 1080),
                scrollable=True,
                vertical_scroll_only=True,
            )
        ]
    ]

    window = sg.Window('chillchamber', layout).Finalize()
    window.Maximize()

    while True:
        event, values = window.read()

        if debug:
            print(event)

        if event == sg.WIN_CLOSED:
            break

        elif event in app_tiles:
            shift_workspace(app_tiles[event].workspace)
            app_tiles[event].run()

    window.close()
