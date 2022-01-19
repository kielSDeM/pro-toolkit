#!/bin/bash
echo "This script will install some pen testing tools for me to learn"
sudo apt install nmap
sudo apt install aircrack-ng
sudo apt install wireshark
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall
