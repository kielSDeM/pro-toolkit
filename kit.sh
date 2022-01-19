#!/bin/bash
./pro-lan.sh 
./alfa.sh 
./metasploit.sh
./meta3.sh 
python3 dev_ops_installer.py
echo "terraform version: "
terraform -v
echo "metasploit version:"
msfconsole --version
echo "npm version: "
npm -v
echo "node version: "
node --version
echo "Python version: "
python3
echo "Rust version: "
rustc --version
echo "Nmap version:"
nmap --version
echo "Wireshark Version:"
wireshark -v
