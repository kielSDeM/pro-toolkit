#!/bin/bash
echo "going to install my favorite tools for programming"
sudo apt-get update ; sudo apt-get upgrade -y ; sudo apt-get dist-upgrade -y
#This installs my programming languages, ides and virtual enviroments
cd py_scripts ; python3 py_run.py
declare -A prolang='(["nmap version: "]=`nmap -v` 
["wireshark version: "]=`wireshark --version`
["python verison: "]=`python3 --version`
["Rust version: "]=`rustc --version` ["node version: "]=`node --version` 
["npm version: "]=`npm --version`)'
for i in "${!prolang[@]}"; 
    do echo "$i ${prolang[$i]}"; 
    done
