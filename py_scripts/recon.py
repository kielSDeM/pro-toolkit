import os


class Recon:
    print("This script will install some recon tools")
    recon = [
        "sudo apt-get update && sudo apt get upgrade -y",
        "sudo apt-get install nmap -y",
        "sudo apt-get install wireshark -y",
        "sudo apt-get install aircrack-ng -y",
        "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall",
        "chmod 755 msfinstall",
        "./msfinstall",
    ]
    for i in recon:
        os.system(i)


class Alfa:
    print("This will install the alfa1900 adapter in ubuntu")
    alfa = [
        "sudo apt install build-essentials",
        "sudo apt install bc",
        "sudo apt install linux-headers-`uname -r",
        "git clone https://github.com/aircrack-ng/rtl8812au.git",
        "cd rtl8812au ; make ; sudo make install",
    ]
    for i in alfa:
        os.system(i)
    print("The installation is now complete")
