#!/bin/sh
# Be sure that the file /etc/wpa_supplicant.conf has the proper PSK and SSID
dhcpcd -x wlan0
dhclient -v wlan0