#!/bin/bash

cp /etc/wpa_supplicant/$1 /etc/wpa_supplicant/wpa_supplicant.conf

dhclient -r wlan0
ifdown wlan0
ifup wlan0
dhclient -v wlan0

echo
iwconfig wlan0
ifconfig wlan0