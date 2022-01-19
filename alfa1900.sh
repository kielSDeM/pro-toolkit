#!/bin/bash
sudo apt update ; apt upgrade -y
sudo apt install realtek-rtl88xxau-dkms
#Set interface down
sudo ip link set wlan0 down
#Set monitor mode
sudo iwconfig wlan0 mode monitor
#Set interface up
sudo ip link set wlan0 up
sudo reboot
#Set interface down
sudo ip link set wlan0 down
#Set monitor mode
sudo iwconfig wlan0 mode monitor
#Set interface up
sudo ip link set wlan0 up
