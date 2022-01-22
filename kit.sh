#!/bin/bash
#./*.sh 
declare -A prolang='(["metasploit version: "]=`msfconsole --version`
["nmap version: "]=`nmap -v` ["wireshark version: "]=`wireshark --version`
["python verison: "]=`python3 --version`
["Rust version: "]=`rustc --version`)'
for i in "${!prolang[@]}"; 
    do echo "$i ${prolang[$i]}"; 
    done
