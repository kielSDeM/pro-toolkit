#!/bin/bash
declare -a codium='(`sudo apt update ; sudo apt upgrade -y` 
`sudo apt-get dist-upgrade -y` `sudo apt install -y curl` 
`sudo apt install snapd` 
`sudo snap install core ; sudo snap install codium --classic`)'

for(i=0; i<${#codium[@]}; i++);
do
${codium[i]};
done
