#!/bin/bash
declare -a codium='(`sudo apt-get update ; sudo apt-get upgrade -y` 
`sudo apt-get dist-upgrade -y` `sudo apt-get install -y curl ; sudo apt-get install snapd` 
`sudo snap install core ; sudo snap install codium --classic`)'

for(i=0; i<${#codium[@]}; i++);
do
${codium[i]};
done
