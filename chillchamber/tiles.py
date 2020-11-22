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

    """
    ### shitty way of doing a 4x4 grid menu
    tile_layout = list()
    i = 0
    row = list()
    for app_name, app in app_tiles.items():
        if i % 2 == 0:
            visible=True
        else:
            visible = False
        row.append(sg.Button(key=app_name, image_filename=app.icon_path(), visible=visible))
        i += 1
        if i == 4:
            i = 0
            tile_layout.append(row)
            row = list()
    if row:
        tile_layout.append(row)
    ###
    """

    ### generate 4x2 grid experiment :)
    tile_n = 1
    tile_row_a = list()
    tile_row_b = list()
    for app_name, app in app_tiles.items():
        if tile_n <= 4:
            visible_a = True
            visible_b = False
        elif tile_n <= 8:
            visible_a = False
            visible_b = True
        else:
            visible_a = False
            visible_b = False
        tile_row_a.append(
            sg.Button(key=app_name, image_filename=app.icon_path(), visible=visible_a)
        )
        tile_row_b.append(
            sg.Button(key=app_name, image_filename=app.icon_path(), visible=visible_b)
        )
        tile_n += 1

    layout = [
        [
            sg.Image(filename=get_image('logo_smoke')),
            sg.Image(filename=get_image('logo_text')),
        ],
        tile_row_a,
        tile_row_b,
    ]

    window = sg.Window(
        'chillchamber',
        layout,
        return_keyboard_events=True,
        element_justification='center',
    ).Finalize()
    window.Maximize()

    while True:
        event, values = window.read()

        if debug:
            print(event)

        if event == sg.WIN_CLOSED:
            break

        elif event == 'Up:111':
            # window.FindElement
            print('up')

        elif event == 'Down:116':
            print('down')

        # launch selected app
        for app_name in app_tiles:
            if app_name in event:
                shift_workspace(app_tiles[app_name].workspace)
                app_tiles[app_name].run()

    window.close()
