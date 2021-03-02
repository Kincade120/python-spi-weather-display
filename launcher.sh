#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/octoprint-spi
if [ -z "$STY" ]; then exec screen -dm -S api /bin/bash "sudo python api.py"; fi
sudo python main.py
cd 
