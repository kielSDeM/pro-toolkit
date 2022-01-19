#!/bin/bash
echo "This script will install vagrant & metasploitable3"
sudo apt update; sudo apt upgrade -y
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install vagrant
vagrant plugin install vagrant-vbguest
vagrant plugin install vagrant-libvirt
sudo apt update; sudo apt upgrade -y
mkdir metasploitable3-workspace
cd metasploitable3-workspace
curl -O https://raw.githubusercontent.com/rapid7/metasploitable3/master/Vagrantfile 
cd  metasploitable3-workspace; vagrant up
