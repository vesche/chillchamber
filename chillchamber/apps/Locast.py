"""
chillchamber.apps.Locast
"""

import os
import time
import random
import requests

from chillchamber.gui import sg
from chillchamber.common import App, run_command, get_root_pwd

LOCATIONS = {
    'Atlanta': ('33.7', '-84.4'),
    'Baltimore': ('39.2', '-76.6'),
    'Boston': ('42.3', '-71.1'),
    'Chicago': ('41.8', '-87.7'),
    'Dallas': ('32.7', '-96.6'),
    'Denver': ('39.7', '-105.0'),
    'Detroit': ('42.3', '-83.0'),
    'Houston': ('29.7', '-95.3'),
    'Indianapolis': ('39.7', '-86.1'),
    'Los Angeles': ('34.0', '-118.3'),
    'Miami': ('25.7', '-80.2'),
    'Minneapolis': ('45.0', '-93.2'),
    'New York': ('40.6', '-73.9'),
    'Philadelphia': ('40.0', '-75.1'),
    'Phoenix': ('33.5', '-112.0'),
    'Puerto Rico': ('18.2', '-66.4'),
    'Rapid City': ('44.0', '-103.2'),
    'San Francisco': ('37.7', '-122.4'),
    'Scranton': ('41.4', '75.6'),
    'Seattle': ('47.6', '-122.3'),
    'Sioux Falls': ('43.5', '-96.7'),
    'Tampa Bay': ('27.9', '-82.5'),
    'Washington Dc': ('38.9', '-77.0'),
    'West Palm Beach': ('26.7', '-80.0'),
}


class Locast(App):
    def __init__(self):
        super().__init__('Locast')
        self.base_url = 'https://api.locastnet.org/api'
        self.session = requests.Session()
        self._randomize_user_agent()

    def _request(self, endpoint, payload=None, method='GET'):
        r = self.session.request(
            method,
            self.base_url + endpoint,
            json=payload
        )
        return r.json()

    def _randomize_user_agent(self):
        ua_path = os.path.join(get_root_pwd(), 'extras/useragents.txt')
        rua = random.choice(open(ua_path).read().splitlines())
        self.session.headers['User-Agent'] = rua

    def get_token(self):
        resp = self._request(
            '/user/login',
            payload={
                'username': self.config['username'],
                'password': self.config['password']
            },
            method='POST'
        )
        self.session.headers['authorization'] = f"Bearer {resp['token']}"

    def get_dma(self, latitude, longitude):
        resp = self._request(
            f'/watch/dma/{latitude}/{longitude}'
        )
        return resp['DMA']

    def get_station_list(self, dma):
        return self._request(f'/watch/epg/{dma}')

    def get_stream(self, latitude, longitude, station_id):
        resp = self._request(f'/watch/station/{station_id}/{latitude}/{longitude}')
        return resp['streamUrl']

    def select_location(self):
        layout = list()
        for i in range(0, 24, 4):
            layout.append(
                [sg.Button(location) for location in list(LOCATIONS.keys())[i:i+4]]
            )

        window = sg.Window(
            'chillchamber - Locast (Locations)',
            layout,
        ).Finalize()
        window.Maximize()

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event in LOCATIONS.keys():
                latitude, longitude = LOCATIONS[event]
                break

        window.close()
        return latitude, longitude

    def select_channel(self, stations):
        channels = list()
        current_epoch = int(time.time())
        for station in stations:
            listing_details = {
                'channel': '',
                'call_sign': station['callSign'],
                'station_id': 0,
                'delta': 999999
            }
            for listing in station['listings']:
                listing_time = int(str(listing['startTime'])[:-3])
                if current_epoch < listing_time:
                    continue
                delta = current_epoch - listing_time
                if delta < listing_details['delta']:
                    listing_details['channel'] = ' - '.join(
                        [listing_details['call_sign'], listing['title']]
                    )
                    listing_details['station_id'] = listing['stationId']
                    listing_details['delta'] = delta
            channels.append(listing_details)

        layout = list()
        for c in channels:
            layout.append([sg.Button(c['channel'])])

        window = sg.Window(
            'chillchamber - Locast (Channels)',
            layout,
        ).Finalize()
        window.Maximize()

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event in [c['channel'] for c in channels]:
                station_id = c['station_id']
                break

        window.close()
        return station_id

    def run(self):
        if not (self.config['username'] or self.config['password']):
            print('Error: No user/pass for Locast')
            return

        # get Locast bearer token
        self.get_token()

        # select location, get latitude & longitude
        latitude, longitude = self.select_location()

        # get DMA using latitude & longitude
        dma = self.get_dma(latitude, longitude)

        # get list of stations using DMA
        stations = self.get_station_list(dma)

        # select station, get station ID
        station_id = self.select_channel(stations)

        # get stream link using latitude, longitude, and station ID
        stream_link = self.get_stream(latitude, longitude, station_id)

        # start stream via VLC
        run_command(f'/usr/bin/vlc -f {stream_link}')
