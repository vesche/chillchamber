"""
chillchamber.apps
"""

from chillchamber.apps.Locast   import Locast
from chillchamber.apps.Spotify  import Spotify
from chillchamber.apps.Terminal import Terminal
from chillchamber.apps.Twitch   import Twitch
from chillchamber.apps.Wormhole import Wormhole


app_list = [
    Locast,
    Spotify,
    Terminal,
    Twitch,
    Wormhole,
]