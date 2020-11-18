"""
chillchamber.apps
"""

from chillchamber.apps.Locast       import Locast
from chillchamber.apps.PrimeVideo   import PrimeVideo
from chillchamber.apps.Spotify      import Spotify
from chillchamber.apps.Terminal     import Terminal
from chillchamber.apps.Twitch       import Twitch
from chillchamber.apps.Wormhole     import Wormhole
from chillchamber.apps.YouTube      import YouTube


app_list = [
    Locast,
    PrimeVideo,
    Spotify,
    Terminal,
    Twitch,
    Wormhole,
    YouTube,
]