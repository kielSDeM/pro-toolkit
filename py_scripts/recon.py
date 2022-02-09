import os


class Recon:
    def info_gather(command):
        print("This script will install some recon tools")
        command = [
            "sudo apt-get update && sudo apt get upgrade -y",
            "sudo apt-get install nmap -y",
            "sudo apt-get install wireshark -y",
            "sudo apt-get install aircrack-ng -y",
            "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall",
            "chmod 755 msfinstall",
            "./msfinstall",
            ]
            return command

        def alfa(command):
            print("This will install the alfa1900 adapter in ubuntu")
            command = [
                "sudo apt install build-essentials",
                "sudo apt install bc",
                "sudo apt install linux-headers-`uname -r",
                "git clone https://github.com/aircrack-ng/rtl8812au.git",
                "cd rtl8812au ; make ; sudo make install",
                ]
            return command
