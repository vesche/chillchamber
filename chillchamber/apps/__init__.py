"""
chillchamber.apps
"""

from chillchamber.apps.emby       import Emby
from chillchamber.apps.firefox    import Firefox
from chillchamber.apps.gameboy    import GameBoy
from chillchamber.apps.google     import Google
from chillchamber.apps.locast     import Locast
from chillchamber.apps.plunder    import Plunder
from chillchamber.apps.primevideo import PrimeVideo
from chillchamber.apps.snes       import Snes
from chillchamber.apps.spotify    import Spotify
from chillchamber.apps.terminal   import Terminal
from chillchamber.apps.twitch     import Twitch
from chillchamber.apps.wormhole   import Wormhole
from chillchamber.apps.youtube    import YouTube


app_list = [
    Emby,
    Firefox,
    GameBoy,
    Google,
    Locast,
    Plunder,
    PrimeVideo,
    Snes,
    Spotify,
    Terminal,
    Twitch,
    Wormhole,
    YouTube,
]