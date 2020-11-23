#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]
    then echo "Error, the chillchamber install must be run as root."
    exit
fi

mkdir -p /opt/chillchamber/apps
mkdir /opt/chillchamber/luggage
mkdir /opt/chillchamber/wormhole

for app_config in $(ls chillchamber/configs/*.json); do
    cp "$app_config" /opt/chillchamber/apps/
done

sudo -Hu user bash -c "python setup.py install --user"