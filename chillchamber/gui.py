"""
chillchamber.gui
"""

import PySimpleGUI as sg

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
