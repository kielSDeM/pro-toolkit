#!/bin/bash
sudo apt install build-essential
sudo apt install bc
sudo apt install linux-headers-`uname -r`
git clone https://github.com/aircrack-ng/rtl8812au.git
cd rtl8812au
make
sudo make install

declare -a alfa(`sudo apt install build-essentials` `sudo apt install bc` 
`sudo apt install linux-headers-`uname -r`` `git clone https://github.com/aircrack-ng/rtl8812au.git`
`cd rtl8812au ; make ; sudo make install`)
