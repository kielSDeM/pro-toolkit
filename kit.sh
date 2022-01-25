#!/bin/bash
echo "going to install my favorite tools for programming"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

cd py_scripts ; python3 py_run.py
declare -A prolang='(["metasploit version: "]=`msfconsole --version`
["nmap version: "]=`nmap -v` ["wireshark version: "]=`wireshark --version`
["python verison: "]=`python3 --version`
["Rust version: "]=`rustc --version`)'
for i in "${!prolang[@]}"; 
    do echo "$i ${prolang[$i]}"; 
    done
