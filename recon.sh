#!/bin/bash
echo "This script will install some pen testing tools for me to learn"
  declare -a recon='(`sudo apt-get install nmap; sudo apt-get install aircrack-ng; 
  sudo apt-get install wireshark`)'
  
for ((i=0; i<${#recon[@]}; i++)) ; do ${recon[i]} ; done
