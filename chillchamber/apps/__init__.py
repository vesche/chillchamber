"""
chillchamber.apps
"""

from chillchamber.apps.locast import Locast
from chillchamber.apps.terminal import Terminal
from chillchamber.apps.wormhole import Wormhole


app_list = [
    Locast,
    Terminal,
    Wormhole,
]