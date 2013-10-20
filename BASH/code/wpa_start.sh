#!/bin/sh
# Start WPA wireless connection
# Be sure that the file /etc/wpa_supplicant.conf has the proper PSK and SSID
pkill wpa_supplicant
iwconfig wlan0
wpa_supplicant -Dwext -iwlan0 -dd -c/etc/wpa_supplicant.conf -B
dhclient wlan0