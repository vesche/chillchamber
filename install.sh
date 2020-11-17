#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]
    then echo "Error, the chillchamber install must be run as root."
    exit
fi

mkdir -p /opt/chillchamber/apps/

#for app in $(cat chillchamber/apps/__init__.py | grep "chillchamber.apps." | cut -d' ' -f4); do
#    echo "{}" > "/opt/chillchamber/apps/$app.json"
#done

for app_config in $(ls chillchamber/apps/*.json); do
    cp "$app_config" /opt/chillchamber/apps/
done

sudo -Hu user bash -c "python setup.py install --user"